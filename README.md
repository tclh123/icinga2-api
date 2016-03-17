# icinga2-api

An icinga2 API client, see <http://docs.icinga.org/icinga2/latest/doc/module/icinga2/chapter/icinga2-api> to learn more about icinga2 API.

## development guide

```
virtualenv venv
. venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools
pip install -e . --process-dependency-links
```

### run examples

```
. venv/bin/activate
cp examples/local_config.py.example examples/local_config.py
# edit examples/local_config.py
vi examples/local_config.py
python examples/example.py
```

## icinga2 API reference

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

```
from icinga2_api.api import Api

api = Api(ICINGA_HOSTS,
          ICINGA_AUTH,
          ICINGA_CACERT)

print api.objects.hosts.get(attrs=["name"])
print api.objects.hosts.get(attrs=["name"], filter='host.name == "sindar1a"')
```

## NOTES

- only support Advanced Filters
- only support http basic auth
- I think there's bug in icinga2 api, that you better query to only one host(your cluster config master) when you need to manipulate config package
