#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Create a Webhook.
    sonar.webhooks.create_webhook(name="My Webhook", url="https://www.my-webhook-listener.com/sonar")
    # or
    sonar.webhooks.create_webhook(name="My Webhook",
                                  project="QXDevOPS:searchcode-server",
                                  url="https://www.my-webhook-listener.com/sonar")

    # Delete a Webhook.
    sonar.webhooks.delete_webhook(webhook_key="AXQoj7QajOKlq86mQnzT")

    # Get the recent deliveries for a specified project
    deliveries = sonar.webhooks.get_webhook_deliveries(componentKey="my-project")

    # Get a webhook delivery by its id.
    delivery = sonar.webhooks.get_webhook_delivery(delivery_id="AXHAfha9dxfTzNWG9hAN")

    # Search for global webhooks or project webhooks. Webhooks are ordered by name.
    webhooks = sonar.webhooks.search_webhooks(project="my-project")

    # Update a Webhook.
    sonar.webhooks.update_webhook(webhook_key="AXQojxbgjOKlq86mQnzS",
                                  new_name="My Webhook",
                                  new_url="https://www.my-webhook-listener.com/sonar",
                                  secret="your_secret")
