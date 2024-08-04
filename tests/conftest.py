#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
import os
import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def sonar_client():
    from sonarqube import SonarCloudClient

    sonarcloud_url = "https://sonarcloud.io"
    token = os.getenv("SONARCLOUD_TOKEN")

    if not token:
        raise ValueError("SONARCLOUD_TOKEN not found in environment variables")

    client = SonarCloudClient(
        sonarcloud_url, token=token, verify=False
    )

    return client
