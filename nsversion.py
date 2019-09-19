#!/usr/bin/env python
#
# parses the netscaler rss feed from citrix.com and  returns all 
# available releases and the latest available build for each release.
# 
# @author: Simon Lauger <simon@lauger.name>
# @date:   2018-03-11

import requests
import feedparser
import re

class nsversion:
  # RSS feed for Citrix NetScaler releases
  url = 'https://www.citrix.com/content/citrix/en_us/downloads/netscaler-adc.rss'

  # New - NetScaler Release (Feature Phase) 12.0 Build 57.19
  # New - NetScaler Release (Maintenance Phase) 11.1 Build 57.11
  pattern= 'New \- NetScaler Release( \(Feature Phase\)| \(Maintenance Phase\))? (1[012]\.[0-9]) Build ([0-9]{2}\.[0-9]{1,2})'

  # All major releases and latest available build per major version
  releases = {}

  def __init__(self):
    self.feed  = feedparser.parse(self.url)
    self.regex = re.compile(self.pattern)
    self.parse()

  def parse(self):
    for item in self.feed['items']:
      matches = self.regex.match(item['title'])
      if matches:
        if not matches.group(2) in self.releases:
          self.releases[matches.group(2)] = matches.group(3)

  def get(self, major = None):
    if major == None:
      print(str(self.releases))
    else:
      print(self.releases[major])

instance = nsversion().get()
