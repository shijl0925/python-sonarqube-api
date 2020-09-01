#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Search for a collection of relevant rules matching a specified query.
    rules = sonar.rules.search_rules(tags="correctness", languages="java")

    # Create a a custom rule.
    sonar.rules.create_rule(key="Todo_should_not_be_used",
                            name="My custom rule",
                            description="Description of my custom rule",
                            template_key="squid:S2253",
                            severity="BLOCKER")

    # Update an existing rule.
    sonar.rules.update_rule(key="squid:Todo_should_not_be_used", severity="INFO")

    # Delete custom rule.
    sonar.rules.delete_rule(rule_key="squid:Todo_should_not_be_used")

    # Get detailed information about a rule.
    rule = sonar.rules.get_rule(rule_key="squid:S2204")

    # List available rule repositories
    rule_repositories = sonar.rules.get_rule_repositories(language="java")

    # List rule tags
    rule_tags = sonar.rules.get_rule_tags()
