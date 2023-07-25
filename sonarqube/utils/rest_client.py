#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import json as js
from sonarqube.utils.exceptions import (
    ClientError,
    AuthError,
    NotFoundError,
    ValidationError,
    ServerError,
)


class RestClient(object):
    """
    rest request

    """

    default_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    default_timeout = 60
    special_attributes_map = {}
    MAX_SEARCH_NUM = 10000

    def __init__(self, api):
        self.api = api

    def request(
        self,
        method="GET",
        path="/",
        data=None,
        json=None,
        params=None,
        headers=None,
        files=None,
    ):
        """
        http request

        :param method:
        :param path:
        :param data:
        :param json:
        :param params:
        :param headers:
        :param files:
        :return:
        """
        url = self.url_joiner(self.api.base_url, path)

        timeout = self.api.timeout or self.default_timeout

        res = self.api.session.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            data=data,
            json=json,
            files=files,
            timeout=timeout,
        )
        res.encoding = "utf-8"

        error_message = "Error in request. "
        if res.status_code < 300:
            # OK, return http response
            return res

        # raise error. res.raise_for_status()
        elif res.status_code == 400:
            # Validation error
            msg = error_message + "Possibly validation error [%s]: %s" % (
                res.status_code,
                ", ".join(e["msg"] for e in res.json()["errors"]),
            )

            raise ValidationError(msg)

        elif res.status_code in (401, 403):
            # Auth error
            msg = error_message + "Possibly authentication failed [%s]: %s" % (
                res.status_code,
                res.reason,
            )
            if res.text:
                msg += "\n" + res.text

            raise AuthError(msg)

        elif res.status_code == 404:
            # Not Found error
            msg = error_message + "Possibly Not Found error [%s]: %s" % (
                res.status_code,
                ", ".join(e["msg"] for e in res.json()["errors"]),
            )

            raise NotFoundError(msg)

        elif res.status_code < 500:
            # Other 4xx, generic client error
            msg = error_message + "Possibly client error [%s]: %s" % (
                res.status_code,
                ", ".join(e["msg"] for e in res.json()["errors"]),
            )

            raise ClientError(msg)

        else:
            # 5xx is server error
            msg = error_message + "Possibly server error [%s]: %s" % (
                res.status_code,
                res.reason,
            )

            raise ServerError(msg)

    @staticmethod
    def url_joiner(url, path):
        """
        create url

        :param url:
        :param path:
        :return:
        """
        url_link = "/".join(s.strip("/") for s in [url, path])
        return url_link

    def _get(self, path, data=None, params=None, headers=None):
        """
        Get request based on the python-requests module.

        :param path:
        :param data:
        :param params:
        :param headers:
        :return:
        """
        return self.request("GET", path=path, params=params, data=data, headers=headers)

    def _post(self, path, data=None, json=None, headers=None, files=None, params=None):
        """
        Post request based on the python-requests module.

        :param path:
        :param data:
        :param json:
        :param headers:
        :param files:
        :param params:
        :return:
        """
        return self.request(
            "POST",
            path=path,
            data=data,
            json=json,
            headers=headers,
            files=files,
            params=params,
        )

    def _put(self, path, data=None, headers=None, files=None, params=None):
        """
        Post request based on the python-requests module.

        :param path:
        :param data:
        :param headers:
        :param files:
        :param params:
        :return:
        """
        return self.request(
            "PUT", path=path, data=data, headers=headers, files=files, params=params
        )

    def _delete(self, path, data=None, headers=None, params=None):
        """
        Delete request based on the python-requests module.

        :param path:
        :param data:
        :param headers:
        :param params:
        :return:
        """
        return self.request(
            "DELETE", path=path, data=data, headers=headers, params=params
        )
