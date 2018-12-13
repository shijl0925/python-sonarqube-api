#-*- coding:utf-8 -*-
from .config import *

class SonarQubeQualityGates(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_qualitygates_project_status(self, project_key):
        """
        获取项目质量阈状态，返回 'ok','WARN','ERROR'
        :param project_key:
        :return:
        """
        params = {
            'projectKey': project_key
        }
        resp = self.sonarqube._make_call('get', RULES_QUALITYGATES_PROJECT_STATUS_ENDPOINT, **params)
        data = resp.json()
        return data['projectStatus']['status']