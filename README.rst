
.. image:: https://img.shields.io/pypi/pyversions/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://img.shields.io/pypi/v/python-sonarqube-api.svg
    :target: https://pypi.python.org/pypi/python-sonarqube-api
.. image:: https://pepy.tech/badge/python-sonarqube-api
    :target: https://pepy.tech/project/python-sonarqube-api
.. image:: https://static.pepy.tech/badge/python-sonarqube-api/month
    :target: https://pepy.tech/project/python-sonarqube-api
.. image:: https://sonarcloud.io/api/project_badges/measure?project=shijl0925_python-sonarqube-api&metric=alert_status
    :target: https://sonarcloud.io/dashboard?id=shijl0925_python-sonarqube-api
.. image:: https://img.shields.io/github/license/shijl0925/python-sonarqube-api.svg
    :target: LICENSE
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


==========================================================================================================================================
Python Client library for interacting with Community, Developer, and Enterprise Editions SonarQube's REST APIs and SonarCloud's REST APIs.
==========================================================================================================================================

python-sonarqube-api provides a simple interface for clients to interact with SonarQube via the REST API.

Editions
========

There are two editions of python-sonarqube-api:

 * Community Edition (CE) is available freely under the GNU Affero General Public License v3.0.
 * Professional Edition (PE) includes `extra features <https://python-sonarqube-pro-api.readthedocs.io/en/latest/#api-reference>`_
   that are more useful for developers with more than 280 interface functions. To use PE and get timely Email support and continuous updates,
   please become a Purchaser(https://shijl0925.gumroad.com/l/nlokc) and become a subscriber(https://shijl0925.gumroad.com/subscribe).

+---------------------+---------------------+-----------------------+
| Differences         | Community Edition   | Professional Edition  |
+=====================+=====================+=======================+
| License             | GNU AGPLv3 License  | MIT License           |
+---------------------+---------------------+-----------------------+
| Commercial Use      | No                  | Yes                   |
+---------------------+---------------------+-----------------------+
| Functions           | 60                  | more than 280         |
| (REST APIs)         |                     |                       |
+---------------------+---------------------+-----------------------+
| Compatibility       | 7.9.x - 8.9.x       | 7.9.x - 10.x          |
| (SonarQube Versions)|                     |                       |
+---------------------+---------------------+-----------------------+

Installation
============

Community Edition
-----------------

The easiest way to install the latest version is by using pip to pull it from PyPI::

    pip install  --upgrade python-sonarqube-api

You may also use Git to clone the repository from Github and install it manually::

    git clone https://github.com/shijl0925/python-sonarqube-api.git
    cd python-sonarqube-api
    python setup.py install


Professional Edition
--------------------
Use command pip to install the Python wheel or source package, Use --force-reinstall to force an installation If necessary::

    pip install python_sonarqube_pro_api-x.y.z-py3-none-any.whl


Documentation
=============

The full documentation for API is available on `readthedocs
<https://python-sonarqube-pro-api.readthedocs.io/en/latest/>`_.


Compatibility
=============

* This package is compatible Python versions 2.7, 3.3+.
* Tested with SonarQube Community Edition 8.9.x LTS and SonarCloud Server.

Donate
======

donations are not mandatory but very welcomed
If you like my work and want to support development or buy me a coffee `PayPal Donate <https://paypal.me/shijialiang0925>`_

Usage
=====

The Client is easy to use, you just need to initialize it with the
connection parameters (default sonarqube url is http://localhost:9000).

Example::

    from sonarqube import SonarQubeClient

    sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')


Sonar authentication tokens can also be used in place of username and password::

    sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", token='*****************')


API example
-----------

The example documentation for SonarQubeClient APIs is available on `API examples
<https://python-sonarqube-pro-api.readthedocs.io/en/latest/examples.html>`_.


Licensing
-----------
See the `LICENSE <https://github.com/shijl0925/python-sonarqube-api/blob/master/LICENSE>`_ file for licensing information as it pertains to files in this repository.
