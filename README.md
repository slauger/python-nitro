# python-nitro

Examples for connecting to the NITRO API for the Citrix NetScaler ADC with Python (using Requests)

## Usage

**Print out all lbvservers**
```
./cli.py https://ns01.customer.local get stat lbvserver
```

**Download a file with systemfile**
```
./cli.py https://ns01.customer.local get config systemfile --params 'args=filename:fullbackup.tgz,filelocation:%2Fvar%2Fns_sys_backup%2F'
```

## TODOs

- read username and password from configuration file
