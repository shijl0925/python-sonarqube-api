#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeMeasure(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_measures_component(self, project_key, branch):
        """
        获取项目分析结果
        :param project_key:
        :param branch:
        :return:
        """
        params = {
            'additionalFields':'metrics,periods',
            'metricKeys':'code_smells,bugs,vulnerabilities,new_bugs,new_vulnerabilities,new_code_smells',
            'component':project_key,
            'branch':branch
        }
        resp = self.sonarqube._make_call('get', RULES_MEASURES_COMPONENT_ENDPOINT, **params)
        data = resp.json()
        measures = {}
        for metric in data['component']['measures']:
            if metric['metric'] == 'code_smells' or metric['metric'] == 'bugs' or metric['metric'] == 'vulnerabilities':
                measures[metric['metric']] = metric['value']

            if metric['metric'] == 'new_code_smells' or metric['metric'] == 'new_bugs' or metric['metric'] == 'new_vulnerabilities':
                measures[metric['metric']] = metric['periods'][0]['value']
        return measures

    def get_measures_history_page(self, project_key, branch, page):
        """
        Search measures history of a component by page.
        :param project_key:
        :param branch:
        :param page:
        :return:
        """
        params = {
            'metrics':'code_smells,bugs,vulnerabilities,new_bugs,new_vulnerabilities,new_code_smells',
            'component':project_key,
            'branch':branch,
            'p':page
        }
        resp = self.sonarqube._make_call('get', RULES_MEASURES_SEARCH_HISTORY_ENDPOINT, **params)
        data = resp.json()
        return data

    def get_measures_history(self, project_key, branch):
        """
        Search measures history of a component
        :return:
        """
        response = self.get_measures_history_page(project_key, branch, 1)
        measures_history = []

        total_nums = response['paging']['total']
        page_size = response['paging']['pageSize']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.get_measures_history_page(project_key, branch, i + 1)
            measures_history.extend(response['measures'])
        return measures_history

    def get_project_measures_component(self, project_key, branch):
        """
        获取项目measures(只包含bugs/vulnerabilities/code_smells)
        :param project_key:
        :param branch:
        :return:
        """
        measures_component = self.get_measures_component(project_key, branch)
        if 'new_bugs' in measures_component:
            del measures_component['new_bugs']
        if 'new_vulnerabilities' in measures_component:
            del measures_component['new_vulnerabilities']
        if 'new_code_smells' in measures_component:
            del measures_component['new_code_smells']
        return measures_component
