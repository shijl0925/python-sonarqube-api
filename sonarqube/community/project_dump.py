#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_DUMP_EXPORT_ENDPOINT,
    API_PROJECT_DUMP_IMPORT_ENDPOINT,
)
from sonarqube.utils.common import POST


class SonarQubeProjectdump(RestClient):
    """
    SonarQube Project export/import Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectdump, self).__init__(**kwargs)

    @POST(API_PROJECT_DUMP_EXPORT_ENDPOINT)
    def export_project_dump(self, key):
        """
        SINCE 1.0
        Triggers project dump so that the project can be copied to another SonarQube server (see api/project_dump/import).

        :param key:
        :return:
        """

    @POST(API_PROJECT_DUMP_IMPORT_ENDPOINT)
    def import_project_dump(self, key):
        """
        SINCE 1.0
        Triggers the import of a project dump.

        :param key:
        :return:
        """