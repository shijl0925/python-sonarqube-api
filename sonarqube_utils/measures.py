#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeMeasure(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_measures_component(self, component, branch):
        """
        获取项目分析结果
        :param component:
        :param branch:
        :return:
        """
        params = {
            'additionalFields': 'metrics,periods',
            'metricKeys': 'code_smells,bugs,vulnerabilities,new_bugs,new_vulnerabilities,new_code_smells,comment_lines_density',
            'component': component,
            'branch': branch
        }
        resp = self.sonarqube._make_call('get', RULES_MEASURES_COMPONENT_ENDPOINT, **params)
        data = resp.json()
        return data

    def get_measures_history(self, component, branch, **kwargs):
        """
        Search measures history of a component
        :param component:
        :param branch:
        :return:
        """
        params = {
            'metrics': 'code_smells,bugs,vulnerabilities,new_bugs,new_vulnerabilities,new_code_smells',
            'component': component,
            'branch': branch
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_MEASURES_SEARCH_HISTORY_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for measure in response['measures']:
                yield measure

    def get_project_measures_component(self, project_key, branch, filter=None):
        """
        获取项目measures(可以过滤不需要的数据)
        :param project_key:
        :param branch:
        :param filter:
        :return:
        """
        if filter:
            if isinstance(filter, str):
                filter = filter.split(',')

        measures_component = self.get_measures_component(project_key, branch)['component']['measures']

        measures = {}
        for metric in measures_component:
            if metric['metric'] == 'code_smells' or metric['metric'] == 'bugs' or metric['metric'] == 'vulnerabilities' or metric['metric'] == 'comment_lines_density':
                measures[metric['metric']] = metric['value']

            if metric['metric'] == 'new_code_smells' or metric['metric'] == 'new_bugs' or metric['metric'] == 'new_vulnerabilities':
                measures[metric['metric']] = metric['periods'][0]['value']

        for item in list(measures.keys()):
            if filter and item in filter:
                del measures[item]

        return measures

