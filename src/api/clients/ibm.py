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
from src.api.payloads.cancelchgoccrequest import (
    cancel_change_occupation_request_payload,
)
from src.api.payloads.change_occupation_laborers_list import (
    change_occupation_laborers_list_payload,
)
from src.api.payloads.contract_details import contract_details_payload
from src.api.payloads.employee_transfer_request_ae import (
    employee_transfer_request_ae_payload,
)
from src.api.payloads.employee_transfer_request_bme import (
    employee_transfer_request_bme_payload,
)
from src.api.payloads.establishment_information import establishment_information_payload
from src.api.payloads.laborers_co_requests import laborers_co_requests_payload
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

    def create_new_contract(self, user: User, laborer: Laborer) -> None:
        response = self.client.post(
            url=self.url,
            endpoint="/takamol/staging/contractmanagement/createnewcontract",
            json=contract_details_payload(laborer, user),
            headers=HEADERS,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    def get_change_occupation_laborers_list(self, user: User) -> dict:
        return self.client.post(
            url=self.url,
            endpoint=self.route + "/chgoccupation/getchangeoccupationlaborerslist",
            headers=HEADERS,
            json=change_occupation_laborers_list_payload(user),
        ).json()

    def create_employee_transfer_request_bme(
        self, user: User, laborer: Laborer, transfer_type: TransferType
    ) -> None:
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/changesponsor/submitchangesponsorrequest",
            headers=HEADERS,
            json=employee_transfer_request_bme_payload(user, laborer, transfer_type),
        )
        response = response.json()["SubmitChangeSponsorRequestRs"]["Header"]["ResponseStatus"]
        if response["Status"].lower() == "error":
            pytest.fail(reason=response["EnglishMsg"])

    def create_employee_transfer_request_ae(
        self, user: User, laborer: Laborer, sponsor: User = None
    ) -> None:
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/changesponsor/submitcsrequests",
            headers=HEADERS,
            json=employee_transfer_request_ae_payload(user, laborer, sponsor),
        )
        response = response.json()["SubmitCSRequestRs"]["Header"]["ResponseStatus"]
        if response["Status"].lower() == "error":
            pytest.fail(reason=response["EnglishMsg"])

    def get_laborers_co_requests(self, user: User, status_id: int) -> dict:
        return self.client.post(
            url=self.url,
            endpoint=self.route + "/chgoccupation/getlaborerscorequests",
            headers=HEADERS,
            json=laborers_co_requests_payload(user, status_id),
        ).json()

    def cancel_change_occupation_request(self, request_number: str) -> None:
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/qiwalo/cancelchgoccrequestlo",
            headers=HEADERS,
            json=cancel_change_occupation_request_payload(request_number),
        )
        response = response.json()["CancelChangeOccupationRequestLORs"]["Header"]["ResponseStatus"]
        if response["Status"].lower() == "error":
            print(response["EnglishMsg"])


ibm_api = IbmApi()
