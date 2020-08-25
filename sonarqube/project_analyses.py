#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECT_ANALYSES_CREATE_EVENT_ENDPOINT,
    API_PROJECT_ANALYSES_DELETE_ENDPOINT,
    API_PROJECT_ANALYSES_DELETE_EVENT_ENDPOINT,
    API_PROJECT_ANALYSES_SEARCH_ENDPOINT,
    API_PROJECT_ANALYSES_SET_BASELINE_ENDPOINT,
    API_PROJECT_ANALYSES_UNSET_BASELINE_ENDPOINT,
    API_PROJECT_ANALYSES_UPDATE_EVENT_ENDPOINT
)


class SonarQubeProjectAnalyses:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def create_project_analysis_event(self, analysis, name, category="OTHER"):
        """
        Create a project analysis event.Only event of category 'VERSION' and 'OTHER' can be created.
        :param analysis: Analysis key
        :param name: Name
        :param category: Category. such as:
          * VERSION
          * OTHER
          default value is OTHER.
        :return:
        """
        params = {
            'analysis': analysis,
            'name': name,
            'category': category
        }

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_CREATE_EVENT_ENDPOINT, **params)

    def delete_project_analysis(self, analysis):
        """
        Delete a project analysis.
        :param analysis: Analysis key
        :return:
        """
        params = {
            'analysis': analysis
        }

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_DELETE_ENDPOINT, **params)

    def delete_project_analysis_event(self, event):
        """
        Delete a project analysis event.Only event of category 'VERSION' and 'OTHER' can be deleted.
        :param event: Event key
        :return:
        """
        params = {
            'event': event
        }

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_DELETE_EVENT_ENDPOINT, **params)

    def search_project_analyses_and_events(self, project, branch=None, category=None, from_date=None, to_date=None):
        """
        Search a project analyses and attached events.
        :param project: Project key
        :param branch: Branch key
        :param category: Event category. Filter analyses that have at least one event of the category specified.
          such as:
          * VERSION
          * OTHER
          * QUALITY_PROFILE
          * QUALITY_GATE
          * DEFINITION_CHANGE
        :param from_date: Filter analyses created after the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :param to_date: Filter analyses created before the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :return:
        """
        params = {
            'project': project,
        }

        if branch:
            params.update({'branch': branch})

        if category:
            params.update({'category': category})

        if from_date:
            params.update({'from': from_date})

        if to_date:
            params.update({'to': to_date})

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_PROJECT_ANALYSES_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for analysis in response['analyses']:
                yield analysis

    def set_analysis_as_baseline_on_project(self, project, analysis, branch=None):
        """
        Set an analysis as the baseline of the New Code Period on a project or a long-lived branch.
        This manually set baseline overrides the `sonar.leak.period` setting.
        :param project: Project key
        :param analysis: Analysis key
        :param branch: Branch key
        :return:
        """
        params = {
            'analysis': analysis,
            'project': project,
        }
        if branch:
            params.update({'branch': branch})

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_SET_BASELINE_ENDPOINT, **params)

    def unset_baseline_on_project(self, project, branch=None):
        """
        Unset any manually-set New Code Period baseline on a project or a long-lived branch.
        Unsetting a manual baseline restores the use of the `sonar.leak.period` setting.
        :param project: Project key
        :param branch: Branch key
        :return:
        """
        params = {
            'project': project,
        }
        if branch:
            params.update({'branch': branch})

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_UNSET_BASELINE_ENDPOINT, **params)

    def update_project_analysis_event(self, event, name):
        """
        Update a project analysis event.
        Only events of category 'VERSION' and 'OTHER' can be updated.
        :param event: Event key
        :param name: New name
        :return:
        """
        params = {
            'event': event,
            'name': name,
        }

        self.sonarqube.make_call('post', API_PROJECT_ANALYSES_UPDATE_EVENT_ENDPOINT, **params)
