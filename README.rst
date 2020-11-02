
.. image:: https://img.shields.io/pypi/pyversions/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://img.shields.io/pypi/v/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://pepy.tech/badge/python-sonarqube-api
    :target: https://pepy.tech/project/python-sonarqube-api
.. image:: https://sonarcloud.io/api/project_badges/measure?project=shijl0925_python-sonarqube-api&metric=alert_status
    :target: https://sonarcloud.io/dashboard?id=shijl0925_python-sonarqube-api
.. image:: https://img.shields.io/github/license/shijl0925/python-sonarqube-api.svg
    :target: LICENSE
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


====================================================
Python wrapper for the SonarQube and SonarCloud API.
====================================================

Installation
============

The easiest way to install the latest version is by using pip to pull it from PyPI::

    pip install  --upgrade python-sonarqube-api

You may also use Git to clone the repository from Github and install it manually::

    git clone https://github.com/shijl0925/python-sonarqube-api.git
    cd python-sonarqube-api
    python setup.py install


Documentation
=============

The full documentation for API is available on `readthedocs
<https://python-sonarqube-api.readthedocs.io/en/1.1.7/>`_.


Compatibility
=============

* This package is compatible Python versions 2.7, 3.3+.
* Tested with SonarQube Community Edition 7.9.x LTS and SonarCloud Server.

Usage
=====

For SonarQube Community Edition
-------------------------------

The Client is easy to use, you just need to initialize it with the
connection parameters (default sonarqube url is http://localhost:9000).

Example::

    from sonarqube import SonarQubeClient

    h = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')


Sonar authentication tokens can also be used in place of username and password::

    h = SonarQubeClient(sonarqube_url="http://localhost:9000", token='*****************')


For SonarCloud
--------------

Example::

    from sonarqube import SonarCloudClient
    h = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token='*****************')


API example
-----------

The example documentation for SonarQubeClient APIs is available on `API examples
<https://python-sonarqube-api.readthedocs.io/en/1.1.7/examples.html>`_.

