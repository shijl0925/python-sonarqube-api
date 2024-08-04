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

def test_create_project(sonar_client):
    organization = "williamsedmond90"
    name = "sonar-java"
    project_key = f"{organization}_sonar_java"
    visibility = "public"
    mainBranch = "master"

    resp = sonar_client.projects.search_projects(projects=project_key, organization=organization)
    components = resp.get("components", [])
    if components:
        return

    sonar_client.projects.create_project(
        project=project_key,
        name=name,
        organization=organization,
        visibility=visibility,
        mainBranch=mainBranch
    )
