from __future__ import annotations

from requests import Response

import config
from src.api.http_client import HTTPClient


class GroupsApi:
    url = config.qiwa_urls.api
    route = "/admin/groups"

    def __init__(self, client: HTTPClient):
        self.client = client

    @property
    def as_user(self) -> GroupsApi:
        self.route = "/groups"
        return self

    def create_group(self, payload: dict) -> Response:
        return self.client.post(self.url, self.route, json=payload)

    def get_groups(self) -> Response:
        return self.client.get(self.url, self.route)

    class GroupById:
        def __init__(self, client: HTTPClient, url: str):
            self.client = client
            self.url = url

        def find(self) -> Response:
            return self.client.get(self.url, "")

        def update(self, payload: dict) -> Response:
            return self.client.put(self.url, "", json=payload)

        def delete(self) -> Response:
            return self.client.delete(self.url, "")

    def group(self, group_id: str) -> GroupById:
        return self.GroupById(self.client, f"{self.url}{self.route}/{group_id}")
