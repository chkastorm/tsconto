#!/usr/bin/bash

################################################################################
###                                                                          ###
### Script : Telnet-Simulated-CONsole shortcut TO consoles of guests in GNS3 ###
### Abbreviation : tsconto                                                   ###
### Author : Kastor M.                                                       ###
### Modified : Kastor M.                                                     ###
### Version : 1.0.2                                                          ###
### Date : Tue 29 Mar 2022 10:45:28 PM UTC                                   ###
###                                                                          ###
################################################################################

mv /tmp/tsconto-1.0.1/tsconto.py /usr/local/bin/tsconto
chmod 755 /usr/local/bin/tsconto
chown root:root /usr/local/bin/tsconto
rm -f /tmp/v1.0.1.tar.gz
rm -rf /tmp/tsconto-1.0.1
echo ""
echo "Install completed. Please issue \"tsconto\" to find the user manual."
echo ""


