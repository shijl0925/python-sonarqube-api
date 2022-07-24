================
api/alm_settings
================

Manage the Pull Request Decoration ALM settings for the project.
-----------------------------------------------------------------------------------------------------------

Examples
--------

For _project_ set the configuration to the first found BitBucket configuration (defined in the global settings), and the project key and repository SLUG to respective values.
    bitbucket = ""

    for setting in sonar.alm_settings.list():
        if setting["alm"] == "bitbucket":
            return setting["key"]
            
    sonar.alm_settings.set_bitbucket_binding(bitbucket, project, project_key, repository_slug)
