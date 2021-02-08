#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jacek Hojczak
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECTS_SEARCH_ENDPOINT,
    API_APPLICATION_CREATE_ENDPOINT,
    API_APPLICATION_DELETE_ENDPOINT,
    API_APPLICATION_SHOW_ENDPOINT,
    API_APPLICATION_UPDATE_ENDPOINT,
    API_APPLICATION_ADD_PROJECT_ENDPOINT,
    API_APPLICATION_REMOVE_PROJECT_ENDPOINT,
    API_APPLICATION_CREATE_BRANCH_ENDPOINT,
    API_APPLICATION_DELETE_BRANCH_ENDPOINT,
    API_APPLICATION_SET_TAGS_ENDPOINT,
    API_APPLICATION_UPDATE_BRANCH_ENDPOINT
)
from sonarqube.utils.common import PAGE_GET, POST, GET


class SonarQubeApplications(RestClient):
    """
    SonarQube applications Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeApplications, self).__init__(**kwargs)

    def get(self, key):
        result = list(self.search_applications(projects=key))
        for project in result:
            if project["key"] == key:
                return project

    @PAGE_GET(API_PROJECTS_SEARCH_ENDPOINT, item="components")
    def search_applications(
            self,
            analyzedBefore=None,
            onProvisionedOnly="false",
            projects=None,
            q=None,
            qualifiers="APP",
    ):
        """
        Search for projects or views to administrate them.

        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned.
          Possible values are for: true or false. default value is false.
        :param projects: Comma-separated list of project keys
        :param q:
          Limit search to:
            * component names that contain the supplied string
            * component keys that contain the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified
          qualifiers. Possible values are for:
            * TRK
            * VW
            * APP
          default value is APP.

        :return:
        """

    @POST(API_APPLICATION_CREATE_ENDPOINT)
    def create_application(self, name, key=None, visibility=None, description=None):
        """
        Create a application.

        :param description:
        :param key:
        :param name: Name of the Application. If name is longer than 500, it is abbreviated.
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          Possible values are for:
            * private
            * public
        :return: request response
        """

    @POST(API_APPLICATION_DELETE_ENDPOINT)
    def delete_application(self, application):
        """
        Delete a application.

        :param application: Application key
        :return:
        """

    @GET(API_APPLICATION_SHOW_ENDPOINT)
    def show_project(self, application, branch=None):
        """
        Returns an application and its associated projects.

        :param application: Application key
        :param branch: Branch name
        :return:
        """

    @POST(API_APPLICATION_ADD_PROJECT_ENDPOINT)
    def add_project(self, application, project):
        """
        Add project to application.

        :param application: Application key
        :param project: Project key
        :return:
        """

    @POST(API_APPLICATION_REMOVE_PROJECT_ENDPOINT)
    def remove_project(self, application, project):
        """
        Remove project to application.

        :param application: Application key
        :param project: Project key
        :return:
        """

    @POST(API_APPLICATION_CREATE_BRANCH_ENDPOINT)
    def create_branch(self, application, branch, project, projectBranch):
        """
        Create a new branch on a given application.

        :param application: Application key
        :param branch: Branch name
        :param project: Project keys
        :param projectBranch: Project branches

        :return:
        """

    @POST(API_APPLICATION_DELETE_BRANCH_ENDPOINT)
    def delete_branch(self, application, branch):
        """
        Delete a branch on a given application.

        :param application: Application key
        :param branch: Branch name


        :return:
        """

    @POST(API_APPLICATION_UPDATE_BRANCH_ENDPOINT)
    def update_branch(self, application, branch, name, project, projectBranch):
        """
        Update a branch on a given application.

        :param application: Application key
        :param branch: Branch name
        :param name: New branch name
        :param project: Project keys
        :param projectBranch: Project branches

        :return:
        """

    @POST(API_APPLICATION_UPDATE_ENDPOINT)
    def update_application(self, application, name, description=None):
        """
        Update an application.

        :param description: Application description
        :param name: Application name
        :type application: Application key
        :
        :return:
        """

    @POST(API_APPLICATION_SET_TAGS_ENDPOINT)
    def set_tags(self, application, tags):
        """
        Set tags on a application.

        :type application: Comma-separated list of tags
        :param tags: Comma-separated list of tags
        :return:
        """
