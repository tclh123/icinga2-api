#!/usr/bin/env python
# coding: utf-8

import logging
from pprint import pprint

from icinga2_api.api import Api
from examples.config import (ICINGA_HOSTS,
                             ICINGA_AUTH,
                             ICINGA_CACERT)

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s')

api = Api(ICINGA_HOSTS,
          ICINGA_AUTH,
          ICINGA_CACERT)

# print api.objects.hosts.get(attrs=["name"])
pprint(api.objects.hosts.get(attrs=["name"], filter='host.name == "sindar1a"'))

pprint(api.config.packages.dae.post())
# print api.config.packages.dae.delete()
pprint(api.config.packages.get())

files = {
    'zones.d/global-templates/dae.conf': '// Hello DAE yesyesyes',
    'zones.d/checker/dae.conf': '// Hello DAE',
}
pprint(api.config.stages.dae.post(files=files))

"""
{u'results': [{u'attrs': {u'name': u'sindar1a'},
               u'joins': {},
               u'meta': {},
               u'name': u'sindar1a',
               u'type': u'Host'}]}
{'Error': u'cannot parse json: {"error":500.0,"status":"Could not create package."}{"results":[{"code":200.0,"status":"Created package."}]}'}
{u'results': [{u'active-stage': u'sindar33a-1456295880-0',
               u'name': u'_api',
               u'stages': [u'sindar33a-1456295880-0']},
              {u'active-stage': u'sindar33a-1458203812-0',
               u'name': u'dae',
               u'stages': [u'sindar33a-1458203812-0']}]}
{u'results': [{u'code': 200.0,
               u'package': u'dae',
               u'stage': u'sindar33a-1458203964-0',
               u'status': u'Created stage.'}]}
"""
