#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .common import expand_url
import requests
from .exceptions import ClientError, AuthError, ValidationError, ServerError

from .users import SonarQubeUser
from .projects import SonarQubeProject
from .user_groups import SonarQubeUser_Groups
from .issues import SonarQubeIssue
from .measures import SonarQubeMeasure
from .notifications import SonarQubeNotification
from .project_links import SonarQubeProject_Links
from .permissions import SonarQubePermissions
from .ce import SonarQubeCe
from .project_branches import SonarQubeProject_Branches
from .qualitygates import SonarQubeQualityGates


class SonarAPIHandler(object):
    # Default host is local
    DEFAULT_HOST = 'http://localhost'
    DEFAULT_PORT = 9000
    DEFAULT_BASE_PATH = ''

    def __init__(self, sonarqube_url=None, user=None, password=None,
                 base_path=None, token=None):
        """
        Set connection info and session, including auth (if user+password
        and/or auth token were provided).
        """
        self._sonarqube_url = sonarqube_url or '{}:{}'.format(self.DEFAULT_HOST,self.DEFAULT_PORT)
        self._base_path = base_path or self.DEFAULT_BASE_PATH
        self._session = requests.Session()

        # Prefer revocable authentication token over username/password if
        # both are provided
        if token:
            self._session.auth = token, ''
        elif user and password:
            self._session.auth = user, password

    def __str__(self):
        return '{}'.format(self._sonarqube_url)

    def _get_url(self, endpoint):
        """
        Return the complete url including host and port for a given endpoint.

        :param endpoint: service endpoint as str
        :return: complete url (including host and port) as str
        """
        return '{}{}{}'.format(self._sonarqube_url, self._base_path, endpoint)

    def _make_call(self, method, endpoint, **data):
        """
        Make the call to the service with the given method, queryset and data,
        using the initial session.

        Note: data is not passed as a single dictionary for better testability
        (see https://github.com/kako-nawao/python-sonarqube-api/issues/15).

        :param method: http method (get, post, put, patch)
        :param endpoint: relative url to make the call
        :param data: queryset or body
        :return: response
        """
        # Get method and make the call
        call = getattr(self._session, method.lower())
        base_url = self._get_url(endpoint)
        url = expand_url(base_url, params=data or {})

        res = call(url)
        # Analyse response status and return or raise exception
        # Note: redirects are followed automatically by requests
        if res.status_code < 300:
            # OK, return http response
            return res

        elif res.status_code == 400:
            # Validation error
            msg = ', '.join(e['msg'] for e in res.json()['errors'])
            raise ValidationError(msg)

        elif res.status_code in (401, 403):
            # Auth error
            raise AuthError(res.reason)

        elif res.status_code < 500:
            # Other 4xx, generic client error
            raise ClientError(res.reason)

        else:
            # 5xx is server error
            raise ServerError(res.reason)

    @property
    def users(self):
        return SonarQubeUser(self)

    @property
    def user_groups(self):
        return SonarQubeUser_Groups(self)

    @property
    def projects(self):
        return SonarQubeProject(self)

    @property
    def measures(self):
        return SonarQubeMeasure(self)

    @property
    def issues(self):
        return SonarQubeIssue(self)

    @property
    def notifications(self):
        return SonarQubeNotification(self)

    @property
    def project_links(self):
        return SonarQubeProject_Links(self)

    @property
    def permissions(self):
        return SonarQubePermissions(self)

    @property
    def ce(self):
        return SonarQubeCe(self)

    @property
    def project_branches(self):
        return SonarQubeProject_Branches(self)

    @property
    def qualitygates(self):
        return SonarQubeQualityGates(self)
