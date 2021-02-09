from sonarqube import SonarQubeClient
from sonarqube.enterprise.applications import SonarQubeApplications
from sonarqube.enterprise.alm_integrations import SonarQubeAlmIntegrations
from sonarqube.enterprise.alm_settings import SonarQubeAlmSettings
from sonarqube.enterprise.editions import SonarQubeEditions
from sonarqube.enterprise.views import SonarQubeViews


class SonarEnterpriseClient(SonarQubeClient):
    """
    A Python Client for SonarQube Enterprise Server APIs.
    """
    @property
    def applications(self):
        """
        SonarQube applications Operations

        :return:
        """
        return SonarQubeApplications(api=self)

    @property
    def alm_integrations(self):
        """
        ALM Integrations
        """
        return SonarQubeAlmIntegrations(api=self)

    @property
    def alm_settings(self):
        """
        ALM settings
        """
        return SonarQubeAlmSettings(api=self)

    @property
    def editions(self):
        """
        Manage SonarSource commercial editions
        """
        return SonarQubeEditions(api=self)

    @property
    def views(self):
        """
        Manage Portfolios
        """
        return SonarQubeViews(api=self)
