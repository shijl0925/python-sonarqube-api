#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BADGES_MEASURE_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeProjectBadges(RestClient):
    """
    SonarQube project badges Operations
    """

    @GET(API_PROJECT_BADGES_MEASURE_ENDPOINT)
    def generate_badge_for_project_measures(self, project, metric, branch=None, token=None):
        """
        SINCE 7.1
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :param token: Security token
        :return:
        """
