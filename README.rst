====================
Python SonarQube API
====================

API Handler for SonarQube web service, providing basic authentication (which
seems to be the only kind that SonarQube supports) and a few methods.

Installation
============

Install::

    pip install python-sonarqube-api

Compatibility
-------------

This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.


Usage
=====

The API handler is easy to use, you just need to initialize it with the
connection parameters (by default *localhost* on port *9000* without
authentication) and use any of the methods to get the required information or
create rules.

Example getting projects with coverage and issues metrics::

    from sonarqube.base_api import SonarAPIHandler

    h = SonarAPIHandler(user='admin', password='admin')
    for project in h.projects:
        # do something with project data...

Since the actual response data from SonarQube server is usually paged, all
methods return generators to optimize memory as well retrieval performance of
the first items.

Sonar authentication tokens can also be used in place of username and password,
which is particularly useful when accessing the SonarQube API from a CI server,
as tokens can easily be revoked in the event of unintended exposure::

    h = SonarAPIHandler(token='f052f55b127bb06f63c31cb2064ea301048d9e5d')


