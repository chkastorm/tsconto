#!/usr/bin/bash

################################################################################
###                                                                          ###
### Script : Telnet-Simulated-CONsole shortcut TO consoles of guests in GNS3 ###
### Abbreviation : tsconto                                                   ###
### Author : Kastor M.                                                       ###
### Modified : Kastor M.                                                     ###
### Version : 1.0.0                                                          ###
### Date : Mon Jan 17 03:43:42 UTC 2022                                      ###
###                                                                          ###
################################################################################

mv ./tsconto.py /usr/local/bin/tsconto
chmod 755 /usr/local/bin/tsconto
chown root:root /usr/local/bin/tsconto
rm -f ./tsconto-v1.0.0-gns3.tar
rm -f ./uninstall.sh
rm -f ./install.sh
echo ""
echo "Install completed. Please issue \"tsconto\" to find the user manual."
echo ""


