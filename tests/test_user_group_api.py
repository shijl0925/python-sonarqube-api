#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_user_groups(sonar_client):
    res = sonar_client.user_groups.search_user_groups(
        organization="shijl0925",
    )

    assert "groups" in res