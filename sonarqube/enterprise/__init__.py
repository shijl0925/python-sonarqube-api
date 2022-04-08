from sonarqube.community import SonarQubeClient
from sonarqube.enterprise.applications import SonarQubeApplications
from sonarqube.enterprise.audit_logs import SonarQubeAuditLogs
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
    def audit_logs(self):
        return SonarQubeAuditLogs(api=self)

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
