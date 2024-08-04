#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECTS_BULK_DELETE_ENDPOINT,
    API_PROJECTS_DELETE_ENDPOINT,
    API_PROJECTS_SEARCH_ENDPOINT,
    API_PROJECTS_CREATE_ENDPOINT
)
from sonarqube.utils.common import GET, POST


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

    @POST(API_PROJECTS_BULK_DELETE_ENDPOINT)
    def bulk_delete_project(self, analyzedBefore=None, onProvisionedOnly=False, projects=None, q=None, qualifiers="TRK"):
        """
        SINCE 5.2
        Delete one or several projects.

        :param analyzedBefore: Filter the projects for which last analysis of any branch is older than the given date (exclusive).
                               Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned
        :param projects: Comma-separated list of project keys
        :param q: Limit to:
                    component names that contain the supplied string
                    component keys that contain the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified qualifiers

        :return:
        """

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

    @POST(API_PROJECTS_CREATE_ENDPOINT)
    def create_project(self, project, name, visibility=None):
        """
        SINCE 4.0
        Create a project. Requires 'Create Projects' permission.

        :param project: required. Key of the project
        :param name: required. Name of the project. If name is longer than 500, it is abbreviated.
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          Possible values
            * private
            * public

        """

    @POST(API_PROJECTS_DELETE_ENDPOINT)
    def delete_project(self, project):
        """
        SINCE 5.2
        Delete a project

        :param project: Project key

        :return:
        """
