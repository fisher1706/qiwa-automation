from pydantic.main import BaseModel

from src.api.payloads.ibm.header import Header


class LaborerDetails(BaseModel):
    LaborerIdNo: int


class EstablishmentDetails(BaseModel):
    LaborOfficeId: int
    SequenceNumber: int


class StatusItem(BaseModel):
    StatusId: int


class StatusList(BaseModel):
    StatusItem: StatusItem


class RequestDetails(BaseModel):
    StatusList: StatusList


class Body(BaseModel):
    RequestDetails: RequestDetails
    EstablishmentDetails: EstablishmentDetails
    LaborerDetails: LaborerDetails
    PageSize: int
    PageIndex: int


class GetLaborersCORequestsRq(BaseModel):
    Header: Header
    Body: Body


class GetLaborersCORequestsRqPayload(BaseModel):
    GetLaborersCORequestsRq: GetLaborersCORequestsRq
