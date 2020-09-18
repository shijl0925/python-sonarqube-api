#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.ce import SonarQubeCe


class SonarCloudCe(SonarQubeCe):
    """
    SonarCloud ce Operations
    """
    OPTIONS_SEARCH = ['component', 'maxExecutedAt', 'minSubmittedAt',
                      'onlyCurrents', 'ps', 'q', 'status', 'type']

    def search_tasks(self, **kwargs):
        """
        Search for tasks. optional parameters:
          * component: Key of the component (project) to filter on
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
        :param kwargs:
        :return:
        """
        return super().search_tasks(**kwargs)
