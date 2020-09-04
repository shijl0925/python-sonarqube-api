#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from .exceptions import ClientError, AuthError, ValidationError, ServerError
from .requester import Requester
from .users import SonarQubeUser
from .projects import SonarQubeProject
from .user_groups import SonarQubeUserGroups
from .issues import SonarQubeIssues
from .measures import SonarQubeMeasure
from .notifications import SonarQubeNotification
from .project_links import SonarQubeProjectLinks
from .permissions import SonarQubePermissions
from .ce import SonarQubeCe
from .project_branches import SonarQubeProjectBranches
from .qualitygates import SonarQubeQualityGates
from .components import SonarQubeComponents
from .rules import SonarQubeRules
from .qualityprofiles import SonarQubeQualityProfiles
from .duplications import SonarQubeDuplications
from .metrics import SonarQubeMetrics
from .settings import SonarQubeSettings
from .sources import SonarQubeSources
from .auth import SonarQubeAuth
from .favorite import SonarQubeFavorites
from .languages import SonarQubeLanguages
from .project_badges import SonarQubeProjectBadges
from .project_tags import SonarQubeProjectTags
from .project_pull_requests import SonarQubepRrojectPullRequests
from .project_analyses import SonarQubeProjectAnalyses
from .server import SonarQubeServer
from .user_tokens import SonarQubeUsertokens
from .webhooks import SonarQubeWebhooks
from .webservices import SonarQubeWebservices
from .system import SonarQubeSystem


class SonarQubeClient:
    """
    A Python Client for SonarQube Server APIs.
    """
    DEFAULT_URL = "http://localhost:9000"

    def __init__(self,
                 sonarqube_url=None,
                 username=None,
                 password=None,
                 token=None,
                 ssl_verify=True,
                 cert=None,
                 timeout=10,
                 max_retries=None):
        self._sonarqube_url = self.strip_trailing_slash(sonarqube_url or self.DEFAULT_URL)

        if token:
            auth = (token, )
        elif username and password:
            auth = (username, password)
        else:
            raise ValidationError("Please provide both username and password, or provide token!")

        self.requester = Requester(
            *auth,
            baseurl=self._sonarqube_url,
            ssl_verify=ssl_verify,
            cert=cert,
            timeout=timeout,
            max_retries=max_retries
        )

    @classmethod
    def strip_trailing_slash(cls, url):
        """
        remove url's trailing slash

        :param url:
        :return:
        """
        while url.endswith('/'):
            url = url[:-1]
        return url

    def __str__(self):
        return '{}'.format(self._sonarqube_url)

    def _get_endpoint_url(self, endpoint):
        """
        Return the complete url including host and port for a given endpoint.

        :param endpoint: service endpoint as str
        :return: complete url (including host and port) as str
        """
        return '{}{}'.format(self._sonarqube_url, endpoint)

    def make_call(self, method, endpoint, **data):
        """
        Make the call to the service with the given method, queryset and data,
        using the requester.

        :param method: http method (get, post, put, delete)
        :param endpoint: relative url to make the call
        :param data: queryset or body
        :return: response
        """
        call = getattr(self.requester, method.lower())
        base_url = self._get_endpoint_url(endpoint)
        res = call(base_url, params=data or {})
        # Analyse response status and return or raise exception
        # Note: redirects are followed automatically by requests

        error_message = "Error in request. "
        if res.status_code < 300:
            # OK, return http response
            return res

        # raise error. res.raise_for_status()
        elif res.status_code == 400:
            # Validation error
            msg = error_message + \
                  'Possibly validation error [%s]: %s' % (
                      res.status_code, ', '.join(e['msg'] for e in res.json()['errors']))

            raise ValidationError(msg)

        elif res.status_code in (401, 403):
            # Auth error
            msg = error_message + \
                  'Possibly authentication failed [%s]: %s' % (
                      res.status_code, res.reason)
            if res.text:
                msg += '\n' + res.text

            raise AuthError(msg)

        elif res.status_code < 500:
            # Other 4xx, generic client error
            msg = error_message + \
                  'Possibly client error [%s]: %s' % (
                      res.status_code, ', '.join(e['msg'] for e in res.json()['errors']))

            raise ClientError(msg)

        else:
            # 5xx is server error
            msg = error_message + \
                  'Possibly server error [%s]: %s' % (
                      res.status_code, res.reason)

            raise ServerError(msg)

    @property
    def users(self):
        return SonarQubeUser(self)

    @property
    def user_groups(self):
        return SonarQubeUserGroups(self)

    @property
    def projects(self):
        return SonarQubeProject(self)

    @property
    def measures(self):
        return SonarQubeMeasure(self)

    @property
    def issues(self):
        return SonarQubeIssues(self)

    @property
    def notifications(self):
        return SonarQubeNotification(self)

    @property
    def project_links(self):
        return SonarQubeProjectLinks(self)

    @property
    def permissions(self):
        return SonarQubePermissions(self)

    @property
    def ce(self):
        return SonarQubeCe(self)

    @property
    def project_branches(self):
        return SonarQubeProjectBranches(self)

    @property
    def qualitygates(self):
        return SonarQubeQualityGates(self)

    @property
    def components(self):
        return SonarQubeComponents(self)

    @property
    def rules(self):
        return SonarQubeRules(self)

    @property
    def qualityprofiles(self):
        return SonarQubeQualityProfiles(self)

    @property
    def duplications(self):
        return SonarQubeDuplications(self)

    @property
    def metrics(self):
        return SonarQubeMetrics(self)

    @property
    def settings(self):
        return SonarQubeSettings(self)

    @property
    def sources(self):
        return SonarQubeSources(self)

    @property
    def auth(self):
        return SonarQubeAuth(self)

    @property
    def favorites(self):
        return SonarQubeFavorites(self)

    @property
    def languages(self):
        return SonarQubeLanguages(self)

    @property
    def project_badges(self):
        return SonarQubeProjectBadges(self)

    @property
    def project_tags(self):
        return SonarQubeProjectTags(self)

    @property
    def project_pull_requests(self):
        return SonarQubepRrojectPullRequests(self)

    @property
    def project_analyses(self):
        return SonarQubeProjectAnalyses(self)

    @property
    def server(self):
        return SonarQubeServer(self)

    @property
    def user_tokens(self):
        return SonarQubeUsertokens(self)

    @property
    def webhooks(self):
        return SonarQubeWebhooks(self)

    @property
    def webservices(self):
        return SonarQubeWebservices(self)

    @property
    def system(self):
        return SonarQubeSystem(self)

    @staticmethod
    def copy_dict(dest, src, option):
        for k, v in src.items():
            if k in option:
                if isinstance(v, dict):
                    for dict_k, dict_v in v.items():
                        dest['%s[%s]' % (k, dict_k)] = dict_v
                else:
                    dest[k] = v
