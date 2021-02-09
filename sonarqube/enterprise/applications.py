#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jacek Hojczak
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_APPLICATIONS_CREATE_ENDPOINT,
    API_APPLICATIONS_DELETE_ENDPOINT,
    API_APPLICATIONS_SHOW_ENDPOINT,
    API_APPLICATIONS_UPDATE_ENDPOINT,
    API_APPLICATIONS_ADD_PROJECT_ENDPOINT,
    API_APPLICATIONS_REMOVE_PROJECT_ENDPOINT,
    API_APPLICATIONS_CREATE_BRANCH_ENDPOINT,
    API_APPLICATIONS_DELETE_BRANCH_ENDPOINT,
    API_APPLICATIONS_SET_TAGS_ENDPOINT,
    API_APPLICATIONS_UPDATE_BRANCH_ENDPOINT
)
from sonarqube.utils.common import POST, GET


class SonarQubeApplications(RestClient):
    """
    SonarQube applications Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeApplications, self).__init__(**kwargs)

    @POST(API_APPLICATIONS_CREATE_ENDPOINT)
    def create_application(self, name, key=None, visibility=None, description=None):
        """
        SINCE 7.3
        Create a new application.

        :param description: Application description
        :param key: Application key. A suitable key will be generated if not provided
        :param name: Name of the Application.
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          Possible values are for:
            * private
            * public

        :return: request response
        """

    @POST(API_APPLICATIONS_DELETE_ENDPOINT)
    def delete_application(self, application):
        """
        SINCE 7.3
        Delete an application definition.

        :param application: Application key
        :return:
        """

    @GET(API_APPLICATIONS_SHOW_ENDPOINT)
    def show_application(self, application, branch=None):
        """
        SINCE 7.3
        Returns an application and its associated projects.

        :param application: Application key
        :param branch: Branch name
        :return:
        """

    @POST(API_APPLICATIONS_ADD_PROJECT_ENDPOINT)
    def add_project(self, application, project):
        """
        SINCE 7.3
        Add project to application.

        :param application: Application key
        :param project: Project key
        :return:
        """

    @POST(API_APPLICATIONS_REMOVE_PROJECT_ENDPOINT)
    def remove_project(self, application, project):
        """
        SINCE 7.3
        Remove project to application.

        :param application: Application key
        :param project: Project key
        :return:
        """

    @POST(API_APPLICATIONS_CREATE_BRANCH_ENDPOINT)
    def create_branch(self, application, branch, project, projectBranch):
        """
        SINCE 7.3
        Create a new branch on a given application.

        :param application: Application key
        :param branch: Branch name
        :param project: Project keys.To set several values, the parameter must be called once for each value.
        :param projectBranch: Project branches.To set main branch, provide an empty value.
          To set several values, the parameter must be called once for each value.

        :return:
        """

    @POST(API_APPLICATIONS_DELETE_BRANCH_ENDPOINT)
    def delete_branch(self, application, branch):
        """
        SINCE 7.3
        Delete a branch on a given application.

        :param application: Application key
        :param branch: Branch name


        :return:
        """

    @POST(API_APPLICATIONS_UPDATE_BRANCH_ENDPOINT)
    def update_branch(self, application, branch, name, project, projectBranch):
        """
        SINCE 7.3
        Update a branch on a given application.

        :param application: Application key
        :param branch: Branch name
        :param name: New branch name
        :param project: Project keys.To set several values, the parameter must be called once for each value.
        :param projectBranch: Project branches.To set main branch, provide an empty value. To set several values,
          the parameter must be called once for each value.

        :return:
        """

    @POST(API_APPLICATIONS_UPDATE_ENDPOINT)
    def update_application(self, application, name, description=None):
        """
        SINCE 7.3
        Update an application.

        :param application: Application key
        :param name: New name for the application
        :param description: New description for the application

        :return:
        """

    @POST(API_APPLICATIONS_SET_TAGS_ENDPOINT)
    def set_tags(self, application, tags):
        """
        SINCE 8.3
        Set tags on a application.

        :type application: Application key
        :param tags: Comma-separated list of tags
        :return:
        """
