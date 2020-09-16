#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_CE_ACTIVITY_ENDPOINT,
    API_CE_ACTIVITY_STATUS_ENDPOINT,
    API_CE_COMPONENT_ENDPOINT,
    API_CE_TASK_ENDPOINT
)


class SonarQubeCe(RestClient):
    """
    SonarQube ce Operations
    """
    OPTIONS_SEARCH = ['componentId', 'maxExecutedAt', 'minSubmittedAt',
                      'onlyCurrents', 'ps', 'q', 'status', 'type']

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeCe, self).__init__(**kwargs)

    def search_tasks(self, **kwargs):
        """
        Search for tasks. optional parameters:
          * componentId: Id of the component (project) to filter on
          * maxExecutedAt: Maximum date of end of task processing (inclusive)
          * minSubmittedAt: Minimum date of task submission (inclusive)
          * onlyCurrents: Filter on the last tasks (only the most recent finished task by project).
            default value is false.
          * ps: Page size. Must be greater than 0 and less or equal than 1000
          * q: Limit search to:

            * component names that contain the supplied string
            * component keys that are exactly the same as the supplied string
            * task ids that are exactly the same as the supplied string

            Must not be set together with componentId
          * status: Comma separated list of task statuses. Possible values are for:

            * SUCCESS
            * FAILED
            * CANCELED
            * PENDING
            * IN_PROGRESS

            default value is SUCCESS,FAILED,CANCELED
          * type: Task type
        :return:
        """
        params = {}
        if kwargs:
            self.api.copy_dict(params, kwargs, self.OPTIONS_SEARCH)

        resp = self.get(API_CE_ACTIVITY_ENDPOINT, params=params)
        response = resp.json()
        return response['tasks']

    def get_ce_activity_related_metrics(self, component_id=None):
        """
        Returns CE activity related metrics.

        :param component_id: Id of the component (project) to filter on
        :return:
        """
        params = {}
        if component_id:
            params.update({'componentId': component_id})

        resp = self.get(API_CE_ACTIVITY_STATUS_ENDPOINT, params=params)
        return resp.json()

    def get_component_queue_and_current_tasks(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project).

        :param component: Component key
        :return:
        """
        params = {'component': component}

        resp = self.get(API_CE_COMPONENT_ENDPOINT, params=params)
        return resp.json()

    def get_task(self, task_id, fields=None):
        """
        Give Compute Engine task details such as type, status, duration and associated component.

        :param task_id: Id of task
        :param fields: Comma-separated list of the optional fields to be returned in response.
          Possible values are for: stacktrace,scannerContext,warnings
        :return:
        """
        params = {'id': task_id}
        if fields:
            params.update({'additionalFields': fields})

        resp = self.get(API_CE_TASK_ENDPOINT, params=params)
        return resp.json()
