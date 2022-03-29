#!/usr/bin/python3

################################################################################
###                                                                          ###
### Script : Telnet-Simulated-CONsole shortcut TO consoles of guests in GNS3 ###
### Abbreviation : tsconto                                                   ###
### Author : Kastor M.                                                       ###
### Modified : Kastor M.                                                     ###
### Version : 1.0.1                                                          ###
### Date : Mon Jan 17 19:45:44 UTC 2022                                      ###
###                                                                          ###
################################################################################

import os
import sys
import json
import datetime
import subprocess
from pprint import pprint

db_name_append_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
db_folder_at_home_directory = os.path.expanduser("~/.rhpn-gns3-stsc/")
db_at_user_home_directory = os.path.expanduser("~/.rhpn-gns3-stsc/dict-GNS3-NEs-list.json")

def message_user_manual():
    print("\n#############\n### Usage ###\n#############\n")
    print("=============================================================== Connect to console ===============================================================\n")
    print("tsconto connect < Registered Hostname >             ::: Connect to the Telnet-Simulated Console of a node in GNS3")
    print("\n")
    print("============================================================== Database Operations ===============================================================\n")
    print("tsconto database list                               ::: List out contents of the existing Database")
    print("tsconto database list checkpoint < Filename >       ::: List out contents of the Database at a Specific Checkpoint")
    print("tsconto database checkpoint                         ::: List out ALL Checkpoints of the Database")
    print("tsconto database revert from < Filename >           ::: Revert the Database status back to the Reference Point")
    print("tsconto database clean [ --all ]                    ::: Clean ALL Database Checkpoints [ Deep Clean including the in-force Database ]")
    print("tsconto database scan                               ::: Automatically scan over a specific .gns3 file for a project and import ALL nodes to the DB")
    print("tsconto database add < Hostname > < Port Number >   ::: To add a node manually")
    print("tsconto database delete < Hostname >                ::: To delete a node manually from the DB\n")

def message_database_empty():
    print("\nIn-Force Database Empty.\nPlease register at least one node to the in-force Database.\n\nFormat : tsconto database add < Hostname > < Port Number >\n///OR/// tsconto database scan\n")

def message_database_checkpoint_empty():
    print("\nCheckpoint Empty. Checkpoint will be generated automatically when registering node(s).\n\nFormat : tsconto database add < Hostname > < Port Number >\n///OR/// tsconto database scan\n")

def message_database_checkpoint_not_found():
    print("\nCheckpoint < Filename > CANNOT be found from the Registry. Please check and try again.\n\nFormat : tsconto database list checkpoint < Filename >\n  e.g.   tsconto database list checkpoint dict-GNS3-NEs-list.json.20220116222106\n")

def message_hostname_not_found():
    print("\nThe input < Hostname > CANNOT be found from the Registry. Please check and try again. Thank you.\n")

def message_unknown_cmd():
    print("\n[ Unknown command ] Please check and try again. Thank you.\n")

