#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PERMISSIONS_ADD_GROUP_ENDPOINT,
    API_PERMISSIONS_REMOVE_GROUP_ENDPOINT,
    API_PERMISSIONS_ADD_USER_ENDPOINT,
    API_PERMISSIONS_REMOVE_USER_ENDPOINT,
    API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT
)


class SonarQubePermissions:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def project_permissions_add_group(self, projectKey, groupName, permission):
        """
        Add permission to a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.
        :param projectKey: Project key
        :param groupName: Group name or 'anyone' (case insensitive)
        :param permission: Permission
          * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
          * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'groupName': groupName,
            'projectKey': projectKey,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)

    def project_permissions_remove_group(self, projectKey, groupName, permission):
        """
        Remove a permission from a group.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        The group name must be provided.
        :param projectKey: Project key
        :param groupName: Group name or 'anyone' (case insensitive)
        :param permission: Permission
          * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
          * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'groupName': groupName,
            'projectKey': projectKey,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)

    def project_permissions_add_user(self, projectKey, login, permission):
        """
        Add permission to a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        :param projectKey: Project key
        :param login: User login
        :param permission: Permission
          * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
          * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'login': login,
            'projectKey': projectKey,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_ADD_USER_ENDPOINT, **params)

    def project_permissions_remove_user(self, projectKey, login, permission):
        """
        Remove permission from a user.
        This service defaults to global permissions, but can be limited to project permissions by providing project key.
        :param projectKey: Project key
        :param login: User login
        :param permission: Permission
          * Possible values for global permissions: admin, profileadmin, gateadmin, scan, provisioning
          * Possible values for project permissions admin, codeviewer, issueadmin, securityhotspotadmin, scan, user
        :return:
        """
        params = {
            'login': login,
            'projectKey': projectKey,
            'permission': permission
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)

    def apply_template_to_project(self, project_key, template_id):
        """
        Apply a permission template to one project.
        :param project_key: Project key
        :param template_id: Template id
        :return:
        """
        params = {
            'projectKey': project_key,
            'templateId': template_id
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT, **params)
