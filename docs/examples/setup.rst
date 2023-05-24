============
Setup
============

Setup a SonarQube Client::

    from sonarqube import SonarQubeClient
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)


