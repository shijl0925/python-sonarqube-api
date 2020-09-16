#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
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


class SonarCloudIssues(RestClient):
    """
    SonarCloud issues Operations
    """
    MAX_SEARCH_NUM = 100
    OPTIONS_SEARCH = ['additionalFields', 'asc', 'assigned', 'assignees', 'author', 'componentKeys', 'branch',
                      'pullRequest', 'createdAfter', 'createdAt', 'createdBefore', 'createdInLast', 'cwe', 'facets',
                      'issues', 'languages', 'onComponentOnly', 'owaspTop10', 'ps', 'resolutions', 'resolved', 'rules',
                      's', 'sansTop25', 'severities', 'sinceLeakPeriod', 'sonarsourceSecurity', 'statuses', 'tags',
                      'types', 'organization']

    OPTIONS_BULK = ['add_tags', 'assign', 'comment', 'do_transition', 'remove_tags',
                    'sendNotifications', 'set_severity', 'set_type']

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudIssues, self).__init__(**kwargs)

    def __getitem__(self, key):
        result = list(self.search_issues(issues=key))
        for issue in result:
            if issue['key'] == key:
                return issue

    def search_issues(self, **kwargs):
        """
        Search for issues.
        optional parameters:
          * componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
          * branch: Branch key.
          * pullRequest: Pull request id.
          * additionalFields: Comma-separated list of the optional fields to be returned in response. Possible values are for:

            * _all
            * comments
            * languages
            * actionPlans
            * rules
            * transitions
            * actions
            * users

          * asc: Ascending sort. Possible values are for: true, false, yes, no.default value is true
          * assigned: To retrieve assigned or unassigned issues. Possible values are for: true, false, yes, no
          * assignees: Comma-separated list of assignee logins. The value '__me__' can be used as a placeholder
            for user who performs the request
          * author: SCM accounts. To set several values, the parameter must be called once for each value.
          * componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
          * createdAfter: To retrieve issues created after the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
            If this parameter is set, createdSince must not be set
          * createdBefore: To retrieve issues created before the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
          * createdAt: Datetime to retrieve issues created during a specific analysis
          * createdInLast: To retrieve issues created during a time span before the current time (exclusive).
            Accepted units are 'y' for year, 'm' for month, 'w' for week and 'd' for day. If this parameter is set,
            createdAfter must not be set.such as: 1m2w (1 month 2 weeks)
          * cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select issues not associated to any CWE.
          * facets: Comma-separated list of the facets to be computed. No facet is computed by default. Possible values are for:

            * projects
            * moduleUuids
            * fileUuids
            * assigned_to_me
            * severities
            * statuses
            * resolutions
            * rules
            * assignees
            * authors
            * author
            * directories
            * languages
            * tags
            * types
            * owaspTop10
            * sansTop25
            * cwe
            * createdAt
            * sonarsourceSecurity

          * issues: Comma-separated list of issue keys
          * languages: Comma-separated list of languages. such as: java,js
          * onComponentOnly: Return only issues at a component's level, not on its descendants (modules, directories,
            files, etc). This parameter is only considered when componentKeys or componentUuids is set. Possible values are for: true,
            false, yes, no. default value is false.
          *  owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
          *  resolutions: Comma-separated list of resolutions.Possible values are for:

            * FALSE-POSITIVE
            * WONTFIX
            * FIXED
            * REMOVED

          *  resolved: To match resolved or unresolved issues. Possible values are for: true, false, yes, no
          *  rules: Comma-separated list of coding rule keys. Format is <repository>:<rule>.such as: squid:AvoidCycles
          *  s: Sort field. Possible values are for:

            * CREATION_DATE
            * UPDATE_DATE
            * CLOSE_DATE
            * ASSIGNEE
            * SEVERITY
            * STATUS
            * FILE_LINE

          *  sansTop25: Comma-separated list of SANS Top 25 categories. Possible values are for:

            * insecure-interaction
            * risky-resource
            * porous-defenses

          *  severities: Comma-separated list of severities.Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

          *  sinceLeakPeriod: To retrieve issues created since the leak period.If this parameter is set to
            a truthy value, createdAfter must not be set and one component id or key must be provided.
            Possible values are for: true, false, yes, no. default value is false.
          *  sonarsourceSecurity: Comma-separated list of SonarSource security categories. Use 'others' to
            select issues not associated with any category。Possible values are for:

            * sql-injection
            * command-injection
            * path-traversal-injection
            * ldap-injection
            * xpath-injection
            * rce
            * dos
            * ssrf
            * csrf
            * xss
            * log-injection
            * http-response-splitting
            * open-redirect
            * xxe
            * object-injection
            * weak-cryptography
            * auth
            * insecure-conf
            * file-manipulation
            * others

          *  statuses: Comma-separated list of statuses.Possible values are for:

            * OPEN
            * CONFIRMED
            * REOPENED
            * RESOLVED
            * CLOSED
            * TO_REVIEW
            * IN_REVIEW
            * REVIEWED

          *  tags: Comma-separated list of tags.such as: security,convention
          *  types: Comma-separated list of types.Possible values are for:

            * CODE_SMELL
            * BUG
            * VULNERABILITY
            * SECURITY_HOTSPOT

          * organization: Organization key


        :return:
        """
        params = {}
        if kwargs:
            self.api.copy_dict(params, kwargs, self.OPTIONS_SEARCH)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_ISSUES_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for issue in response['issues']:
                yield issue

            if page_num >= self.MAX_SEARCH_NUM:
                break

    def issue_assign(self, issue, assignee=None):
        """
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """
        params = {
            'issue': issue
        }
        if assignee:
            params.update({'assignee': assignee})

        return self.post(API_ISSUES_ASSIGN_ENDPOINT, params=params)

    def issue_change_severity(self, issue, severity):
        """
        Change severity.

        :param issue: Issue key
        :param severity: New severity.Possible values are for:

          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER

        :return: request response
        """
        params = {
            'issue': issue,
            'severity': severity.upper()
        }

        return self.post(API_ISSUES_SET_SEVERITY_ENDPOINT, params=params)

    def issue_set_type(self, issue, issue_type):
        """
        Change type of issue, for instance from 'code smell' to 'bug'.

        :param issue: Issue key
        :param issue_type: New type.Possible values are for:

          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT

        :return: request response
        """
        params = {
            'issue': issue,
            'type': issue_type
        }

        return self.post(API_ISSUES_SET_TYPE_ENDPOINT, params=params)

    def issue_add_comment(self, issue, text, feedback=False):
        """
        Add a comment.

        :param issue: Issue key
        :param text: Comment text
        :param feedback: Define is the given comment is a feedback
        :return: request response
        """
        params = {
            'issue': issue,
            'text': text
        }

        if feedback:
            params.update({"isFeedback": feedback and 'true' or 'false'})

        return self.post(API_ISSUES_ADD_COMMENT_ENDPOINT, params=params)

    def issue_delete_comment(self, comment):
        """
        Delete a comment.

        :param comment: Comment key
        :return: request response
        """
        params = {
            'comment': comment
        }

        return self.post(API_ISSUES_DELETE_COMMENT_ENDPOINT, params=params)

    def issue_edit_comment(self, comment, text):
        """
        Edit a comment.

        :param comment: Comment key
        :param text: Comment text
        :return: request response
        """
        params = {
            'comment': comment,
            'text': text
        }

        return self.post(API_ISSUES_EDIT_COMMENT_ENDPOINT, params=params)

    def issue_do_transition(self, issue, transition):
        """
        Do workflow transition on an issue. Requires authentication and Browse permission on project.
        The transitions 'wontfix' and 'falsepositive' require the permission 'Administer Issues'.
        The transitions involving security hotspots require the permission 'Administer Security Hotspot'.

        :param issue: Issue key
        :param transition: Transition.Possible values are for:

          * confirm
          * unconfirm
          * reopen
          * resolve
          * falsepositive
          * wontfix
          * close
          * setinreview
          * resolveasreviewed
          * openasvulnerability
          * resetastoreview

        :return: request response
        """
        params = {
            'issue': issue,
            'transition': transition
        }

        return self.post(API_ISSUES_DO_TRANSITION_ENDPOINT, params=params)

    def search_scm_accounts(self, organization, project, q=None):
        """
        Search SCM accounts which match a given query

        :param organization: Organization key
        :param project: Project key
        :param q: Limit search to authors that contain the supplied string.
        :return:
        """
        params = {
            'organization': organization,
            'project': project,
        }
        if q:
            params.update({'q': q})

        resp = self.get(API_ISSUES_AUTHORS_ENDPOINT, params=params)
        response = resp.json()
        return response['authors']

    def issues_bulk_change(self, issues, **kwargs):
        """
        Bulk change on issues.

        :param issues: Comma-separated list of issue keys

        optional parameters:
          * add_tags: Add tags.such as: security,java8
          * assign: To assign the list of issues to a specific user (login), or un-assign all the issues
          * comment: To add a comment to a list of issues
          * do_transition: Transition, Possible values are for:

            * confirm
            * unconfirm
            * reopen
            * resolve
            * falsepositive
            * wontfix
            * close
            * setinreview
            * resolveasreviewed
            * openasvulnerability
            * resetastoreview

          * remove_tags: Remove tags.such as: security,java8
          * sendNotifications: Possible values are for: true, false, yes, no. default value is false.
          * issue_severity: To change the severity of the list of issues. Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

          * issue_type: To change the type of the list of issues. Possible values are for:

            * CODE_SMELL
            * BUG
            * VULNERABILITY
            * SECURITY_HOTSPOT

        :return: request response
        """
        params = {
            'issues': issues
        }
        if kwargs:
            self.api.copy_dict(params, kwargs, self.OPTIONS_BULK)

        return self.post(API_ISSUES_BULK_CHANGE_ENDPOINT, params=params)

    def get_issue_changelog(self, issue):
        """
        Display changelog of an issue.

        :param issue: Issue key
        :return:
        """
        params = {'issue': issue}
        resp = self.get(API_ISSUES_CHANGELOG_ENDPOINT, params=params)
        return resp.json()

    def issue_set_tags(self, issue, tags=None):
        """
        Set tags on an issue.

        :param issue: Issue key
        :param tags: Comma-separated list of tags. All tags are removed if parameter is empty or not set.
          such as: security,cwe,misra-c
        :return: request response
        """
        params = {
            'issue': issue
        }
        if tags:
            params.update({'tags': tags})

        return self.post(API_ISSUES_SET_TAGS_ENDPOINT, params=params)

    def get_issues_tags(self, organization, project, q=None):
        """
        List tags

        :param organization: Organization key
        :param project:
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {'organization': organization, 'project': project}
        if q:
            params.update({'q': q})

        resp = self.get(API_ISSUES_TAGS_ENDPOINT, params=params)
        return resp.json()