if (len(sys.argv) >=3 and sys.argv[1] == "database" and os.path.isfile(db_at_user_home_directory) == True):

    if len(sys.argv) == 3:

        if sys.argv[2] == "list":
            with open(db_at_user_home_directory, "r") as list_nodes:
                list_registered_nodes = json.loads(list_nodes.read())
            print("")
            pprint(list_registered_nodes)
            print("")

        elif sys.argv[2] == "checkpoint":
            print("")
            os.system('ls -trl ' + db_folder_at_home_directory)
            print("")

        elif sys.argv[2] == "clean":
            double_confirm_clean_db_backup = input("Do you really want to CLEAR ALL Backup of the Database? (yes/no) : ")
            if double_confirm_clean_db_backup == "yes":
                os.system('rm -rf ' + db_at_user_home_directory + '.*')
                print("\nALL Checkpoints cleared.\nONLY the in-force DB remains.\n")
            elif double_confirm_clean_db_backup == "no":
                print("\nGood Choice ^^\" !!\n")
            else:
                print("\nPlease ONLY Enter \"yes\" or \"no\". Thank you.\n")

        elif sys.argv[2] == "scan":
            scan_target_project_id = input("Please Enter GNS3 Project ID : ")
            scan_target_project_name = input("Please Enter GNS3 Project Name : ")
            scan_target_gns3_file_path = "/opt/gns3/projects/" + scan_target_project_id + "/" + scan_target_project_name + ".gns3"
            with open(scan_target_gns3_file_path, "r") as gns3_file:
                list_all_gns3_parameters = json.loads(gns3_file.read())
                list_all_gns3_nodes = ((list_all_gns3_parameters["topology"])["nodes"])
            list_registered_nodes_duplicate_hostname_checked = []
            list_registered_nodes_duplicate_checked = []
            with open(db_at_user_home_directory, "r") as list_nodes:
                list_registered_nodes = json.loads(list_nodes.read())
            for each_node in list_all_gns3_nodes:
                for entry_as_dict_hostname_check in list_registered_nodes:
                    for entry_of_list_registered_nodes_duplicate_hostname_checked in list_registered_nodes_duplicate_hostname_checked:
                        if (entry_as_dict_hostname_check["Hostname"] != each_node["name"] and entry_as_dict_hostname_check["Hostname"] != entry_of_list_registered_nodes_duplicate_hostname_checked["Hostname"]):
                            list_registered_nodes_duplicate_hostname_checked.append({"Hostname": entry_as_dict_hostname_check["Hostname"], "Port": entry_as_dict_hostname_check["Port"]})
            for each_node in list_all_gns3_nodes:
                for entry_as_dict in list_registered_nodes_duplicate_hostname_checked:
                    for entry_of_list_registered_nodes_duplicate_checked in list_registered_nodes_duplicate_checked:
                        if (entry_as_dict["Port"] != each_node["console"] and entry_as_dict["Port"] != entry_of_list_registered_nodes_duplicate_checked["Port"]):
                            list_registered_nodes_duplicate_checked.append({"Hostname": entry_as_dict["Hostname"], "Port": entry_as_dict["Port"]})
            for each_node in list_all_gns3_nodes:
                list_registered_nodes_duplicate_checked.append({"Hostname": each_node["name"], "Port": each_node["console"]})
            os.system('mv ' + db_at_user_home_directory + ' ' + db_at_user_home_directory + '.' + db_name_append_datetime)
            with open(db_at_user_home_directory, "w") as list_nodes:
                list_nodes.write(json.dumps(list_registered_nodes_duplicate_checked))
            print("\nBackup Complete.\nNew Database Created.\n")

        else:
            message_user_manual()

    elif len(sys.argv) == 4:

        if sys.argv[2] == "clean" and sys.argv[3] == "--all":
            double_confirm_clean_db_backup = input("Do you really want to CLEAR the Entire Database? (yes/no) : ")
            if double_confirm_clean_db_backup == "yes":
                os.system('rm -rf ' + db_at_user_home_directory + '*')
                print("\nDatabase Deep clean finished.\nDatabase is now Empty.\n")
            elif double_confirm_clean_db_backup == "no":
                print("\nGood Choice ^^\" !!\n")

        elif sys.argv[2] == "delete":
            input_node_hostname = sys.argv[3]
            with open(db_at_user_home_directory, "r") as list_nodes:
                list_registered_nodes = json.loads(list_nodes.read())
            is_deletable_hostname = []
            for deletable_hostname_entry in list_registered_nodes:
                if deletable_hostname_entry["Hostname"] == input_node_hostname:
                    is_deletable_hostname.append(deletable_hostname_entry)
            if not is_deletable_hostname:
                print("\nNo matched entry in the in-force DB. Please check as below,\n\nFormat : tsconto database list\n")
            else:
                reduced_list_registered_nodes = []
                for entry_as_dict in list_registered_nodes:
                    if not entry_as_dict["Hostname"] == input_node_hostname:
                        reduced_list_registered_nodes.append(entry_as_dict)
                    else:
                        pass
                os.system('mv ' + db_at_user_home_directory + ' ' + db_at_user_home_directory + '.' + db_name_append_datetime)
                with open(db_at_user_home_directory, "w") as list_nodes:
                    list_nodes.write(json.dumps(reduced_list_registered_nodes))
                if not reduced_list_registered_nodes:
                    os.system('rm -rf ' + db_at_user_home_directory)
                else:
                    pass
                print("\nEntry Deleted.\n")

        else:
            message_user_manual()

    elif len(sys.argv) == 5:

        if (sys.argv[2] == "list" and sys.argv[3] == "checkpoint"):
            try:
                input_checkpoint_filename = sys.argv[4]
                specific_checkpoint_file = (db_folder_at_home_directory + input_checkpoint_filename)
                with open(specific_checkpoint_file, "r") as list_nodes:
                    list_registered_nodes = json.loads(list_nodes.read())
                print("")
                pprint(list_registered_nodes)
                print("")
            except:
                message_database_checkpoint_not_found()
                sys.exit(1)

        elif (sys.argv[2] == "revert" and sys.argv[3] == "from"):
            input_checkpoint_filename = sys.argv[4]
            os.system('cp ' + db_at_user_home_directory + ' ' + db_at_user_home_directory + '.' + db_name_append_datetime)
            revert_file = db_folder_at_home_directory + input_checkpoint_filename
            revert_file_output = subprocess.run(['cp', revert_file, db_at_user_home_directory], capture_output = True, text = True)
            if revert_file_output.returncode == 0:
                print("\nReverted to " + sys.argv[4] + "\n")
            else:
                message_database_checkpoint_not_found()

        elif sys.argv[2] == "add":
            input_node_hostname = sys.argv[3]
            input_node_port_number = sys.argv[4]
            with open(db_at_user_home_directory, "r") as list_nodes:
                list_registered_nodes = json.loads(list_nodes.read())
            list_registered_nodes_duplicate_hostname_checked = []
            for entry_as_dict_hostname_check in list_registered_nodes:
                if entry_as_dict_hostname_check["Hostname"] != input_node_hostname:
                    list_registered_nodes_duplicate_hostname_checked.append({"Hostname": entry_as_dict_hostname_check["Hostname"], "Port": entry_as_dict_hostname_check["Port"]})
            list_registered_nodes_duplicate_checked = []
            for entry_as_dict in list_registered_nodes_duplicate_hostname_checked:
                if entry_as_dict["Port"] != input_node_port_number:
                    list_registered_nodes_duplicate_checked.append({"Hostname": entry_as_dict["Hostname"], "Port": entry_as_dict["Port"]})
            list_registered_nodes_duplicate_checked.append({"Hostname": input_node_hostname, "Port": input_node_port_number})
            os.system('mv ' + db_at_user_home_directory + ' ' + db_at_user_home_directory + '.' + db_name_append_datetime)
            with open(db_at_user_home_directory, "w") as list_nodes:
                list_nodes.write(json.dumps(list_registered_nodes_duplicate_checked))
            print("\nBackup Complete.\nNew Database Created.\n")

        else:
            message_user_manual()

    else:
        message_user_manual()

