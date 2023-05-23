#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USER_TOKENS_GENERATE_ENDPOINT,
    API_USER_TOKENS_REVOKE_ENDPOINT,
    API_USER_TOKENS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeUserTokens(RestClient):
    """
    SonarQube user tokens Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUserTokens, self).__init__(**kwargs)

    @POST(API_USER_TOKENS_GENERATE_ENDPOINT)
    def generate_user_token(self, name, login=None):
        """
        SINCE 5.3
        Generate a user access token.
        Please keep your tokens secret. They enable to authenticate and analyze projects.
        It requires administration permissions to specify a 'login' and generate a token for another user. Otherwise,
        a token is generated for the current user.

        :param name: Token name
        :param login: User login. If not set, the token is generated for the authenticated user.
        :return: request response
        """

    @POST(API_USER_TOKENS_REVOKE_ENDPOINT)
    def revoke_user_token(self, name, login=None):
        """
        SINCE 5.3
        Revoke a user access token.
        It requires administration permissions to specify a 'login' and revoke a token for another user.
        Otherwise, the token for the current user is revoked.

        :param name: Token name
        :param login: User login
        :return:
        """

    @GET(API_USER_TOKENS_SEARCH_ENDPOINT)
    def search_user_tokens(self, login=None):
        """
        SINCE 5.3
        List the access tokens of a user.
        The login must exist and active.
        Field 'lastConnectionDate' is only updated every hour, so it may not be accurate,
        for instance when a user is using a token many times in less than one hour.

        :param login: User login
        :return:
        """
