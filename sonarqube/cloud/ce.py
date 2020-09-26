#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.config import API_CE_ACTIVITY_ENDPOINT
from sonarqube.community.ce import SonarQubeCe
from sonarqube.utils.common import GET


class SonarCloudCe(SonarQubeCe):
    """
    SonarCloud ce Operations
    """

    @GET(API_CE_ACTIVITY_ENDPOINT)
    def search_tasks(
        self,
        component=None,
        maxExecutedAt=None,
        minSubmittedAt=None,
        onlyCurrents=None,
        ps=None,
        q=None,
        status=None,
        type=None,
    ):
        """
        Search for tasks.

        :param component: Key of the component (project) to filter on
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