elif len(sys.argv) == 2:
    message_user_manual()

elif (len(sys.argv) == 3 and sys.argv[1] == "database"):

    if sys.argv[2] == "checkpoint":
        if os.path.isdir(db_folder_at_home_directory):
            if not len(os.listdir(db_folder_at_home_directory)) == 0:
                print("")
                os.system('ls -trl ' + db_folder_at_home_directory)
                print("")
            else:
                message_database_checkpoint_empty()
        else:
            message_database_checkpoint_empty()

    elif sys.argv[2] == "scan":
        os.system('mkdir -p ' + db_folder_at_home_directory)
        scan_target_project_id = input("Please Enter GNS3 Project ID : ")
        scan_target_project_name = input("Please Enter GNS3 Project Name : ")
        scan_target_gns3_file_path = "/opt/gns3/projects/" + scan_target_project_id + "/" + scan_target_project_name + ".gns3"
        with open(scan_target_gns3_file_path, "r") as gns3_file:
            list_all_gns3_parameters = json.loads(gns3_file.read())
            list_all_gns3_nodes = ((list_all_gns3_parameters["topology"])["nodes"])
        list_registered_nodes = []
        for each_node in list_all_gns3_nodes:
            list_registered_nodes.append({"Hostname": each_node["name"], "Port": each_node["console"]})
        with open(db_at_user_home_directory, "w") as list_nodes:
            list_nodes.write(json.dumps(list_registered_nodes))
        print("\nCreated new Database.\n")

    elif (sys.argv[2] == "list" or sys.argv[2] == "clean"):
        message_database_empty()

    else:
        message_user_manual()

