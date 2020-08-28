#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_USER_TOKENS_GENERATE_ENDPOINT,
    API_USER_TOKENS_REVOKE_ENDPOINT,
    API_USER_TOKENS_SEARCH_ENDPOINT
)


class SonarQubeUsertokens:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def generate_user_token(self, token_name, user_login=None):
        """
        Generate a user access token.
        Please keep your tokens secret. They enable to authenticate and analyze projects.
        It requires administration permissions to specify a 'login' and generate a token for another user. Otherwise,
        a token is generated for the current user.

        :param token_name: Token name
        :param user_login: User login. If not set, the token is generated for the authenticated user.
        :return:
        """
        params = {
            'name': token_name,
        }

        if user_login:
            params.update({'login': user_login})

        resp = self.sonarqube.make_call('post', API_USER_TOKENS_GENERATE_ENDPOINT, **params)
        return resp.json()

    def revoke_user_token(self, token_name, user_login=None):
        """
        Revoke a user access token.
        It requires administration permissions to specify a 'login' and revoke a token for another user.
        Otherwise, the token for the current user is revoked.

        :param token_name:
        :param user_login:
        :return:
        """
        params = {
            'name': token_name,
        }

        if user_login:
            params.update({'login': user_login})

        self.sonarqube.make_call('post', API_USER_TOKENS_REVOKE_ENDPOINT, **params)

    def search_user_tokens(self, user_login=None):
        """
        List the access tokens of a user.
        The login must exist and active.
        Field 'lastConnectionDate' is only updated every hour, so it may not be accurate,
        for instance when a user is using a token many times in less than one hour.

        :param user_login:
        :return:
        """
        params = {}

        if user_login:
            params.update({'login': user_login})

        resp = self.sonarqube.make_call('get', API_USER_TOKENS_SEARCH_ENDPOINT, **params)
        response = resp.json()
        return response['userTokens']
