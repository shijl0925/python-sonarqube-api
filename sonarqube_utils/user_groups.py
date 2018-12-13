#!/usr/bin/env python
#-*- coding:utf-8 -*-
from .config import *

class SonarQubeUser_Groups(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_groups_page(self, page):
        """
        按页获取所有组信息
        :param page:
        :return:
        """
        params = {
            'p':page
        }
        resp = self.sonarqube._make_call('get', RULES_USER_GROUPS_SEARCH_ENDPOINT, **params)
        response = resp.json()
        return response

    def get_groups_info(self):
        """
        获取所有组的信息
        :return:
        """
        response = self.get_groups_page(1)
        groups = []

        total_nums = response['paging']['total']
        page_size = response['paging']['pageSize']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.get_groups_page(i + 1)
            groups.extend(response['groups'])

        groups_info = []
        for item in groups:
            groups_info.append(item)
        return groups_info

    def group_exist(self, group_name):
        """
        判断组是否存在
        :param group_name:
        :return:
        """
        params = {
            'q': group_name
        }
        resp = self.sonarqube._make_call('get', RULES_USER_GROUPS_SEARCH_ENDPOINT, **params)
        response = resp.json()
        groups_info = response['groups']
        groups = [g['name'] for g in groups_info]
        if group_name in groups:
            return True
        else:
            return False

    def create_group(self, group_name, description=None):
        """
        创建组
        :param group_name:
        :param description:
        :return:
        """
        params = {
            'name': group_name
        }
        if description:
            params['description'] = description

        self.sonarqube._make_call('post', RULES_USER_GROUPS_CREATE_ENDPOINT, **params)

    def delete_group(self, group_name):
        """
        删除组
        :param group_name:
        :return:
        """
        params = {
            'name': group_name
        }
        self.sonarqube._make_call('post', RULES_USER_GROUPS_DELETE_ENDPOINT, **params)

    def update_group(self, group_id, group_name, description=None):
        """
        更新组信息
        :param group_id:
        :param group_name:
        :param description:
        :return:
        """
        params = {
            'id': group_id,
            'name': group_name
        }
        if description:
            params['description'] = description

        self.sonarqube._make_call('post', RULES_USER_GROUPS_UPDATE_ENDPOINT, **params)

    def add_group_user(self, group, login):
        """
        将用户添加到组
        :param group:
        :param login:
        :return:
        """
        params = {
            'login': login,
            'name': group
        }
        self.sonarqube._make_call('post', RULES_USER_GROUPS_ADD_USER_ENDPOINT, **params)

    def delete_group_user(self, group, login):
        """
        将用户从组中删除
        :param group:
        :param login:
        :return:
        """
        params = {
            'login': login,
            'name': group
        }
        self.sonarqube._make_call('post', RULES_USER_GROUPS_REMOVE_USER_ENDPOINT, **params)

    def group_users_info_page(self, group, page):
        """
        按页查看指定组内成员
        :param group:
        :param page:
        :return:
        """
        params = {
            'name': group,
            'p':page
        }
        resp = self.sonarqube._make_call('get', RULES_USER_GROUPS_USERS_ENDPOINT, **params)
        response = resp.json()
        return response

    def group_users_info(self, group):
        """
        查看指定组内成员
        :param group:
        :return:
        """
        response = self.group_users_info_page(group, 1)
        users_info = []

        total_nums = response['total']
        page_size = response['ps']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.group_users_info_page(group, i + 1)
            users_info.extend(response['users'])
        return users_info

    def group_has_users(self, group):
        """
        查看指定组内成员的名字
        :param group:
        :return:
        """
        users_info = self.group_users_info(group)
        group_users = []
        for user_info in users_info:
            group_users.append(user_info['login'])
        return group_users
