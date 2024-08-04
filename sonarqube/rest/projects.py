#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECTS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeProjects(RestClient):
    """
    SonarQube projects Operations
    """

    def get_project(self, key, organization=None):
        result = self.search_projects(organization=organization, projects=key)
        projects = result.get("components", [])

        item = None
        for project in projects:
            if project["key"] == key:
                item = project
                break

        return item

    @GET(API_PROJECTS_SEARCH_ENDPOINT)
    def search_projects(
        self,
        organization=None,
        analyzedBefore=None,
        onProvisionedOnly="false",
        projects=None,
        p=None,
        ps=None,
        q=None,
        qualifiers="TRK",
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :param organization: The key of the organization
        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned.
          Possible values are for: true or false. default value is false.
        :param projects: Comma-separated list of project keys
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param q:
          Limit search to:
            * component names that contain the supplied string
            * component keys that contain the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified
          qualifiers. Possible values are for:
            * TRK
            * VW
            * APP
          default value is TRK.

        :return:
        """
