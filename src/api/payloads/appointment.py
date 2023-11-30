from datetime import datetime

from data.dedicated.models.services import Service
from data.dedicated.models.user import User
from src.api.payloads.ibm.createnewappointment import (
    Body,
    CreateNewAppointmentRq,
    CreateNewAppointmentRqPayload,
    EstablishmentDetails,
    RequesterDetails,
)
from src.api.payloads.ibm.header import Header, UserInfo


def appointment_payload(user: User, service: Service):
    return CreateNewAppointmentRqPayload(
        CreateNewAppointmentRq=CreateNewAppointmentRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2023-08-03 09:00:00.555",
                ServiceCode="CNA00001",
                DebugFlag="1",
                UserInfo=UserInfo(UserId=user.personal_number, IDNumber=user.personal_number),
            ),
            Body=Body(
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
            ),
        )
    ).dict(exclude_none=True)
