#
# IP TO COUNTRY
# Google App Engine port from http://www.phptutorial.info/iptocountry/the_script.html
# Uses IP to Country database from http://software77.net/cgi-bin/ip-country/geo-ip.pl
# 
# This database is provided FREE under the terms of the GENERAL PUBLIC LICENSE,
# June 1991
#

from google.appengine.api import memcache
import sys
import os

from countries import countries

#
# covert(ip=False) -> String
# - ip (String): IP address, if not set visitor IP is used
#
# Converts an IP to a two-letter country code
# 
def convert(ip=False):
    if not ip:
        ip = os.environ['REMOTE_ADDR']
    location = memcache.get("ip_%s" % ip)
    if location is not None:
        return location
    numbers = ip.split(".")
    sys.path.append(os.path.dirname(__file__))
    r = __import__("ip%s" % numbers[0])
    code = (int(numbers[0]) * 16777216) + (int(numbers[1]) * 65536) + (int(numbers[2]) * 256) + (int(numbers[3]))   
    for z in r.ranges:
        if int(z)<=code and int(r.ranges[z][0])>=code:
            location = r.ranges[z][1]
            # Serbia and Motenegro, Yugoslavia -> Serbia 
            if location == "CS" or location == "YU":
                location = "RS"
     
            memcache.set("ip_%s" % ip, location, 3600*24*60)
            return location
    memcache.set("ip_%s" % ip, "ZZ", 3600*24*60)
    return "ZZ"

#
# country(ip=False) -> String
# - ip (String): IP address, if not set visitor IP is used
#
# Converts an IP to a country name
#
def country(ip=False):
    location = convert(ip)
    if not location in countries:
        location="ZZ"
    return countries[location][1]