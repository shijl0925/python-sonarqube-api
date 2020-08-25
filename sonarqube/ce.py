#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_CE_ACTIVITY_ENDPOINT,
    API_CE_ACTIVITY_STATUS_ENDPOINT,
    API_CE_COMPONENT_ENDPOINT,
    API_CE_TASK_ENDPOINT
)


class SonarQubeCe:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def search_tasks(self, componentId=None, maxExecutedAt=None, minSubmittedAt=None, onlyCurrents="false",
                     ps=None, q=None, status="SUCCESS,FAILED,CANCELED", task_type=None):
        """
        Search for tasks.
        :param componentId: Id of the component (project) to filter on
        :param maxExecutedAt: Maximum date of end of task processing (inclusive)
        :param minSubmittedAt: Minimum date of task submission (inclusive)
        :param onlyCurrents: Filter on the last tasks (only the most recent finished task by project).
          default value is false.
        :param ps: Page size. Must be greater than 0 and less or equal than 1000
        :param q: Limit search to:
          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
          * task ids that are exactly the same as the supplied string
           Must not be set together with componentId
        :param status: Comma separated list of task statuses. such as:
          * SUCCESS
          * FAILED
          * CANCELED
          * PENDING
          * IN_PROGRESS
          default value is SUCCESS,FAILED,CANCELED
        :param task_type: Task type
        :return:
        """
        params = {
            'onlyCurrents': onlyCurrents,
            'statue': status.upper()
        }

        if componentId:
            params.update({'componentId': componentId})

        if maxExecutedAt:
            params.update({'maxExecutedAt': maxExecutedAt})

        if minSubmittedAt:
            params.update({'minSubmittedAt': minSubmittedAt})

        if ps:
            params.update({'ps': ps})

        if q:
            params.update({'q': q})

        if task_type:
            params.update({'type': task_type})

        resp = self.sonarqube.make_call('get', API_CE_ACTIVITY_ENDPOINT, **params)
        data = resp.json()
        for task in data['tasks']:
            yield task

    def get_ce_activity_related_metrics(self, componentId=None):
        """
        Returns CE activity related metrics.
        :param componentId: Id of the component (project) to filter on
        :return:
        """
        params = {}
        if componentId:
            params.update({'componentId': componentId})

        resp = self.sonarqube.make_call('get', API_CE_ACTIVITY_STATUS_ENDPOINT, **params)
        return resp.json()

    def get_component_queue_and_current_tasks(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project).
        :param component: Component key
        :return:
        """
        params = {'component': component}
        resp = self.sonarqube.make_call('get', API_CE_COMPONENT_ENDPOINT, **params)
        return resp.json()

    def get_task(self, task_id, additionalFields=None):
        """
        Give Compute Engine task details such as type, status, duration and associated component.
        :param task_id: Id of task
        :param additionalFields: Comma-separated list of the optional fields to be returned in response.
        such as: stacktrace,scannerContext,warning
        :return:
        """
        params = {'id': task_id}
        if additionalFields:
            params.update({'additionalFields': additionalFields})

        resp = self.sonarqube.make_call('get', API_CE_TASK_ENDPOINT, **params)
        return resp.json()
