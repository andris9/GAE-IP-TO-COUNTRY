# NB! No need to use this module anymore

Since SDK 1.5.1 you can use `X-AppEngine-country` request header (returns a two letter country code or ZZ for unknow locations) to retriev the country of the visitor, no need for external modules anymore.

IP to Country
=============

*IP to Country* is a Google App Engine module (Python) to convert IP addresses into country names and country codes.

License
-------

This module is provided FREE under the terms of the GENERAL PUBLIC LICENSE, June 1991

 - This product is a Google App Engine port of http://www.phptutorial.info/iptocountry/the_script.html
 - This product includes IP to Country database from http://software77.net/cgi-bin/ip-country/geo-ip.pl

Usage
-----

    sys.path.insert(0, 'iptocountry.zip')
    from iptocountry import convert as iptolocation, country as iptocountry

    location = iptolocation()
    country = iptocountry()

    print "You are from %s (country code - %s)" % (country, location)

Updating
--------

To update the database, upzip the PHP files from http://www.phptutorial.info/iptocountry/ip_files.zip to /*src/ip_files*. Then run *parser.php* which generates new .PY files to *src/iptocountry*. Zip the directory *src/iptocountry* to *iptocountry.zip* and use the file instead of the old one in your projects.

Comments
--------

*IP to Country* does not use database but a collection of files to find the country for a particular IP address. Google App Engine has a limit of 1000 files per application so it is highly encouraged to ZIP all the module files into one bigger file. See *build* for an example.