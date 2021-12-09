#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.permissions import SonarQubePermissions
from sonarqube.utils.config import (
    API_PERMISSIONS_ADD_GROUP_ENDPOINT,
    API_PERMISSIONS_REMOVE_GROUP_ENDPOINT,
    API_PERMISSIONS_ADD_USER_ENDPOINT,
    API_PERMISSIONS_REMOVE_USER_ENDPOINT,
    API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_ADD_GROUP_TO_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_REMOVE_GROUP_FROM_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_ADD_PROJECT_CREATOR_TO_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_REMOVE_PROJECT_CREATOR_FROM_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_ADD_USER_TO_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_REMOVE_USER_FROM_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_BULK_APPLY_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_CREATE_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_DELETE_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT,
    API_PERMISSIONS_SET_DEFAULT_TEMPLATE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarCloudPermissions(SonarQubePermissions):
    """
    SonarCloud permissions Operations
    """

    @POST(API_PERMISSIONS_ADD_GROUP_ENDPOINT)
    def add_permission_to_group(
        self, groupName, organization, permission, projectKey=None
    ):
        """
        Add permission to a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param organization: Key of organization
        :param permission: Permission.
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_GROUP_ENDPOINT)
    def remove_permission_from_group(
        self, groupName, organization, permission, projectKey=None
    ):
        """
        Remove a permission from a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param organization: Key of organization
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_ADD_USER_ENDPOINT)
    def add_permission_to_user(self, login, organization, permission, projectKey=None):
        """
        Add permission to a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.

        :param login: User login
        :param organization: Key of organization
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_USER_ENDPOINT)
    def remove_permission_from_user(
        self, login, organization, permission, projectKey=None
    ):
        """
        Remove permission from a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.

        :param login: User login
        :param organization: Key of organization
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT)
    def apply_template_to_project(self, templateName, organization, projectKey):
        """
        Apply a permission template to one project.

        :param templateName: Template name
        :param organization: Key of organization
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_BULK_APPLY_TEMPLATE_ENDPOINT)
    def apply_template_to_projects(
        self,
        templateName,
        organization,
        projects=None,
        analyzedBefore=None,
        onProvisionedOnly="false",
        q=None,
        qualifiers="TRK",
    ):
        """
        Apply a permission template to several projects.

        :param templateName: Template name
        :param organization: Key of organization
        :param projects: Comma-separated list of project keys
        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
        :param onProvisionedOnly: Filter the projects that are provisioned.
          Possible values are for: true or false. default value is false.
        :param q: Limit search to:
          Possible values are for:
            * project names that contain the supplied string
            * project keys that are exactly the same as the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified
          qualifiers. Possible values are:
            * TRK - Projects
          default value is TRK.
        :return:
        """

    @POST(API_PERMISSIONS_ADD_GROUP_TO_TEMPLATE_ENDPOINT)
    def add_group_to_template(self, groupName, organization, templateName, permission):
        """
        Add a group to a permission template.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param organization: Key of organization
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_GROUP_FROM_TEMPLATE_ENDPOINT)
    def remove_group_from_template(
        self, groupName, organization, templateName, permission
    ):
        """
        Remove a group from a permission template.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param organization: Key of organization
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_ADD_PROJECT_CREATOR_TO_TEMPLATE_ENDPOINT)
    def add_project_creator_to_template(self, templateName, organization, permission):
        """
        Add a project creator to a permission template.

        :param templateName: Template name
        :param organization: Key of organizatio
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_PROJECT_CREATOR_FROM_TEMPLATE_ENDPOINT)
    def remove_project_creator_from_template(
        self, templateName, organization, permission
    ):
        """
        Remove a project creator from a permission template.

        :param templateName: Template name
        :param organization: Key of organization
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_ADD_USER_TO_TEMPLATE_ENDPOINT)
    def add_user_to_template(self, login, organization, templateName, permission):
        """
        Add a user to a permission template.

        :param login: User login
        :param organization: Key of organization
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_USER_FROM_TEMPLATE_ENDPOINT)
    def remove_user_from_template(self, login, organization, templateName, permission):
        """
        Remove a user from a permission template.

        :param login: User login
        :param organization: Key of organization
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_CREATE_TEMPLATE_ENDPOINT)
    def create_template(
        self, name, organization, description=None, projectKeyPattern=None
    ):
        """
        Create a permission template.

        :param name: Template name
        :param organization: Key of organization
        :param description: Template description
        :param projectKeyPattern: Project key pattern. Must be a valid Java regular expression
        :return: request response.
        """

    @POST(API_PERMISSIONS_DELETE_TEMPLATE_ENDPOINT)
    def delete_template(self, templateName, organization):
        """
        Delete a permission template.

        :param templateName: Template name
        :param organization: Key of organization
        :return:
        """

    @GET(API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT)
    def search_templates(self, organization, q=None):
        """
        List permission templates.

        :param organization: Key of organization
        :param q: Limit search to permission template names that contain the supplied string.
        :return: defaultTemplates, permissionTemplates, permissions
        """

    @POST(API_PERMISSIONS_SET_DEFAULT_TEMPLATE_ENDPOINT)
    def set_default_template(self, templateName, organization, qualifier="TRK"):
        """
        Set a permission template as default.

        :param templateName: Template name
        :param organization: Key of organization
        :param qualifier: Project qualifier. Filter the results with the specified qualifier.
          Possible values are:
            * TRK - Projects
          default value is TRK.
        :return:
        """
