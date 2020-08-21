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

    def get_ce_activity(self, **kwargs):
        """
        Search for tasks.
        :param kwargs:
        componentId: Id of the component (project) to filter on
        status: Comma separated list of task statuses;SUCCESS,FAILED,CANCELED,PENDING,IN_PROGRESS
        type: Task type
        onlyCurrents: Filter on the last tasks (only the most recent finished task by project)
        maxExecutedAt: Maximum date of end of task processing (inclusive)
        minSubmittedAt: Minimum date of task submission (inclusive)
        ps: Page size. Must be greater than 0 and less or equal than 1000
        q: Limit search to:
           * component names that contain the supplied string
           * component keys that are exactly the same as the supplied string
           * task ids that are exactly the same as the supplied string
           Must not be set together with componentId
        :return:
        """
        resp = self.sonarqube.make_call('get', API_CE_ACTIVITY_ENDPOINT, **kwargs)
        data = resp.json()
        for task in data['tasks']:
            yield task

    def get_ce_activity_status(self, componentId):
        """
        Returns CE activity related metrics.
        :param componentId: Id of the component (project) to filter on
        :return:
        """
        params = {'componentId': componentId}
        resp = self.sonarqube.make_call('get', API_CE_ACTIVITY_STATUS_ENDPOINT, **params)
        return resp.json()

    def get_ce_component(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project).
        :param component:
        :return:
        """
        params = {'component': component}
        resp = self.sonarqube.make_call('get', API_CE_COMPONENT_ENDPOINT, **params)
        return resp.json()

    def get_ce_task(self, task_id, additionalFields=None):
        """
        Give Compute Engine task details such as type, status, duration and associated component.
        :param task_id: Id of task
        :param additionalFields: Comma-separated list of the optional fields to be returned in response.
        such as: stacktrace,scannerContext,warning
        :return:
        """
        params = {'id': task_id}
        if additionalFields:
            params['additionalFields'] = additionalFields
        resp = self.sonarqube.make_call('get', API_CE_TASK_ENDPOINT, **params)
        return resp.json()
