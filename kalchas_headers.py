#!/usr/bin/python
#
# Setup the print headers
#

def location_headers():
    print ("---------------------------------------------------------------------------")
    print ("Country".ljust(10), "City".ljust(10), "Region".ljust(10), "Zip Code".ljust(10), "Longitude".ljust(10),"Latitude".ljust(10))
    print ("---------------------------------------------------------------------------\n")


def proxy_headers():
    print ("---------------------------------------------------------------------------")
    print ("Proxy Type".ljust(10), "Country".ljust(10), "Region".ljust(10), "City".ljust(10), "ISP".ljust(10), "Longitude".ljust(10), "Latitude".ljust(10))
    print ("---------------------------------------------------------------------------\n")


def misc_headers():
    print ("---------------------------------------------------------------------------")
    print ("Proxy Type".ljust(10),"Country".ljust(10),"Region".ljust(10),"City".ljust(10),"Zip Code".ljust(10),"Longitude".ljust(10),"Latitude".ljust(10))
    print ("---------------------------------------------------------------------------\n")


