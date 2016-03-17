#!/usr/bin/env python
# coding: utf-8

import logging

from icinga2_api.api import Api
from examples.config import (ICINGA_HOSTS,
                             ICINGA_AUTH,
                             ICINGA_CACERT)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

api = Api(ICINGA_HOSTS,
          ICINGA_AUTH,
          ICINGA_CACERT)

print api.objects.hosts.get(attrs=["name"])
print api.objects.hosts.get(attrs=["name"], filter='host.name == "sindar1a"')
