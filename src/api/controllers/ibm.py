from datetime import datetime
from http import HTTPStatus

import allure
import pytest

import config
import src
from data.dedicated.change_occupation import User
from data.dedicated.services import Service
from src.api.constants.auth import HEADERS, CLIENT_ID, CLIENT_SECRET
from src.api.constants.ibm import IBMServicesRequest, IBMServicesResponse
from src.api.http_client import HTTPClient
from src.api.models.ibm.getsaudicert import GetSaudiCertificateRsBody
from src.api.models.ibm.getworkpermitrequests import IBMWorkPermitRequestList
from src.api.models.ibm.root import IBMResponse, IBMResponseData
from src.api.payloads.ibm.createnewappointment import (
    Body,
    CreateNewAppointmentRq,
    CreateNewAppointmentRqPayload,
    EstablishmentDetails,
    Header,
    RequesterDetails,
    UserInfo,
)
from src.api.payloads.ibm.getestablishmentinformation import (
    EstablishmentInformation,
    GetEstablishmentInformationPayload,
    GetEstablishmentInformationRq,
)
from src.api.payloads.ibm.token import Token
from utils.assertion import assert_status_code


class IBMApiController:
    def __init__(self) -> None:
        self.client = HTTPClient()
        self.url = config.settings.ibm_url
        self.route = "/takamol/staging"

    def _get_token(self):
        payload = Token(
            grant_type="client_credentials",
            scope="IntegrationScope",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        )
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/takamol-oauth/oauth2/token",
            data=payload.dict(),
        )
        response = response.json()
        return f"{response['token_type']} {response['access_token']}"

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
            url=self.url, endpoint=self.route + "/workpermit/getworkpermitrequests", json=payload
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
            url=self.url, endpoint=self.route + "/saudicer/getsaudicert", json=payload
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
            url=self.url, endpoint=self.route + "/saudicer/validestsaudicert", json=payload
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
            url=self.url,
            endpoint=self.route + "/chgoccupation/searchchangeoccupation",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        json_model = IBMResponse[src.api.models.ibm.searchchangeoccupation.Body].parse_obj(
            response.json()
        )
        return json_model[IBMServicesResponse.SEARCH_CHANGE_OCCUPATION]

    @allure.step
    def create_new_appointment(self, user: User, service: Service) -> int:
        header = Header(
            TransactionId="0",
            ChannelId="Qiwa",
            SessionId="0",
            RequestTime="2023-08-03 09:00:00.555",
            ServiceCode="CNA00001",
            DebugFlag="1",
            UserInfo=UserInfo(UserId=user.personal_number, IDNumber=user.personal_number),
        )

        body = Body(
            EstablishmentDetails=EstablishmentDetails(
                LaborOfficeId=user.labor_office_id,
                SequenceNumber=user.sequence_number,
            ),
            OfficeID=user.office_id,
            ClientServiceId=service.client_service_id,
            RequesterDetails=RequesterDetails(
                RequesterIdNo=user.personal_number,
                RequesterName="",
                RequesterUserId=user.personal_number,
            ),
            Time="93",
            Date=datetime.today().strftime("%Y-%m-%d"),
            RegionId="1",
            RequesterTypeId="2",
            SubServiceId=service.sub_service_id,
            VisitReasonId="1",
        )
        payload = CreateNewAppointmentRqPayload(
            CreateNewAppointmentRq=CreateNewAppointmentRq(Header=header, Body=body)
        )
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/qiwalo/createnewappointment",
            headers=HEADERS,
            json=payload.dict(),
        )
        response = response.json()
        try:
            return response["CreateNewAppointmentRs"]["Body"]["AppointmentId"]
        except KeyError:
            pytest.fail(reason=str(response))
        return 0

    @allure.step
    def get_economic_activity_id(self, user: User) -> str:
        header = Header(
            TransactionId="0",
            ChannelId="Qiwa",
            SessionId="0",
            RequestTime="2019-10-10 00:00:00.555",
            ServiceCode="GEI00001",
            DebugFlag="1",
        )
        body = EstablishmentInformation(
            LaborOfficeId=user.labor_office_id,
            EstablishmentSequanceNumber=user.sequence_number,
        )
        payload = GetEstablishmentInformationPayload(
            GetEstablishmentInformationRq=GetEstablishmentInformationRq(Header=header, Body=body)
        )
        response = self.client.post(
            url=self.url,
            endpoint=self.route + "/qiwa/esb/getestablishmentinformation",
            headers=HEADERS,
            json=payload.dict(),
        )
        return response.json()['GetEstablishmentInformationRs']['Body']['EstablishmentDetails']["EconomicActivityId"]

    @allure.step
    def get_first_unrelated_occupation(self, economic_activity_id: str) -> int:
        headers = HEADERS
        headers['Authorization'] = self._get_token()
        response = self.client.get(
            url=self.url,
            endpoint=self.route + f"/qiwa/v2/economic-activity/{economic_activity_id}/occupations",
            headers=headers,
        )
        return response.json()['occupationsList'][0]["descriptionAr"]
