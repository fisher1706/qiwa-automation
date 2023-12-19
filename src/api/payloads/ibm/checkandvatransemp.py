from pydantic import BaseModel

from src.api.payloads.ibm.header import Header


class Body(BaseModel):
    IdNo: str
    DestinationLaborOfficeId: str
    DestinationSequenceNumber: str


class CheckandValidateTransferredEmployeeRq(BaseModel):
    Header: Header
    Body: Body


class CheckandValidateTransferredEmployeeRqPayload(BaseModel):
    CheckandValidateTransferredEmployeeRq: CheckandValidateTransferredEmployeeRq
