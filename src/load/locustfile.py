from http import HTTPStatus
from random import randrange

from locust import HttpUser, between, run_single_user, task
from requests import Response

import config
from data.constants import UserInfo
from src.api.clients.mock_api import MockApi
from src.api.payloads import Data, Root
from src.api.payloads.raw.auth import Auth


def establishment_laborers(sequence_number: str, role: str) -> list[str]:
    data_api = MockApi()
    laborers = data_api.get_establishment_laborers(sequence_number)
    return [laborer["laborer_id_no"] for laborer in laborers if laborer["role"] == role]


COMPANY_ID = 701781
SEQUENCE_NUMBER = "2297081"
users = establishment_laborers(sequence_number=SEQUENCE_NUMBER, role="Owner")
employees = establishment_laborers(sequence_number=SEQUENCE_NUMBER, role="Employee")


class QiwaUser(HttpUser):
    wait_time = between(1, 3)
    host = config.settings.api_url
    first_start = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.personal_number = None
        self.pages = len(employees) // 10

    def pass_login(self) -> Response:
        payload = Root(
            data=Data(
                type="login",
                attributes=Auth(login=self.personal_number, password=UserInfo.DEFAULT_PASSWORD),
            )
        )
        return self.client.post(
            "/context", json=payload.dict(exclude_unset=True), catch_response=True
        )

    def pass_otp_code(self) -> Response:
        payload = Root(
            data=Data(
                type="login",
                attributes=Auth(
                    login=self.personal_number, password=UserInfo.DEFAULT_PASSWORD, otp_code="0000"
                ),
            )
        )
        return self.client.post("/context", json=payload.dict(), catch_response=True)

    def select_company(self) -> Response:
        return self.client.patch(f"/context/company/{COMPANY_ID}", catch_response=True)

    def logout(self) -> Response:
        return self.client.delete("/context", catch_response=True)

    def on_start(self) -> None:
        self.personal_number = users.pop()
        login = self.pass_login()
        if login.status_code == HTTPStatus.OK:
            otp = self.pass_otp_code()
            if otp.status_code == HTTPStatus.CREATED:
                company = self.select_company()
                if company.status_code == HTTPStatus.OK:
                    return
        self.stop()

    def on_stop(self) -> None:
        self.logout()
        users.append(self.personal_number)

    @task
    def get_work_permit_employees(self) -> None:
        page = 1 if self.first_start else randrange(1, self.pages)
        self.client.get(
            "/working-permit-request/employees",
            params={"page": page, "per": 10},
            name="/working-permit-request/employees",
        )
        self.first_start = False


if __name__ == "__main__":
    run_single_user(QiwaUser)
