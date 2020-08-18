#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import six.moves.urllib.parse as urlparse
from requests import Session
from requests.adapters import HTTPAdapter


class Requester:

    """
    A class which carries out HTTP requests. You can replace this
    class with one of your own implementation if you require some other
    way to access SonarQube.

    This default class can handle simple authentication only.
    """

    VALID_STATUS_CODES = [200, ]
    AUTH_COOKIE = None

    def __init__(self, *args, **kwargs):

        username = None
        password = None
        token = None
        timeout = 10

        if len(args) == 1:
            token, = args
        elif len(args) == 2:
            username, password = args

        baseurl = kwargs.get('baseurl')
        self.base_scheme = urlparse.urlsplit(baseurl).scheme if baseurl else None
        self.username = kwargs.get('username', username)
        self.password = kwargs.get('password', password)
        self.token = kwargs.get('token', token)
        self.ssl_verify = kwargs.get('ssl_verify')
        self.cert = kwargs.get('cert')
        self.timeout = kwargs.get('timeout', timeout)
        self.session = Session()

        self.max_retries = kwargs.get('max_retries')
        if self.max_retries is not None:
            retry_adapter = HTTPAdapter(max_retries=self.max_retries)
            self.session.mount('http://', retry_adapter)
            self.session.mount('https://', retry_adapter)

    def get_request_dict(self, params=None, data=None, files=None, headers=None, **kwargs):
        requestKwargs = kwargs
        if self.token:
            requestKwargs['auth'] = self.token, ''
        elif self.username and self.password:
            requestKwargs['auth'] = (self.username, self.password)

        if params:
            assert isinstance(
                params, dict), 'Params must be a dict, got %s' % repr(params)
            requestKwargs['params'] = params

        if headers:
            assert isinstance(
                headers, dict), \
                'headers must be a dict, got %s' % repr(headers)
            requestKwargs['headers'] = headers

        if self.AUTH_COOKIE:
            currentheaders = requestKwargs.get('headers', {})
            currentheaders.update({'Cookie': self.AUTH_COOKIE})
            requestKwargs['headers'] = currentheaders

        requestKwargs['verify'] = self.ssl_verify
        requestKwargs['cert'] = self.cert

        if data:
            # It may seem odd, but some SonarQube operations require posting
            # an empty string.
            requestKwargs['data'] = data

        if files:
            requestKwargs['files'] = files

        requestKwargs['timeout'] = self.timeout

        return requestKwargs

    def _update_url_scheme(self, url):
        """
        Updates scheme of given url to the one used in SonarQube baseurl.
        """
        if self.base_scheme and not url.startswith("%s://" % self.base_scheme):
            url_split = urlparse.urlsplit(url)
            url = urlparse.urlunsplit(
                [
                    self.base_scheme,
                    url_split.netloc,
                    url_split.path,
                    url_split.query,
                    url_split.fragment
                ]
            )
        return url

    def get(self, url, params=None, headers=None, allow_redirects=True, stream=False):
        requestKwargs = self.get_request_dict(
            params=params,
            headers=headers,
            allow_redirects=allow_redirects,
            stream=stream
        )
        return self.session.get(self._update_url_scheme(url), **requestKwargs)

    def post(self, url, params=None, data=None, files=None, headers=None, allow_redirects=True, **kwargs):
        requestKwargs = self.get_request_dict(
            params=params,
            data=data,
            files=files,
            headers=headers,
            allow_redirects=allow_redirects,
            **kwargs)
        return self.session.post(self._update_url_scheme(url), **requestKwargs)
