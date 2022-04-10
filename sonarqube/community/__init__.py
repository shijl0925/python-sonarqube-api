#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import json
import requests

from sonarqube.utils.common import strip_trailing_slash
from sonarqube.community.users import SonarQubeUsers
from sonarqube.community.projects import SonarQubeProjects
from sonarqube.community.user_groups import SonarQubeUserGroups
from sonarqube.community.issues import SonarQubeIssues
from sonarqube.community.measures import SonarQubeMeasures
from sonarqube.community.notifications import SonarQubeNotifications
from sonarqube.community.project_links import SonarQubeProjectLinks
from sonarqube.community.permissions import SonarQubePermissions
from sonarqube.community.ce import SonarQubeCe
from sonarqube.community.project_branches import SonarQubeProjectBranches
from sonarqube.community.qualitygates import SonarQubeQualityGates
from sonarqube.community.components import SonarQubeComponents
from sonarqube.community.rules import SonarQubeRules
from sonarqube.community.qualityprofiles import SonarQubeQualityProfiles
from sonarqube.community.duplications import SonarQubeDuplications
from sonarqube.community.metrics import SonarQubeMetrics
from sonarqube.community.hotspots import SonarQubeHotspots
from sonarqube.community.new_code_periods import SonarQubeNewcodeperiods
from sonarqube.community.settings import SonarQubeSettings
from sonarqube.community.sources import SonarQubeSources
from sonarqube.community.auth import SonarQubeAuth
from sonarqube.community.favorites import SonarQubeFavorites
from sonarqube.community.languages import SonarQubeLanguages
from sonarqube.community.plugins import SonarQubePlugins
from sonarqube.community.project_badges import SonarQubeProjectBadges
from sonarqube.community.project_tags import SonarQubeProjectTags
from sonarqube.community.project_pull_requests import SonarQubeProjectPullRequests
from sonarqube.community.project_analyses import SonarQubeProjectAnalyses
from sonarqube.community.server import SonarQubeServer
from sonarqube.community.user_tokens import SonarQubeUserTokens
from sonarqube.community.webhooks import SonarQubeWebhooks
from sonarqube.community.webservices import SonarQubeWebservices
from sonarqube.community.system import SonarQubeSystem
from sonarqube.community.alm_integrations import SonarQubeAlmIntegrations
from sonarqube.community.alm_settings import SonarQubeAlmSettings
from sonarqube.community.monitoring import SonarQubeMonitoring
from sonarqube.community.project_dump import SonarQubeProjectdump


