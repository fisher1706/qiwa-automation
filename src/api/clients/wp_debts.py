from requests import Response

import config
from src.api.http_client import HTTPClient


class WPDebtsApi:
    url = config.settings.api_url
    route = "/wp-debts"

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_info(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(self.url, f"{self.route}/info", params={"page": page, "per": per})
