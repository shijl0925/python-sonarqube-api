#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_RULES_SEARCH_ENDPOINT,
    API_RULES_CREATE_ENDPOINT,
    API_RULES_UPDATE_ENDPOINT,
    API_RULES_DELETE_ENDPOINT,
    API_RULES_SHOW_ENDPOINT,
    API_RULES_TAGS_ENDPOINT,
    API_RULES_REPOSITORIES_ENDPOINT
)


class SonarQubeRules:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def search_rules(self, activation=None, qprofile=None, languages=None, active_severities=None, asc="true",
                     available_since=None, cwe=None, f=None, facets=None, include_external="false", inheritance=None,
                     is_template=None, owaspTop10=None, q=None, repositories=None, rule_key=None, s=None,
                     sansTop25=None, severities=None, sonarsourceSecurity=None, statuses=None, tags=None,
                     template_key=None, issue_types=None):
        """
        Search for a collection of relevant rules matching a specified query.
        :param activation: Filter rules that are activated or deactivated on the selected Quality profile.
          Ignored if the parameter 'qprofile' is not set.
        :param qprofile: Quality profile key to filter on. Used only if the parameter 'activation' is set.
        :param languages: Comma-separated list of languages
        :param active_severities: Comma-separated list of activation severities,
          i.e the severity of rules in Quality profiles. such as:
            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER
        :param asc: Ascending sort.such as true, false, yes, no. default value is true
        :param available_since: Filters rules added since date. Format is yyyy-MM-dd
        :param cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select rules not associated to any CWE.
        :param f: Comma-separated list of the fields to be returned in response. All the fields are returned by default,
         except actives.Since 5.5, following fields have been deprecated :
           * "defaultDebtRemFn" becomes "defaultRemFn"
           * "debtRemFn" becomes "remFn"
           * "effortToFixDescription" becomes "gapDescription"
           * "debtOverloaded" becomes "remFnOverloaded"
           such as:
           * actives
           * createdAt
           * debtOverloaded
           * debtRemFn
           * defaultDebtRemFn
           * defaultRemFn
           * effortToFixDescription
           * gapDescription
           * htmlDesc
           * htmlNote
           * internalKey
           * isExternal
           * isTemplate
           * lang
           * langName
           * mdDesc
           * mdNote
           * name
           * noteLogin
           * params
           * remFn
           * remFnOverloaded
           * repo
           * scope
           * severity
           * status
           * sysTags
           * tags
           * templateKey
           * updatedAt
        :param facets: Comma-separated list of the facets to be computed. No facet is computed by default. such as:
          * languages
          * repositories
          * tags
          * severities
          * active_severities
          * statuses
          * types
          * true
          * cwe
          * owaspTop10
          * sansTop25
          * sonarsourceSecurity
        :param include_external: Include external engine rules in the results.
          such as true, false, yes, no. default value is false.
        :param inheritance: Comma-separated list of values of inheritance for a rule within a quality profile.
          Used only if the parameter 'activation' is set. such as:
          * NONE
          * INHERITED
          * OVERRIDES
        :param is_template: Filter template rules.such as true, false, yes, no.
        :param owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        :param q: UTF-8 search query
        :param repositories: Comma-separated list of repositories
        :param rule_key: Key of rule to search for
        :param s: Sort field. such as:
          * name
          * updatedAt
          * createdAt
          * key
        :param sansTop25: Comma-separated list of SANS Top 25 categories. such as:
          * insecure-interaction
          * risky-resource
          * porous-defenses
        :param severities: Comma-separated list of default severities.
          Not the same than severity of rules in Quality profiles.such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :param sonarsourceSecurity: Comma-separated list of SonarSource security categories.
          Use 'others' to select rules not associated with any category. such as:
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
        :param statuses: Comma-separated list of status codes. such as:
          * BETA
          * DEPRECATED
          * READY
          * REMOVED
        :param tags: Comma-separated list of tags. Returned rules match any of the tags (OR operator).
          such as: security,java8
        :param template_key: Key of the template rule to filter on. Used to search for the custom rules based
          on this template.
        :param issue_types: Comma-separated list of types. Returned rules match any of the tags (OR operator).such as;
          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT
        :return:
        """
        params = {
            'asc': asc,
            'include_external': include_external
        }

        # Add profile and activity params
        if qprofile:
            params.update({'activation': activation, 'qprofile': qprofile, 'inheritance': inheritance.upper()})

        # Add language param
        if languages:
            params.update({'languages': languages.lower()})

        if active_severities:
            params.update({'active_severities': active_severities.upper()})

        if available_since:
            params.update({'available_since': available_since})

        if cwe:
            params.update({'cwe': cwe})

        if f:
            params.update({'f': f})

        if facets:
            params.update({'facets': facets})

        if is_template:
            params.update({'is_template': is_template})

        if owaspTop10:
            params.update({'owaspTop10': owaspTop10})

        if q:
            params.update({'q': q})

        if repositories:
            params.update({'repositories': repositories})

        if rule_key:
            params.update({'rule_key': rule_key})

        if s:
            params.update({'s': s})

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

        if template_key:
            params.update({'template_key': template_key})

        if issue_types:
            params.update({'types': issue_types.upper()})

        # Page counters
        page_num = 1
        page_size = 1
        n_rules = 2

        # Cycle through rules
        while page_num * page_size < n_rules:
            # Update paging information for calculation
            res = self.sonarqube.make_call('get', API_RULES_SEARCH_ENDPOINT, **params).json()
            page_num = res['p']
            page_size = res['ps']
            n_rules = res['total']

            # Update page number (next) in queryset
            params['p'] = page_num + 1

            # Yield rules
            for rule in res['rules']:
                yield rule

    def create_rule(self, key, name, description, template_key, severity, status=None, rule_type=None, **params):
        """
        Create a a custom rule.
        :param key: Key of the custom rule
        :param name: Rule name
        :param description: Rule description
        :param template_key: Key of the template rule in order to create a custom rule (mandatory for custom rule)
        :param severity: Rule severity.such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :param status: Rule status.such as:
          * BETA
          * DEPRECATED
          * READY
          * REMOVED
        :param rule_type: Rule type.such as:
          * CODE_SMELL
          * BUG
          * VULNERABILITY
          * SECURITY_HOTSPOT
        :return: request response
        """
        # Build data to post
        data = {
            'custom_key': key,
            'name': name,
            'markdown_description': description,
            "template_key": template_key,
            "severity": severity.upper()
        }

        if status:
            data.update({"status": status.upper()})

        if rule_type:
            data.update({"type": rule_type.upper()})

        params = ';'.join('{}={}'.format(k, v) for k, v in sorted(params.items()) if v)
        if params:
            data.update({"params": params})

        self.sonarqube.make_call('post', API_RULES_CREATE_ENDPOINT, **data)

    def update_rule(self, key, name=None, description=None, markdown_note=None, remediation_fn_base_effort=None,
                    remediation_fn_type=None, remediation_fy_gap_multiplier=None, severity=None, status=None,
                    tags=None, **params):
        """
        Update an existing rule.
        :param key: Key of the rule to update
        :param name: Rule name (mandatory for custom rule)
        :param description: Rule description (mandatory for custom rule and manual rule)
        :param markdown_note: Optional note in markdown format. Use empty value to remove current note.
          Note is not changed if the parameter is not set.
        :param remediation_fn_base_effort: Base effort of the remediation function of the rule
        :param remediation_fn_type: Type of the remediation function of the rule
        :param remediation_fy_gap_multiplier: Gap multiplier of the remediation function of the rule
        :param severity: Rule severity (Only when updating a custom rule).such as:
          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER
        :param status: Rule status (Only when updating a custom rule). such as:
          * BETA
          * DEPRECATED
          * READY
          * REMOVED
        :param tags: Optional comma-separated list of tags to set. Use blank value to remove current tags.
          Tags are not changed if the parameter is not set.
        :param params: Parameters as semi-colon list of =, for example 'params=key1=v1;key2=v2'
          (Only when updating a custom rule)
        :return:
        """
        data = {'key': key}

        if description:
            data.update({"markdown_description": description})

        if markdown_note:
            data.update({"markdown_note": markdown_note})

        if name:
            data.update({"name": name})

        if remediation_fn_base_effort:
            data.update({"remediation_fn_base_effort": remediation_fn_base_effort})

        if remediation_fn_type:
            data.update({"remediation_fn_type": remediation_fn_type})

        if remediation_fy_gap_multiplier:
            data.update({"remediation_fy_gap_multiplier": remediation_fy_gap_multiplier})

        if severity:
            data.update({"severity": severity.upper()})

        if status:
            data.update({"status": status.upper()})

        if tags:
            data.update({"tags": tags})

        params = ';'.join('{}={}'.format(k, v) for k, v in sorted(params.items()) if v)
        if params:
            data.update({"params": params})

        self.sonarqube.make_call('post', API_RULES_UPDATE_ENDPOINT, **data)

    def delete_rule(self, rule_key):
        """
        Delete custom rule.
        :param rule_key:
        :return:
        """
        params = {
            'key': rule_key
        }
        self.sonarqube.make_call('post', API_RULES_DELETE_ENDPOINT, **params)

    def get_rule(self, rule_key, actives="false"):
        """
        Get detailed information about a rule.
        :param rule_key: Rule key
        :param actives: Show rule's activations for all profiles ("active rules"). such as: true, false, yes, no
          default value is fasle.
        :return:
        """
        params = {'key': rule_key, 'actives': actives}

        res = self.sonarqube.make_call('get', API_RULES_SHOW_ENDPOINT, **params)
        return res.json()

    def get_rule_repositories(self, language=None, q=None):
        """
        List available rule repositories
        :param language: A language key; if provided, only repositories for the given language will be returned
        :param q: A pattern to match repository keys/names against
        :return:
        """
        params = {}

        if language:
            params.update({"language": language})

        if q:
            params.update({"q": q})

        resp = self.sonarqube.make_call('get', API_RULES_REPOSITORIES_ENDPOINT, **params)
        response = resp.json()
        return response['repositories']

    def get_rule_tags(self, ps=10, q=None):
        """
        List rule tags
        :param ps: Page size. Must be greater than 0 and less or equal than 100.default value is 10.
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {'ps': ps}

        if q:
            params.update({"q": q})

        resp = self.sonarqube.make_call('get', API_RULES_TAGS_ENDPOINT, **params)
        response = resp.json()
        return response['tags']
