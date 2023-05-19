#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.project_dump import SonarQubeProjectDump
from sonarqube.utils.config import (
    API_PROJECT_DUMP_IMPORT_ENDPOINT,
)
from sonarqube.utils.common import POST


class SonarEnterpriseProjectDump(SonarQubeProjectDump):
    """
    SonarQube Project export/import Operations
    """

    @POST(API_PROJECT_DUMP_IMPORT_ENDPOINT)
    def import_project_dump(self, key):
        """
        SINCE 1.0
        Triggers the import of a project dump.

        :param key:
        :return:
        """
