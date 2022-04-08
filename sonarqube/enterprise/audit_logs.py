#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_AUDIT_LOGS_DOWNLOAD_ENDPOINT
from sonarqube.utils.common import GET


class SonarQubeAuditLogs(RestClient):
    """
    SonarQube audit logs Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeAuditLogs, self).__init__(**kwargs)

    @GET(API_AUDIT_LOGS_DOWNLOAD_ENDPOINT)
    def download_audit_logs(self, from_date, to_date):
        """
        since 9.1
        Returns security related audits of this SonarQube instance.

        :param from_date: Date in ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hh:mm)
          from which the logs will be returned. Inclusive.
        :param to_date: Date in ISO 8601 datetime format (YYYY-MM-DDThh:mm:ss±hh:mm)
          until which the logs will be returned. Inclusive.
        :return:
        """
