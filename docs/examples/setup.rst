============
Setup
============

setup a sonarqube client::

    from sonarqube import SonarQubeClient
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)
