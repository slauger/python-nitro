# python-nitro

Examples for connecting to the NITRO API for the Citrix NetScaler ADC with Python (using Requests)

## Config

```
[netscaler]
url = https://netscaler.customer.local
verify_ssl = True
username = nsroot
password = nsroot
```

## Usage

**Print out all lbvservers**
```
./cli.py get stat lbvserver
```

**Download a file with systemfile**
```
./cli.py get config systemfile --params 'args=filename:fullbackup.tgz,filelocation:%2Fvar%2Fns_sys_backup%2F'
```

**Push bulk configuration**
```
./config.py post configs/xenmobile-01.json
./config.py put configs/xenmobile-02.json
```

## Hints

- [Use DHCP for inital bootstrap process](https://docs.citrix.com/ja-jp/netscaler/11/netscaler-hardware-installation/netscaler-initial-configuration.html)
