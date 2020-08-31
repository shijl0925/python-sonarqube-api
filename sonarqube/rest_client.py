#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import requests
from six.moves.urllib.parse import urlencode


class RestClient:
    default_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def __init__(self, url, username=None, password=None, token=None, verify_ssl=None, cookies=None,
                 proxies=None, cert=None, allow_redirects=True, timeout=None):
        self.url = url
        self.username = username
        self.password = password
        self.token = token
        self.verify_ssl = verify_ssl
        self.cookies = cookies
        self.proxies = proxies
        self.cert = cert
        self.allow_redirects = allow_redirects
        self.timeout = int(timeout)
        self._session = requests.Session()

        if token:
            self._session.auth = (token, '')
        elif username and password:
            self._session.auth = (username, password)

        if cookies is not None:
            self._session.cookies.update(cookies)

    def request(self, method='GET', path='/', data=None, json=None, params=None, headers=None, files=None):
        """
        :param method:
        :param path:
        :param data:
        :param json:
        :param params:
        :param headers:
        :param files:
        :return:
        """
        url = self.url_joiner(self.url, path)
        if params:
            url += '?'
            url += urlencode(params or {})

        if files is None:
            data = None if not data else json.dumps(data)

        headers = headers or self.default_headers
        response = self._session.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            json=json,
            timeout=self.timeout,
            verify=self.verify_ssl,
            files=files,
            proxies=self.proxies,
            cert=self.cert,
            allow_redirects=self.allow_redirects
        )
        response.encoding = 'utf-8'

        response.raise_for_status()
        return response

    @staticmethod
    def url_joiner(url, path):
        url_link = '/'.join(s.strip('/') for s in [url, path])
        return url_link

    def get(self, path, data=None, params=None, headers=None):
        """
        Get request based on the python-requests module. You can override headers, and also, get not json response
        :param path:
        :param data:
        :param params:
        :param headers:
        :return:
        """
        response = self.request('GET', path=path, params=params, data=data, headers=headers)
        return response

    def post(self, path, data=None, json=None, headers=None, files=None, params=None):
        response = self.request('POST', path=path, data=data, json=json, headers=headers, files=files, params=params)

        return response

    def put(self, path, data=None, headers=None, files=None, params=None):
        response = self.request('PUT', path=path, data=data, headers=headers, files=files, params=params)

        return response

    def delete(self, path, data=None, headers=None, params=None):
        """
        Deletes resources at given paths.
        :rtype: dict
        :return: Empty dictionary to have consistent interface.
        Some of Atlassian REST resources don't return any content.
        """
        response = self.request('DELETE', path=path, data=data, headers=headers, params=params)

        return response
