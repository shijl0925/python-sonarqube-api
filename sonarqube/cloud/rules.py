#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.rules import SonarQubeRules
from sonarqube.utils.config import (
    API_RULES_SEARCH_ENDPOINT,
    API_RULES_UPDATE_ENDPOINT,
    API_RULES_SHOW_ENDPOINT,
    API_RULES_TAGS_ENDPOINT
)


class SonarCloudRules(SonarQubeRules):
    """
    SonarCloud rules Operations
    """
    def __getitem__(self, key):
        raise AttributeError("%s does not support this method" % self.__class__.__name__)

    def search_rules(self, organization, **kwargs):
        """
        Search for a collection of relevant rules matching a specified query.

        :param organization: organization key.

          optional parameters:
          * organization: organization key.
          * activation: Filter rules that are activated or deactivated on the selected Quality profile. Ignored if the parameter 'qprofile' is not set.
          * qprofile: Quality profile key to filter on. Used only if the parameter 'activation' is set.
          * languages: Comma-separated list of languages
          * active_severities: Comma-separated list of activation severities,
            i.e the severity of rules in Quality profiles. Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

          * asc: Ascending sort.Possible values are for: true, false, yes, no. default value is true
          * available_since: Filters rules added since date. Format is yyyy-MM-dd
          * cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select rules not associated to any CWE.
          * f: Comma-separated list of the fields to be returned in response. All the fields are returned by default,
            except actives.Since 5.5, following fields have been deprecated :

            * "defaultDebtRemFn" becomes "defaultRemFn"
            * "debtRemFn" becomes "remFn"
            * "effortToFixDescription" becomes "gapDescription"
            * "debtOverloaded" becomes "remFnOverloaded"

            Possible values are for:

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

          * facets: Comma-separated list of the facets to be computed. No facet is computed by default.
            Possible values are for:

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

          * include_external: Include external engine rules in the results.
            Possible values are for: true, false, yes, no. default value is false.
          * inheritance: Comma-separated list of values of inheritance for a rule within a quality profile.
            Used only if the parameter 'activation' is set. Possible values are for:

            * NONE
            * INHERITED
            * OVERRIDES

          * is_template: Filter template rules.Possible values are for: true, false, yes, no.
          * owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
          * q: UTF-8 search query
          * repositories: Comma-separated list of repositories
          * rule_key: Key of rule to search for
          * s: Sort field. Possible values are for:

            * name
            * updatedAt
            * createdAt
            * key

          * sansTop25: Comma-separated list of SANS Top 25 categories. Possible values are for:

            * insecure-interaction
            * risky-resource
            * porous-defenses

          * severities: Comma-separated list of default severities.
            Not the same than severity of rules in Quality profiles.Possible values are for:

              * INFO
              * MINOR
              * MAJOR
              * CRITICAL
              * BLOCKER

          * sonarsourceSecurity: Comma-separated list of SonarSource security categories.
            Use 'others' to select rules not associated with any category. Possible values are for:

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

          * statuses: Comma-separated list of status codes. Possible values are for:

            * BETA
            * DEPRECATED
            * READY
            * REMOVED

          * tags: Comma-separated list of tags. Returned rules match any of the tags (OR operator).
            Possible values are for: security,java8
          * template_key: Key of the template rule to filter on. Used to search for the custom rules based
            on this template.
          * types: Comma-separated list of types. Returned rules match any of the tags (OR operator).such as;

            * CODE_SMELL
            * BUG
            * VULNERABILITY
            * SECURITY_HOTSPOT

        :return:
        """
        params = {'organization': organization}
        if kwargs:
            self.api.copy_dict(params, kwargs, self.OPTIONS_SEARCH)

        page_num = 1
        page_size = 1
        n_rules = 2

        while page_num * page_size < n_rules:
            resp = self.get(API_RULES_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            n_rules = response['total']

            params['p'] = page_num + 1

            # Yield rules
            for rule in response['rules']:
                yield rule

    def update_rule(self, key, organization, **kwargs):
        """
        Update an existing rule.

        :param key: Key of the rule to update
        :param organization: organization key.

        optional parameters:
          * name: Rule name (mandatory for custom rule)
          * description: Rule description (mandatory for custom rule and manual rule)
          * markdown_note: Optional note in markdown format. Use empty value to remove current note.
            Note is not changed if the parameter is not set.
          * params: Parameters as semi-colon list of =, for example 'params=key1=v1;key2=v2'
            (Only when updating a custom rule)
          * remediation_fn_base_effort: Base effort of the remediation function of the rule
          * remediation_fn_type: Type of the remediation function of the rule
          * remediation_fy_gap_multiplier: Gap multiplier of the remediation function of the rule
          * severity: Rule severity (Only when updating a custom rule).Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

          * status: Rule status (Only when updating a custom rule). Possible values are for:

            * BETA
            * DEPRECATED
            * READY
            * REMOVED

          * tags: Optional comma-separated list of tags to set. Use blank value to remove current tags.
            Tags are not changed if the parameter is not set.

        :return: request response
        """
        data = {'key': key, 'organization': organization}
        if kwargs:
            self.api.copy_dict(data, kwargs, self.OPTIONS_UPDATE)

        return self.post(API_RULES_UPDATE_ENDPOINT, params=data)

    def get_rule(self, rule_key, organization, actives=False):
        """
        Get detailed information about a rule.

        :param rule_key: Rule key
        :param organization: organization key.
        :param actives: Show rule's activations for all profiles ("active rules").
          Possible values are for: True or False. default value is False.
        :return:
        """
        params = {
            'key': rule_key,
            'organization': organization,
            'actives': actives and 'true' or 'false'
        }

        res = self.get(API_RULES_SHOW_ENDPOINT, params=params)
        return res.json()

    def get_rule_tags(self, organization, ps=10, q=None):
        """
        List rule tags

        :param organization: organization key.
        :param ps: Page size. Must be greater than 0 and less or equal than 100.default value is 10.
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {'organization': organization, 'ps': ps}

        if q:
            params.update({"q": q})

        resp = self.get(API_RULES_TAGS_ENDPOINT, params=params)
        response = resp.json()
        return response['tags']
