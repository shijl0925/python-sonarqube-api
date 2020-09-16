#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_DUPLICATIONS_SHOW_ENDPOINT


class SonarQubeDuplications(RestClient):
    """
    SonarQube duplications Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeDuplications, self).__init__(**kwargs)

    def get_duplications(self, key, branch=None, pull_request_id=None):
        """
        Get duplications. Require Browse permission on file's project

        :param key: File key
        :param branch: Branch key
        :param pull_request_id: Pull request id
        :return:
        """
        params = {'key': key}

        if branch:
            params.update({'branch': branch})

        if pull_request_id:
            params.update({'pullRequest': pull_request_id})

        resp = self.get(API_DUPLICATIONS_SHOW_ENDPOINT, params=params)
        return resp.json()
