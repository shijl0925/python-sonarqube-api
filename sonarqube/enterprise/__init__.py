#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community import SonarQubeClient
from sonarqube.enterprise.applications import SonarQubeApplications
from sonarqube.enterprise.audit_logs import SonarQubeAuditLogs
from sonarqube.enterprise.editions import SonarQubeEditions
from sonarqube.enterprise.views import SonarQubeViews
from sonarqube.enterprise.alm_settings import SonarEnterpriseAlmSettings
from sonarqube.enterprise.hotspots import SonarEnterpriseHotspots
from sonarqube.enterprise.project_dump import SonarEnterpriseProjectDump
from sonarqube.enterprise.projects import SonarEnterpriseProjects
from sonarqube.enterprise.project_pull_requests import SonarQubeProjectPullRequests


class SonarEnterpriseClient(SonarQubeClient):
    """
    A Python Client for SonarQube Enterprise Server APIs.
    """
    @property
    def alm_settings(self):
        """
        ALM settings

        """
        return SonarEnterpriseAlmSettings(api=self)

    @property
    def hotspots(self):
        """
        Security Hotspots

        """
        return SonarEnterpriseHotspots(api=self)

    @property
    def applications(self):
        """
        SonarQube applications Operations

        :return:
        """
        return SonarQubeApplications(api=self)

    @property
    def audit_logs(self):
        return SonarQubeAuditLogs(api=self)

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

    @property
    def project_pull_requests(self):
        """
        SonarQube project pull requests Operations

        :return:
        """
        return SonarQubeProjectPullRequests(api=self)

    @property
    def project_dump(self):
        """
        Project export/import

        :return:
        """
        return SonarEnterpriseProjectDump(api=self)

    @property
    def projects(self):
        """
        SonarQube projects Operations

        :return:
        """
        return SonarEnterpriseProjects(api=self)
