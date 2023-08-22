from requests import Response

from src.api import payloads
from src.api.clients.e_service.e_service_api import EServiceApi
from src.api.http_client import HTTPClient
from src.api.payloads.e_service.groups import EService, Group


class EServiceApiController:
    def __init__(self, client: HTTPClient):
        self.api = EServiceApi(client)

    def create_e_service_group(self, payload: Group) -> Response:
        create_group_payload = payloads.data.group(payload)
        return self.api.groups.create_group(create_group_payload.dict(by_alias=True))

    def create_group_for_e_services(self, *services: EService) -> Response:
        payload = Group(e_services=list(services))
        return self.create_e_service_group(payload)

    def update_e_service_group(self, group_id: str, payload: Group) -> Response:
        update_group_payload = payloads.data.group(payload)
        return self.api.groups.group(group_id).update(update_group_payload.dict(by_alias=True))
