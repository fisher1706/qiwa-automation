from pydantic.main import BaseModel


class GetChangeOccupationLaborersListBody(BaseModel):
    LaborOfficeId: str
    SequenceNumber: str
    PageSize: str
    PageIndex: str


class GetChangeOccupationLaborersListRq(BaseModel):
    Header: dict
    Body: GetChangeOccupationLaborersListBody


class GetChangeOccupationLaborersListRqPayload(BaseModel):
    GetChangeOccupationLaborersListRq: GetChangeOccupationLaborersListRq
