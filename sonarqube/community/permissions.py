#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PERMISSIONS_ADD_GROUP_ENDPOINT,
    API_PERMISSIONS_REMOVE_GROUP_ENDPOINT,
    API_PERMISSIONS_USERS_ENDPOINT,
    API_PERMISSIONS_GROUPS_ENDPOINT,
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
    API_PERMISSIONS_UPDATE_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_GET_TEMPLATE_USERS,
    API_PERMISSIONS_GET_TEMPLATE_GROUPS,
)
from sonarqube.utils.common import GET, PAGES_GET, POST


class SonarQubePermissions(RestClient):
    """
    SonarQube permissions Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubePermissions, self).__init__(**kwargs)

    @POST(API_PERMISSIONS_ADD_GROUP_ENDPOINT)
    def add_permission_to_group(self, groupName, permission, projectKey=None):
        """
        SINCE 5.2
        Add permission to a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param permission: Permission.
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_GROUP_ENDPOINT)
    def remove_permission_from_group(self, groupName, permission, projectKey=None):
        """
        SINCE 5.2
        Remove a permission from a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_ADD_USER_ENDPOINT)
    def add_permission_to_user(self, login, permission, projectKey=None):
        """
        SINCE 5.2
        Add permission to a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.

        :param login: User login
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @PAGES_GET(API_PERMISSIONS_USERS_ENDPOINT, item="users")
    def get_users_permissions(self, permission=None, projectKey=None, q=None):
        """
        SINCE 5.2
        Lists the users with their permissions as individual users rather than through group affiliation.
        This service defaults to global permissions, but can be limited to project permissions by providing project id or project key.
        This service defaults to all users, but can be limited to users with a specific permission by providing the desired permission.

        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :param q: Limit search to user names that contain the supplied string
        :return:
        """

    @PAGES_GET(API_PERMISSIONS_GROUPS_ENDPOINT, item="groups")
    def get_groups_permissions(self, permission=None, projectKey=None, q=None):
        """
        SINCE 5.2
        Lists the groups with their permissions.
        This service defaults to global permissions, but can be limited to project permissions by providing project id or project key.
        This service defaults to all groups, but can be limited to groups with a specific permission by providing the desired permission.

        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :param projectId: Project id
        :param q: Limit search to group names that contain the supplied string
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_USER_ENDPOINT)
    def remove_permission_from_user(self, login, permission, projectKey=None):
        """
        SINCE 5.2
        Remove permission from a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.

        :param login: User login
        :param permission: Permission
          Possible values are for:
            * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT)
    def apply_template_to_project(self, templateName, projectKey):
        """
        SINCE 5.2
        Apply a permission template to one project.

        :param templateName: Template name
        :param projectKey: Project key
        :return:
        """

    @POST(API_PERMISSIONS_BULK_APPLY_TEMPLATE_ENDPOINT)
    def apply_template_to_projects(
        self,
        templateName,
        projects=None,
        analyzedBefore=None,
        onProvisionedOnly="false",
        q=None,
        qualifiers="TRK",
    ):
        """
        SINCE 5.5
        Apply a permission template to several projects.

        :param templateName: Template name
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
    def add_group_to_template(self, groupName, templateName, permission):
        """
        SINCE 5.2
        Add a group to a permission template.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_GROUP_FROM_TEMPLATE_ENDPOINT)
    def remove_group_from_template(self, groupName, templateName, permission):
        """
        SINCE 5.2
        Remove a group from a permission template.

        :param groupName: Group name or 'anyone' (case insensitive)
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_ADD_PROJECT_CREATOR_TO_TEMPLATE_ENDPOINT)
    def add_project_creator_to_template(self, templateName, permission):
        """
        SINCE 6.0
        Add a project creator to a permission template.

        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_PROJECT_CREATOR_FROM_TEMPLATE_ENDPOINT)
    def remove_project_creator_from_template(self, templateName, permission):
        """
        SINCE 6.0
        Remove a project creator from a permission template.

        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_ADD_USER_TO_TEMPLATE_ENDPOINT)
    def add_user_to_template(self, login, templateName, permission):
        """
        SINCE 5.2
        Add a user to a permission template.

        :param login: User login
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_REMOVE_USER_FROM_TEMPLATE_ENDPOINT)
    def remove_user_from_template(self, login, templateName, permission):
        """
        SINCE 5.2
        Remove a user from a permission template.

        :param login: User login
        :param templateName: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """

    @POST(API_PERMISSIONS_CREATE_TEMPLATE_ENDPOINT)
    def create_template(self, name, description=None, projectKeyPattern=None):
        """
        SINCE 5.2
        Create a permission template.

        :param name: Template name
        :param description: Template description
        :param projectKeyPattern: Project key pattern. Must be a valid Java regular expression
        :return: request response.
        """

    @POST(API_PERMISSIONS_DELETE_TEMPLATE_ENDPOINT)
    def delete_template(self, templateName):
        """
        SINCE 5.2
        Delete a permission template.

        :param templateName: Template name
        :return:
        """

    @GET(API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT)
    def search_templates(self, q=None):
        """
        SINCE 5.2
        List permission templates.

        :param q: Limit search to permission template names that contain the supplied string.
        :return: defaultTemplates, permissionTemplates, permissions
        """

    @PAGES_GET(API_PERMISSIONS_GET_TEMPLATE_USERS, item="users")
    def get_template_users(self, templateId, permission=None):
        """
        List of users and their permissions for the specified template.

        :param templateId: Id of permission template
        :param permission: Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        return: users
        """

    @PAGES_GET(API_PERMISSIONS_GET_TEMPLATE_GROUPS, item="groups")
    def get_template_groups(self, templateId, permission=None):
        """
        List of groups and their permissions for the specified template.

        :param templateId: Id of permission template
        :param permission: Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        return: groups
        """

    @POST(API_PERMISSIONS_SET_DEFAULT_TEMPLATE_ENDPOINT)
    def set_default_template(self, templateName, qualifier="TRK"):
        """
        SINCE 5.2
        Set a permission template as default.

        :param templateName: Template name
        :param qualifier: Project qualifier. Filter the results with the specified qualifier.
          Possible values are:
            * TRK - Projects
          default value is TRK.
        :return:
        """

    @POST(API_PERMISSIONS_UPDATE_TEMPLATE_ENDPOINT)
    def update_template(self, id, name=None, description=None, projectKeyPattern=None):
        """
        SINCE 5.2
        Update a permission template.

        :param id: Template id
        :param name: Template name
        :param description: Template description
        :param projectKeyPattern: Project key pattern. Must be a valid Java regular expression
        :return: request response
        """