class SonarQubeClient:
    """
    A Python Client for SonarQube Server APIs.
    """

    DEFAULT_URL = "http://localhost:9000"

    def __init__(
        self,
        sonarqube_url=None,
        username=None,
        password=None,
        token=None,
        verify=None,
        cert=None,
        timeout=None
    ):

        self.base_url = strip_trailing_slash(sonarqube_url or self.DEFAULT_URL)

        _session = requests.Session()
        if token:
            _session.auth = (token, "")
        elif username and password:
            _session.auth = (username, password)
        if verify is not None:
            _session.verify = verify
        if cert is not None:
            _session.cert = cert

        self.session = _session
        self.timeout = timeout

    @property
    def users(self):
        """
        SonarQube users Operations

        :return:
        """
        return SonarQubeUsers(api=self)

    @property
    def user_groups(self):
        """
        SonarQube user_groups Operations

        :return:
        """
        return SonarQubeUserGroups(api=self)

    @property
    def projects(self):
        """
        SonarQube projects Operations

        :return:
        """
        return SonarQubeProjects(api=self)

    @property
    def measures(self):
        """
        SonarQube measures Operations

        :return:
        """
        return SonarQubeMeasures(api=self)

    @property
    def issues(self):
        """
        SonarQube issues Operations

        :return:
        """
        return SonarQubeIssues(api=self)

    @property
    def notifications(self):
        """
        SonarQube notifications Operations

        :return:
        """
        return SonarQubeNotifications(api=self)

    @property
    def project_links(self):
        """
        SonarQube project links Operations

        :return:
        """
        return SonarQubeProjectLinks(api=self)

    @property
    def permissions(self):
        """
        SonarQube permissions Operations

        :return:
        """
        return SonarQubePermissions(api=self)

    @property
    def ce(self):
        """
        SonarQube ce Operations

        :return:
        """
        return SonarQubeCe(api=self)

    @property
    def project_branches(self):
        """
        SonarQube project branches Operations

        :return:
        """
        return SonarQubeProjectBranches(api=self)

    @property
    def qualitygates(self):
        """
        SonarQube quality gates Operations

        :return:
        """
        return SonarQubeQualityGates(api=self)

    @property
    def components(self):
        """
        SonarQube components Operations

        :return:
        """
        return SonarQubeComponents(api=self)

    @property
    def rules(self):
        """
        SonarQube rules Operations

        :return:
        """
        return SonarQubeRules(api=self)

    @property
    def qualityprofiles(self):
        """
        SonarQube quality profiles Operations

        :return:
        """
        return SonarQubeQualityProfiles(api=self)

    @property
    def duplications(self):
        """
        SonarQube duplications Operations

        :return:
        """
        return SonarQubeDuplications(api=self)

    @property
    def metrics(self):
        """
        SonarQube metrics Operations

        :return:
        """
        return SonarQubeMetrics(api=self)

    @property
    def hotspots(self):
        """

        :return:
        """
        return SonarQubeHotspots(api=self)

    @property
    def new_code_periods(self):
        """
        SonarQube new code periods Operations

        :return:
        """
        return SonarQubeNewcodeperiods(api=self)

    @property
    def settings(self):
        """
        SonarQube settings Operations

        :return:
        """
        return SonarQubeSettings(api=self)

    @property
    def sources(self):
        """
        SonarQube sources Operations

        :return:
        """
        return SonarQubeSources(api=self)

    @property
    def auth(self):
        """
        SonarQube authentication Operations

        :return:
        """
        return SonarQubeAuth(api=self)

    @property
    def favorites(self):
        """
        SonarQube favorites Operations

        :return:
        """
        return SonarQubeFavorites(api=self)

    @property
    def languages(self):
        """
        SonarQube languages Operations

        :return:
        """
        return SonarQubeLanguages(api=self)

    @property
    def project_badges(self):
        """
        SonarQube project badges Operations

        :return:
        """
        return SonarQubeProjectBadges(api=self)

    @property
    def project_tags(self):
        """
        SonarQube project tags Operations

        :return:
        """
        return SonarQubeProjectTags(api=self)

    @property
    def project_pull_requests(self):
        """
        SonarQube project pull requests Operations

        :return:
        """
        return SonarQubeProjectPullRequests(api=self)

    @property
    def project_analyses(self):
        """
        SonarQube project analyses Operations

        :return:
        """
        return SonarQubeProjectAnalyses(api=self)

    @property
    def server(self):
        """
        SonarQube server Operations

        :return:
        """
        return SonarQubeServer(api=self)

    @property
    def user_tokens(self):
        """
        SonarQube user tokens Operations

        :return:
        """
        return SonarQubeUserTokens(api=self)

    @property
    def webhooks(self):
        """
        SonarQube webhooks Operations

        :return:
        """
        return SonarQubeWebhooks(api=self)

    @property
    def webservices(self):
        """
        SonarQube webservices Operations

        :return:
        """
        return SonarQubeWebservices(api=self)

    @property
    def system(self):
        """
        SonarQube system Operations

        :return:
        """
        return SonarQubeSystem(api=self)

    @property
    def plugins(self):
        """
        SonarQube plugins Operations

        :return:
        """
        return SonarQubePlugins(api=self)

    @property
    def alm_integrations(self):
        """
        ALM Integrations

        """
        return SonarQubeAlmIntegrations(api=self)

    @property
    def alm_settings(self):
        """
        ALM settings

        """
        return SonarQubeAlmSettings(api=self)

    @property
    def monitoring(self):
        return SonarQubeMonitoring(api=self)

    @property
    def project_dump(self):
        """
        Project export/import

        :return:
        """
        return SonarQubeProjectdump(api=self)

    @staticmethod
    def decode_response(response):
        """

        :returns:
            Decoded JSON content as a dict, or raw text if content could not be
            decoded as JSON.
        :raises:
            requests.HTTPError if the response contains an HTTP error status code.
        """
        content_type = response.headers.get("content-type", "")

        content = response.content.strip()
        if response.encoding:
            content = content.decode(response.encoding)
        if not content:
            return content
        if content_type.split(";")[0] != "application/json":
            return content
        try:
            return json.loads(content)
        except ValueError:
            raise ValueError("Invalid json content: {}".format(content))

    def get_endpoint_url(self, endpoint):
        """
        Return the complete url including host and port for a given endpoint.
        :param endpoint: service endpoint as str
        :return: complete url (including host and port) as str
        """
        return "{}{}".format(self.base_url, endpoint)

    def request_get(self, endpoint, **kwargs):
        """
        Send HTTP GET to the endpoint.

        :param endpoint: The endpoint to send to.
        :return:
        """
        response = self.session.get(self.get_endpoint_url(endpoint), **kwargs)
        result = self.decode_response(response)
        return result

    def request_post(self, endpoint, **kwargs):
        """
        Send HTTP POST to the endpoint.

        :param endpoint: The endpoint to send to.
        :return:
        """
        response = self.session.post(self.get_endpoint_url(endpoint), **kwargs)
        result = self.decode_response(response)
        return result
