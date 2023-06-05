# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

- when get one project/group/rule/user, need parameter 'organization' in sonarcloud.

### Changed

- get one issue use 'get_issue' instead.
- get one project use 'get_project' instead.
- get one group use 'get_user_group' instead.
- get one user use 'get_user' instead.
- get one view use 'get_view' instead.
- Search for projects associated (or not) to a quality gate, with parameter 'gateName', not 'gateId'.
  From Sonarqube 8.4 Parameter 'gateId' is deprecated. Use 'gateName' instead.

## [2.0.3] - 2023-06-02

### Added

### Fixed

### Changed

### Removed

## [2.0.2] - 2023-05-28

### Added

### Fixed

### Changed

### Removed


[unreleased]: https://github.com/shijl0925/python-sonarqube-api/compare/2.0.3...HEAD
[2.0.3]: https://github.com/shijl0925/python-sonarqube-api/compare/2.0.2...2.0.3
