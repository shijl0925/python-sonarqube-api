#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_issues(sonar_client):
    organization = "microsoft"
    res = sonar_client.issues.search_issues(
        organization=organization, componentKeys="microsoft_vscode-python", p=1, ps=10, pp=2
    )

    assert len(res.get("issues"))
