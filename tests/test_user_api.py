#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import logging

logger = logging.getLogger(__name__)


def test_search_users(sonar_client):
    res = sonar_client.users.search_users()
    assert "users" in res
