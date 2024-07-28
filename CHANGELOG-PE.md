# Professional Edition Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed


## [2.0.3] - 2024-07-28

### Added
- Provide functions to read all issues / components / hotspots / users ... page by page:
  * 'issues.search_all_issues', Search All issues.
  * 'ce.search_all_tasks', Search All tasks.
  * 'components.search_all_components', Search All components
  * 'components.get_all_components_tree', Navigate through all components based on the chosen strategy.
  * 'components.search_all_projects', Search all projects
  * 'hotspots.search_all_hotspots', Search all Security Hotpots.
  * 'measures.search_all_measures_history'
  * 'measures.get_all_component_tree_with_specified_measures'
  * 'project_analyses.search_project_all_analyses_and_events'
  * 'projects.search_all_projects', Search all projects or views to administrate them.
  * 'qualitygates.list_all_groups_allowed_to_gate'
  * 'qualitygates.list_all_users_allowed_to_gate'
  * 'qualityprofiles.get_all_history_of_changes_on_quality_profile'
  * 'qualityprofiles.get_all_projects_associate_with_quality_profile'
  * 'rules.search_all_rules', Search all rules matching a specified query.
  * 'user_groups.search_all_user_groups', Search all user groups.
  * 'user_groups.search_all_users_belong_to_group', Search all users with membership information with respect to a group.
  * 'users.search_all_users', Get a list of all users. 
  * 'users.search_all_groups_user_belongs_to', Lists all groups a user belongs to.
  * 'webhooks.get_all_webhook_deliveries'

- function 'alm_integrations.import_azure_project' was added,
   Create a SonarQube project with the information from the provided Azure DevOps project.

- function 'alm_integrations.import_bitbucketcloud_repo' was added,
   Create a SonarQube project with the information from the provided Bitbucket Cloud repository.

- function 'alm_integrations.import_bitbucketserver_project' was added,
   Create a SonarQube project with the information from the provided BitbucketServer project.

- function 'alm_integrations.import_github_project' was added,
   Create a SonarQube project with the information from the provided GitHub repository.

- function 'editions.activate_grace_period' was added,
   Enable a license 7-days grace period if the Server ID is invalid.

- function 'issues.gitlab_sast_export' was added,
   Return a list of vulnerabilities according to the Gitlab SAST JSON format.

- function 'project_branches.set_main' was added,
   Allow to set a new main branch.

- function 'qualityprofiles.activate_rules' was added,
   Bulk-activate rules on one quality profile.

- function 'qualityprofiles.deactivate_rules' was added,
   Bulk deactivate rules on Quality profiles.

### Fixed

### Changed

### Removed

## [2.0.2] - 2024-07-27

### Added

### Fixed

- alm_integrations.import_gitlab_project
  * Parameter almSetting becomes optional if you have only one configuration for GitLab
  * Add optional parameters newCodeDefinitionType and newCodeDefinitionValue

- alm_integrations.search_bitbucketclound_repos
  * function name change to search_bitbucketcloud_repos
  * param p set default value: 1
  * param ps set default value: 20
  
- alm_integrations.search_gitlab_repos
  * param p set default value: 1
  * param ps set default value: 25
  
- alm_integrations.set_pat
  * Parameter almSetting becomes optional if you have only one DevOps Platform configuration
  
- alm_settings.create_github
  * Optional parameter 'webhookSecret' was added
  
- alm_settings.set_azure_binding alm_settings.set_bitbucket_binding alm_settings.set_bitbucketcloud_binding
   alm_settings.set_github_binding alm_settings.set_gitlab_binding
  * parameter monorepo becomes required
  
- alm_settings.update_azure alm_settings.update_bitbucket
  * Parameter 'personalAccessToken' becomes optional
  
- alm_settings.update_bitbucket
  * function name change to update_bitbucketcloud
  * remove param 'personalAccessToken' and 'url'
  * add param 'clientId' and 'clientSecret'
  
- alm_settings.update_github
  * Parameter 'privateKey' and 'clientSecret' is no longer required
  * Optional parameter 'webhookSecret' was added
  
