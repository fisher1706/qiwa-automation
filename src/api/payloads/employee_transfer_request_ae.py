from data.dedicated.employee_trasfer.employee_transfer_constants import type_12, type_9
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


def employee_transfer_request_ae_payload(
    employer: User, laborer: Laborer, employee_info: dict
) -> dict:
    sponsor_id, labor_office_id, sequence_number = 0, "11", "1945041"
    if laborer.transfer_type.code == type_12.code:
        sponsor_id = int(employee_info["SponsorDetails"]["SponsorIdNo"])
    elif laborer.transfer_type.code == type_9.code:
        labor_office_id = employer.labor_office_id
        sequence_number = employer.sequence_number
    else:
        labor_office_id = employee_info["SourceDetails"]["LaborOfficeId"]
        sequence_number = employee_info["SourceDetails"]["SequenceNumber"]
    return SubmitCSRequestRqPayload(
        SubmitCSRequestRq=SubmitCSRequestRq(
            Header=Header(
                TransactionId="0",
                ChannelId="Qiwa",
                SessionId="0",
                RequestTime="2023-08-03 09:00:00.555",
                ServiceCode="SCSR0003",
                DebugFlag="1",
                UserInfo=UserInfo(IDNumber=employer.personal_number),
            ),
            Body=Body(
                DestinationDetails=DestinationDetails(
                    EstablishmentName="AQA EstablishmentName",
                    LaborOfficeId=employer.labor_office_id,
                    SequenceNumber=employer.sequence_number,
                ),
                LaborersDetailsList=LaborersDetailsList(
                    LaborersDetailsItem=LaborersDetailsItem(
                        LaborerDetails=LaborerDetails(
                            LaborerName="AQA LaborerName",
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
                            SponsorIdNo=sponsor_id,
                            SponsorName="",
                        ),
                        SourceDetails=SourceDetails(
                            EstablishmentName="",
                            EstablishmentId="",
                            LaborOfficeId=labor_office_id,
                            SequenceNumber=sequence_number,
                        ),
                    )
                ),
            ),
        )
    ).dict(exclude_none=True)
