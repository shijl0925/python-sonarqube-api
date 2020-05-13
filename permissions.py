#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *


class SonarQubePermissions(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def project_permissions_add_group(self, projectKey, groupName, permissions):
        """
        给项目添加组权限
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
                self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)

    def project_permissions_remove_group(self, projectKey, groupName, permissions):
        """
        给项目删除组权限
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
                self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)

    def project_permissions_add_user(self, projectKey, login, permissions):
        """
        给项目添加用户权限
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
                self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_USER_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_USER_ENDPOINT, **params)

    def project_permissions_remove_user(self, projectKey, login, permissions):
        """
        给项目删除用户权限
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
                self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)

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
        self.sonarqube._make_call('post', RULES_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT, **params)
