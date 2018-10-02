#!/usr/bin/python
#
#This script search the BIN files for the given IP
#

import kalchas_headers
import os
import IP2Location
import IP2Proxy


#Initialize the main functions
Location2BIN = "IP2LOCATION-LITE-DB11.IPV6.BIN"
Proxy2BIN = "IP2PROXY-LITE-PX4.BIN"

proxy = IP2Proxy.IP2Proxy()
location = IP2Location.IP2Location()


#Get the real path which the bin files are saved
location.open(os.path.realpath(Location2BIN))
proxy.open(os.path.realpath(Proxy2BIN))


def check_ip(ip):

    #Get all results for the given IP from IP2Proxy Lite
    proxyResults = proxy.get_all(ip)

    #GEt all results for the given IP from IP2Location Lite
    locationResults = location.get_all(ip)
    
    proxyConfirmation = str(proxy.is_proxy(ip))

    #Check if there are no values in Proxy DB
    if proxyResults['isp'] == "-":
        proxyResults['isp'] = "-"

   # if proxyResults['country_log'] == "-":
   #     proxyResults['country_log'] = "-"
    
    if proxyResults['region'] == "-":
        proxyResults['region'] ="-"
    
    if proxyResults['city'] == "-":
        proxyResults['city'] = "-"


    if proxyConfirmation == "0":
        #The ip is not in Proxy database, and probable is real ip
        kalchas_headers.location_headers()
        print (locationResults.country_long.decode('ascii').ljust(10), locationResults.region.decode('ascii').ljust(10), locationResults.city.decode('ascii').ljust(10), locationResults.zipcode.decode('ascii').ljust(10), str(locationResults.longitude).ljust(10), str(locationResults.latitude).ljust(10))

        #The IP is on Proxy Database
    if proxyConfirmation == "1":
        #Check the proxy type
        if proxyResults['proxy_type'] == "PUB":

            kalchas_headers.proxy_headers()
            print (proxyResults['proxy_type'].ljust(10), proxyResults['country_long'].ljust(10), proxyResults['region'].ljust(10), proxyResults['city'].ljust(10), proxyResults['isp'].ljust(10), str(locationResults.longitude).ljust(10), str(locationResults.latitude).ljust(10))
        
        if proxyResults['proxy_type'] == "TOR":
            kalchas_headers.misc_headers()
            print (proxyResults['proxy_type'].ljust(10), locationResults.country_long.decode('ascii').ljust(10), locationResults.region.decode('ascii').ljust(10), locationResults.city.decode('ascii').ljust(10), locationResults.zipcode.decode('ascii').ljust(10), str(locationResults.longitude).ljust(10), str(locationResults.latitude).ljust(10))

        if proxyResults['proxy_type'] == "VPN":
            kalchas_headers.misc_headers()
            print (proxyResults['proxy_type'].ljust(10), locationResults.country_long.decode('ascii').ljust(10), locationResults.region.decode('ascii').ljust(10), locationResults.city.decode('ascii').ljust(10), locationResults.zipcode.decode('ascii').ljust(10), str(locationResults.longitude).ljust(10), str(locationResults.latitude).ljust(10))

    #The IP is DHC
    if proxyConfirmation == "2":
        kalchas_headers.misc_headers()
        print (proxyResults['proxy_type'].ljust(10), locationResults.country_long.decode('ascii').ljust(10), locationResults.region.decode('ascii').ljust(10), locationResults.city.decode('ascii').ljust(10), locationResults.zipcode.decode('ascii').ljust(10), str(locationResults.longitude).ljust(10), str(locationResults.latitude).ljust(10))


