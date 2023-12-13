from data.dedicated.models.user import User
from src.api.payloads.ibm.checkandvatransemp import (
    Body,
    CheckandValidateTransferredEmployeeRq,
    CheckandValidateTransferredEmployeeRqPayload,
)
from src.api.payloads.ibm.getchangeoccupationlaborerslist import (
    GetChangeOccupationLaborersListBody,
    GetChangeOccupationLaborersListRq,
    GetChangeOccupationLaborersListRqPayload,
)
from src.api.payloads.ibm.header import Header, UserInfo


def check_and_validate_transferred_employee_payload(personal_number: str) -> dict:
    return CheckandValidateTransferredEmployeeRqPayload(
        CheckandValidateTransferredEmployeeRq=CheckandValidateTransferredEmployeeRq(
            Header=Header(
                TransactionId="0",
                ChannelId="ESB",
                RequestTime="2019-10-10 00:00:00.555",
                ServiceCode="CVTE0001",
                UserInfo=UserInfo(IDNumber="2283737795"),
            ),
            Body=Body(
                IdNo=personal_number,
                DestinationLaborOfficeId="9",
                DestinationSequenceNumber="3212",
            ),
        )
    ).dict(exclude_none=True)
