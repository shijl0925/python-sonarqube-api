
.. image:: https://img.shields.io/pypi/pyversions/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://img.shields.io/pypi/v/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://pepy.tech/badge/python-sonarqube-api/month
    :target: https://pepy.tech/project/python-sonarqube-api/month
.. image:: https://sonarcloud.io/api/project_badges/measure?project=shijl0925_python-sonarqube-api&metric=alert_status
    :target: https://sonarcloud.io/dashboard?id=shijl0925_python-sonarqube-api
.. image:: https://img.shields.io/github/license/shijl0925/python-sonarqube-api.svg
    :target: LICENSE

=======================
Python SonarQube Client
=======================

A Python Client for SonarQube Server APIs.

Installation
============

Install::

    pip install  --upgrade python-sonarqube-api

Documentation
=============

The full documentation for API is available on `readthedocs
<https://python-sonarqube-api.readthedocs.io/en/1.1.0/>`_.


Compatibility
=============

* This package is compatible Python versions 2.7, 3.3+.
* Tested with SonarQube v7.9.x Community Edition

Usage
=====

The Client is easy to use, you just need to initialize it with the
connection parameters (default sonarqube url is http://localhost:9000).

Example getting projects with coverage and issues metrics::

    from sonarqube import SonarQubeClient

    h = SonarQubeClient(sonarqube_url="http://localhost:9000", user='admin', password='admin')
    for project in h.projects:
        # do something with project data...

Since the actual response data from SonarQube server is usually paged, all
methods return generators to optimize memory as well retrieval performance of
the first items.

Sonar authentication tokens can also be used in place of username and password,
which is particularly useful when accessing the SonarQube API from a CI server,
as tokens can easily be revoked in the event of unintended exposure::

    h = SonarQubeClient(sonarqube_url="http://localhost:9000", token='*****************')


API example
-----------

The API example supported by the SonarQubeClient are:
The example documentation for API is available on `API examples
<https://python-sonarqube-api.readthedocs.io/en/1.1.0/examples.html>`_.

