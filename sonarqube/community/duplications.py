#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_DUPLICATIONS_SHOW_ENDPOINT
from sonarqube.utils.common import GET


class SonarQubeDuplications(RestClient):
    """
    SonarQube duplications Operations
    """
    special_attributes_map = {'pull_request_id': 'pullRequest'}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeDuplications, self).__init__(**kwargs)

    @GET(API_DUPLICATIONS_SHOW_ENDPOINT)
    def get_duplications(self, key, branch=None, pull_request_id=None):
        """
        Get duplications. Require Browse permission on file's project

        :param key: File key
        :param branch: Branch key
        :param pull_request_id: Pull request id
        :return:
        """
