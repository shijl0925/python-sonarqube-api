# -*- coding:utf-8 -*-
from .config import *


class SonarQubePdfReport(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_pdf_report(self, component):
        """
        PDFReport file get
        :param component:
        :return:
        """
        params = {
            'componentKey': component
        }
        resp = self.sonarqube._make_call('get', RULES_PDFREPORT_GET_ENDPOINT, **params)
        return resp.content
