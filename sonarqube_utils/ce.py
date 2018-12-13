#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeCe(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_activity_status(self,project_key,status):
        """
        获取项目指定状态的tasks
        :param project_key:
        :param status:
        :return:
        """
        params = {
            'status':status,
            'project':project_key
        }
        resp = self.sonarqube._make_call('get',RULES_CE_ACTIVITY_ENDPOINT,**params)

        data = resp.json()
        return data['tasks']