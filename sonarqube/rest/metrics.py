#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_METRICS_SEARCH_ENDPOINT,
    API_METRICS_TYPES_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeMetrics(RestClient):
    """
    SonarQube metrics Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMetrics, self).__init__(**kwargs)

    @GET(API_METRICS_SEARCH_ENDPOINT)
    def search_metrics(self, p=None, ps=None):
        """
        SINCE 5.2
        Search for metrics

        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500

        :return:
        """

    @GET(API_METRICS_TYPES_ENDPOINT)
    def get_metrics_types(self):
        """
        SINCE 5.2
        List all available metric types.

        :return:
        """
