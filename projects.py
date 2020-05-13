#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeProject(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.get_projects_data()

    def iterkeys(self):
        """
        获取所有项目的key，返回生成器
        """
        for item in self:
            yield item['key']

    def keys(self):
        """
        获取所有项目的key，返回列表
        """
        return list(self.iterkeys())

    def __len__(self):
        """
        获取项目
        :return:
        """
        return len(self.keys())

    def __contains__(self, project_key):
        """
        判断项目是否存在
        """
        result = self.get_projects_data()
        project_keys = [item['key'] for item in result]
        return project_key in project_keys

    def __getitem__(self, index):
        """
        根据坐标获取项目信息
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

    def get_projects_data(self, **kwargs):
        """
        获取所有项目信息
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_PROJECTS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def create_project(self, project, name, branch=None):
        """
        创建项目
        :param project:
        :param name:
        :param branch:
        :return:
        """
        params = {
            'name': name,
            'project': project
        }
        if branch:
            params['branch'] = branch

        self.sonarqube._make_call('post', RULES_PROJECTS_CREATE_ENDPOINT, **params)

    def get_project_id(self, project_key):
        """
        获取指定项目的id
        :param project_key:
        :return:
        """
        components = self.sonarqube.components.get_project_component(project_key)
        return components['id']

    def delete_project(self, project):
        """
        删除项目
        :param project:
        :return:
        """
        params = {
            'project': project
        }
        self.sonarqube._make_call('post', RULES_PROJECTS_DELETE_ENDPOINT, **params)

    def update_project_key(self, previous_project_key, new_project_key):
        """
        更新项目key
        :param previous_project_key:
        :param new_project_key:
        :return:
        """
        params = {
            'from': previous_project_key,
            'to': new_project_key
        }
        self.sonarqube._make_call('post',RULES_PROJECTS_UPDATE_KEY_ENDPOINT,**params)

    def update_project_visibility(self, project, visibility):
        """
        更新项目可视状态('public','private')
        :param project:
        :param visibility:
        :return:
        """
        params = {
            'project': project,
            'visibility': visibility
        }
        self.sonarqube._make_call('post', RULES_PROJECTS_UPDATE_VISIBILITY_ENDPOINT, **params)
