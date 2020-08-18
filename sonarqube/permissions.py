#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sonarqube.config import (
    API_PERMISSIONS_ADD_GROUP_ENDPOINT,
    API_PERMISSIONS_REMOVE_GROUP_ENDPOINT,
    API_PERMISSIONS_ADD_USER_ENDPOINT,
    API_PERMISSIONS_REMOVE_USER_ENDPOINT,
    API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT,
    API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT
)


class SonarQubePermissions:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def project_permissions_add_group(self, projectKey, groupName, permissions):
        """
        Add permission to a group.
        :param projectKey:
        :param groupName:
        :param permissions:
        :return:
        """
        params = {
            'groupName': groupName,
            'projectKey': projectKey
        }
        if isinstance(permissions, list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube.make_call('post', API_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube.make_call('post', API_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)

    def project_permissions_remove_group(self, projectKey, groupName, permissions):
        """
        Remove a permission from a group.
        :param projectKey:
        :param groupName:
        :param permissions:
        :return:
        """
        params = {
            'groupName': groupName,
            'projectKey': projectKey
        }
        if isinstance(permissions, list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)

    def project_permissions_add_user(self, projectKey, login, permissions):
        """
        Add permission to a user.
        :param projectKey:
        :param login:
        :param permissions:
        :return:
        """
        params = {
            'login': login,
            'projectKey': projectKey
        }
        if isinstance(permissions, list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube.make_call('post', API_PERMISSIONS_ADD_USER_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube.make_call('post', API_PERMISSIONS_ADD_USER_ENDPOINT, **params)

    def project_permissions_remove_user(self, projectKey, login, permissions):
        """
        Remove permission from a user.
        :param projectKey:
        :param login:
        :param permissions:
        :return:
        """
        params = {
            'login': login,
            'projectKey': projectKey
        }
        if isinstance(permissions, list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube.make_call('post', API_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)

    def apply_template_to_project(self, project_key, template_id):
        """
        Apply a permission template to one project.
        :param project_key:
        :param template_id:
        :return:
        """
        params = {
            'projectKey': project_key,
            'templateId': template_id
        }
        self.sonarqube.make_call('post', API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT, **params)
    
    def get_all_permission_templates(self, templateName):
        """
        Search for permission templates.
        If no template name, response will contain all permission templates in list of dicts. Otherwise, will return single json dict.
        :param templateName:
        :return:
        """
        params = {
            'template': templateName
        }
        response = self.sonarqube._make_call('get', API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT, **params)
        return response
        
