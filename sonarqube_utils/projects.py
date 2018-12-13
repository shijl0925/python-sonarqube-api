#!/usr/bin/env python
#-*- coding:utf-8 -*-
from .config import *

class SonarQubeProject(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_projects_info_page(self, page):
        """
        按页获取项目信息
        :param page:
        :return:
        """
        params = {
            'p':page
        }
        resp = self.sonarqube._make_call('get', RULES_PROJECTS_SEARCH_ENDPOINT, **params)
        response = resp.json()
        return response

    def get_projects_info(self):
        """
        获取所有项目信息
        :return:
        """
        response = self.get_projects_info_page(1)
        components = []

        total_nums = response['paging']['total']
        page_size = response['paging']['pageSize']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.get_projects_info_page(i + 1)
            components.extend(response['components'])

        projects_info = {}
        for item in components:
            projects_info[item['key']] = item
        return projects_info

    def project_exist(self, project_key):
        """
        判断项目是否存在
        :param project_key:
        :return:
        """
        project_keys = self.get_projects_info().keys()
        if project_key in project_keys:
            return True
        else:
            return False

    def create_project(self, key, name, branch = None):
        """
        创建项目
        :param key:
        :param name:
        :param branch:
        :return:
        """
        params = {
            'name': name,
            'project': key
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
        project_id = self.get_projects_info()[project_key]['id']
        return project_id

    def delete_project(self, project_key):
        """
        删除项目
        :param project_key:
        :return:
        """
        params = {
            'project': project_key
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

    def update_project_visibility(self, project_key, visibility):
        """
        更新项目可视状态('public','private')
        :param project_key:
        :param visibility:
        :return:
        """
        params = {
            'project': project_key,
            'visibility': visibility
        }
        self.sonarqube._make_call('post', RULES_PROJECTS_UPDATE_VISIBILITY_ENDPOINT, **params)
