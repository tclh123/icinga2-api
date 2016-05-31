#!/usr/bin/env python
# coding: utf-8

import json
import logging
import warnings
import requests

logger = logging.getLogger(__name__)


class Api(object):

    class _RequestMaker(object):
        HTTP_METHODS = ('GET', 'POST', 'PUT', 'DELETE')

        def __init__(self, api, url):
            self._api = api
            self._url = url

        def __getattr__(self, attr):
            if attr == 'url':
                def _func_url(url):
                    self._url += '/%s' % url
                    return self
                return _func_url
            if attr.upper() in self.HTTP_METHODS:
                def _func_call(**kw):
                    res = None
                    for i in range(len(self._api._hosts)):
                        host = self._api._hosts[0]
                        try:
                            res = self._api._request(attr, self._url, kw, host=host)
                            return res
                        except requests.exceptions.RequestException as e:
                            res = e
                            logger.warn('request %s error: %s' % (host, e))
                            pass
                        except Exception:
                            raise
                    return {'Error': 'failed on all hosts, last fail: %s' % res}
                return _func_call
            self._url += '/%s' % attr
            return self

    def __init__(self, hosts, auth, cacert, port=5665, url_prefix='/v1',
                 ignore_python_warnings=True, timeout=None):
        self._hosts = list(hosts)
        self._auth = tuple(auth)
        self._cacert = cacert
        self._url_base_pattern = ('https://%s:{port}/{url_prefix}'
                                  .format(port=port,
                                          url_prefix=url_prefix.strip('/')))
        self._ignore_python_warnings = ignore_python_warnings
        self._timeout = timeout

    def _request(self, method, url, data, host=None):
        if not host:
            host = self._hosts[0]
        url_base = self._url_base_pattern % host
        # rotate
        self._hosts = self._hosts[1:] + [self._hosts[0]]
        url = '%s/%s' % (url_base, url)
        headers = {
            'Accept': 'application/json',
            'X-HTTP-Method-Override': method.upper(),
        }
        logger.info('request: %s %s %s' % (method, url, data))
        with warnings.catch_warnings():
            if self._ignore_python_warnings:
                warnings.simplefilter('ignore')
            r = requests.post(url,
                              headers=headers,
                              auth=self._auth,
                              data=json.dumps(data),
                              verify=self._cacert,
                              timeout=self._timeout)
        try:
            res = r.json()
        except:
            res = {'Error': "cannot parse json: %s" % r.text}
        return res

    def __getattr__(self, attr):
        return self._RequestMaker(self, attr)
