#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECT_BADGES_MEASURE_ENDPOINT,
    API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT
)


class SonarQubeProjectBadges:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def generate_badge_for_project_measures(self, project, branch, metric):
        """
        Generate badge for project's measure as an SVG.
        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key, such as:
          bugs,code_smells,coverage,duplicated_lines_density,ncloc,sqale_rating,alert_status,reliability_rating,
          security_rating,sqale_index,vulnerabilities
        :return:
        """
        params = {
            'project': project,
            'branch': branch,
            'metric': metric
        }
        resp = self.sonarqube.make_call('get', API_PROJECT_BADGES_MEASURE_ENDPOINT, **params)
        return resp.text

    def generate_badge_for_project_quality_gate(self, project, branch):
        """
        Generate badge for project's quality gate as an SVG.
        :param project: Project or application key
        :param branch: Long living branch key
        :return:
        """
        params = {
            'project': project,
            'branch': branch,
        }
        resp = self.sonarqube.make_call('get', API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT, **params)
        return resp.text
