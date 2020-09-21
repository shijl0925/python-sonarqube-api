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
from sonarqube.utils.common import GET


class SonarQubeCe(RestClient):
    """
    SonarQube ce Operations
    """
    special_attributes_map = {'task_id': 'id', 'fields': 'additionalFields'}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeCe, self).__init__(**kwargs)

    @GET(API_CE_ACTIVITY_ENDPOINT)
    def search_tasks(self, componentId=None, maxExecutedAt=None, minSubmittedAt=None, onlyCurrents=None, ps=None,
                     q=None, status=None, type=None):
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
        :param status: Comma separated list of task statuses. Possible values are for:

          * SUCCESS
          * FAILED
          * CANCELED
          * PENDING
          * IN_PROGRESS

          default value is SUCCESS,FAILED,CANCELED
        :param type: Task type

        :return:
        """

    @GET(API_CE_ACTIVITY_STATUS_ENDPOINT)
    def get_ce_activity_related_metrics(self, component_id=None):
        """
        Returns CE activity related metrics.

        :param component_id: Id of the component (project) to filter on
        :return:
        """

    @GET(API_CE_COMPONENT_ENDPOINT)
    def get_component_queue_and_current_tasks(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project).

        :param component: Component key
        :return:
        """

    @GET(API_CE_TASK_ENDPOINT)
    def get_task(self, task_id, fields=None):
        """
        Give Compute Engine task details such as type, status, duration and associated component.

        :param task_id: Id of task
        :param fields: Comma-separated list of the optional fields to be returned in response.
          Possible values are for: stacktrace,scannerContext,warnings
        :return:
        """
