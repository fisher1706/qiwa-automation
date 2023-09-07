from datetime import datetime

import allure
import pytest

import config
from data.constants import HEADERS
from data.dedicated.change_occupation import User
from src.api.http_client import HTTPClient
from src.api.payloads.ibm.createnewappointment import (
    Header,
    UserInfo,
    EstablishmentDetails,
    RequesterDetails,
    CreateNewAppointmentRq,
    CreateNewAppointmentRqPayload,
    Body,
)


# TODO: Adjust and move it to the ibm.py
class IBMApiStageController:
    def __init__(self, client: HTTPClient):
        self.client = client
        self.url = config.qiwa_urls.ibm_url
        self.route = "/takamol/staging/qiwalo/createnewappointment"

    @allure.step
    def create_new_appointment(self, user: User) -> int:
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
            OfficeID="1413",
            ClientServiceId="3",
            RequesterDetails=RequesterDetails(
                RequesterIdNo=user.personal_number,
                RequesterName="",
                RequesterUserId=user.personal_number,
            ),
            Time="93",
            Date=datetime.today().strftime("%Y-%m-%d"),
            RegionId="1",
            RequesterTypeId="2",
            SubServiceId="6",
            VisitReasonId="1",
        )
        create_new_appointment = CreateNewAppointmentRq(Header=header, Body=body)
        payload = CreateNewAppointmentRqPayload(CreateNewAppointmentRq=create_new_appointment)
        response = self.client.post(
            url=self.url,
            endpoint=self.route,
            json=payload.dict(),
            headers=HEADERS,
        )
        response = response.json()
        try:
            return response["CreateNewAppointmentRs"]["Body"]["AppointmentId"]
        except KeyError:
            pytest.fail(reason=str(response))
        return 0
