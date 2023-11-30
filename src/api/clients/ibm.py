from http import HTTPStatus

import pytest

import config
from data.dedicated.enums import TransferType
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.services import Service
from data.dedicated.models.user import User
from src.api.constants.auth import HEADERS
from src.api.http_client import HTTPClient
from src.api.payloads.appointment import appointment_payload
from src.api.payloads.contract_details import contract_details_payload
from src.api.payloads.employee_transfer_request import employee_transfer_request_payload
from src.api.payloads.establishment_information import establishment_information_payload
from utils.allure import allure_steps
from utils.assertion import assert_status_code


@allure_steps
class IbmApi:
    def __init__(self):
        self.client = HTTPClient()
        self.url = config.settings.ibm_url
        self.route = "/takamol/staging"

    def create_new_appointment(self, user: User, service: Service) -> dict:
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/qiwalo/createnewappointment",
            headers=HEADERS,
            json=appointment_payload(user, service),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    def get_establishment_information(self, user: User) -> dict:
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/qiwa/esb/getestablishmentinformation",
            headers=HEADERS,
            json=establishment_information_payload(user),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    def create_new_contract(self, laborer: Laborer, employer: User):
        response = self.client.post(
            url=self.url,
            endpoint="/takamol/staging/contractmanagement/createnewcontract",
            json=contract_details_payload(laborer, employer),
            headers=HEADERS,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def create_employee_transfer_request(
        self, user: User, laborer: Laborer, transfer_type: TransferType
    ):
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/changesponsor/submitchangesponsorrequest",
            headers=HEADERS,
            json=employee_transfer_request_payload(user, laborer, transfer_type),
        )
        response = response.json()["SubmitChangeSponsorRequestRs"]["Header"]["ResponseStatus"]
        if response["Status"] == "ERROR":
            pytest.fail(reason=response["EnglishMsg"])


ibm_api = IbmApi()
