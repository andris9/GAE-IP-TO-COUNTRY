#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import sys
import logging
logging.error("moh");
sys.path.insert(0, 'iptocountry.zip')
from iptocountry import convert as iptolocation, country as iptocountry

class MainHandler(webapp.RequestHandler):

  def get(self):
    location = iptolocation()
    country = iptocountry()
    note = "You are from <strong>%s</strong> (country code - <strong>%s</strong>)";
    self.response.out.write(note % (country, location))
    self.response.out.write("""
<p>Download from <a href="http://github.com/andris9/GAE-IP-TO-COUNTRY">Github</a></p>
""")

def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
