import json

import allure
from requests import Response

from data.constants import HEADERS
from data.employee_transfer import employer, laborer
from utils.schema_parser import load_json_schema
from src.api.assertions.response_validator import ResponseValidator


class EmployeeTransferApi:
    # TODO: Need to update after when project structure will be applied
    def __init__(self, api):
        self.api = api
        self.url_create_new_contract = "https://gw-apic.qiwa.info"
        self.url_prepare_laborer_for_et_request = "http://192.168.168.29:5000"

    def __check_status_response(
        self, response: Response, name: str, expected_status: str = "SUCCESS"
    ):
        response = response.json()["CreateNewContractRs"]["Header"]
        actual_status = response["ResponseStatus"]["Status"]
        assert actual_status == expected_status, (
            f"Request for {name} failed.\n"
            f"Request URL: {response.request.url}\n"
            f"Request body: {response.request.body}\n"
            f"Expected status: {expected_status}\n"
            f"Actual status: {actual_status}\n"
            f"Reason: {response['ResponseStatus']['EnglishMsg']}\n"
        )

    @allure.step("POST create new contract")
    def post_create_new_contract(
        self,
        laborer_id_no: int = laborer.login_id,
        labor_office_id: str = employer.labor_office_id,
        sequence_number: str = employer.establishment_number,
        expect_code=200,
    ):
        json_body = load_json_schema("create_contract.json")
        json_body["CreateNewContractRq"]["Body"]["LaborerDetails"]["LaborerIdNo"] = laborer_id_no
        json_body["CreateNewContractRq"]["Body"]["EstablishmentDetails"][
            "LaborOfficeId"
        ] = labor_office_id
        json_body["CreateNewContractRq"]["Body"]["EstablishmentDetails"][
            "SequenceNumber"
        ] = sequence_number
        response = self.api.post(
            url=self.url_create_new_contract,
            endpoint="/takamol/staging/contractmanagement/createnewcontract",
            body=json.dumps(json_body),
            headers=HEADERS,
        )
        ResponseValidator(response).check_status_code(
            name="Prepare laborer for et request", expect_code=expect_code
        )
        self.__check_status_response(response, name="Prepare laborer for et request")

    @allure.step("POST prepare laborer for et request")
    def post_prepare_laborer_for_et_request(
        self, laborer_id: int = laborer.login_id, expect_code=200
    ):
        params = {"laborerId": laborer_id}
        response = self.api.post(
            url=self.url_prepare_laborer_for_et_request,
            endpoint="/employeeTransfer/prepareLaborerForETrequest",
            params=params,
            headers={},
        )
        ResponseValidator(response).check_status_code(
            name="Prepare laborer for et request", expect_code=expect_code
        )
