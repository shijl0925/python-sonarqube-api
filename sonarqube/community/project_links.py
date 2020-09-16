#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_LINKS_CREATE_ENDPOINT,
    API_PROJECT_LINKS_DELETE_ENDPOINT,
    API_PROJECT_LINKS_SEARCH_ENDPOINT
)


class SonarQubeProjectLinks(RestClient):
    """
    SonarQube project links Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectLinks, self).__init__(**kwargs)

    def create_project_link(self, project_key, name, url):
        """
        Create a new project link.

        :param project_key: Project key
        :param name: Link name
        :param url: Link url
        :return: request response
        """
        params = {
            'projectKey': project_key,
            'name': name,
            'url': url
        }

        return self.post(API_PROJECT_LINKS_CREATE_ENDPOINT, params=params)

    def delete_project_link(self, link_id):
        """
        Delete existing project link.

        :param link_id: Link id
        :return:
        """
        params = {
            'id': link_id
        }

        self.post(API_PROJECT_LINKS_DELETE_ENDPOINT, params=params)

    def search_project_links(self, project_key):
        """
        List links of a project.

        :param project_key: Project Key
        :return:
        """
        params = {
            'projectKey': project_key
        }

        resp = self.get(API_PROJECT_LINKS_SEARCH_ENDPOINT, params=params)
        response = resp.json()
        return response["links"]
