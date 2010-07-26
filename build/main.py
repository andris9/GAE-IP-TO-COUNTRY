#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import sys
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
