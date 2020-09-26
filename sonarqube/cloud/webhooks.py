#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.webservices import SonarQubeWebservices
from sonarqube.utils.config import (
    API_WEBHOOKS_CREATE_ENDPOINT,
    API_WEBHOOKS_LIST_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarCloudWebhooks(SonarQubeWebservices):
    """
    SonarCloud webhooks Operations
    """

    @POST(API_WEBHOOKS_CREATE_ENDPOINT)
    def create_webhook(self, name, url, organization, project=None, secret=None):
        """
        Create a Webhook.

        :param name: Name displayed in the administration console of webhooks
        :param url: Server endpoint that will receive the webhook payload, for example 'http://my_server/foo'. If HTTP
          Basic authentication is used, HTTPS is recommended to avoid man in the middle attacks.
          Example: 'https://myLogin:myPassword@my_server/foo'
        :param organization: organization key.
        :param project: The key of the project that will own the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return: request response
        """

    @GET(API_WEBHOOKS_LIST_ENDPOINT)
    def search_webhooks(self, organization, project=None):
        """
        Search for global webhooks or project webhooks. Webhooks are ordered by name.

        :param organization: organization key.
        :param project: Project key
        :return:
        """
