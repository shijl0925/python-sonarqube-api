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

    def search_project_issues(self, componentKeys, branch, additionalFields=None, asc="true", assigned=None,
                              assignees=None, author=None, createdAfter=None, createdAt=None, createdBefore=None,
                              createdInLast=None, cwe=None, facets=None, issues=None, languages=None,
                              onComponentOnly="false", owaspTop10=None, resolutions=None, resolved=None, rules=None,
                              s=None, sansTop25=None, severities=None, sinceLeakPeriod="false",
                              sonarsourceSecurity=None, statuses=None, tags=None, types=None):
        """
        Search for the project's issues.
        :param componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
          components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        :param branch:
        :param additionalFields: Comma-separated list of the optional fields to be returned in response. such as:
          * _all
          * comments
          * languages
          * actionPlans
          * rules
          * transitions
          * actions
          * users
        :param asc: Ascending sort. such as true, false, yes, no.default value is true
        :param assigned: To retrieve assigned or unassigned issues. such as true, false, yes, no
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
        :param facets: Comma-separated list of the facets to be computed. No facet is computed by default. such as:
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
          files, etc). This parameter is only considered when componentKeys or componentUuids is set. such as: true,
          false, yes, no. default value is false.
        :param owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        :param resolutions: Comma-separated list of resolutions.such as:
          * FALSE-POSITIVE
          * WONTFIX
          * FIXED
          * REMOVED
        :param resolved: To match resolved or unresolved issues. such as true, false, yes, no
        :param rules: Comma-separated list of coding rule keys. Format is <repository>:<rule>.such as: squid:AvoidCycles
        :param s: Sort field. such as:
          * CREATION_DATE
          * UPDATE_DATE
          * CLOSE_DATE
          * ASSIGNEE
          * SEVERITY
          * STATUS
          * FILE_LINE
        :param sansTop25: Comma-separated list of SANS Top 25 categories. such as:
          * insecure-interaction
          * risky-resource
          * porous-defenses
        :param severities: Comma-separated list of severities.such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :param sinceLeakPeriod: To retrieve issues created since the leak period.If this parameter is set to
          a truthy value, createdAfter must not be set and one component id or key must be provided.
          such as true, false, yes, no. default value is false.
        :param sonarsourceSecurity: Comma-separated list of SonarSource security categories. Use 'others' to
          select issues not associated with any category。such as:
          * sql-injection
          command-injection
          path-traversal-injection
          ldap-injection
          xpath-injection
          rce
          dos
          ssrf
          csrf
          xss
          log-injection
          http-response-splitting
          open-redirect
          xxe
          object-injection
          weak-cryptography
          auth
          insecure-conf
          file-manipulation
          others
        :param statuses: Comma-separated list of statuses.such as:
          * OPEN
          * CONFIRMED
          * REOPENED
          * RESOLVED
          * CLOSED
          * TO_REVIEW
          * IN_REVIEW
          * REVIEWED
        :param tags: Comma-separated list of tags.such as: security,convention
        :param types: Comma-separated list of types.such as:
          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT
        :return:
        """
        params = {
            'componentKeys': componentKeys,
            'branch': branch,
            'asc': asc,
            'onComponentOnly': onComponentOnly,
            'sinceLeakPeriod': sinceLeakPeriod
        }

        if additionalFields:
            params.update({'additionalFields': additionalFields})

        if assigned:
            params.update({'assigned': assigned})

        if assignees:
            params.update({'assignees': assignees})

        if author:
            params.update({'author': author})

        if createdAfter:
            params.update({'createdAfter': createdAfter})

        if createdAt:
            params.update({'createdAt': createdAt})

        if createdBefore:
            params.update({'createdBefore': createdBefore})

        if createdInLast:
            params.update({'createdInLast': createdInLast})

        if cwe:
            params.update({'cwe': cwe})

        if facets:
            params.update({'facets': facets})

        if issues:
            params.update({'issues': issues})

        if languages:
            params.update({'languages': languages})

        if owaspTop10:
            params.update({'owaspTop10': owaspTop10})

        if resolutions:
            params.update({'resolutions': resolutions.upper()})

        if resolved:
            params.update({'resolved': resolved})

        if rules:
            params.update({'rules': rules})

        if s:
            params.update({'s': s.upper()})

        if sansTop25:
            params.update({'sansTop25': sansTop25})

        if severities:
            params.update({'severities': severities.upper()})

        if sonarsourceSecurity:
            params.update({'sonarsourceSecurity': sonarsourceSecurity})

        if statuses:
            params.update({'statuses': statuses.upper()})

        if tags:
            params.update({'tags': tags})

        if types:
            params.update({'types': types.upper()})

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
            params.update({'assignee': assignee})

        self.sonarqube.make_call('post', API_ISSUES_ASSIGN_ENDPOINT, **params)

    def issue_change_severity(self, issue, severity):
        """
        Change severity.
        :param issue: Issue key
        :param severity: New severity.such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :return:
        """
        params = {
            'issue': issue,
            'severity': severity.upper()
        }
        self.sonarqube.make_call('post', API_ISSUES_SET_SEVERITY_ENDPOINT, **params)

    def issue_set_type(self, issue, issue_type):
        """
        Change type of issue, for instance from 'code smell' to 'bug'.
        :param issue: Issue key
        :param issue_type: New type.such as:
          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT
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
        :param issue: Issue key
        :param transition: Transition.such as:
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
        :return:
        """
        params = {
            'issue': issue,
            'transition': transition
        }
        self.sonarqube.make_call('post', API_ISSUES_DO_TRANSITION_ENDPOINT, **params)

    def search_scm_accounts(self, project, q=None):
        """
        Search SCM accounts which match a given query
        :param project: Project key
        :param q: Limit search to authors that contain the supplied string.
        :return:
        """
        params = {
            'project': project,
        }
        if q:
            params.update({'q': q})

        resp = self.sonarqube.make_call('get', API_ISSUES_AUTHORS_ENDPOINT, **params)
        response = resp.json()
        return response['authors']

    def issues_bulk_change(self, issues, add_tags=None, assign=None, remove_tags=None, comment=None, do_transition=None,
                           sendNotifications="false", issue_severity=None, issue_type=None):
        """
        Bulk change on issues.
        :param issues: Comma-separated list of issue keys
        :param add_tags: Add tags.such as: security,java8
        :param assign: To assign the list of issues to a specific user (login), or un-assign all the issues
        :param comment: To add a comment to a list of issues
        :param do_transition: Transition, such as:
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
        :param sendNotifications: such as: true, false, yes, no. default value is false.
        :param issue_severity: To change the severity of the list of issues. such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :param issue_type: To change the type of the list of issues. such as:
          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT
        :return:
        """
        params = {
            'issues': issues,
            'sendNotifications': sendNotifications
        }

        if add_tags:
            params.update({'add_tags': add_tags})

        if assign:
            params.update({'assign': assign})

        if remove_tags:
            params.update({'remove_tags': remove_tags})

        if comment:
            params.update({'comment': comment})

        if do_transition:
            params.update({'do_transition': do_transition})

        if issue_severity:
            params.update({'set_severity': issue_severity.upper()})

        if issue_type:
            params.update({'set_type': issue_type.upper()})

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
          such as: security,cwe,misra-c
        :return:
        """
        params = {
            'issue': issue
        }
        if tags:
            params.update({'tags': tags})

        self.sonarqube.make_call('post', API_ISSUES_SET_TAGS_ENDPOINT, **params)

    def get_issues_tags(self, project, q=None):
        """
        List tags
        :param project:
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {'project': project}
        if q:
            params.update({'q': q})

        resp = self.sonarqube.make_call('get', API_ISSUES_TAGS_ENDPOINT, **params)
        return resp.json()
