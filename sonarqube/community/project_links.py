#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_LINKS_CREATE_ENDPOINT,
    API_PROJECT_LINKS_DELETE_ENDPOINT,
    API_PROJECT_LINKS_SEARCH_ENDPOINT
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectLinks(RestClient):
    """
    SonarQube project links Operations
    """
    special_attributes_map = {
        'project_key': 'projectKey',
        'link_id': 'id'
    }

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectLinks, self).__init__(**kwargs)

    @POST(API_PROJECT_LINKS_CREATE_ENDPOINT)
    def create_project_link(self, project_key, name, url):
        """
        Create a new project link.

        :param project_key: Project key
        :param name: Link name
        :param url: Link url
        :return: request response
        """

    @POST(API_PROJECT_LINKS_DELETE_ENDPOINT)
    def delete_project_link(self, link_id):
        """
        Delete existing project link.

        :param link_id: Link id
        :return:
        """

    @GET(API_PROJECT_LINKS_SEARCH_ENDPOINT)
    def search_project_links(self, project_key):
        """
        List links of a project.

        :param project_key: Project Key
        :return:
        """
