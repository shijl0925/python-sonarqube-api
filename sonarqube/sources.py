#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import (
    API_SOURCES_SCM_ENDPOINT,
    API_SOURCES_SHOW_ENDPOINT,
    API_SOURCES_RAW_ENDPOINT
)


class SonarQubeSources(RestClient):
    """
    SonarQube sources Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeSources, self).__init__(**kwargs)

    def get_source_file_scm(self, file_key, from_line=1, to_line=None, commits_by_line='false'):
        """
        Get SCM information of source files. Require See Source Code permission on file's project.
        Each element of the result array is composed of:
          * Line number
          * Author of the commit
          * Datetime of the commit (before 5.2 it was only the Date)
          * Revision of the commit (added in 5.2)

        :param file_key: File key
        :param from_line: First line to return. Starts at 1
        :param to_line: Last line to return (inclusive)
        :param commits_by_line: Group lines by SCM commit if value is false, else display commits for each line,even if
          two consecutive lines relate to the same commit. Possible values are for: true, false, yes, no. default value
          is false.
        :return:
        """
        params = {
            'key': file_key,
            'from': from_line,
            'commits_by_line': commits_by_line
        }

        if to_line:
            params.update({"to": to_line})

        resp = self.get(API_SOURCES_SCM_ENDPOINT, params=params)
        response = resp.json()
        return response['scm']

    def get_source_code(self, file_key, from_line=1, to_line=None):
        """
        Get source code. Requires See Source Code permission on file's project.

        :param file_key: File key
        :param from_line: First line to return. Starts at 1
        :param to_line: Last line to return (inclusive)
        :return:
        """
        params = {
            'key': file_key,
            'from': from_line
        }

        if to_line:
            params.update({"to": to_line})

        resp = self.get(API_SOURCES_SHOW_ENDPOINT, params=params)
        response = resp.json()
        return response['sources']

    def get_sources_raw(self, file_key):
        """
        Get source code as raw text. Require 'See Source Code' permission on file.

        :param file_key: File key
        :return:
        """
        params = {
            'key': file_key
        }

        resp = self.get(API_SOURCES_RAW_ENDPOINT, params=params)
        return resp.text
