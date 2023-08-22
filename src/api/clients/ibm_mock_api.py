from http import HTTPStatus

import allure

import config
from src.api.constants.ibm import IBMServicesRequest, IBMServicesResponse
from src.api.http_client import HTTPClient
from src.api.models.ibm.getsaudicert import GetSaudiCertificateRsBody
from src.api.models.ibm.getworkpermitrequests import IBMWorkPermitRequestList
from src.api.models.ibm.root import IBMResponse, IBMResponseData
from src.api.payloads.ibm.searchchangeoccupation import Body
from utils.assertion import assert_status_code


class IBMMockApi:
    client = HTTPClient()
    url = config.settings.mock_mlsd_url

    @allure.step
    def get_work_permit_requests_from_ibm(
        self, body: src.api.models.ibm.payloads.GetWorkPermitRequestsRq
    ) -> IBMWorkPermitRequestList:
        payload = {
            IBMServicesRequest.GET_WORK_PERMIT_REQUESTS.value: {
                "Body": body.dict(exclude_none=True, by_alias=True),
            }
        }
        response = self.client.post(
            self.url, "/takamol/staging/workpermit/getworkpermitrequests", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        json_model = IBMResponse[IBMWorkPermitRequestList].parse_obj(response.json())
        return json_model[IBMServicesResponse.GET_WORK_PERMIT_REQUESTS].Body

    @allure.step
    def get_saudization_certificate_from_ibm(
        self, body: src.api.models.ibm.payloads.GetSaudiCertificateRq
    ) -> IBMResponseData[GetSaudiCertificateRsBody]:
        payload = {
            IBMServicesRequest.GET_SAUDI_CERTIFICATE.value: {
                "Body": body.dict(exclude_none=True, by_alias=True)
            }
        }
        response = self.client.post(
            self.url, "/takamol/staging/saudicer/getsaudicert", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        json_model = IBMResponse[GetSaudiCertificateRsBody].parse_obj(response.json())
        return json_model[IBMServicesResponse.GET_SAUDI_CERTIFICATE]

    @allure.step
    def validate_establishment_saudization_in_ibm(
        self, body: src.api.models.ibm.payloads.ValidEstSaudiCertificateRq
    ) -> IBMResponseData:
        payload = {
            IBMServicesRequest.VALIDATE_EST_SAUDI_CERTIFICATE.value: {
                "Body": body.dict(exclude_none=True, by_alias=True)
            }
        }
        response = self.client.post(
            self.url, "/takamol/staging/saudicer/validestsaudicert", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        json_model = IBMResponse.parse_obj(response.json())
        return json_model[IBMServicesResponse.VALIDATE_EST_SAUDI_CERTIFICATE]

    @allure.step
    def get_change_occupation_requests_from_ibm(
        self, body: Body
    ) -> IBMResponseData[src.api.models.ibm.searchchangeoccupation.Body]:
        payload = {
            IBMServicesRequest.SEARCH_CHANGE_OCCUPATION.value: {
                "Body": body.dict(exclude_none=True)
            }
        }
        response = self.client.post(
            self.url, "/takamol/staging/chgoccupation/searchchangeoccupation", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        json_model = IBMResponse[src.api.models.ibm.searchchangeoccupation.Body].parse_obj(
            response.json()
        )
        return json_model[IBMServicesResponse.SEARCH_CHANGE_OCCUPATION]
