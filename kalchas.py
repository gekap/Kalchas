#!/usr/bin/python
#
#This is the main script to get details for the ip or the domain
#

import argparse
import k_domain
import k_ip
import k_checkIP
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-ipaddr", help="Support IPv4 or IPv6")
parser.add_argument("-server", help="Add the FQDN of the server without the protocol")
args = parser.parse_args()

if args.server:
    ip = k_domain.convert_domain(args.server)
    k_checkIP.check_ip(ip)

if args.ipaddr:
    ip = k_ip.validate_ipaddress(args.ipaddr)
    if ip is False:
        print("This is an invalid address.")
        sys.exit(1)
    else:
        ip = args.ipaddr
        k_checkIP.check_ip(ip)
