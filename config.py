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
import os.path
from ConfigParser import SafeConfigParser

add_args = {
  '--config': {
    'metavar': '<file>',
    'help': 'Path to the ini config file (default: ~/.netscaler.ini)',
    'type': str,
    'default': '~/.netscaler.ini',
    'required': False,
  },
  '--section': {
    'metavar': '<section>',
    'help': 'Section in the ini config file (default: netscaler)',
    'type': str,
    'default': 'netscaler',
    'required': False,
  },
}

def add_argument(parser, arg, params):
    parser.add_argument(
        arg,
        metavar=params['metavar'],
        type=params['type'],
        help=params['help'],
        default=params['default'],
        required=params['required']
    )

# add cli arguments
parser = argparse.ArgumentParser(description='command line arguments.')

# required arguments
parser.add_argument('host',
    metavar='<method>',
    help='HTTP method (get, post, put, delete)',
    type=str,
    default=None,
)
parser.add_argument('file',
    metavar='<endpoint>',
    help='NITRO API endpoint (config, stat)',
    type=str,
    default=None,
)

# optional arguments
for key in add_args:
  add_argument(parser, key, add_args[key])

# parse arguments
args = parser.parse_args()

# read configuration from ~/.netscaler.ini
cfgfile = os.path.expanduser(args.config)
section = args.section

if not os.path.isfile(cfgfile):
   raise Exception('required config does not exist')

config = SafeConfigParser()
config.read(cfgfile)

if config.has_option(section, 'url'):
    url = config.get(section, 'url')
else:
    raise Exception('no system url defined in config file')

if config.has_option(section, 'username'):
    username = config.get(section, 'username')
else:
    username = 'nsroot'

if config.has_option(section, 'password'):
    password = config.get(section, 'password')
else:
    password = 'nsroot'

if config.has_option(section, 'verify_ssl'):
   verify_ssl = config.getboolean(section, 'verify_ssl')
else:
    verify_ssl = True

with open(args.file, 'r') as socket:
  payload = file.read(socket)

print(payload)

# start nitro client
nitro_client = nitro.NitroClient(url, username, password)

# disable ssl verification if needed
nitro_client.set_verify(verify_ssl)

# do the request to the NITRO API
result = nitro_client.request(
    'post',
    endpoint='config',
    objecttype='macroapi',
    data=payload
)

# print result
try:
    print(result.json())
except:
    print(result)
