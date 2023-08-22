import allure
from requests import Response

import config
from src.api.http_client import HTTPClient


class SaudizationCertificateApi:
    url = config.settings.api_url
    route = "/saudization-certificate"

    def __init__(self, client: HTTPClient):
        self.client = client

    @allure.step
    def create_certificate(self) -> Response:
        return self.client.post(self.url, self.route)

    @allure.step
    def get_certificate_details(self) -> Response:
        return self.client.get(self.url, f"{self.route}/details")

    @allure.step
    def extend_certificate(self) -> Response:
        return self.client.post(self.url, f"{self.route}/extend")
