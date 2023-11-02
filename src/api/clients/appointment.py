from datetime import datetime
from http import HTTPStatus

import allure

import config
from data.dedicated.models.services import Service
from data.dedicated.models.user import User
from src.api.constants.auth import HEADERS
from src.api.http_client import HTTPClient
from src.api.payloads.ibm.createnewappointment import (
    Body,
    CreateNewAppointmentRq,
    CreateNewAppointmentRqPayload,
    EstablishmentDetails,
    Header,
    RequesterDetails,
    UserInfo,
)
from utils.assertion import assert_status_code


class CreateAppointment:
    def __init__(self):
        self.client = HTTPClient()
        self.url = config.settings.ibm_url
        self.route = "/takamol/staging"

    @allure.step
    def get_response_book_an_appointment(self, user: User, service: Service):
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
            Time="90",
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
            json=payload.dict(exclude_none=True),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()
