#!/usr/bin/python
#
# This script convert a domain to ip address and validate it
#

import socket
import k_ip
import sys


def convert_domain(domain):
    try:
        getIP = socket.gethostbyname(domain)

        if getIP == "0.0.0.0":
            return False
            sys.exit(0)
        else:
            ipvResult = k_ip.validate_ipaddress(getIP)
            return getIP
    except socket.gaierror:
        print ("Domain "+domain+" cannot resolv\n")
        print ("It can be behind firewall, or register on private DNS")
        sys.exit(0)
