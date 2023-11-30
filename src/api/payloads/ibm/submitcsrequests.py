from pydantic.main import BaseModel

from src.api.payloads.ibm.header import Header


class SourceDetails(BaseModel):
    EstablishmentName: str
    EstablishmentId: str
    LaborOfficeId: str
    SequenceNumber: str


class LaborerNationality(BaseModel):
    Code: str
    NameAr: str
    NameEn: str


class LaborerDetails(BaseModel):
    LaborerName: str
    LaborerIdNo: str
    LaborerNationality: LaborerNationality
    LaborerStatusCode: str
    IqamaExpiryDate: str
    TransferTypeId: str


class LaborersDetailsItem(BaseModel):
    LaborerDetails: LaborerDetails
    SourceDetails: SourceDetails


class LaborersDetailsList(BaseModel):
    LaborersDetailsItem: LaborersDetailsItem


class DestinationDetails(BaseModel):
    EstablishmentName: str
    LaborOfficeId: str
    SequenceNumber: str


class Body(BaseModel):
    DestinationDetails: DestinationDetails
    LaborersDetailsList: LaborersDetailsList


class SubmitCSRequestRq(BaseModel):
    Header: Header
    Body: Body


class SubmitCSRequestRqPayload(BaseModel):
    SubmitCSRequestRq: SubmitCSRequestRq
