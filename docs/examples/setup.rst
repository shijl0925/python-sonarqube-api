============
Setup
============

setup a sonarqube client::

    from sonarqube import SonarQubeClient
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)


setup sonarcloud client::

    from sonarqube import SonarCloudClient
    sonarcloud_url = "https://sonarcloud.io"
    sonarcloud_token = "*********************"
    sonar = SonarCloudClient(sonarcloud_url=sonarcloud_url, token=sonarcloud_token)

