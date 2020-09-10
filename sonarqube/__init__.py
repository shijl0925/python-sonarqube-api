#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import requests
from .exceptions import ValidationError
from .users import SonarQubeUsers
from .projects import SonarQubeProjects
from .user_groups import SonarQubeUserGroups
from .issues import SonarQubeIssues
from .measures import SonarQubeMeasures
from .notifications import SonarQubeNotifications
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
from .favorites import SonarQubeFavorites
from .languages import SonarQubeLanguages
from .plugins import SonarQubePlugins
from .project_badges import SonarQubeProjectBadges
from .project_tags import SonarQubeProjectTags
from .project_pull_requests import SonarQubeRrojectPullRequests
from .project_analyses import SonarQubeProjectAnalyses
from .server import SonarQubeServer
from .user_tokens import SonarQubeUserTokens
from .webhooks import SonarQubeWebhooks
from .webservices import SonarQubeWebservices
from .system import SonarQubeSystem


class SonarQubeClient:
    """
    A Python Client for SonarQube Server APIs.
    """
    DEFAULT_URL = "http://localhost:9000"

    def __init__(self, sonarqube_url=None, username=None, password=None, token=None):

        self.sonarqube_url = self.strip_trailing_slash(sonarqube_url or self.DEFAULT_URL)

        _session = requests.Session()
        if token:
            _session.auth = (token, '')
        elif username and password:
            _session.auth = (username, password)
        else:
            raise ValidationError("Please provide both username and password, or provide token!")

        self.session = _session

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
        return '{}'.format(self.sonarqube_url)

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
        return SonarQubeRrojectPullRequests(api=self)

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

    @staticmethod
    def copy_dict(dest, src, option):
        """
        copy a dictionary to anther dictionary

        :param dest:
        :param src:
        :param option:
        :return:
        """
        for k, v in src.items():
            if k in option:
                if isinstance(v, dict):
                    for dict_k, dict_v in v.items():
                        dest['%s[%s]' % (k, dict_k)] = dict_v
                else:
                    dest[k] = v
