from sonarqube import SonarQubeClient
from sonarqube.enterprise.alm_integrations import SonarAlmIntegrations
from sonarqube.enterprise.alm_settings import SonarAlmSettings
from sonarqube.enterprise.applications import SonarApplications
from sonarqube.enterprise.editions import SonarEditions
from sonarqube.enterprise.views import SonarViews


class SonarEnterpriseClient(SonarQubeClient):
    """
    A Python Client for SonarQube Enterprise Server APIs.
    """

    @property
    def alm_integrations(self):
        """
        ALM Integrations
        """
        return SonarAlmIntegrations(api=self)

    @property
    def alm_settings(self):
        """
        ALM settings
        """
        return SonarAlmSettings(api=self)

    @property
    def applications(self):
        """
        Manage Applications
        """
        return SonarApplications(api=self)

    @property
    def editions(self):
        """
        Manage SonarSource commercial editions
        """
        return SonarEditions(api=self)

    @property
    def views(self):
        """
        Manage Portfolios
        """
        return SonarViews(api=self)