- alm_settings.update_gitlab
  * Parameter 'personalAccessToken' is no longer required
  
- ce.search_tasks
  * Remove deprecated field 'componentId'
  * param p set default value: 1
  * param ps set default value: 100
  * param onlyCurrents set default value: false
  * param status set default value: 'SUCCESS,FAILED,CANCELED'
 
- components.search_components
  * Param 'language' has been removed
  * param p set default value: 1
  * param ps set default value: 100
  
- components.get_components_tree components.search_projects
  * param p set default value: 1
  * param ps set default value: 100
  
- favorites.search_favorites
  * param p set default value: 1
  * param ps set default value: 100

- hotspots.search_hotspots
  * remove param 'sinceLeakPeriod'
  * use param 'project' instead of 'projectKey'
  * Optional parameter 'sansTop25' was added
  * param inNewCodePeriod set default value: false
  * param p set default value: 1
  * param ps set default value: 100

- issues.search_scm_accounts
  * param ps set default value: 10

- issues.issues_bulk_change
  * param sendNotifications set default value: false
  
- issues.search_issues
  * Optional parameter 'components' was added, Replaces parameter 'componentKeys'
  * Parameter 'sinceLeakPeriod' is removed, please use 'inNewCodePeriod' instead
  * param ps set default value: 100
  * Optional parameter 'cleanCodeAttributeCategories' was added
  * Optional parameter 'fixedInPullRequest' was added
  * Optional parameter 'impactSeverities' was added
  * Optional parameter 'impactSoftwareQualities' was added
  * Optional parameter 'issueStatuses' was added
  * Optional parameter 'prioritizedRule' was added

- issues.get_issues_tags
  * param ps set default value: 10
  * param all set default value: false
  
- languages.get_supported_programming_languages
  * Optional parameter 'components' was added, default value is 0, means all languages;
  
- measures.get_component_with_specified_measures, measures.search_measures_history, measures.get_component_tree_with_specified_measures
  * param p set default value: 1
  * param ps set default value: 100

- metrics.search_metrics
  * param p set default value: 1
  * param ps set default value: 100
  
- notifications.add_notification_for_user notifications.get_user_notifications notifications.remove_notification_for_user
  * Parameter 'login' becomes optional
  
- permissions.add_group_to_template, permissions.add_project_creator_to_template, permissions.add_user_to_template, 
    notifications.apply_template_to_projects, notifications.delete_template, notifications.remove_group_from_template
	notifications.remove_project_creator_from_template notifications.remove_user_from_template notifications.set_default_template
  * Optional parameter 'templateId' was added
  * Parameter 'templateName' becomes optional

- permissions.apply_template_to_project
  * Optional parameter 'templateId' was added
  * Parameter 'templateName' becomes optional
  * Parameter 'projectKey' becomes optional
  * Optional parameter 'projectId' was added
  
- permissions.add_permission_to_group, notifications.remove_permission_from_group,
    permissions.add_permission_to_user, notifications.remove_permission_from_user
  * Optional parameter 'projectId' was added

- project_analyses.search_project_analyses_and_events
  * param p set default value: 1
  * param ps set default value: 100
  
- project_links.create_project_link, project_links.search_project_links
  * Optional parameter 'projectId' was added
  * Parameter 'projectKey' becomes optional
  
- project_tags.search_project_tags
  * param p set default value: 1
  * param ps set default value: 10
  
- projects.create_project
  * Optional parameter 'newCodeDefinitionType' was added
  * Optional parameter 'newCodeDefinitionValue' was added
  
- projects.search_projects
  * param p set default value: 1
  * param ps set default value: 100
  
- qualityprofiles.change_parent_of_quality_profile
  * Parameter 'parentQualityProfile' becomes optional
  
- qualityprofiles.get_history_of_changes_on_quality_profile
  * param p set default value: 1
  * param ps set default value: 50
  
- qualityprofiles.get_projects_associate_with_quality_profile
  * param p set default value: 1
  * param ps set default value: 100

- qualitygates.get_project_qualitygates_status
  * Optional parameter 'projectId' was added

