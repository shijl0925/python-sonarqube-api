#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import json
import requests
from requests.auth import HTTPBasicAuth

from sonarqube.utils.common import strip_trailing_slash
from sonarqube.rest.users import SonarQubeUsers
from sonarqube.rest.projects import SonarQubeProjects
from sonarqube.rest.user_groups import SonarQubeUserGroups
from sonarqube.rest.issues import SonarQubeIssues
from sonarqube.rest.measures import SonarQubeMeasures
from sonarqube.rest.ce import SonarQubeCe
from sonarqube.rest.project_branches import SonarQubeProjectBranches
from sonarqube.rest.qualitygates import SonarQubeQualityGates
from sonarqube.rest.rules import SonarQubeRules
from sonarqube.rest.qualityprofiles import SonarQubeQualityProfiles
from sonarqube.rest.duplications import SonarQubeDuplications
from sonarqube.rest.metrics import SonarQubeMetrics
from sonarqube.rest.auth import SonarQubeAuth
from sonarqube.rest.favorites import SonarQubeFavorites
from sonarqube.rest.languages import SonarQubeLanguages
from sonarqube.rest.project_badges import SonarQubeProjectBadges
from sonarqube.rest.project_links import SonarQubeProjectLinks
from sonarqube.rest.project_tags import SonarQubeProjectTags
from sonarqube.rest.project_analyses import SonarQubeProjectAnalyses
from sonarqube.rest.server import SonarQubeServer
from sonarqube.rest.user_tokens import SonarQubeUserTokens
from sonarqube.rest.project_dump import SonarQubeProjectDump
from sonarqube.rest.editions import SonarQubeEditions
from sonarqube.rest.views import SonarQubeViews


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
            _auth = HTTPBasicAuth(token, "")
        elif username and password:
            _auth = HTTPBasicAuth(username, password)
        else:
            _auth = None
        _session.auth = _auth

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
    def project_links(self):
        """
        SonarQube project links Operations

        :return:
        """
        return SonarQubeProjectLinks(api=self)

    @property
    def project_tags(self):
        """
        SonarQube project tags Operations

        :return:
        """
        return SonarQubeProjectTags(api=self)

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
    def project_dump(self):
        """
        Project export/import

        :return:
        """
        return SonarQubeProjectDump(api=self)

    @property
    def editions(self):
        """
        Manage SonarSource commercial editions

        """
        return SonarQubeEditions(api=self)

    @property
    def views(self):
        """
        Manage Portfolios

        """
        return SonarQubeViews(api=self)


class SonarEnterpriseClient(SonarQubeClient):
    pass


class SonarCloudClient(SonarQubeClient):
    pass
