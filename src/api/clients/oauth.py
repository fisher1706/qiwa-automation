from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads import Data, Root
from src.api.payloads.sso.oauth import OauthInit


class OAuthApi:
    url = config.qiwa_urls.api
    route = "/oauth"

    def __init__(self, client: HTTPClient):
        self.client = client

    def init(self) -> Response:
        payload = Root(data=Data(type="oauth-init", attributes=OauthInit(state={})))
        return self.client.post(
            self.url, f"{self.route}/init", json=payload.dict(exclude_unset=True)
        )

    def callback(self, state: str, auth_code: str) -> Response:
        payload = Root(
            data=Data(type="oauth-callback", attributes=OauthInit(state=state, code=auth_code))
        )
        return self.client.post(
            self.url, f"{self.route}/callback", json=payload.dict(exclude_unset=True)
        )
