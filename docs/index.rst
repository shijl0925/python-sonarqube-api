.. SonarQube Client with Python documentation master file, created by
   sphinx-quickstart on Mon May 22 22:11:45 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SonarQube Client with Python's documentation!
========================================================

python-sonarqube-api provides a simple interface for clients to interact with SonarQube via the REST API.


Compatibility
=============

* This package is compatible Python versions 2.7, 3.3+.
* Tested with SonarQube Community Edition 8.9.x LTS and SonarCloud Server.

Editions
========

There are two editions of python-sonarqube-api:

 * Community Edition (CE) is available freely under the GNU Affero General Public License v3.0.
 * Professional Edition (PE) includes [extra features](https://python-sonarqube-pro-api.readthedocs.io/en/latest/#api-reference)
   that are more useful for developers with more than 280 interface functions. To use PE and get timely Email support and continuous updates,
   please become a Purchaser(https://shijl0925.gumroad.com/l/nlokc) and become a subscriber(https://shijl0925.gumroad.com/subscribe).

+---------------------+---------------------+-----------------------+
| Differences         | Community Edition   | Professional Edition  |
+=====================+=====================+=======================+
| License             | GNU AGPLv3 License  | MIT License           |
+---------------------+---------------------+-----------------------+
| Commercial Use      | No                  | Yes                   |
+---------------------+---------------------+-----------------------+
| Supported APIs      | 40                  | more than 280         |
| (SonarQube Web APIs)|                     |                       |
+---------------------+---------------------+-----------------------+
| Compatibility       | 7.9.x - 8.9.x       | 7.9.x - 10.x          |
| (SonarQube Versions)|                     |                       |
+---------------------+---------------------+-----------------------+


Installation
============

Community Edition
-----------------
Use :command:`pip` to install the latest stable version of ``python-sonarqube-api``:

.. code-block:: console

   $ pip install --upgrade python-sonarqube-api

The current development version is available on `github
<https://github.com/shijl0925/python-sonarqube-api>`__. Use :command:`git` and
:command:`python setup.py` to install it:

.. code-block:: console

   $ git clone https://github.com/shijl0925/python-sonarqube-api.git
   $ cd python-sonarqube-api
   $ python setup.py install


Professional Edition
--------------------
Use :command:`pip` to install the Python wheel or source package, Use --force-reinstall to force an installation If necessary:

.. code-block:: console

   $ pip install python_sonarqube_pro_api-x.y.z-py3-none-any.whl


Documentation
=============

This part of the documentation will show you how to get started in using python-sonarqube-api.

The Client is easy to use, you just need to initialize it with the
connection parameters (default sonarqube url is http://localhost:9000).

Setup a SonarQube Client
------------------------
.. code-block:: python

    from sonarqube import SonarQubeClient

    sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')


Sonar authentication tokens can also be used in place of username and password:

.. code-block:: python

    sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", token='*****************')


Example
-------
Refer to the example script for a full working example.

.. toctree::
   :maxdepth: 2

   examples

API Reference
-------------

If you are looking for information on a specific function, class or
method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   sonarqube.rest


Additional Notes
----------------
If you find that the interface in the this Python library does not meet your requirements or is missing,
you can use `request_get` and `request_post` to extend your code. (Only for Professional Edition)

for example:

.. code-block:: python

    from sonarqube import SonarQubeClient
    sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", username='admin', password='admin')

    # Get Request
    res = sonar.request_get(endpoint="/api/components/search", params={"qualifiers": "TRK"})

    # Post Request
    res = sonar.request_post(endpoint="/api/users/deactivate", data={"login": "login"})


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
