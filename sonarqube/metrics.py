#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *


class SonarQubeMetrics(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_metrics(self):
        """
        Search for metrics
        :return:
        """

        params = {}

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', API_METRICS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for metric in response['metrics']:
                yield metric

    def get_metics_types(self):
        """
        List all available metric types.
        :return:
        """
        resp = self.sonarqube._make_call('get', API_METRICS_TYPES_ENDPOINT)
        response = resp.json()
        types = response['types']
        return types