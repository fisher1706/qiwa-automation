from data.dedicated.models.user import User
from src.api.payloads.ibm.getchangeoccupationlaborerslist import (
    GetChangeOccupationLaborersListBody,
    GetChangeOccupationLaborersListRq,
    GetChangeOccupationLaborersListRqPayload,
)
from src.api.payloads.ibm.header import Header


def change_occupation_laborers_list_payload(user: User) -> dict:
    return GetChangeOccupationLaborersListRqPayload(
        GetChangeOccupationLaborersListRq=GetChangeOccupationLaborersListRq(
            Header=Header(
                TransactionId="0",
                RequestTime="2019-10-10 00:00:00.555",
                ServiceCode="GCOLL001",
            ),
            Body=GetChangeOccupationLaborersListBody(
                LaborOfficeId=user.labor_office_id,
                SequenceNumber=user.sequence_number,
                PageSize=5,
                PageIndex=1,
            ),
        )
    ).dict(exclude_none=True)