- qualitygates.get_qualitygate_projects
  * param page set default value: 1
  
- qualitygates.list_groups_allowed_to_gate, qualitygates.list_users_allowed_to_gate
  * param p set default value: 1
  * param ps set default value: 25
  * param selected set default value: 'selected'
  
- rules.create_rule
  * remove parameters 'custom_key' , 'markdown_description' , 'template_key', 'prevent_reactivation'
  * parameter 'customKey' , ''markdownDescription and 'templateKey' become required
  * param 'preventReactivation' set default value: false
  * param 'status' set default value: READY
  * Optional parameters 'cleanCodeAttribute' and 'impacts' was added

- rules.search_rules
  * Optional parameter 'cleanCodeAttributeCategories' was added
  * Optional parameter 'impactSeverities' was added 
  * Optional parameter 'impactSoftwareQualities' was added
  * Optional parameter 'prioritizedRule' was added
  * Optional parameter 'owaspTop10_2021' was added
  * param p set default value: 1
  * param ps set default value: 100

- rules.update_rule
  * Optional parameter 'markdownDescription' was added, Replaces parameter 'markdown_description'

- issues.search_issues
  * Optional parameter 'pciDss_3_2' was added. Comma-separated list of PCI DSS v3.2 categories.
  * Optional parameter 'pciDss_4_0' was added. Comma-separated list of PCI DSS v4.0 categories.
  * Optional parameter 'owaspAsvs_4_0' was added. Comma-separated list of OWASP ASVS v4.0 categories.
  * Optional parameter 'owaspTop10_2021' was added. Comma-separated list of OWASP Top 10 2021 lowercase categories.
  * Optional parameter 'stig_ASD_V5R3' was added. Comma-separated list of STIG V5R3 categories.
  * Optional parameter 'casa' was added. Comma-separated list of CASA categories.

- hotspots.search_hotspots
  * Optional parameter 'owaspAsvs_4_0' was added. Comma-separated list of OWASP ASVS v4.0 categories or rules.
  * Optional parameter 'owaspTop10_2021' was added. Comma-separated list of OWASP 2021 Top 10 lowercase categories.
  * Optional parameter 'pciDss_3_2' was added. Comma-separated list of PCI DSS v3.2 categories.
  * Optional parameter 'pciDss_4_0' was added. Comma-separated list of PCI DSS v4.0 categories.
  * Optional parameter 'stig_ASD_V5R3' was added. Comma-separated list of STIG V5R3 lowercase categories.
  * Optional parameter 'casa' was added. Comma-separated list of CASA categories.

- settings.update_setting_value
  * Parameter 'value' becomes optional
  * Optional parameter 'values' was added

- bug fix:
  * system.get_database_migration_status funtion (api/system/db_migration_status) use GET request method
  * system.get_health_status funtion (api/system/health) use GET request method
  
- system.get_logs
  * parameter 'name' was added, Replaces parameter 'process'
  
- user_groups.search_user_groups
  * param p set default value: 1
  * param ps set default value: 100
  
- user_groups.search_users_belong_to_group
  * param p set default value: 1
  * param ps set default value: 25

- user_tokens.generate_user_token
  * param type set default value: USER_TOKEN

- users.deactivate_user
  * param anonymize set default value: false

- users.search_groups_user_belongs_to
  * param p set default value: 1
  * param ps set default value: 25

- users.search_users
  * param p set default value: 1
  * param ps set default value: 50
  * param deactivated set default value: false
  * Optional parameter 'externalIdentity' was added

- views.create
  * Parameter 'parent' added to create sub-portfolios

- views.set_regexp_mode, views.set_remaining_projects_mode, views.set_tags_mode
  * Optional parameter 'branch' was added

- webhooks.get_webhook_deliveries
  * param p set default value: 1
  * param ps set default value: 10

- bug fix:
  * webservices.web_service_response_example funtion (api/webservices/response_example) use GET request method

### Changed

### Removed

## [2.0.1] - 2023-06-06

### Added

