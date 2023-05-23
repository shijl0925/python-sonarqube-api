#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_SOURCES_SCM_ENDPOINT,
    API_SOURCES_SHOW_ENDPOINT,
    API_SOURCES_RAW_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeSources(RestClient):
    """
    SonarQube sources Operations
    """

    special_attributes_map = {"from_line": "from", "to_line": "to"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeSources, self).__init__(**kwargs)

    @GET(API_SOURCES_SCM_ENDPOINT)
    def get_source_file_scm(
        self, key, from_line=1, to_line=None, commits_by_line="false"
    ):
        """
        SINCE 4.4
        Get SCM information of source files. Require See Source Code permission on file's project.
        Each element of the result array is composed of:
          * Line number
          * Author of the commit
          * Datetime of the commit (before 5.2 it was only the Date)
          * Revision of the commit (added in 5.2)

        :param key: File key
        :param from_line: First line to return. Starts at 1
        :param to_line: Last line to return (inclusive)
        :param commits_by_line: Group lines by SCM commit if value is false, else display commits for each line,even if
          two consecutive lines relate to the same commit. Possible values are for: true, false, yes, no. default value
          is false.
        :return:
        """

    @GET(API_SOURCES_SHOW_ENDPOINT)
    def get_source_code(self, key, from_line=1, to_line=None):
        """
        SINCE 4.4
        Get source code. Requires See Source Code permission on file's project.

        :param key: File key
        :param from_line: First line to return. Starts at 1
        :param to_line: Last line to return (inclusive)
        :return:
        """

    @GET(API_SOURCES_RAW_ENDPOINT)
    def get_sources_raw(self, key, branch=None, pullRequest=None):
        """
        SINCE 5.0
        Get source code as raw text. Require 'See Source Code' permission on file.

        :param key: File key
        :param branch: Branch key
        :param pullRequest: Pull request id
        :return:
        """
