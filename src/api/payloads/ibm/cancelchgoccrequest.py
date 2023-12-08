from pydantic import BaseModel

from src.api.payloads.ibm.header import Header


class Body(BaseModel):
    RequestNumber: str


class CancelChangeOccupationRequestLORq(BaseModel):
    Header: Header
    Body: Body


class CancelChangeOccupationRequestLORqPayload(BaseModel):
    CancelChangeOccupationRequestLORq: CancelChangeOccupationRequestLORq
