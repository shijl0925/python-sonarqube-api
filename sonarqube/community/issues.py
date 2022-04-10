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
    API_ISSUES_TAGS_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarQubeIssues(RestClient):
    """
    SonarQube issues Operations
    """

    MAX_SEARCH_NUM = 100

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeIssues, self).__init__(**kwargs)

    def get(self, key):
        result = list(self.search_issues(issues=key))
        for issue in result:
            if issue["key"] == key:
                return issue

    @PAGES_GET(API_ISSUES_SEARCH_ENDPOINT, item="issues")
    def search_issues(
        self,
        componentKeys=None,
        branch=None,
        pullRequest=None,
        additionalFields=None,
        asc="true",
        assigned=None,
        assignees=None,
        author=None,
        createdAfter=None,
        createdAt=None,
        createdBefore=None,
        createdInLast=None,
        cwe=None,
        facets=None,
        issues=None,
        languages=None,
        onComponentOnly="false",
        owaspTop10=None,
        ps=None,
        resolutions=None,
        resolved=None,
        rules=None,
        s=None,
        sansTop25=None,
        severities=None,
        sinceLeakPeriod="false",
        sonarsourceSecurity=None,
        statuses=None,
        tags=None,
        types=None,
    ):
        """
        SINCE 3.6
        Search for issues.

        :param componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of the optional fields to be returned in response. Possible values are for:

            * _all
            * comments
            * languages
            * actionPlans
            * rules
            * transitions
            * actions
            * users

        :param asc: Ascending sort. Possible values are for: true, false, yes, no.default value is true
        :param assigned: To retrieve assigned or unassigned issues. Possible values are for: true, false, yes, no
        :param assignees: Comma-separated list of assignee logins. The value '__me__' can be used as a placeholder
            for user who performs the request
        :param author: SCM accounts. To set several values, the parameter must be called once for each value.
        :param componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        :param createdAfter: To retrieve issues created after the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
            If this parameter is set, createdSince must not be set
        :param createdBefore: To retrieve issues created before the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
        :param createdAt: Datetime to retrieve issues created during a specific analysis
        :param createdInLast: To retrieve issues created during a time span before the current time (exclusive).
            Accepted units are 'y' for year, 'm' for month, 'w' for week and 'd' for day. If this parameter is set,
            createdAfter must not be set.such as: 1m2w (1 month 2 weeks)
        :param cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select issues not associated to any CWE.
        :param facets: Comma-separated list of the facets to be computed. No facet is computed by default. Possible values are for:

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

        :param issues: Comma-separated list of issue keys
        :param languages: Comma-separated list of languages. such as: java,js
        :param onComponentOnly: Return only issues at a component's level, not on its descendants (modules, directories,
            files, etc). This parameter is only considered when componentKeys or componentUuids is set. Possible values are for: true,
            false, yes, no. default value is false.
        :param owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param resolutions: Comma-separated list of resolutions.Possible values are for:

            * FALSE-POSITIVE
            * WONTFIX
            * FIXED
            * REMOVED

        :param resolved: To match resolved or unresolved issues. Possible values are for: true, false, yes, no
        :param rules: Comma-separated list of coding rule keys. Format is <repository>:<rule>.such as: squid:AvoidCycles
        :param s: Sort field. Possible values are for:

            * CREATION_DATE
            * UPDATE_DATE
            * CLOSE_DATE
            * ASSIGNEE
            * SEVERITY
            * STATUS
            * FILE_LINE

        :param sansTop25: Comma-separated list of SANS Top 25 categories. Possible values are for:

            * insecure-interaction
            * risky-resource
            * porous-defenses

        :param severities: Comma-separated list of severities.Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

        :param sinceLeakPeriod: To retrieve issues created since the leak period.If this parameter is set to
            a truthy value, createdAfter must not be set and one component id or key must be provided.
            Possible values are for: true, false, yes, no. default value is false.
        :param sonarsourceSecurity: Comma-separated list of SonarSource security categories. Use 'others' to
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

        :param statuses: Comma-separated list of statuses.Possible values are for:

            * OPEN
            * CONFIRMED
            * REOPENED
            * RESOLVED
            * CLOSED
            * TO_REVIEW
            * IN_REVIEW
            * REVIEWED

        :param tags: Comma-separated list of tags.such as: security,convention
        :param types: Comma-separated list of types.Possible values are for:

            * CODE_SMELL
            * BUG
            * VULNERABILITY

        :return:
        """

    @POST(API_ISSUES_ASSIGN_ENDPOINT)
    def issue_assign(self, issue, assignee=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_SET_SEVERITY_ENDPOINT)
    def issue_change_severity(self, issue, severity):
        """
        SINCE 3.6
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

    @POST(API_ISSUES_SET_TYPE_ENDPOINT)
    def issue_set_type(self, issue, type):
        """
        SINCE 5.5
        Change type of issue, for instance from 'code smell' to 'bug'.

        :param issue: Issue key
        :param type: New type.Possible values are for:

          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT

        :return: request response
        """

    @POST(API_ISSUES_ADD_COMMENT_ENDPOINT)
    def issue_add_comment(self, issue, text):
        """
        SINCE 3.6
        Add a comment.

        :param issue: Issue key
        :param text: Comment text
        :return: request response
        """

    @POST(API_ISSUES_DELETE_COMMENT_ENDPOINT)
    def issue_delete_comment(self, comment):
        """
        SINCE 3.6
        Delete a comment.

        :param comment: Comment key
        :return: request response
        """

    @POST(API_ISSUES_EDIT_COMMENT_ENDPOINT)
    def issue_edit_comment(self, comment, text):
        """
        SINCE 3.6
        Edit a comment.

        :param comment: Comment key
        :param text: Comment text
        :return: request response
        """

    @POST(API_ISSUES_DO_TRANSITION_ENDPOINT)
    def issue_do_transition(self, issue, transition):
        """
        SINCE 3.6
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

    @GET(API_ISSUES_AUTHORS_ENDPOINT)
    def search_scm_accounts(self, project, q=None):
        """
        SINCE 5.1
        Search SCM accounts which match a given query

        :param project: Project key
        :param q: Limit search to authors that contain the supplied string.
        :return:
        """

    @POST(API_ISSUES_BULK_CHANGE_ENDPOINT)
    def issues_bulk_change(
        self,
        issues,
        add_tags=None,
        assign=None,
        comment=None,
        do_transition=None,
        remove_tags=None,
        sendNotifications=None,
        set_severity=None,
        set_type=None,
    ):
        """
        SINCE 3.7
        Bulk change on issues.

        :param issues: Comma-separated list of issue keys

        optional parameters:
        :param add_tags: Add tags.such as: security,java8
        :param assign: To assign the list of issues to a specific user (login), or un-assign all the issues
        :param comment: To add a comment to a list of issues
        :param do_transition: Transition, Possible values are for:

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

        :param remove_tags: Remove tags.such as: security,java8
        :param sendNotifications: Possible values are for: true, false, yes, no. default value is false.
        :param set_severity: To change the severity of the list of issues. Possible values are for:

          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER

        :param set_type: To change the type of the list of issues. Possible values are for:

          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT

        :return: request response
        """

    @GET(API_ISSUES_CHANGELOG_ENDPOINT)
    def get_issue_changelog(self, issue):
        """
        SINCE 4.1
        Display changelog of an issue.

        :param issue: Issue key
        :return:
        """

    @POST(API_ISSUES_SET_TAGS_ENDPOINT)
    def issue_set_tags(self, issue, tags=None):
        """
        SINCE 5.1
        Set tags on an issue.

        :param issue: Issue key
        :param tags: Comma-separated list of tags. All tags are removed if parameter is empty or not set.
          such as: security,cwe,misra-c
        :return: request response
        """

    @GET(API_ISSUES_TAGS_ENDPOINT)
    def get_issues_tags(self, project, q=None):
        """
        SINCE 5.1
        List tags

        :param project:
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
