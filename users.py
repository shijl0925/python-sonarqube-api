#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *


class SonarQubeUser(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.search_users()

    def iterkeys(self):
        """
        获取所有用户的登录名，返回生成器
        """
        for item in self:
            yield item['login']

    def keys(self):
        """
        获取所有用户的登录名，返回列表
        """
        return list(self.iterkeys())

    def __len__(self):
        """
        获取用户数量
        :return:
        """
        return len(self.keys())

    def __contains__(self, login_name):
        """
        判断用户是否存在
        """
        result = self.search_users(filter=login_name)
        logins = [item['login'] for item in result]
        return login_name in logins

    def __getitem__(self, index):
        """
        根据坐标获取用户信息
        :param index:
        :return:
        """
        return list(self)[index]

    def __iter__(self):
        """
        实现迭代
        :return:
        """
        self.poll()
        return self._data

    def search_users(self, filter=None):
        """
        获取所有用户信息
        :param filter:
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        if filter is not None:
            params['q'] = filter

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_USERS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for user in response['users']:
                yield user

    def create_user(self, login, name, email, password=None, local='true', scm=None):
        """
        创建用户
        :param login:
        :param name:
        :param email:
        :param password:
        :param local:
        :param scm:
        :return:
        """
        params = {
            'login': login,
            'name': name,
            'email': email,
            'local': local
        }
        if local == 'true' and password:
            params['password'] = password

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

    def get_user_belong_to_groups(self, login):
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
