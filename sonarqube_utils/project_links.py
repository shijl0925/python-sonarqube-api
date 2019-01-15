#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeProject_Links(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def create_project_links(self, projectKey, name, url):
        """
        创建链接
        :param projectKey:
        :param name:
        :param url:
        :return:
        """
        params = {
            'projectKey': projectKey,
            'name': name,
            'url': url
        }
        self.sonarqube._make_call('post', RULES_PROJECT_LINKS_CREATE_ENDPOINT, **params)

    def delete_project_links(self, id):
        """
        删除链接
        :param id:
        :return:
        """
        params = {
            'id': id
        }
        self.sonarqube._make_call('post', RULES_PROJECT_LINKS_DELETE_ENDPOINT, **params)

    def search_project_links(self, projectKey):
        """
        搜索链接
        :param projectKey:
        :return:
        """
        params = {
            'projectKey': projectKey
        }
        resp = self.sonarqube._make_call('get', RULES_PROJECT_LINKS_SEARCH_ENDPOINT, **params)
        data = resp.json()
        return data["links"]