elif (len(sys.argv) == 4 and sys.argv[1] == "database"):

    if (sys.argv[2] == "clean" and sys.argv[3] =="--all"):
        double_confirm_clean_db_backup = input("Do you really want to CLEAR the Entire Database? (yes/no) : ")
        if double_confirm_clean_db_backup == "yes":
            os.system('rm -rf ' + db_at_user_home_directory + '*')
            print("\nDatabase Deep clean finished.\nDatabase is now Empty.\n")
        elif double_confirm_clean_db_backup == "no":
            print("\nGood Choice ^^\" !!\n")

    elif sys.argv[2] == "delete":
        message_database_empty()

    else:
        message_user_manual()

elif (len(sys.argv) == 5 and sys.argv[1] == "database"):

    if (sys.argv[2] == "list" and sys.argv[3] == "checkpoint"):
        try:
            input_checkpoint_filename = sys.argv[4]
            specific_checkpoint_file = (db_folder_at_home_directory + input_checkpoint_filename)
            with open(specific_checkpoint_file, "r") as list_nodes:
                list_registered_nodes = json.loads(list_nodes.read())
            print("")
            pprint(list_registered_nodes)
            print("")
        except:
            message_database_checkpoint_not_found()
            sys.exit(1)

    elif (sys.argv[2] == "revert" and sys.argv[3] == "from"):
        if not len(os.listdir(db_folder_at_home_directory)) == 0:
            input_checkpoint_filename = sys.argv[4]
            os.system('cp ' + db_at_user_home_directory + ' ' + db_at_user_home_directory + '.' + db_name_append_datetime)
            revert_file = db_folder_at_home_directory + input_checkpoint_filename
            revert_file_output = subprocess.run(['cp', revert_file, db_at_user_home_directory], capture_output = True, text = True)
            if revert_file_output.returncode == 0:
                print("\nReverted to " + sys.argv[4] + "\n")
            else:
                message_database_checkpoint_not_found()
        else:
            message_database_checkpoint_empty()

    elif sys.argv[2] == "add":
        input_node_hostname = sys.argv[3]
        input_node_port_number = sys.argv[4]
        list_registered_nodes = [{"Hostname": input_node_hostname, "Port": input_node_port_number}]
        os.system('mkdir -p ' + db_folder_at_home_directory + ' && touch ' + db_at_user_home_directory)
        with open(db_at_user_home_directory, "a") as list_nodes:
            list_nodes.write(json.dumps(list_registered_nodes))
        print("\nCreated new Database.\n")

    else:
        message_user_manual()

elif (len(sys.argv) == 3 and sys.argv[1] == "connect"):

    if os.path.isfile(db_at_user_home_directory) == True:
        db_at_user_home_directory = os.path.expanduser("~/.rhpn-gns3-stsc/dict-GNS3-NEs-list.json")
        with open(db_at_user_home_directory, "r") as list_nodes:
            list_registered_nodes = json.loads(list_nodes.read())
        for entry_as_dict in list_registered_nodes:
            if entry_as_dict["Hostname"] == sys.argv[2]:
                os.system('telnet 127.0.0.1 ' + str(entry_as_dict["Port"]))
            else:
                message_hostname_not_found()

    elif os.path.isfile(db_at_user_home_directory) == False:
        message_database_empty()

    else:
        message_user_manual()

else:
    message_user_manual()

