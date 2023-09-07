from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.delegation import get_all_delegations_request


class DelegationAPI:
    url = config.qiwa_urls.delegation_service_api
    route = "/proxy/delegations/find/all"

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_delegations(self) -> Response:
        token = self.client.session.cookies.get("qiwa.authorization")
        headers = {"Cookie": f"qiwa.authorization={token}", "X-Service-Id": "delegation"}
        return self.client.post(
            url=self.url,
            endpoint=self.route,
            json=get_all_delegations_request(),
            headers=headers,
        )
