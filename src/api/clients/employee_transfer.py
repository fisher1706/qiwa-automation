import allure

import config
from data.dedicated.employee_trasfer.employee_transfer_users import laborer
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient


class EmployeeTransferApi:
    def __init__(self, client=HTTPClient()):
        self.client = client
        self.url = config.settings.ibm_url
        self.url_prepare_laborer_for_et_request = "http://192.168.168.29:5000"

    @allure.step
    def post_prepare_laborer_for_et_request(self, laborer_id: int = laborer.personal_number):
        response = self.client.post(
            url=self.url_prepare_laborer_for_et_request,
            endpoint="/employeeTransfer/prepareLaborerForETrequest",
            json={"laborerId": laborer_id},
            headers={},
        )
        ResponseValidator(response).check_status_code(
            name="Prepare laborer for et request", expect_code=200
        )


employee_transfer_api = EmployeeTransferApi()
