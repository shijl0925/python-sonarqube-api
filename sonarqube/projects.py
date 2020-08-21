#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECTS_BULK_DELETE_ENDPOINT,
    API_PROJECTS_SEARCH_ENDPOINT,
    API_PROJECTS_CREATE_ENDPOINT,
    API_PROJECTS_DELETE_ENDPOINT,
    API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT,
    API_PROJECTS_UPDATE_KEY_ENDPOINT
)


class SonarQubeProject:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.get_projects()

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
        result = self.get_projects()
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

    def get_projects(self, **kwargs):
        """
        Search for projects or views to administrate them.
        :param kwargs:
        analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        onProvisionedOnly: Filter the projects that are provisioned
        projects: Comma-separated list of project keys
        q: Limit search to:
          * component names that contain the supplied string
          * component keys that contain the supplied string
        qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified qualifiers.
          such as: TRK,VW,APP
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_PROJECTS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def create_project(self, project, name, visibility=None):
        """
        Create a project.
        :param project: Key of the project
        :param name: Name of the project. If name is longer than 500, it is abbreviated.
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          such as private or public.
        :return:
        """
        params = {
            'name': name,
            'project': project
        }
        if visibility:
            params['visibility'] = visibility

        self.sonarqube.make_call('post', API_PROJECTS_CREATE_ENDPOINT, **params)

    def get_project_id(self, project_key):
        """
        get project id
        :param project_key:
        :return:
        """
        components = self.sonarqube.components.get_project_component(project_key)
        return components['component']['id']

    def delete_project(self, project):
        """
        Delete a project.
        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }
        self.sonarqube.make_call('post', API_PROJECTS_DELETE_ENDPOINT, **params)

    def bulk_delete_projects(self, **kwargs):
        """
        Delete one or several projects.
        At least one parameter is required among analyzedBefore, projects, projectIds (deprecated since 6.4) and q
        :param kwargs:
        analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        onProvisionedOnly: Filter the projects that are provisioned
        projects: Comma-separated list of project keys
        q: Limit to:
          * component names that contain the supplied string
          * component keys that contain the supplied string
        qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified qualifiers
        :return:
        """
        self.sonarqube.make_call('post', API_PROJECTS_BULK_DELETE_ENDPOINT, **kwargs)

    def update_project_key(self, previous_project_key, new_project_key):
        """
        Update a project or module key and all its sub-components keys.
        :param previous_project_key: Project or module key
        :param new_project_key: New component key
        :return:
        """
        params = {
            'from': previous_project_key,
            'to': new_project_key
        }
        self.sonarqube.make_call('post', API_PROJECTS_UPDATE_KEY_ENDPOINT, **params)

    def update_project_visibility(self, project, visibility):
        """
        Updates visibility of a project.
        :param project: Project key
        :param visibility: New visibility
        :return:
        """
        params = {
            'project': project,
            'visibility': visibility
        }
        self.sonarqube.make_call('post', API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT, **params)
