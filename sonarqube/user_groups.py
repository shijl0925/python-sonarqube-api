#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_USER_GROUPS_SEARCH_ENDPOINT,
    API_USER_GROUPS_CREATE_ENDPOINT,
    API_USER_GROUPS_DELETE_ENDPOINT,
    API_USER_GROUPS_UPDATE_ENDPOINT,
    API_USER_GROUPS_USERS_ENDPOINT,
    API_USER_GROUPS_ADD_USER_ENDPOINT,
    API_USER_GROUPS_REMOVE_USER_ENDPOINT
)


class SonarQubeUserGroups:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.search_user_groups()

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
        result = self.search_user_groups(q=group_name)
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

    def search_user_groups(self, fields=None, q=None):
        """
        Search for user groups.
        :param fields: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. such as:
            * name
            * description
            * membersCount
        :param q: Limit search to names that contain the supplied string.
        :return:
        """
        params = {}

        if fields:
            params.update({"f": fields})

        page_num = 1
        page_size = 1
        total = 2

        if q:
            params['q'] = q

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_USER_GROUPS_SEARCH_ENDPOINT, **params)
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
        :param group_name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
           The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return:
        """
        params = {
            'name': group_name
        }
        if description:
            params.update({'description': description})

        self.sonarqube.make_call('post', API_USER_GROUPS_CREATE_ENDPOINT, **params)

    def delete_group(self, group_name):
        """
        Delete a group. The default groups cannot be deleted.
        :param group_name:
        :return:
        """
        params = {
            'name': group_name
        }

        self.sonarqube.make_call('post', API_USER_GROUPS_DELETE_ENDPOINT, **params)

    def update_group(self, group_id, group_name=None, description=None):
        """
        Update a group.
        :param group_id: Identifier of the group.
        :param group_name: New optional name for the group. A group name cannot be larger than 255 characters and must
          be unique. Value 'anyone' (whatever the case) is reserved and cannot be used. If value is empty or not
        defined, then name is not changed.
        :param description: New optional description for the group. A group description cannot be larger than
          200 characters. If value is not defined, then description is not changed.
        :return:
        """
        params = {'id': group_id}

        if group_name:
            params.update({'name': group_name})

        if description:
            params.update({'description': description})

        self.sonarqube.make_call('post', API_USER_GROUPS_UPDATE_ENDPOINT, **params)

    def add_user_to_group(self, group_name, user_login):
        """
        Add a user to a group.
        :param group_name: Group name
        :param user_login: User login
        :return:
        """
        params = {
            'login': user_login,
            'name': group_name
        }
        self.sonarqube.make_call('post', API_USER_GROUPS_ADD_USER_ENDPOINT, **params)

    def remove_user_from_group(self, group_name, user_login):
        """
        Remove a user from a group.
        :param group_name: Group name
        :param user_login: User login
        :return:
        """
        params = {
            'login': user_login,
            'name': group_name
        }
        self.sonarqube.make_call('post', API_USER_GROUPS_REMOVE_USER_ENDPOINT, **params)

    def search_users_belong_to_group(self, group_name, q=None, selected="selected"):
        """
        Search for users with membership information with respect to a group.
        :param group_name: Group name
        :param q: Limit search to names or logins that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).such as:
          * all
          * deselected
          * selected
          default value is selected.
        :return:
        """
        params = {
            'name': group_name,
            'selected': selected
        }
        page_num = 1
        page_size = 1
        total = 2

        if q:
            params.update({'q': q})

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_USER_GROUPS_USERS_ENDPOINT, **params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for user in response['users']:
                yield user
