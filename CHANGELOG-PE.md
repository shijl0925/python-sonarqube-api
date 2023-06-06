# Professional Edition Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

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

[unreleased]: https://gitlab.com/shijl0925/python-sonarqube-pro-api/-/compare/2.0.1...HEAD
[2.0.1]: https://gitlab.com/shijl0925/python-sonarqube-pro-api/-/compare/2.0.0...2.0.1
[2.0.0]: https://gitlab.com/shijl0925/python-sonarqube-pro-api/-/compare/1.3.7...2.0.0
