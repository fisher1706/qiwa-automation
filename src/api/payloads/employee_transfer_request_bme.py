from data.dedicated.enums import TransferType
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.api.payloads.ibm.header import Header, UserInfo
from src.api.payloads.ibm.submitchangesponsorrequest import (
    Body,
    DestinationDetails,
    LaborerItem,
    LaborerList,
    LaborersNationalitiesItem,
    LaborersNationalitiesList,
    SourceLaborerItem,
    SourceLaborerList,
    SubmitChangeSponsorRequestRq,
    SubmitChangeSponsorRequestRqPayload,
)


def employee_transfer_request_bme_payload(
    user: User, laborer: Laborer, transfer_type: TransferType
):
    return SubmitChangeSponsorRequestRqPayload(
        SubmitChangeSponsorRequestRq=SubmitChangeSponsorRequestRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2023-08-03 09:00:00.555",
                ServiceCode="SCSR0002",
                DebugFlag="1",
                UserInfo=UserInfo(UserId=user.personal_number, IDNumber=user.personal_number),
            ),
            Body=Body(
                DestinationDetails=DestinationDetails(
                    DestinationLaborOfficeId=user.labor_office_id,
                    DestinationSequenceNumber=user.sequence_number,
                ),
                SourceLaborerList=SourceLaborerList(
                    SourceLaborerItem=SourceLaborerItem(
                        SourceLaborOfficeId=user.labor_office_id,
                        SourceSequenceNumber=user.sequence_number,
                        LaborerList=LaborerList(
                            LaborerItem=LaborerItem(LaborerName="", LaborerIdNo=laborer.personal_number)
                        ),
                    )
                ),
                LaborersNationalitiesList=LaborersNationalitiesList(
                    LaborersNationalitiesItem=LaborersNationalitiesItem(
                        Nationality="1", NumberOfLaborers="1"
                    )
                ),
                ChangeOrTransfer=transfer_type,
            ),
        )
    ).dict(exclude_none=True)
