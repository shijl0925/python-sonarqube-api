#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ Search for tasks """
    tasks1 = sonar.ce.search_tasks(componentId="AXD1qDmE5ohQwTlZZPR6", status="FAILED,CANCELED,PENDING,IN_PROGRESS")
    # or
    tasks2 = sonar.ce.search_tasks(componentId="AXD1qDmE5ohQwTlZZPR6", task_type="REPORT")

    """ Returns CE activity related metrics """
    metrics = sonar.ce.get_ce_activity_related_metrics(componentId="AXD1qDmE5ohQwTlZZPR6")

    """ Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project) """
    tasks = sonar.ce.get_component_queue_and_current_tasks(component="virgo:bmw-monitor")

    """ Give Compute Engine task details such as type, status, duration and associated component """
    task = sonar.ce.get_task(task_id="AXQJiIU3jOKlq86mQnLe", additionalFields="stacktrace,scannerContext,warnings")
