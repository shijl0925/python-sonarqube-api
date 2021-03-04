#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import requests
from sonarqube.utils.common import strip_trailing_slash
from sonarqube.cloud.users import SonarCloudUsers
from sonarqube.cloud.projects import SonarCloudProjects
from sonarqube.cloud.user_groups import SonarCloudUserGroups
from sonarqube.cloud.issues import SonarCloudIssues
from sonarqube.community.measures import SonarQubeMeasures as SonarCloudMeasures
from sonarqube.community.notifications import (
    SonarQubeNotifications as SonarCloudNotifications,
)
from sonarqube.community.project_links import (
    SonarQubeProjectLinks as SonarCloudProjectLinks,
)
from sonarqube.cloud.permissions import SonarCloudPermissions
from sonarqube.cloud.ce import SonarCloudCe
from sonarqube.community.project_branches import (
    SonarQubeProjectBranches as SonarCloudProjectBranches,
)
from sonarqube.cloud.qualitygates import SonarCloudQualityGates
from sonarqube.cloud.components import SonarCloudComponents
from sonarqube.cloud.rules import SonarCloudRules
from sonarqube.cloud.qualityprofiles import SonarCloudQualityProfiles
from sonarqube.community.duplications import (
    SonarQubeDuplications as SonarCloudDuplications,
)
from sonarqube.community.metrics import SonarQubeMetrics as SonarCloudMetrics
from sonarqube.cloud.settings import SonarCloudSettings
from sonarqube.community.sources import SonarQubeSources as SonarCloudSources
from sonarqube.cloud.auth import SonarCloudAuth
from sonarqube.community.favorites import SonarQubeFavorites as SonarCloudFavorites
from sonarqube.community.languages import SonarQubeLanguages as SonarCloudLanguages
from sonarqube.cloud.project_badges import SonarCloudProjectBadges
from sonarqube.community.project_tags import (
    SonarQubeProjectTags as SonarCloudProjectTags,
)
from sonarqube.community.project_pull_requests import (
    SonarQubeProjectPullRequests as SonarCloudProjectPullRequests,
)
from sonarqube.community.project_analyses import (
    SonarQubeProjectAnalyses as SonarCloudProjectAnalyses,
)
from sonarqube.community.user_tokens import SonarQubeUserTokens as SonarCloudUserTokens
from sonarqube.cloud.webhooks import SonarCloudWebhooks
from sonarqube.community.webservices import (
    SonarQubeWebservices as SonarCloudWebservices,
)


class SonarCloudClient:
    """
    A Python Client for SonarCloud Server APIs.
    """

    def __init__(self, sonarcloud_url, token, timeout=None):
        self.base_url = strip_trailing_slash(sonarcloud_url)
        _session = requests.Session()
        _session.auth = (token, "")
        self.session = _session
        self.timeout = timeout

    @property
    def users(self):
        """
        SonarCloud users Operations

        :return:
        """
        return SonarCloudUsers(api=self)

    @property
    def user_groups(self):
        """
        SonarCloud user_groups Operations

        :return:
        """
        return SonarCloudUserGroups(api=self)

    @property
    def projects(self):
        """
        SonarCloud projects Operations

        :return:
        """
        return SonarCloudProjects(api=self)

    @property
    def measures(self):
        """
        SonarCloud measures Operations

        :return:
        """
        return SonarCloudMeasures(api=self)

    @property
    def issues(self):
        """
        SonarCloud issues Operations

        :return:
        """
        return SonarCloudIssues(api=self)

    @property
    def notifications(self):
        """
        SonarCloud notifications Operations

        :return:
        """
        return SonarCloudNotifications(api=self)

    @property
    def project_links(self):
        """
        SonarCloud project links Operations

        :return:
        """
        return SonarCloudProjectLinks(api=self)

    @property
    def permissions(self):
        """
        SonarCloud permissions Operations

        :return:
        """
        return SonarCloudPermissions(api=self)

    @property
    def ce(self):
        """
        SonarCloud ce Operations

        :return:
        """
        return SonarCloudCe(api=self)

    @property
    def project_branches(self):
        """
        SonarCloud project branches Operations

        :return:
        """
        return SonarCloudProjectBranches(api=self)

    @property
    def qualitygates(self):
        """
        SonarCloud quality gates Operations

        :return:
        """
        return SonarCloudQualityGates(api=self)

    @property
    def components(self):
        """
        SonarCloud components Operations

        :return:
        """
        return SonarCloudComponents(api=self)

    @property
    def rules(self):
        """
        SonarCloud rules Operations

        :return:
        """
        return SonarCloudRules(api=self)

    @property
    def qualityprofiles(self):
        """
        SonarCloud quality profiles Operations

        :return:
        """
        return SonarCloudQualityProfiles(api=self)

    @property
    def duplications(self):
        """
        SonarCloud duplications Operations

        :return:
        """
        return SonarCloudDuplications(api=self)

    @property
    def metrics(self):
        """
        SonarCloud metrics Operations

        :return:
        """
        return SonarCloudMetrics(api=self)

    @property
    def settings(self):
        """
        SonarCloud settings Operations

        :return:
        """
        return SonarCloudSettings(api=self)

    @property
    def sources(self):
        """
        SonarCloud sources Operations

        :return:
        """
        return SonarCloudSources(api=self)

    @property
    def auth(self):
        """
        SonarCloud authentication Operations

        :return:
        """
        return SonarCloudAuth(api=self)

    @property
    def favorites(self):
        """
        SonarCloud favorites Operations

        :return:
        """
        return SonarCloudFavorites(api=self)

    @property
    def languages(self):
        """
        SonarCloud languages Operations

        :return:
        """
        return SonarCloudLanguages(api=self)

    @property
    def project_badges(self):
        """
        SonarCloud project badges Operations

        :return:
        """
        return SonarCloudProjectBadges(api=self)

    @property
    def project_tags(self):
        """
        SonarCloud project tags Operations

        :return:
        """
        return SonarCloudProjectTags(api=self)

    @property
    def project_pull_requests(self):
        """
        SonarCloud project pull requests Operations

        :return:
        """
        return SonarCloudProjectPullRequests(api=self)

    @property
    def project_analyses(self):
        """
        SonarCloud project analyses Operations

        :return:
        """
        return SonarCloudProjectAnalyses(api=self)

    @property
    def user_tokens(self):
        """
        SonarCloud user tokens Operations

        :return:
        """
        return SonarCloudUserTokens(api=self)

    @property
    def webhooks(self):
        """
        SonarCloud webhooks Operations

        :return:
        """
        return SonarCloudWebhooks(api=self)

    @property
    def webservices(self):
        """
        SonarCloud webservices Operations

        :return:
        """
        return SonarCloudWebservices(api=self)
