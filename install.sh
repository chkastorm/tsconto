#!/usr/bin/bash

################################################################################
###                                                                          ###
### Script : Telnet-Simulated-CONsole shortcut TO consoles of guests in GNS3 ###
### Abbreviation : tsconto                                                   ###
### Author : Kastor M.                                                       ###
### Modified : Kastor M.                                                     ###
### Version : 1.0.3                                                          ###
### Date : Sun 10 Apr 2022 03:20:16 PM EDT                                   ###
###                                                                          ###
################################################################################

mv /tmp/tsconto-1.0.3/tsconto.py /usr/local/bin/tsconto
chmod 755 /usr/local/bin/tsconto
chown root:root /usr/local/bin/tsconto
rm -f /tmp/v1.0.3.tar.gz
rm -rf /tmp/tsconto-1.0.3
echo ""
echo "Install completed. Please issue \"tsconto\" to find the user manual."
echo ""


