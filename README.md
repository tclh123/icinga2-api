# icinga2-api

![](https://img.shields.io/pypi/pyversions/icinga2py)

An icinga2 API client, see <http://docs.icinga.org/icinga2/latest/doc/module/icinga2/chapter/icinga2-api> to learn more about icinga2 API.

## Installation

```shell
pip install icinga2py
```

## Development Guide

```shell
make init
```

### Run Examples

```shell
. venv/bin/activate
cp examples/local_config.py.example examples/local_config.py
# edit examples/local_config.py
vi examples/local_config.py
python examples/example.py
```

## Icinga2 API Reference

```
perm, url, SUPPORTS FILTERS

actions/<action>        /v1/actions Yes
config/query            /v1/config  No
config/modify           /v1/config  No
objects/query/<type>    /v1/objects Yes
objects/create/<type>   /v1/objects No
objects/modify/<type>   /v1/objects Yes
objects/delete/<type>   /v1/objects Yes
status/query/<type>     /v1/status  Yes
events/<type>           /v1/events  No
console                 /v1/console No

---

base url = /v1

GET     /objects/<type>[/<fullname>]    attrs, joins, meta, filter
PUT     /objects/<type>/<fullname>      templates, attrs
POST    /objects/<type>/<fullname>      attrs
DELETE  /objects/<type>[/<fullname>]    cascade, filter

/actions/<action>

/events     ?
/status     ?
/console    session,command,sandboaxed

GET     /config/packages
POST    /config/packages/<package>
DELETE  /config/packages/<package>
POST    /config/stages/<package>           files(file => content pairs)
GET     /config/stages/<package>/<stage>
DELETE  /config/stages/<package>/<stage>
GET     /config/files/<package>/<stage>/<path>

GET /types/<objectname>

*notes: <type> has to be replaced with the plural name of the object type
```

## Usage

```python
from icinga2_api.api import Api
from pprint import pprint

# init api instance
api = Api(['config-master.localdomain', 'icinga-api1.localdomin', 'icinga-api2.localdomin'],
          (username, passwd),
          'path of your ca cert')

# /objects/hosts
print api.objects.hosts.get(attrs=["name"])
pprint(api.objects.hosts.get(attrs=["name"], filter='host.name == "sindar1a"'))

# /config/packages
pprint(api.config.packages.dae.post())
print api.config.packages.dae.delete()
pprint(api.config.packages.get())
pprint(api.config.stages.dae.url('sindar33a-1458219125-0').get())

## upload config file
files = {
    'zones.d/global-templates/dae.conf': '// Hello DAE yesyesyes',
    'zones.d/checker/dae.conf': '// Hello DAE',
}
pprint(api.config.stages.dae.post(files=files))

## clean old config package stages
MAX_STAGE_RESERVED = 3
r = api.config.packages.get()
for pkg in r.get('results', []):
    if pkg['name'] != 'dae':
        continue
    remove_cnt = max(len(pkg['stages']) - MAX_STAGE_RESERVED, 0)
    remove_stages = pkg['stages'][:remove_cnt]
    print 'going to remove', remove_stages
    for stage in remove_stages:
        api.config.stages.dae.url(stage).delete()
pprint(api.config.packages.get())
```

## NOTES

- only support Advanced Filters
- only support http basic auth
- I think there's bug in icinga2 api, that you better query to only one host(your cluster config master) when you need to manipulate config package
