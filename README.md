# Kalchas
It is python script on which you can get details for a given IP or Domain

# Brief Description
It is a command line script written in python 3.6 which provide details for IP address or Domain mode.


# Detail Description
This python script take two arguments ip address (support IPv4 or IPv6) or a domain (without the protocol) and provide details.
It uses 2 LITE Databases IP2LOCATION-LITE-DB11.IPV6.BIN and IP2PROXY-LITE-PX4.BIN .

First it check in IP2Proxy database if the IP or Domain is register as Proxy/VPN/TOR/DHC or not by searching in IP2PROXY-LITE-PX4.BIN.
If the result is 0 the script search on IP2LOCATION-LITE-DB11.IPV6.BIN and provide details like the Country, Region, Langitude/Latitude etc.

# Installation

First you need to install IP2Location and IP2Proxy modules.
- IP2Location-Python-master.zip
- ip2proxy-python-master.zip

Unzip the files and then run sudo python setup.py install 
```
$ cd ~/ip2proxy-python-master
```
```
$ sudo python3 setup.py install
```
```
$ cd ~/IP2Location-Python-master/
```
```
$ sudo python3 setup.py install
```

The above commands will install the modules for IP2Location and IP2Proxy.

Ungzip the bin files
```
$ gzip -d IP2LOCATION-LITE-DB11.IPV6.BIN.gz
```
```
$ gzip -d IP2PROXY-LITE-PX4.BIN.gz
```
Second requirement is ipaddress.

From the command line run 
```
$ python -m "ipaddress"
```
If you get error "/usr/lib/python-exec/python3.6/python: No module named  ipaddress" then you need to install ipaddress 
on your system.



Examples:

Using a domain
```
$ python3 kalchaspy -server giwma.asuscomm.com
---------------------------------------------------------------------------
Country    City       Region     Zip Code   Longitude  Latitude  
---------------------------------------------------------------------------

Greece     Attiki     Athens     167 77     23.716221  37.97945  
```
Using an IP address
```
$ python3 kalchas.py -ipaddr 185.220.101.45
---------------------------------------------------------------------------
Proxy Type Country    Region     City       Zip Code   Longitude  Latitude  
---------------------------------------------------------------------------

TOR        United Kingdom England    Bristol    BS1 4UA    -2.59665   51.455231 
```
