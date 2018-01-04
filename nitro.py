#!/usr/bin/env python

"""nitro.py: Client for the Citrix NetScaler NITRO API."""

__author__ = "Simon Lauger"
__copyright__ = "Copyright 2018, IT Consulting Simon Lauger"
__license__ = "Apache"
__version__ = "0.0.1"
__maintainer__ = "Simon Lauger"
__email__ = "simon@lauger.de"

import requests
import json

class NitroClient():
  def __init__(self, url, username, password):
    self._url      = url
    self._headers = {
      'X-NITRO-USER': username,
      'X-NITRO-PASS': password,
    }
    self._verify = False
    
  def set_url(self, url):
    self._url = url

  def set_username(self, username):
    self._headers['X-NITRO-USER'] = username

  def set_password(self, password):
    self._headers['X-NITRO-PASS'] = password

  def verify(self, verify):
    self._verify = verify

  def stat(self, objecttype, objectname = None, params = None):
    url = self._url + '/nitro/v1/stat/' + objecttype

    if objectname != None:
      url += '/' + objectname

    if params != None:
      url += '?args='

      if isinstance(params, dict):
        for key, value in params.iteritems():
          url += key + ":" + value
      else:
        url += params

    self._result = requests.get(
      url,
      headers=self._headers,
      verify=self._verify,
    )

    return self._result.json()

  def conf(self):
    return False

