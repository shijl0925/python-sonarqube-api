#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Add permission to a group
    sonar.permissions.add_permission_to_group(groupName="sonar-users", permission="scan", projectKey="my_project")
    # or
    sonar.permissions.add_permission_to_group(groupName="sonar-users", permission="profileadmin")

    # Remove a permission from a group
    sonar.permissions.remove_permission_from_group(groupName="sonar-users", permission="scan", projectKey="my_project")
    # or
    sonar.permissions.remove_permission_from_group(groupName="sonar-users", permission="profileadmin")

    # Add permission to a user
    sonar.permissions.add_permission_to_user(login="kevin", permission="codeviewer", projectKey="my_project")
    # or
    sonar.permissions.add_permission_to_user(login="kevin", permission="gateadmin")

    # Remove permission from a user
    sonar.permissions.remove_permission_from_user(login="kevin", permission="codeviewer", projectKey="my_project")
    # or
    sonar.permissions.add_permission_to_user(login="kevin", permission="gateadmin")

    # Apply a permission template to one project.
    sonar.permissions.apply_template_to_project(template_name="test-template", project_key="my_project")

    # Apply a permission template to several projects.
    sonar.permissions.apply_template_to_projects(template_name="test-template", projects="my_project,another_project")

    # Add a group to a permission template.
    sonar.permissions.add_group_to_template(group_name="sonar-users", template_name="test-template",
                                            permission="user")

    # Remove a group from a permission template.
    sonar.permissions.remove_group_from_template(group_name="sonar-users", template_name="test-template",
                                                 permission="user")

    # Add a project creator to a permission template.
    sonar.permissions.add_project_creator_to_template(template_name="test-template", permission="user")

    # Remove a project creator from a permission template.
    sonar.permissions.remove_project_creator_from_template(template_name="test-template", permission="user")

    # Add a user to a permission template.
    sonar.permissions.add_user_to_template(user_login="kevin", template_name="test-template", permission="codeviewer")

    # Remove a user from a permission template.
    sonar.permissions.remove_user_from_template(user_login="kevin",
                                                template_name="test-template",
                                                permission="codeviewer"
                                                )

    # Create a permission template.
    sonar.permissions.create_template("test-template", description="test template", projectKeyPattern=".*\.finance\..*")

    # Delete a permission template.
    sonar.permissions.delete_template(template_name="test-template")

    # List permission templates.
    templates = sonar.permissions.search_templates()

    # Set a permission template as default.
    sonar.permissions.set_default_template(template_name="test-template")

    # Update a permission template.
    sonar.permissions.update_template(template_id="AXQqe0yfjOKlq86mQn4t",
                                      template_name="test-permission-template",
                                      description="test permission template",
                                      projectKeyPattern=".*\.finance\..*"
                                      )
