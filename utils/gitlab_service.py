#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gitlab
from collections import defaultdict
from common import get_json_data, clock
import sys
import os

# Access level constants
ACCESS_LEVEL_GUEST = gitlab.GUEST_ACCESS
ACCESS_LEVEL_REPORTER = gitlab.REPORTER_ACCESS
ACCESS_LEVEL_DEVELOPER = gitlab.DEVELOPER_ACCESS
ACCESS_LEVEL_MASTER = gitlab.MASTER_ACCESS
ACCESS_LEVEL_OWNER = gitlab.OWNER_ACCESS

class gitlab_service(object):
    def __init__(self, gitlab_server):
        self.gitlab_server = gitlab_server

    def __repr__(self):
        return '[gitlab_service: {}]'.format(self.gitlab_server._url)

    @clock
    def gitlab_groups(self):
        """
        获取所有gitlab
        :return:
        """
        return self.gitlab_server.groups.list(all=True)

    def gitlab_groups_name(self):
        """
        获取所有gitlab分组名字
        :return:
        """
        return self.gitlab_groups_attributes().keys()

    def gitlab_groups_attributes(self, params=None):
        """
        获取gitlab groups属性信息
        :return:
        """
        groups = self.gitlab_groups()
        attributes = {item.path: item.attributes for item in groups}

        if params is not None:
            params_attributes = {}
            pp = params.split(',')
            for path, values in attributes.items():
                v = {}
                for p in pp:
                    if p in values:
                        v[p] = values[p]
                params_attributes[path] = v
            return params_attributes
        else:
            return attributes

    @staticmethod
    def get_gitlab_group_all_members(gitlab_group):
        """
        获取gitlab分组的成员
        :param gitlab_group:
        :return:
        """
        group_members = gitlab_group.members.list(all=True)
        return group_members

    @staticmethod
    def get_gitlab_group_members_with_state(gitlab_group, state):
        """
        获取gitlab分组的成员(state)
        :param gitlab_group:
        :param state:
        :return:
        """
        group_members = gitlab_group.members.list(all=True)
        state_group_members = [m for m in group_members if m.state == state]
        return state_group_members

    @staticmethod
    def get_gitlab_group_members_with_access_levels(gitlab_group, access_levels):
        """
        获取gitlab分组的成员(access_levels)
        :param gitlab_group:
        :param access_levels:
        :return:
        """
        group_members = gitlab_group.members.list(all=True)
        al = list(map(int, access_levels.split(',')))
        access_levels_group_members = [m for m in group_members if m.access_level in al]
        return access_levels_group_members

    def get_gitlab_groups_select_members(self, state=None, access_levels=None):
        """
        获取gitlab所有分组的成员
        :param state:
        :param access_levels:
        :return:
        """
        groups = self.gitlab_groups()
        group_members_dict = defaultdict(list)
        for item in groups:
            group_name = item.name
            all_members = self.get_gitlab_group_all_members(item)

            if state is not None:
                active_members = [m for m in all_members if m.state == state]
            else:
                active_members = all_members

            if access_levels is not None:
                al = list(map(int, access_levels.split(',')))
                access_levels_members = [m for m in all_members if m.access_level in al]
            else:
                access_levels_members = all_members

            group_members = list(set(all_members) & set(active_members) & set(access_levels_members))
            for m in group_members:
                group_members_dict[group_name].append(m)

        return group_members_dict

    def get_gitlab_project(self, project_path):
        """
        通过项目路径得到gitlab项目
        :param project_path:
        :return:
        """
        return self.gitlab_server.projects.get(project_path)

    @clock
    def gitlab_projects(self):
        """
        获取所有gitlab项目
        :return:
        """
        return self.gitlab_server.projects.list(all=True)

    def gitlab_projects_attributes(self, params=None):
        """
        获取gitlab projects属性信息
        :return:
        """
        projects = self.gitlab_projects()
        attributes = {item.path_with_namespace: item.attributes for item in projects}

        if params is not None:
            params_attributes = {}
            pp = params.split(',')
            for path, values in attributes.items():
                v = {}
                for p in pp:
                    if p in values:
                        v[p] = values[p]
                params_attributes[path] = v
            return params_attributes
        else:
            return attributes

    def gitlab_projects_name(self):
        """
        获取所有gitlab项目名字
        :return:
        """
        return self.gitlab_projects_attributes().keys()

    @staticmethod
    def get_gitlab_project_all_members(gitlab_project):
        """
        获取gitlab项目的成员
        :param gitlab_project:
        :return:
        """
        project_members = gitlab_project.members.list(all=True)
        return project_members

    @staticmethod
    def get_gitlab_project_members_with_state(gitlab_project, state):
        """
        获取gitlab项目的成员(state)
        :param gitlab_project:
        :param state:
        :return:
        """
        project_members = gitlab_project.members.list(all=True)
        state_project_members = [m for m in project_members if m.state == state]
        return state_project_members

    @staticmethod
    def get_gitlab_project_members_with_access_levels(gitlab_project, access_levels):
        """
        获取gitlab项目的成员(access_levels)
        :param gitlab_project:
        :param access_levels:
        :return:
        """
        project_members = gitlab_project.members.list(all=True)
        al = list(map(int, access_levels.split(',')))
        access_levels_project_members = [m for m in project_members if m.access_level in al]
        return access_levels_project_members

    def get_gitlab_projects_select_members(self, state=None, access_levels=None):
        """
        获取所有项目的成员
        :param state:
        :param access_levels:
        :return:
        """
        all_projects = self.gitlab_projects()
        projects_members_dict = defaultdict(list)

        for item in all_projects:
            path = item.path_with_namespace
            all_members = self.get_gitlab_project_all_members(item)

            if state is not None:
                state_members = [m for m in all_members if m.state == state]
            else:
                state_members = all_members

            if access_levels is not None:
                al = list(map(int, access_levels.split(',')))
                access_levels_members = [m for m in all_members if m.access_level in al]
            else:
                access_levels_members = all_members

            projects_members = list(set(all_members) & set(state_members) & set(access_levels_members))

            for m in projects_members:
                projects_members_dict[path].append(m)

        return projects_members_dict

    def gitlab_page_projects(self, page):
        """
        获取指定页的项目
        :param page:
        :return:
        """
        return self.gitlab_server.projects.list(page=page)

    def get_gitlab_users_info(self):
        """
        获取gitlab用户信息
        :return:
        """
        users = self.gitlab_server.users.list(all=True)
        users_info = {}
        for u in users:
            username = u.username
            email = u.email
            name = u.name
            state = u.state
            users_info[username] = {'email': email, 'name': name, 'state': state}
        return users_info

