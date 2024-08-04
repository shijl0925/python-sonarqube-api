#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_project_tags(sonar_client):
    res = sonar_client.project_tags.search_project_tags()

    assert "tags" in res
