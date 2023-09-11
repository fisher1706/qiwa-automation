import allure
import jmespath

import config
from data.constants import HEADERS
from data.dedicated.enums import VisitStatus
from src.api.http_client import HTTPClient
from src.api.requests.visit import Visit


class VisitsApiController:
    def __init__(self, client: HTTPClient):
        self.client = client
        self.url = config.qiwa_urls.api
        self.route = "/labor-offices/appointment"

    @allure.step
    def get_active_appointment_id(self, user_id) -> int:
        response = self.client.get(url=self.url, endpoint=self.route, params="q[status-id][eq]=1")
        active_appointment_id = jmespath.search(
            f"data[?attributes.\"status-name-en\"=='Active' && "
            f"attributes.\"requester-personal-number\"=='{user_id}'].id",
            response.json(),
        )
        return active_appointment_id[0] if active_appointment_id else 0

    @allure.step
    def cancel_appointment(self, appointment_id):
        json_body = Visit.delete_visit_body(appointment_id)
        self.client.delete(url=self.url, endpoint=self.route, headers=HEADERS, json=json_body)

    @allure.step
    def get_appointment_info(self, appointment_id):
        return self.client.get(
            url=self.url, endpoint=self.route + f"/{appointment_id}", headers=HEADERS
        )

    @allure.step
    def cancel_active_visit(self, user_id) -> None:
        active_appointment_id = self.get_active_appointment_id(user_id)
        if active_appointment_id:
            self.cancel_appointment(active_appointment_id)
            appointment_options = self.get_appointment_info(active_appointment_id)
            assert (
                appointment_options.json()["data"]["attributes"]["status-name-en"]
                == VisitStatus.CANCELED
            )
