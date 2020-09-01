#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Generate a user access token.
    user_token = sonar.user_tokens.generate_user_token("Project scan on Travis")

    # Revoke a user access token.
    sonar.user_tokens.revoke_user_token("Project scan on Travis")

    # List the access tokens of a user.
    user_tokens = sonar.user_tokens.search_user_tokens(user_login="kevin")
