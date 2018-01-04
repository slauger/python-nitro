#!/usr/bin/env python

"""cli.py: Client for the Citrix NetScaler NITRO API."""

__author__ = "Simon Lauger"
__copyright__ = "Copyright 2018, IT Consulting Simon Lauger"
__license__ = "Apache"
__version__ = "0.0.1"
__maintainer__ = "Simon Lauger"
__email__ = "simon@lauger.de"

import argparse
import nitro

add_args = {
  '--url': {
    'metavar': '<hostname>',
    'help': 'URL to NetScaler appliance to connect to',
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
    'default': None,
    'required': True,
  },
  '--objectname': {
    'metavar': '<objectname>',
    'help': 'Filter request to a specific objectname',
    'type': str,
    'default': None,
    'required': False,
  },
  '--params': {
    'metavar': '<objectname>',
    'help': 'Additional arguments for the request (e.g. name:foo)',
    'type': str,
    'default': None,
    'required': False,
  },
  '--endpoint': {
    'metavar': '<config|stat>',
    'help': 'NITRO API endpoint (default: stat)',
    'type': str,
    'default': 'stat',
    'required': False,
  },
  '--verify': {
    'metavar': '<true|false>',
    'help': 'Verify the ssl certificate of the target machine (default: false)',
    'type': bool,
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

# add cli arguments
parser = argparse.ArgumentParser(description='command line add_args.')
for key in add_args:
  add_argument(parser, key, add_args[key])
args = parser.parse_args()

# start nitro client
nitro_client = nitro.NitroClient(args.url, args.username, args.password)
nitro_client.verify(args.verify)
print(nitro_client.stat(args.objecttype, args.objectname, args.params))
