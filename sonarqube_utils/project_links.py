#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeProject_Links(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def create_project_links(self, project_key, link_name, link_url):
        """
        创建链接
        :param project_key:
        :param link_name:
        :param link_url:
        :return:
        """
        params = {
            'projectKey': project_key,
            'name': link_name,
            'url': link_url
        }
        self.sonarqube._make_call('post', RULES_PROJECT_LINKS_CREATE_ENDPOINT, **params)

    def delete_project_links(self, link_id):
        """
        删除链接
        :param link_id:
        :return:
        """
        params = {
            'id': link_id
        }
        self.sonarqube._make_call('post', RULES_PROJECT_LINKS_DELETE_ENDPOINT, **params)

    def search_project_links(self, project_key):
        """
        搜索链接
        :param project_key:
        :return:
        """
        params = {
            'projectKey': project_key
        }
        resp = self.sonarqube._make_call('get', RULES_PROJECT_LINKS_SEARCH_ENDPOINT, **params)
        data = resp.json()
        return data["links"]
