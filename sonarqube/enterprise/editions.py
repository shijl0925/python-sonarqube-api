from sonarqube.utils.common import POST
from sonarqube.utils.rest_client import RestClient


class SonarEditions(RestClient):
    """
    Manage SonarSource commercial editions
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarEditions, self).__init__(**kwargs)

    @POST("api/editions/set_license")
    def set_license(self, license):
        """
        POST api/editions/set_license
        since 7.2
        Set the license for enabling features of commercial editions. Require 'Administer System' permission.

        Parameters

        license
        required
        """
