#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_SYSTEM_CHANGE_LOG_LEVEL_ENDPOINT,
    API_SYSTEM_DB_MIGRATION_STATUS_ENDPOINT,
    API_SYSTEM_HEALTH_ENDPOINT,
    API_SYSTEM_LOGS_ENDPOINT,
    API_SYSTEM_MIGRATE_DB_ENDPOINT,
    API_SYSTEM_PING_ENDPOINT,
    API_SYSTEM_RESTART_ENDPOINT,
    API_SYSTEM_STATUS_ENDPOINT,
    API_SYSTEM_UPGRADES_ENDPOINT,
    API_SYSTEM_INFO_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeSystem(RestClient):
    """
    SonarQube system Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeSystem, self).__init__(**kwargs)

    @POST(API_SYSTEM_CHANGE_LOG_LEVEL_ENDPOINT)
    def change_log_level(self, level):
        """
        SINCE 5.2
        Temporarily changes level of logs. New level is not persistent and is lost when restarting server.

        :param level: The new level. Be cautious: DEBUG, and even more TRACE, may have performance impacts.
          Possible values are: TRACE, DEBUG, INFO.
        :return:
        """

    @POST(API_SYSTEM_DB_MIGRATION_STATUS_ENDPOINT)
    def get_database_migration_status(self):
        """
        SINCE 5.2
        Display the database migration status of SonarQube.
        State values are:
          * NO_MIGRATION: DB is up to date with current version of SonarQube.
          * NOT_SUPPORTED: Migration is not supported on embedded databases.
          * MIGRATION_RUNNING: DB migration is under go.
          * MIGRATION_SUCCEEDED: DB migration has run and has been successful.
          * MIGRATION_FAILED: DB migration has run and failed. SonarQube must be restarted in order to retry a DB
            migration (optionally after DB has been restored from backup).
          * MIGRATION_REQUIRED: DB migration is required.

        :return:
        """

    @POST(API_SYSTEM_HEALTH_ENDPOINT)
    def get_health_status(self):
        """
        SINCE 6.6
        Provide health status of SonarQube.
        State values are:
          * GREEN: SonarQube is fully operational
          * YELLOW: SonarQube is usable, but it needs attention in order to be fully operational
          * RED: SonarQube is not operational

        :return:
        """

    @GET(API_SYSTEM_LOGS_ENDPOINT)
    def get_logs(self, process="app"):
        """
        SINCE 5.2
        Get system logs in plain-text format.

        :param process: Process to get logs from. Possible values are: app, ce, es, web. default value is app.
        :return:
        """

    @POST(API_SYSTEM_MIGRATE_DB_ENDPOINT)
    def migrate_database(self):
        """
        SINCE 5.2
        Migrate the database to match the current version of SonarQube.
        Sending a POST request to this URL starts the DB migration. It is strongly advised to make a database backup
        before invoking this WS.
        State values are:
          * NO_MIGRATION: DB is up to date with current version of SonarQube.
          * NOT_SUPPORTED: Migration is not supported on embedded databases.
          * MIGRATION_RUNNING: DB migration is under go.
          * MIGRATION_SUCCEEDED: DB migration has run and has been successful.
          * MIGRATION_FAILED: DB migration has run and failed. SonarQube must be restarted in order to retry a DB
            migration (optionally after DB has been restored from backup).
          * MIGRATION_REQUIRED: DB migration is required.

        :return: request response
        """

    @GET(API_SYSTEM_PING_ENDPOINT)
    def ping_server(self):
        """
        SINCE 6.3
        Answers "pong" as plain-text

        :return:
        """

    @POST(API_SYSTEM_RESTART_ENDPOINT)
    def restart_server(self):
        """
        SINCE 4.3
        Restart server.

        :return:
        """

    @GET(API_SYSTEM_STATUS_ENDPOINT)
    def get_server_state(self):
        """
        SINCE 5.2
        Get state information about SonarQube.
        status: the running status
          * STARTING: SonarQube Web Server is up and serving some Web Services (eg. api/system/status) but
            initialization is still ongoing
          * UP: SonarQube instance is up and running
          * DOWN: SonarQube instance is up but not running because migration has failed
           (refer to WS /api/system/migrate_db for details) or some other reason (check logs).
          * RESTARTING: SonarQube instance is still up but a restart has been requested
            (refer to WS /api/system/restart for details).
          * DB_MIGRATION_NEEDED: database migration is required. DB migration can be started using WS
            /api/system/migrate_db.
          * DB_MIGRATION_RUNNING: DB migration is running (refer to WS /api/system/migrate_db for details)

        :return:
        """

    @GET(API_SYSTEM_UPGRADES_ENDPOINT)
    def get_available_upgrades(self):
        """
        SINCE 5.2
        Lists available upgrades for the SonarQube instance (if any) and for each one, lists incompatible plugins
        and plugins requiring upgrade.Plugin information is retrieved from Update Center. Date and time at which Update
        Center was last refreshed is provided in the response.

        :return:
        """

    @GET(API_SYSTEM_INFO_ENDPOINT)
    def get_detailed_information(self):
        """
        SINCE 5.1
        Get detailed information about system configuration.

        :return:
        """