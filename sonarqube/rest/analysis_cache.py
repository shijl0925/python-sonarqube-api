#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.common import GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_ANALYSIS_CACHE,
)


class SonarQubeAnalysisCache(RestClient):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeAnalysisCache, self).__init__(**kwargs)

    @GET(API_ANALYSIS_CACHE)
    def get_analysis_cache(self, project, branch=None):
        """
        since 9.4
        Get the scanner's cached data for a branch. Requires scan permission on the project.
        Data is returned gzipped if the corresponding 'Accept-Encoding' header is set in the request.

        :param project: Project key
        :param branch: Branch key. If not provided, main branch will be used.
        :return:
        """