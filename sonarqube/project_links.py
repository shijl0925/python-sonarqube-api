#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sonarqube.config import (
    API_PROJECT_LINKS_CREATE_ENDPOINT,
    API_PROJECT_LINKS_DELETE_ENDPOINT,
    API_PROJECT_LINKS_SEARCH_ENDPOINT
)


class SonarQubeProjectLinks:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def create_project_links(self, projectKey, name, url):
        """
        Create a new project link.
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
        self.sonarqube.make_call('post', API_PROJECT_LINKS_CREATE_ENDPOINT, **params)

    def delete_project_links(self, link_id):
        """
        Delete existing project link.
        :param link_id:
        :return:
        """
        params = {
            'id': link_id
        }
        self.sonarqube.make_call('post', API_PROJECT_LINKS_DELETE_ENDPOINT, **params)

    def search_project_links(self, projectKey):
        """
        List links of a project.
        :param projectKey:
        :return:
        """
        params = {
            'projectKey': projectKey
        }
        resp = self.sonarqube.make_call('get', API_PROJECT_LINKS_SEARCH_ENDPOINT, **params)
        data = resp.json()
        return data["links"]
