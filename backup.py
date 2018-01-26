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

# start nitro client
nitro_client = nitro.NitroClient(url, username, password)

# disable ssl verification if needed
nitro_client.set_verify(verify_ssl)

# do the request to the NITRO API
result = nitro_client.request(
    method=args.method,
    endpoint=args.endpoint,
    objecttype=args.object,
    objectname=args.name,
    params=args.params
)

# todo: decode base64, write to file

# print result
try:
    print(result.json())
except:
    print(result)
