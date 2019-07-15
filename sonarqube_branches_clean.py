#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

from sonarqube_utils.base_api import SonarAPIHandler

if __name__ == "__main__":
    sonarqube_url = "http://localhost:9000"
    sonarqube_user = "admin"
    sonarqube_password = "admin"

    try:
        sonarhandler = SonarAPIHandler(sonarqube_url,
                                       sonarqube_user,
                                       sonarqube_password)
        print('{} connect successful!'.format(sonarhandler._sonarqube_url))
    except Exception as err:
        print("Connect {} Failed!".format(sonarhandler._sonarqube_url) + str(err))
        sys.exit(1)

    project_list = sonarhandler.projects.keys()

    for project in project_list:
        print("project: " + project)
        branch_list = sonarhandler.project_branches.get_project_branches_list(project=project)
        for branch in branch_list:
            if not branch["isMain"] and branch["type"] == "LONG":
                try:
                    branch_name = branch["name"]
                    print("remove branch: " + branch_name)
                    sonarhandler.project_branches.delete_project_branch(project, branch_name)
                except UnicodeEncodeError:
                    pass
