# Telnet-Simulated-CONsole shortcut TO consoles of guests in GNS3 (tsconto)
- for GNS3 users and Terminal lovers
- for Completely Clean OS addictants (who try to keep their laptop's OS extremely clean by refusing to install any applications or just use the portable version)
- Do not have to check the Telnet-Simulated Console Port anymore. Just use the node name and you are good to go.
- Complete clean installation and uninstallation. You can even copy the file yourselves rather than using the installation script.
- If you are a Clean OS addictants, you will NOT install the GNS3 Client
- If you are even more crazy like me, you will keep your server as clean as possible (for me, I just installed the GNS3 server w/ IOU and i386 and nothing else)
- Fortunately, GNS3 server comes with KVM and Docker (After GNS3 server installation, I do ALL of my remaining jobs inside a Container)
# Description
90% VMs created in the GNS3 server should be accessed by Telnet-Simulated console and the ports are assigned by GNS3 server randomly.
For your own safety, you will enable the ufw and ONLY allow the SSH port (You can then access all the other services via your SSH Tunnel)
You may configure "PermitRootLogin prohibit-password" in "sshd_config" for conveniance.

Then, if you DO NOT prefer the GNS3 Web-UI Web-CLI (because of no [Ctrl] + [w] or the fonts, size, color cannot be customized...), your easiest way to access your VM guests in GNS3 is to Login to the GNS3 server then telnet its Local Port as below,

Local Connect = telnet 127.0.0.1 <GNS3 server randomly assigned port>

This means we, the user, have to remember or check the corresponding port every time when we are going to access the console of a specific VM.

Although we can modify those telnet ports under the

/opt/gns3/projects/< Project-ID >/< Project-Name >.gns3,

it is super annoying cause we have to

systemctl restart gns3

to activate the settings and this action will stop ALL running VMs.

Also, if we delete and re-create a node, the port changes again.

Therefore, I created this handy tool which help everyone to lab easier.
By using this python3 script, you just need to issue a single "scan" command, and tell it your "GNS3 Project ID" and "Project Name".
The Program will then scan the corresponding .gns3 file and automatically create a linkage between each node's Name and their Telnet-Console Port.
After that, you can just simply execute the "connect" command along with the name assigned to the target node to access its console.

For some reason, mainly lazy, the current version (v1.0.0) only support a SINGLE RUNNING GNS3 Project. (if you have to work on another project, you will have to "scan" again)
# Pre-request
- Python3
# Notice
- Backup ALL IMPORTANT FILE(S) under /tmp/ in your GNS3 server (or gns3vm) before installation
- Installation & Uninstallation Scripts are written in bash
- Single DB Design so DO NOT support Multiple GNS3 Projects currently
- For Multiple GNS3 Projects, issue the "scan" command with New < Project ID > & New < Project Name >. The DB will be overwritten (Old DBs can be found from checkpoints).
# Installation
1. Download the release to /tmp/ in your GNS3 server (or gns3vm). You can do it directly in the server:
  
       wget -P /tmp/ https://github.com/chkastorm/tsconto/archive/refs/tags/v1.0.0.tar.gz

2. Decompress the release

       tar -zxvf /tmp/v1.0.1.tar.gz -C /tmp/

3. Run the bash script for installation

       sudo bash /tmp/tsconto-1.0.1/install.sh

4. Finish
# Uninstallion
1. Download the release to /tmp/ in your GNS3 server (or gns3vm). You can do it directly in the server:

       wget -P /tmp/ https://github.com/chkastorm/tsconto/archive/refs/tags/v1.0.0.tar.gz

2. Decompress the release

       tar -zxvf /tmp/v1.0.1.tar.gz -C /tmp/

3. Run the bash script for uninstallation
  
       sudo bash /tmp/tsconto-1.0.1/uninstall.sh

4. Finish


