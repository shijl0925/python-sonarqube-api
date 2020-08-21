#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_ISSUES_SEARCH_ENDPOINT,
    API_ISSUES_ASSIGN_ENDPOINT,
    API_ISSUES_DO_TRANSITION_ENDPOINT,
    API_ISSUES_ADD_COMMENT_ENDPOINT,
    API_ISSUES_EDIT_COMMENT_ENDPOINT,
    API_ISSUES_DELETE_COMMENT_ENDPOINT,
    API_ISSUES_SET_SEVERITY_ENDPOINT,
    API_ISSUES_SET_TYPE_ENDPOINT,
    API_ISSUES_AUTHORS_ENDPOINT,
    API_ISSUES_BULK_CHANGE_ENDPOINT,
    API_ISSUES_CHANGELOG_ENDPOINT,
    API_ISSUES_SET_TAGS_ENDPOINT,
    API_ISSUES_TAGS_ENDPOINT
)


class SonarQubeIssue:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_issues(self, componentKeys, branch, **kwargs):
        """
        Search for the project's issues.
        :param componentKeys:
        :param branch:
        :param kwargs:
        additionalFields: Comma-separated list of the optional fields to be returned in response. such as:
          _all,comments,languages,actionPlans,rules,transitions,actions,users
        asc: Ascending sort
        assigned: To retrieve assigned or unassigned issues
        assignees: Comma-separated list of assignee logins. The value '__me__' can be used as a placeholder for user
          who performs the request
        author: SCM accounts. To set several values, the parameter must be called once for each value.
        componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
          components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        createdAfter: To retrieve issues created after the given date (inclusive).
          Either a date (server timezone) or datetime can be provided.
          If this parameter is set, createdSince must not be set
        createdBefore: To retrieve issues created before the given date (inclusive).
          Either a date (server timezone) or datetime can be provided.
        createdAt: Datetime to retrieve issues created during a specific analysis
        createdInLast: To retrieve issues created during a time span before the current time (exclusive).
          Accepted units are 'y' for year, 'm' for month, 'w' for week and 'd' for day. If this parameter is set,
          createdAfter must not be set.such as: 1m2w (1 month 2 weeks)
        cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select issues not associated to any CWE.
        facets: Comma-separated list of the facets to be computed. No facet is computed by default.
        issues: Comma-separated list of issue keys
        languages: Comma-separated list of languages.
        onComponentOnly: Return only issues at a component's level, not on its descendants (modules, directories,
          files, etc). This parameter is only considered when componentKeys or componentUuids is set.
          owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        resolutions: Comma-separated list of resolutions.such as: FALSE-POSITIVE,WONTFIX,FIXED,REMOVED
        resolved: To match resolved or unresolved issues.such as: true or false.
        rules: Comma-separated list of coding rule keys. Format is <repository>:<rule>.such as: squid:AvoidCycles
        s: Sort field
        sansTop25: Comma-separated list of SANS Top 25 categories.
        severities: Comma-separated list of severities.such as:INFO,MINOR,MAJOR,CRITICAL,BLOCKER
        sinceLeakPeriod: To retrieve issues created since the leak period.If this parameter is set to a truthy value,
        createdAfter must not be set and one component id or key must be provided. such as: true or false.
        sonarsourceSecurity: Comma-separated list of SonarSource security categories. Use 'others' to select issues
          not associated with any category
        statuses: Comma-separated list of statuses.such as: OPEN,CONFIRMED,REOPENED,RESOLVED,CLOSED,TO_REVIEW,
          IN_REVIEW,REVIEWED
        tags: Comma-separated list of tags.such as: security,convention
        types: Comma-separated list of types.such as: CODE_SMELL,BUG,VULNERABILITY,SECURITY_HOTSPOT

        :return:
        """
        params = {
            'componentKeys': componentKeys,
            'branch': branch
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_ISSUES_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for issue in response['issues']:
                yield issue

            if page_num >= 100:
                break

    def issue_assign(self, issue, assignee=None):
        """
        Assign/Unassign an issue
        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return:
        """
        params = {
            'issue': issue
        }
        if assignee:
            params['assignee'] = assignee

        self.sonarqube.make_call('post', API_ISSUES_ASSIGN_ENDPOINT, **params)

    def issue_set_severity(self, issue, severity):
        """
        Change severity.
        :param issue: Issue key
        :param severity: New severity.such as: INFO,MINOR,MAJOR,CRITICAL,BLOCKER
        :return:
        """
        params = {
            'issue': issue,
            'severity': severity
        }
        self.sonarqube.make_call('post', API_ISSUES_SET_SEVERITY_ENDPOINT, **params)

    def issue_set_type(self, issue, issue_type):
        """
        Change type of issue, for instance from 'code smell' to 'bug'.
        :param issue: Issue key
        :param issue_type: New type.such as: CODE_SMELL,BUG,VULNERABILITY,SECURITY_HOTSPOT
        :return:
        """
        params = {
            'issue': issue,
            'type': issue_type
        }
        self.sonarqube.make_call('post', API_ISSUES_SET_TYPE_ENDPOINT, **params)

    def issue_add_comment(self, issue, text):
        """
        Add a comment.
        :param issue: Issue key
        :param text: Comment text
        :return:
        """
        params = {
            'issue': issue,
            'text': text
        }
        self.sonarqube.make_call('post', API_ISSUES_ADD_COMMENT_ENDPOINT, **params)

    def issue_delete_comment(self, comment):
        """
        Delete a comment.
        :param comment: Comment key
        :return:
        """
        params = {
            'comment': comment
        }
        self.sonarqube.make_call('post', API_ISSUES_DELETE_COMMENT_ENDPOINT, **params)

    def issue_edit_comment(self, comment, text):
        """
        Edit a comment.
        :param comment: Comment key
        :param text: Comment text
        :return:
        """
        params = {
            'comment': comment,
            'text': text
        }
        self.sonarqube.make_call('post', API_ISSUES_EDIT_COMMENT_ENDPOINT, **params)

    def issue_do_transition(self, issue, transition):
        """
        Do workflow transition on an issue. Requires authentication and Browse permission on project.
        The transitions 'wontfix' and 'falsepositive' require the permission 'Administer Issues'.
        The transitions involving security hotspots require the permission 'Administer Security Hotspot'.
        :param issue:
        :param transition: Transition.such as:
          confirm,unconfirm,reopen,resolve,falsepositive,wontfix,close,setinreview,resolveasreviewed,
          openasvulnerability,resetastoreview
        :return:
        """
        params = {
            'issue': issue,
            'transition': transition
        }
        self.sonarqube.make_call('post', API_ISSUES_DO_TRANSITION_ENDPOINT, **params)

    def get_issues_author(self, project, **kwargs):
        """
        Search SCM accounts which match a given query
        :param project: Project key
        :param kwargs:
        :return:
        """
        params = {
            'project': project,
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        resp = self.sonarqube.make_call('get', API_ISSUES_AUTHORS_ENDPOINT, **params)
        response = resp.json()
        return response['authors']

    def issues_bulk_change(self, issues, **kwargs):
        """
        Bulk change on issues.
        :param issues: Comma-separated list of issue keys
        :param kwargs:
        add_tags: Add tags.such as:security,java8
        remove_tags: Remove tags
        assign: To assign the list of issues to a specific user (login), or un-assign all the issues
        comment: To add a comment to a list of issues
        do_transition: Transition
        sendNotifications:
        set_severity: To change the severity of the list of issues
        set_type: To change the type of the list of issues
        :return:
        """
        params = {'issues': issues}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube.make_call('post', API_ISSUES_BULK_CHANGE_ENDPOINT, **params)

    def get_issue_changelog(self, issue):
        """
        Display changelog of an issue.
        :param issue: Issue key
        :return:
        """
        params = {'issue': issue}
        resp = self.sonarqube.make_call('get', API_ISSUES_CHANGELOG_ENDPOINT, **params)
        return resp.json()

    def issue_set_tags(self, issue, tags=None):
        """
        Set tags on an issue.
        :param issue: Issue key
        :param tags: Comma-separated list of tags. All tags are removed if parameter is empty or not set.
        :return:
        """
        params = {
            'issue': issue
        }
        if tags:
            params['tags'] = tags

        self.sonarqube.make_call('post', API_ISSUES_SET_TAGS_ENDPOINT, **params)

    def get_issues_tags(self, project, **kwargs):
        """
        List tags
        :param project:
        :param kwargs:
        ps: Page size. Page size. Must be greater than 0 and less or equal than 100, default value is 10
        q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {'project': project}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        resp = self.sonarqube.make_call('get', API_ISSUES_TAGS_ENDPOINT, **params)
        return resp.json()
