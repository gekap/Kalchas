#!/usr/bin/python
#
# This script validate if the ip is version 4 or version 6
#

import ipaddress


def validate_ipaddress(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as errorCode:
        return False
