#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_tasks(sonar_client):
    component = "shijl0925_python-gerrit-api"
    tasks = sonar_client.ce.search_tasks(
        component=component, status="IN_PROGRESS,SUCCESS,FAILED,CANCELED", p=1, ps=10
    )

    assert len(tasks.get("tasks"))
