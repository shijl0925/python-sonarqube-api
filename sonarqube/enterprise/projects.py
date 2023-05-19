#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.projects import SonarQubeProjects
from sonarqube.utils.common import GET

from sonarqube.utils.config import (
    API_PROJECTS_EXPORT_FINDINGS_ENDPOINT,
    API_PROJECTS_LICENSE_USAGE_ENDPOINT
)


class SonarEnterpriseProjects(SonarQubeProjects):
    @GET(API_PROJECTS_EXPORT_FINDINGS_ENDPOINT)
    def export_findings_for_project(self, project, branch=None, pullRequest=None):
        """
        SINCE 9.1
        Export all findings (issues and hotspots) of a specific project branch.

        :param project: Project key
        :param branch: Branch key. When not specified, if no Pull Request key is defined either,
        it will default to the main branch
        :param pullRequest: Pull Request key. When not specified, the branch data will be returned instead
        :return:
        """

    @GET(API_PROJECTS_LICENSE_USAGE_ENDPOINT)
    def get_license_usage_for_project(self):
        """
        SINCE 9.4
        Help admins to understand how the number of lines of code (used for licensing) is distributed between projects,
        i.e. how much each project affects the total number of lines of code. Returns the list of projects together with
        information about their usage, sorted by lines of code descending.
        Requires Administer System permission.

        :return:
        """
