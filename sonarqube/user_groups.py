#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeUser_Groups(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.get_groups_data()

    def iterkeys(self):
        """
        获取所有用户组的名字，返回生成器
        """
        for item in self:
            yield item['name']

    def keys(self):
        """
        获取所有用户组的名字，返回列表
        """
        return list(self.iterkeys())

    def __len__(self):
        """
        获取用户组数量
        :return:
        """
        return len(self.keys())

    def __contains__(self, group_name):
        """
        判断用户组是否存在
        """
        result = self.get_groups_data(filter=group_name)
        groups = [item['name'] for item in result]
        return group_name in groups

    def __iter__(self):
        """
        实现迭代
        :return:
        """
        self.poll()
        return self._data

    def __getitem__(self, index):
        """
        根据坐标获取用户组信息
        :param index:
        :return:
        """
        return list(self)[index]

    def get_groups_data(self, fields=None, filter=None):
        """
        Search for user groups.
        :param fields: 可能的值：name,description,membersCount
        :param filter:
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        if fields:
            if not isinstance(fields, str):
                fields = ','.join(fields)
            params['f'] = fields.lower()

        if filter is not None:
            params['q'] = filter

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', API_USER_GROUPS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for group in response['groups']:
                yield group

    def create_group(self, group_name, description=None):
        """
        Create a group.
        :param group_name:
        :param description:
        :return:
        """
        params = {
            'name': group_name
        }
        if description:
            params['description'] = description

        self.sonarqube._make_call('post', API_USER_GROUPS_CREATE_ENDPOINT, **params)

    def delete_group(self, group_name):
        """
        Delete a group. The default groups cannot be deleted.
        :param group_name:
        :return:
        """
        params = {
            'name': group_name
        }

        self.sonarqube._make_call('post', API_USER_GROUPS_DELETE_ENDPOINT, **params)

    def update_group(self, group_id, **kwargs):
        """
        Update a group.
        :param group_id:
        :param group_name:
        :param description:
        :return:
        """
        params = {'id': group_id}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube._make_call('post', API_USER_GROUPS_UPDATE_ENDPOINT, **params)

    def add_user_to_group(self, name, login):
        """
        Add a user to a group.
        :param name:
        :param login:
        :return:
        """
        params = {
            'login': login,
            'name': name
        }
        self.sonarqube._make_call('post', API_USER_GROUPS_ADD_USER_ENDPOINT, **params)

    def delete_user_from_group(self, name, login):
        """
        Remove a user from a group.
        :param name:
        :param login:
        :return:
        """
        params = {
            'login': login,
            'name': name
        }
        self.sonarqube._make_call('post', API_USER_GROUPS_REMOVE_USER_ENDPOINT, **params)

    def get_users_belong_to_group(self, name, **kwargs):
        """
        Search for users with membership information with respect to a group.
        :param name:
        :return:
        """
        params = {'name': name}
        page_num = 1
        page_size = 1
        total = 2

        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', API_USER_GROUPS_USERS_ENDPOINT, **params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for user in response['users']:
                yield user
