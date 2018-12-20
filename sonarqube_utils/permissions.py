#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *

class SonarQubePermissions(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def project_permissions_add_group(self, project_key, group_name, permissions):
        """
        给项目添加组权限
        :param project_key:
        :param group_name:
        :param permissions:
        :return:
        """
        params = {
            'groupName': group_name,
            'projectKey': project_key,
            'permission': ''
        }
        if isinstance(permissions, list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)
        elif isinstance(permissions, str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_GROUP_ENDPOINT, **params)

    def project_permissions_remove_group(self, project_key, group_name, permissions):
        """
        给项目删除组权限
        :param project_key:
        :param group_name:
        :param permissions:
        :return:
        """
        params = {
            'groupName': group_name,
            'projectKey': project_key,
            'permission': ''
        }
        if isinstance(permissions,list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)
        elif isinstance(permissions,str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_GROUP_ENDPOINT, **params)

    def project_permissions_add_user(self,project_key, login, permissions):
        """
        给项目添加用户权限
        :param project_key:
        :param login:
        :param permissions:
        :return:
        """
        params = {
            'login': login,
            'projectKey': project_key,
            'permission': ''
        }
        if isinstance(permissions,list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_USER_ENDPOINT, **params)
        elif isinstance(permissions,str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_ADD_USER_ENDPOINT, **params)

    def project_permissions_remove_user(self, project_key, login, permissions):
        """
        给项目删除用户权限
        :param project_key:
        :param login:
        :param permissions:
        :return:
        """
        params = {
            'login': login,
            'projectKey': project_key,
            'permission': ''
        }
        if isinstance(permissions,list):
            for perm in permissions:
                params['permission'] = perm
                self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)
        elif isinstance(permissions,str):
            params['permission'] = permissions
            self.sonarqube._make_call('post', RULES_PERMISSIONS_REMOVE_USER_ENDPOINT, **params)
