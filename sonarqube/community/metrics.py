#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_METRICS_SEARCH_ENDPOINT,
    API_METRICS_TYPES_ENDPOINT
)
from sonarqube.utils.common import GET, PAGE_GET


class SonarQubeMetrics(RestClient):
    """
    SonarQube metrics Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMetrics, self).__init__(**kwargs)

    @PAGE_GET(API_METRICS_SEARCH_ENDPOINT, item='metrics')
    def search_metrics(self):
        """
        Search for metrics

        :return:
        """

    @GET(API_METRICS_TYPES_ENDPOINT)
    def get_metrics_types(self):
        """
        List all available metric types.

        :return:
        """
