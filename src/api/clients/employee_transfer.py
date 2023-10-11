import json

import allure

import config
from data.dedicated.employee_transfer import employer_old, laborer
from src.api.assertions.response_validator import ResponseValidator
from src.api.constants.auth import HEADERS
from src.api.http_client import HTTPClient
from utils.schema_parser import load_json_schema


class EmployeeTransferApi:
    def __init__(self, api=HTTPClient()):
        self.api = api
        self.url = config.settings.ibm_url
        self.url_prepare_laborer_for_et_request = "http://192.168.168.29:5000"

    @allure.step
    def post_create_new_contract(
        self,
        laborer_id_no: int = laborer.login_id,
        labor_office_id: str = employer_old.labor_office_id,
        sequence_number: str = employer_old.establishment_number,
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
            url=self.url,
            endpoint="/takamol/staging/contractmanagement/v2/createnewcontract",
            data=json.dumps(json_body),
            headers=HEADERS,
        )
        ResponseValidator(response).check_status_code(
            name="Create new contract", expect_code=expect_code
        )

    @allure.step
    def post_prepare_laborer_for_et_request(
        self, laborer_id: int = laborer.login_id, expect_code=200
    ):
        payload = {"laborerId": laborer_id}
        response = self.api.post(
            url=self.url_prepare_laborer_for_et_request,
            endpoint="/employeeTransfer/prepareLaborerForETrequest",
            json=payload,
            headers={},
        )
        ResponseValidator(response).check_status_code(
            name="Prepare laborer for et request", expect_code=expect_code
        )
