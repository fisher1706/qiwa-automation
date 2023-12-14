from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.api.payloads.ibm.header import Header, UserInfo
from src.api.payloads.ibm.submitcsrequests import (
    Body,
    DestinationDetails,
    LaborerDetails,
    LaborerNationality,
    LaborersDetailsItem,
    LaborersDetailsList,
    SourceDetails,
    SponsorDetails,
    SubmitCSRequestRq,
    SubmitCSRequestRqPayload,
)


def employee_transfer_request_ae_payload(user: User, laborer: Laborer, sponsor_id: int):
    return SubmitCSRequestRqPayload(
        SubmitCSRequestRq=SubmitCSRequestRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2023-08-03 09:00:00.555",
                ServiceCode="SCSR0003",
                DebugFlag="1",
                UserInfo=UserInfo(IDNumber=user.personal_number),
            ),
            Body=Body(
                DestinationDetails=DestinationDetails(
                    EstablishmentName="",
                    LaborOfficeId=user.labor_office_id,
                    SequenceNumber=user.sequence_number,
                ),
                LaborersDetailsList=LaborersDetailsList(
                    LaborersDetailsItem=LaborersDetailsItem(
                        LaborerDetails=LaborerDetails(
                            LaborerName="",
                            LaborerIdNo=laborer.personal_number,
                            LaborerNationality=LaborerNationality(
                                Code="340",
                                NameAr="",
                                NameEn="",
                            ),
                            LaborerStatusCode="1",
                            IqamaExpiryDate="2023-02-09",
                            TransferTypeId=laborer.transfer_type.code,
                        ),
                        SponsorDetails=SponsorDetails(
                            SponsorIdNo=sponsor_id if isinstance(sponsor_id, User) else 0,
                            SponsorName="",
                        ),
                        SourceDetails=SourceDetails(
                            EstablishmentName="",
                            EstablishmentId="",
                            LaborOfficeId="1",
                            SequenceNumber="224981",
                        ),
                    )
                ),
            ),
        )
    ).dict(exclude_none=True)
