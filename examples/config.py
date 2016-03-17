#!/usr/bin/env python
# coding: utf-8

ICINGA_HOSTS = ['', '']
ICINGA_AUTH = ('', '')
ICINGA_CACERT = ''

try:
    from .local_config import *  # NOQA
except:
    pass
