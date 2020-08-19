=======================
Python SonarQube Client
=======================

A Python Client for SonarQube Server APIs.

Installation
============

Install::

    pip install python-sonarqube-api

Compatibility
-------------

* This package is compatible Python versions 2.7, 3.4, 3.5 and 3.6.
* Tested with SonarQube v7.9

Usage
=====

The Client is easy to use, you just need to initialize it with the
connection parameters (default sonarqube url is http://localhost:9000).

Example getting projects with coverage and issues metrics::

    from sonarqube import SonarQubeClient

    h = SonarQubeClient(user='admin', password='admin')
    for project in h.projects:
        # do something with project data...

Since the actual response data from SonarQube server is usually paged, all
methods return generators to optimize memory as well retrieval performance of
the first items.

Sonar authentication tokens can also be used in place of username and password,
which is particularly useful when accessing the SonarQube API from a CI server,
as tokens can easily be revoked in the event of unintended exposure::

    h = SonarQubeClient(token='*****************')


