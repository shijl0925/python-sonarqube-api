#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_WEBHOOKS_CREATE_ENDPOINT,
    API_WEBHOOKS_DELETE_ENDPOINT,
    API_WEBHOOKS_DELIVERIES_ENDPOINT,
    API_WEBHOOKS_DELIVERY_ENDPOINT,
    API_WEBHOOKS_LIST_ENDPOINT,
    API_WEBHOOKS_UPDATE_ENDPOINT
)
from sonarqube.utils.common import GET, POST, PAGE_GET


class SonarQubeWebhooks(RestClient):
    """
    SonarQube webhooks Operations
    """
    special_attributes_map = {
        'webhook_key': 'webhook',
        'delivery_id': 'deliveryId',
        'component_key': 'componentKey',
        'task_id': 'ceTaskId'
    }

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeWebhooks, self).__init__(**kwargs)

    @POST(API_WEBHOOKS_CREATE_ENDPOINT)
    def create_webhook(self, name, url, project=None, secret=None):
        """
        Create a Webhook.

        :param name: Name displayed in the administration console of webhooks
        :param url: Server endpoint that will receive the webhook payload, for example 'http://my_server/foo'. If HTTP
          Basic authentication is used, HTTPS is recommended to avoid man in the middle attacks.
          Example: 'https://myLogin:myPassword@my_server/foo'
        :param project: The key of the project that will own the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return: request response
        """

    @POST(API_WEBHOOKS_DELETE_ENDPOINT)
    def delete_webhook(self, webhook_key):
        """
        Delete a Webhook.

        :param webhook_key: The key of the webhook to be deleted, auto-generated value can be obtained through
          api/webhooks/create or api/webhooks/list
        :return:
        """

    @PAGE_GET(API_WEBHOOKS_DELIVERIES_ENDPOINT, item='deliveries')
    def get_webhook_deliveries(self, webhook_key=None, component_key=None, task_id=None):
        """
        Get the recent deliveries for a specified project or Compute Engine task.

        :param webhook_key: Key of the webhook that triggered those deliveries
        :param component_key: Key of the project
        :param task_id: Id of the Compute Engine task
        :return:
        """

    @GET(API_WEBHOOKS_DELIVERY_ENDPOINT)
    def get_webhook_delivery(self, delivery_id):
        """
        Get a webhook delivery by its id.

        :param delivery_id: Id of delivery
        :return:
        """

    @GET(API_WEBHOOKS_LIST_ENDPOINT)
    def search_webhooks(self, project=None):
        """
        Search for global webhooks or project webhooks. Webhooks are ordered by name.

        :param project: Project key
        :return:
        """

    @POST(API_WEBHOOKS_UPDATE_ENDPOINT)
    def update_webhook(self, webhook_key, name, url, secret=None):
        """
        Update a Webhook.

        :param webhook_key: The key of the webhook to be updated
        :param name: new name of the webhook
        :param url: new url to be called by the webhook
        :param secret: If provided, secret will be used as the key to generate the HMAC hex (lowercase) digest value
          in the 'X-Sonar-Webhook-HMAC-SHA256' header
        :return:
        """
