#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_METRICS_SEARCH_ENDPOINT,
    API_METRICS_TYPES_ENDPOINT,
)
from sonarqube.utils.common import GET, PAGES_GET


class SonarQubeMetrics(RestClient):
    """
    SonarQube metrics Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMetrics, self).__init__(**kwargs)

    @PAGES_GET(API_METRICS_SEARCH_ENDPOINT, item="metrics")
    def search_metrics(self):
        """
        SINCE 5.2
        Search for metrics

        :return:
        """

    @GET(API_METRICS_TYPES_ENDPOINT)
    def get_metrics_types(self):
        """
        SINCE 5.2
        List all available metric types.

        :return:
        """
