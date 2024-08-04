#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_rules(sonar_client):
    res = sonar_client.rules.search_rules(
        organization="shijl0925",
        languages="py"
    )

    assert "rules" in res
