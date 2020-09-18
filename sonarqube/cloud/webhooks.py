#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.webservices import SonarQubeWebservices
from sonarqube.utils.config import (
    API_WEBHOOKS_CREATE_ENDPOINT,
    API_WEBHOOKS_LIST_ENDPOINT
)


class SonarCloudWebhooks(SonarQubeWebservices):
    """
    SonarCloud webhooks Operations
    """
    def create_webhook(self, name, organization, project=None, secret=None, url=None):
        """
        Create a Webhook.

        :param name: Name displayed in the administration console of webhooks
        :param organization: organization key.
        :param project: The key of the project that will own the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :param url: Server endpoint that will receive the webhook payload, for example 'http://my_server/foo'. If HTTP
          Basic authentication is used, HTTPS is recommended to avoid man in the middle attacks.
          Example: 'https://myLogin:myPassword@my_server/foo'
        :return: request response
        """
        params = {
            'name': name,
            'organization': organization
        }

        if project:
            params.update({'project': project})

        if secret:
            params.update({'secret': secret})

        if url:
            params.update({'url': url})

        return self.post(API_WEBHOOKS_CREATE_ENDPOINT, params=params)

    def search_webhooks(self, organization, project=None):
        """
        Search for global webhooks or project webhooks. Webhooks are ordered by name.

        :param organization: organization key.
        :param project: Project key
        :return:
        """
        params = {'organization': organization}
        if project:
            params.update({'project': project})

        resp = self.get(API_WEBHOOKS_LIST_ENDPOINT, params=params)
        response = resp.json()
        return response['webhooks']
