#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_projects(sonar_client):
    organization = "williamsedmond90"
    resp = sonar_client.projects.search_projects(organization=organization)

    projects = [item["key"] for item in resp.get("components", [])]

    assert len(projects) >= 0
