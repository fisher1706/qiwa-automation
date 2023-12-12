from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.api.payloads.ibm.getlaborerscorequests import (
    Body,
    EstablishmentDetails,
    GetLaborersCORequestsRq,
    GetLaborersCORequestsRqPayload,
    LaborerDetails,
    RequestDetails,
    StatusItem,
    StatusList,
)
from src.api.payloads.ibm.header import Header, UserInfo


def laborers_co_requests_payload(user: User, status_id: int):
    return GetLaborersCORequestsRqPayload(
        GetLaborersCORequestsRq=GetLaborersCORequestsRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2023-08-03 09:00:00.555",
                ServiceCode="GCOLL001",
                DebugFlag="1",
                UserInfo=UserInfo(IDNumber=user.personal_number),
            ),
            Body=Body(
                RequestDetails=RequestDetails(
                    StatusList=StatusList(StatusItem=StatusItem(StatusId=status_id)),
                ),
                EstablishmentDetails=EstablishmentDetails(
                    LaborOfficeId=user.labor_office_id, SequenceNumber=user.sequence_number
                ),
                LaborerDetails=LaborerDetails(LaborerIdNo=user.personal_number),
                PageSize=10,
                PageIndex=1,
            ),
        )
    ).dict(exclude_none=True)