- get permission template use 'get_template'
- Support "Search for projects without 'Administer System' permission" by using 'sonarqube.rest.components.SonarQubeComponents.search_projects'
- Support "Get the details of the current authenticated user." by using 'sonarqube.rest.users.SonarQubeUsers.current'

### Fixed

- when get one project/group/rule/user, need parameter 'organization' in sonarcloud.
- Support 'Search the Bitbucket Cloud repositories' use sonarqube.rest.alm_integrations.SonarQubeAlmIntegrations.search_bitbucketclound_repos
- Support 'Configure a new instance of Bitbucket Cloud' use sonarqube.rest.alm_settings.SonarQubeAlmSettings.create_bitbucketcloud

### Changed

- get one ALM setting use 'get_alm_setting' instead.
- get one issue use 'get_issue' instead.
- get one project use 'get_project' instead.
- get one group use 'get_user_group' instead.
- get one user use 'get_user' instead.
- get one view use 'get_view' instead.

### Removed

## [2.0.0] - 2023-05-25

### Added

- add parameter 'p' in sonarqube.rest.ce.SonarQubeCe.search_tasks
- add parameters 'cwe', 'files', 'inNewCodePeriod', 'owaspAsvsLevel', 'owaspTop10', 'sonarsourceSecurity' 
  in sonarqube.rest.hotspots.SonarQubeHotspots.search_hotspots
- add parameters 'scopes', 'timeZone', 'codeVariants', 'inNewCodePeriod', 'owaspAsvsLevel' 
  in sonarqube.rest.issues.SonarQubeIssues.search_issues
- add parameter 'ps' in sonarqube.rest.issues.SonarQubeIssues.search_scm_accounts
- add parameters 'branch', 'all', 'ps' in sonarqube.rest.issues.SonarQubeIssues.get_issues_tags
- Support 'Reindex issues for a project'.
- add parameters 'ps', 'p' in sonarqube.rest.project_tags.SonarQubeProjectTags.search_project_tags
- add parameters 'mainBranch' in sonarqube.rest.projects.SonarQubeProjects.create_project
- Support 'Remove the ability from a group to edit a Quality Gate'.
- Support 'List the groups that are allowed to edit a Quality Gate'.
- Support 'Allow a user to edit a Quality Gate'.
- Support 'Remove the ability from an user to edit a Quality Gate'.
- Support 'List the users that are allowed to edit a Quality Gate'.
- Support parameters 'customKey', 'markdownDescription', 'templateKey', 'preventReactivation'
  in sonarqube.rest.rules.SonarQubeRules.create_rule
- add parameters 'expirationDate', 'projectKey', 'type' in sonarqube.rest.user_tokens.SonarQubeUserTokens.generate_user_token
- add parameters 'deactivated', 'lastConnectedAfter', 'lastConnectedBefore', 'managed', 'slLastConnectedAfter', 'slLastConnectedBefore'
  in sonarqube.rest.users.SonarQubeBaseUsers.search_users
- add parameter 'anonymize' in sonarqube.rest.users.SonarQubeUsers.deactivate_user

### Fixed

- 'Activate a rule for a given quality profile' exist bug, fixed it.

### Changed

- Replace parameter 'component_id' with parameter 'component' in sonarqube.rest.ce.SonarQubeCe.get_ce_activity_related_metrics
- Copy/Delete/Rename/Set Quality Gate with parameter 'name', not 'id'. 
  From Sonarqube 8.4 Parameter 'id' is deprecated.
- Add Quality Gate condition, or Search for projects associated (or not) to a quality gate, with parameter 'gateName', not 'gateId'.
  From Sonarqube 8.4 Parameter 'gateId' is deprecated. Use 'gateName' instead.

### Removed

[unreleased]: https://github.com/shijl0925/python-sonarqube-pro-api/compare/2.0.3...HEAD
[2.0.3]: https://github.com/shijl0925/python-sonarqube-pro-api/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/shijl0925/python-sonarqube-pro-api/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/shijl0925/python-sonarqube-pro-api/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/shijl0925/python-sonarqube-pro-api/compare/1.3.7...2.0.0
