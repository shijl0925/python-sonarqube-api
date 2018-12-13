#!/usr/bin/env python
#-*- coding:utf-8 -*-

from .common import decode_json
from .config import *

class SonarQubeUser(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_users_info_page(self,page):
        params = {
            'p': page
        }
        resp = self.sonarqube._make_call('get', RULES_USERS_SEARCH_ENDPOINT, **params)
        response = resp.json()
        return response

    def get_users_info(self):
        """
        获取所有用户信息
        :return:
        """
        response = self.get_users_info_page(1)
        users = []
        users_info = {}

        total_nums = response['paging']['total']
        page_size = response['paging']['pageSize']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.get_users_info_page(i + 1)
            users.extend(response['users'])
        for user in users:
            users_info[user['login']] = user
        return users_info

    def user_exist(self, login):
        """
        判断用户是否存在
        :param login:
        :return:
        """
        params = {
            'q': login
        }
        resp = self.sonarqube._make_call('get', RULES_USERS_SEARCH_ENDPOINT, **params)

        msg = decode_json(resp.json())
        users_info =  msg['users']

        users = []
        for u in users_info:
            users.append(u['login'])

        if len(users) != 0 and login in users:
            is_exist = True
        else:
            is_exist = False
        return is_exist

    def create_user(self, login, name, email, password, scm=None, local='true'):
        """
        创建用户
        :param login:
        :param name:
        :param email:
        :param password:
        :param scm:
        :param local:
        :return:
        """
        params = {
            'login': login,
            'name': name,
            'password': password,
            'email': email,
            'local': local
        }
        if scm:
            params['scmAccount'] = scm

        self.sonarqube._make_call('post', RULES_USERS_CREATE_ENDPOINT, **params)

    def update_user(self, login, name, email, scm=None):
        """
        更新用户
        :param login:
        :param name:
        :param email:
        :param scm:
        :return:
        """
        params = {
            'login': login,
            'name': name,
            'email': email,
        }
        if scm:
            params['scmAccount'] = scm

        self.sonarqube._make_call('post', RULES_USERS_UPDATE_ENDPOINT, **params)

    def change_user_password(self, login, newPassword, previousPassword=None):
        """
        修改用户密码
        :param login:
        :param newPassword:
        :param previousPassword:
        :return:
        """
        params = {
            'login': login,
            'password': newPassword
        }
        if previousPassword:
            params['previousPassword'] = previousPassword

        self.sonarqube._make_call('post', RULES_USERS_CHANGE_PASSWORD_ENDPOINT, **params)

    def deactivate_user(self, login):
        """
        解除用户
        :param login:
        :return:
        """
        params = {
            'login': login
        }
        self.sonarqube._make_call('post', RULES_USERS_DEACTIVATE_ENDPOINT, **params)

    def get_user_belong_groups(self, login):
        """
        获取指定用户所在的组
        :param login:
        :return:
        """
        params = {
            'login': login
        }
        resp = self.sonarqube._make_call('get', RULES_USERS_GROUPS_ENDPOINT, **params)
        response = resp.json()
        groups_info = response['groups']
        groups = [g['name'] for g in groups_info]
        return groups


