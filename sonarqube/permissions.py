#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
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
    API_PERMISSIONS_UPDATE_TEMPLATE_ENDPOINT
)


class SonarQubePermissions:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def add_permission_to_group(self, groupName, permission, projectKey=None):
        """
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
        params = {
            'groupName': groupName,
            'permission': permission
        }
        if projectKey:
            params.update({"projectKey": projectKey})

        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)

    def remove_permission_from_group(self, groupName, permission, projectKey=None):
        """
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
        params = {
            'groupName': groupName,
            'permission': permission
        }
        if projectKey:
            params.update({"projectKey": projectKey})

        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)

    def add_permission_to_user(self, login, permission, projectKey=None):
        """
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
        params = {
            'login': login,
            'permission': permission
        }
        if projectKey:
            params.update({"projectKey": projectKey})

        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_USER_ENDPOINT, **params)

    def remove_permission_from_user(self, login, permission, projectKey=None):
        """
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
        params = {
            'login': login,
            'permission': permission
        }
        if projectKey:
            params.update({"projectKey": projectKey})

        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)

    def apply_template_to_project(self, template_name, project_key):
        """
        Apply a permission template to one project.

        :param template_name: Template name
        :param project_key: Project key
        :return:
        """
        params = {
            'projectKey': project_key,
            'templateName': template_name
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT, **params)

    def apply_template_to_projects(self, template_name, projects=None, analyzedBefore=None, onProvisionedOnly=None,
                                   q=None, qualifiers="TRK"):
        """
        Apply a permission template to several projects.

        :param template_name: Template name
        :param projects: Comma-separated list of project keys
        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
        :param onProvisionedOnly: Filter the projects that are provisioned
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
        params = {
            'templateName': template_name,
            'qualifiers': qualifiers
        }

        if projects:
            params.update({"projects": projects})

        if analyzedBefore:
            params.update({"analyzedBefore": analyzedBefore})

        if onProvisionedOnly:
            params.update({"onProvisionedOnly": onProvisionedOnly})

        if q:
            params.update({"q": q})

        self.sonarqube.make_call('post', API_PERMISSIONS_BULK_APPLY_TEMPLATE_ENDPOINT, **params)

    def add_group_to_template(self, group_name, template_name, permission):
        """
        Add a group to a permission template.

        :param group_name: Group name or 'anyone' (case insensitive)
        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'groupName': group_name,
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_GROUP_TO_TEMPLATE_ENDPOINT, **params)

    def remove_group_from_template(self, group_name, template_name, permission):
        """
        Remove a group from a permission template.

        :param group_name: Group name or 'anyone' (case insensitive)
        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'groupName': group_name,
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_GROUP_FROM_TEMPLATE_ENDPOINT, **params)

    def add_project_creator_to_template(self, template_name, permission):
        """
        Add a project creator to a permission template.

        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_PROJECT_CREATOR_TO_TEMPLATE_ENDPOINT, **params)

    def remove_project_creator_from_template(self, template_name, permission):
        """
        Remove a project creator from a permission template.

        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_PROJECT_CREATOR_FROM_TEMPLATE_ENDPOINT, **params)

    def add_user_to_template(self, user_login, template_name, permission):
        """
        Add a user to a permission template.

        :param user_login: User login
        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'login': user_login,
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_USER_TO_TEMPLATE_ENDPOINT, **params)

    def remove_user_from_template(self, user_login, template_name, permission):
        """
        Remove a user from a permission template.

        :param user_login: User login
        :param template_name: Template name
        :param permission: Permission
          Possible values are for:
            * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'login': user_login,
            'templateName': template_name,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_USER_FROM_TEMPLATE_ENDPOINT, **params)

    def create_template(self, template_name, description=None, projectKeyPattern=None):
        """
        Create a permission template.

        :param template_name: Template name
        :param description: Template description
        :param projectKeyPattern: Project key pattern. Must be a valid Java regular expression
        :return:
        """
        params = {
            'name': template_name
        }

        if description:
            params.update({"description": description})

        if projectKeyPattern:
            params.update({"projectKeyPattern": projectKeyPattern})

        self.sonarqube.make_call('post', API_PERMISSIONS_CREATE_TEMPLATE_ENDPOINT, **params)

    def delete_template(self, template_name):
        """
        Delete a permission template.

        :param template_name: Template name
        :return:
        """
        params = {
            'templateName': template_name
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_DELETE_TEMPLATE_ENDPOINT, **params)

    def search_templates(self, q=None):
        """
        List permission templates.

        :param q: Limit search to permission template names that contain the supplied string.
        :return: defaultTemplates, permissionTemplates, permissions
        """
        params = {}

        if q:
            params.update({"q": q})

        resp = self.sonarqube.make_call('get', API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT, **params)
        response = resp.json()
        return response

    def set_default_template(self, template_name, qualifier="TRK"):
        """
        Set a permission template as default.

        :param template_name: Template name
        :param qualifier: Project qualifier. Filter the results with the specified qualifier.
          Possible values are:
            * TRK - Projects
          default value is TRK.
        :return:
        """
        params = {
            'templateName': template_name,
            'qualifier': qualifier
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_SET_DEFAULT_TEMPLATE_ENDPOINT, **params)

    def update_template(self, template_id, template_name=None, description=None, projectKeyPattern=None):
        """
        Update a permission template.

        :param template_id: Template id
        :param template_name: Template name
        :param description: Template description
        :param projectKeyPattern: Project key pattern. Must be a valid Java regular expression
        :return:
        """
        params = {
            'id': template_id
        }

        if template_name:
            params.update({"name": template_name})

        if description:
            params.update({"description": description})

        if projectKeyPattern:
            params.update({"projectKeyPattern": projectKeyPattern})

        self.sonarqube.make_call('post', API_PERMISSIONS_UPDATE_TEMPLATE_ENDPOINT, **params)
