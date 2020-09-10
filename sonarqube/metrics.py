#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import (
    API_METRICS_SEARCH_ENDPOINT,
    API_METRICS_TYPES_ENDPOINT
)


class SonarQubeMetrics(RestClient):
    """
    SonarQube metrics Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMetrics, self).__init__(**kwargs)

    def search_metrics(self):
        """
        Search for metrics

        :return:
        """

        params = {}

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_METRICS_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for metric in response['metrics']:
                yield metric

    def get_metrics_types(self):
        """
        List all available metric types.

        :return:
        """
        resp = self.get(API_METRICS_TYPES_ENDPOINT)
        response = resp.json()
        return response['types']
