#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.issues import SonarQubeIssues
from sonarqube.utils.config import (
    API_ISSUES_ADD_COMMENT_ENDPOINT,
    API_ISSUES_AUTHORS_ENDPOINT,
    API_ISSUES_TAGS_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarCloudIssues(SonarQubeIssues):
    """
    SonarCloud issues Operations
    """

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
        return super().search_issues(**kwargs)

    @POST(API_ISSUES_ADD_COMMENT_ENDPOINT)
    def issue_add_comment(self, issue, text, isFeedback="false"):
        """
        Add a comment.

        :param issue: Issue key
        :param text: Comment text
        :param isFeedback: Define is the given comment is a feedback
        :return: request response
        """

    @GET(API_ISSUES_AUTHORS_ENDPOINT)
    def search_scm_accounts(self, organization, project, q=None):
        """
        Search SCM accounts which match a given query

        :param organization: Organization key
        :param project: Project key
        :param q: Limit search to authors that contain the supplied string.
        :return:
        """

    @GET(API_ISSUES_TAGS_ENDPOINT)
    def get_issues_tags(self, organization, project, q=None):
        """
        List tags

        :param organization: Organization key
        :param project:
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
