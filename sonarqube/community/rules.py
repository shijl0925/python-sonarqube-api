#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_RULES_SEARCH_ENDPOINT,
    API_RULES_CREATE_ENDPOINT,
    API_RULES_UPDATE_ENDPOINT,
    API_RULES_DELETE_ENDPOINT,
    API_RULES_SHOW_ENDPOINT,
    API_RULES_TAGS_ENDPOINT,
    API_RULES_REPOSITORIES_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarQubeRules(RestClient):
    """
    SonarQube rules Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeRules, self).__init__(**kwargs)

    def get(self, key):
        result = list(self.search_rules(rule_key=key))
        for rule in result:
            if rule["key"] == key:
                return rule

    @PAGES_GET(API_RULES_SEARCH_ENDPOINT, item="rules")
    def search_rules(
        self,
        activation=None,
        qprofile=None,
        languages=None,
        active_severities=None,
        asc="true",
        available_since=None,
        cwe=None,
        f=None,
        facets=None,
        include_external="false",
        inheritance=None,
        is_template=None,
        owaspTop10=None,
        q=None,
        repositories=None,
        rule_key=None,
        s=None,
        sansTop25=None,
        severities=None,
        sonarsourceSecurity=None,
        statuses=None,
        tags=None,
        template_key=None,
        types=None,
    ):
        """
        SINCE 4.4
        Search for a collection of relevant rules matching a specified query.

        :param activation: Filter rules that are activated or deactivated on the selected Quality profile. Ignored if the parameter 'qprofile' is not set.
        :param qprofile: Quality profile key to filter on. Used only if the parameter 'activation' is set.
        :param languages: Comma-separated list of languages
        :param active_severities: Comma-separated list of activation severities,
            i.e the severity of rules in Quality profiles. Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

        :param asc: Ascending sort.Possible values are for: true, false, yes, no. default value is true
        :param available_since: Filters rules added since date. Format is yyyy-MM-dd
        :param cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select rules not associated to any CWE.
        :param f: Comma-separated list of the fields to be returned in response. All the fields are returned by default,
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

        :param facets: Comma-separated list of the facets to be computed. No facet is computed by default.
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

        :param include_external: Include external engine rules in the results.
            Possible values are for: true, false, yes, no. default value is false.
        :param inheritance: Comma-separated list of values of inheritance for a rule within a quality profile.
            Used only if the parameter 'activation' is set. Possible values are for:

            * NONE
            * INHERITED
            * OVERRIDES

        :param is_template: Filter template rules.Possible values are for: true, false, yes, no.
        :param owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        :param q: UTF-8 search query
        :param repositories: Comma-separated list of repositories
        :param rule_key: Key of rule to search for
        :param s: Sort field. Possible values are for:

            * name
            * updatedAt
            * createdAt
            * key

        :param sansTop25: Comma-separated list of SANS Top 25 categories. Possible values are for:

            * insecure-interaction
            * risky-resource
            * porous-defenses

        :param severities: Comma-separated list of default severities.
            Not the same than severity of rules in Quality profiles.Possible values are for:

              * INFO
              * MINOR
              * MAJOR
              * CRITICAL
              * BLOCKER

        :param sonarsourceSecurity: Comma-separated list of SonarSource security categories.
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

        :param statuses: Comma-separated list of status codes. Possible values are for:

            * BETA
            * DEPRECATED
            * READY
            * REMOVED

        :param tags: Comma-separated list of tags. Returned rules match any of the tags (OR operator).
            Possible values are for: security,java8
        :param template_key: Key of the template rule to filter on. Used to search for the custom rules based
            on this template.
        :param types: Comma-separated list of types. Returned rules match any of the tags (OR operator).such as;

            * CODE_SMELL
            * BUG
            * VULNERABILITY
            * SECURITY_HOTSPOT

        :return:
        """

    @POST(API_RULES_CREATE_ENDPOINT)
    def create_rule(
        self,
        custom_key,
        name,
        markdown_description,
        template_key,
        severity,
        status=None,
        type=None,
        params=None,
    ):
        """
        SINCE 4.4
        Create a a custom rule.

        :param custom_key: Key of the custom rule
        :param name: Rule name
        :param markdown_description: Rule description
        :param template_key: Key of the template rule in order to create a custom rule (mandatory for custom rule)
        :param severity: Rule severity.
          Possible values are for:
            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER
        :param status: Rule status.
          Possible values are for:
            * BETA
            * DEPRECATED
            * READY
            * REMOVED
        :param type: Rule type.
          Possible values are for:
            * CODE_SMELL
            * BUG
            * VULNERABILITY
            * SECURITY_HOTSPOT
        :param params: Parameters as semi-colon list of =, for example 'params=key1=v1;key2=v2' (Only for custom rule)

        :return: request response
        """

    @POST(API_RULES_UPDATE_ENDPOINT)
    def update_rule(
        self,
        key,
        name=None,
        markdown_description=None,
        markdown_note=None,
        remediation_fn_base_effort=None,
        remediation_fn_type=None,
        remediation_fy_gap_multiplier=None,
        severity=None,
        status=None,
        tags=None,
    ):
        """
        SINCE 4.4
        Update an existing rule.

        :param key: Key of the rule to update

        :param name: Rule name (mandatory for custom rule)
        :param markdown_description: Rule description (mandatory for custom rule and manual rule)
        :param markdown_note: Optional note in markdown format. Use empty value to remove current note.
          Note is not changed if the parameter is not set.
        :param params: Parameters as semi-colon list of =, for example 'params=key1=v1;key2=v2'
          (Only when updating a custom rule)
        :param remediation_fn_base_effort: Base effort of the remediation function of the rule
        :param remediation_fn_type: Type of the remediation function of the rule
        :param remediation_fy_gap_multiplier: Gap multiplier of the remediation function of the rule
        :param severity: Rule severity (Only when updating a custom rule).Possible values are for:

          * INFO
          * MINOR
          * MAJOR
          * CRITICAL
          * BLOCKER

        :param status: Rule status (Only when updating a custom rule). Possible values are for:

          * BETA
          * DEPRECATED
          * READY
          * REMOVED

        :param tags: Optional comma-separated list of tags to set. Use blank value to remove current tags.
          Tags are not changed if the parameter is not set.

        :return: request response
        """

    @POST(API_RULES_DELETE_ENDPOINT)
    def delete_rule(self, key):
        """
        SINCE 4.4
        Delete custom rule.
        :param key:
        :return:
        """

    @GET(API_RULES_SHOW_ENDPOINT)
    def get_rule(self, key, actives="false"):
        """
        SINCE 4.2
        Get detailed information about a rule.

        :param key: Rule key
        :param actives: Show rule's activations for all profiles ("active rules").
          Possible values are for: true or false. default value is false.
        :return:
        """

    @GET(API_RULES_REPOSITORIES_ENDPOINT)
    def get_rule_repositories(self, language=None, q=None):
        """
        SINCE 4.5
        List available rule repositories

        :param language: A language key; if provided, only repositories for the given language will be returned
        :param q: A pattern to match repository keys/names against
        :return:
        """

    @GET(API_RULES_TAGS_ENDPOINT)
    def get_rule_tags(self, ps=10, q=None):
        """
        SINCE 4.4
        List rule tags

        :param ps: Page size. Must be greater than 0 and less or equal than 100.default value is 10.
        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
