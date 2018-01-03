#!/usr/bin/env python

"""nitro_client.py: Client for the Citrix NetScaler NITRO API."""

__author__ = "Simon Lauger"
__copyright__ = "Copyright 2018, IT Consulting Simon Lauger"
__license__ = "Apache"
__version__ = "0.0.1"
__maintainer__ = "Simon Lauger"
__email__ = "simon@lauger.de"

import argparse
import requests
import json

# todos:
# - add inifile
# - use choices (e.g. for ssl)
add_args = {
  '--hostname': {
    'metavar': '<hostname>',
    'help': 'Hostname of the NetScaler appliance to connect to',
    'type': str,
    'default': False,
    'required': True,
  },
  '--username': {
    'metavar': '<username>',
    'help': 'Username to log into box as (default: nsroot)',
    'type': str,
    'default': 'nsroot',
    'required': False,
  },
  '--password': {
    'metavar': '<password>',
    'help': 'Password for login username (default: nsroot)',
    'type': str,
    'default': 'nsroot',
    'required': False,
  },
  '--objecttype': {
    'metavar': '<objecttype>',
    'help': 'Objecttype (target) to for the check command',
    'type': str,
    'default': '',
    'required': False,
  },
  '--objectname': {
    'metavar': '<objectname>',
    'help': 'Filter request to a specific objectname',
    'type': str,
    'default': '',
    'required': False,
  },
  '--endpoint': {
    'metavar': '<config|stat>',
    'help': 'NITRO API endpoint (default: stat)',
    'type': str,
    'default': 'stat',
    'required': False,
  },
  '--ssl': {
    'metavar': '<true|false>',
    'help': 'Establish connection to NetScaler using SSL',
    'type': str,
    'default': 'nsroot',
    'required': False,
  },
  '--api': {
    'metavar': '<v1|v2>',
    'help': 'Establish connection to NetScaler using SSL',
    'type': str,
    'default': 'nsroot',
    'required': False,
  },
  '--verify': {
    'metavar': '<true|false>',
    'help': 'Verify the ssl certificate of the target machine (default: false)',
    'type': str,
    'default': False,
    'required': False,
  }
}

def add_argument(parser, arg, params):
  parser.add_argument(
    arg, metavar=params['metavar'],
    type=params['type'],
    help=params['help'],
    default=params['default'],
    required=params['required']
  )

def nitro_client(args):
  if args.ssl == True:
    protocol = "https://"
  else:
    protocol = "http://"
  headers = {
    'X-NITRO-USER': args.username,
    'X-NITRO-PASS': args.password,
    'Content-Type': 'application/vnd.com.citrix.netscaler.' + args.objecttype + '+json',
  }
  port = ""
  api_version = "v1"
  url = protocol + args.hostname + port + "/nitro/" + api_version + "/" + args.endpoint + "/" + args.objecttype
  data = {}
  response = requests.get(url, headers=headers, data=data, verify=False)

  return response.json()

# add cli arguments
parser = argparse.ArgumentParser(description='command line add_args.')
for key in add_args:
  add_argument(parser, key, add_args[key])
args = parser.parse_args()

print(nitro_client(args))
