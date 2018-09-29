#!/usr/bin/python
#
# This script convert a domain to ip address and validate it
#

import socket
import k_ip


def convert_domain(domain):
    getIP = socket.gethostbyname(domain)

    if getIP == "0.0.0.0":
        return False
    else:
        ipvResult = k_ip.validate_ipaddress(getIP)
        return getIP

