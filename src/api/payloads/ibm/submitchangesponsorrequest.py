from typing import Optional

from pydantic.main import BaseModel

from src.api.payloads.ibm.header import Header


class LaborerItem(BaseModel):
    LaborerName: str
    LaborerIdNo: str


class LaborerList(BaseModel):
    LaborerItem: LaborerItem


class SourceLaborerItem(BaseModel):
    SourceLaborOfficeId: str
    SourceSequenceNumber: str
    LaborerList: LaborerList


class LaborersNationalitiesItem(BaseModel):
    Nationality: str
    NumberOfLaborers: str


class LaborersNationalitiesList(BaseModel):
    LaborersNationalitiesItem: LaborersNationalitiesItem


class SourceLaborerList(BaseModel):
    SourceLaborerItem: SourceLaborerItem


class DestinationDetails(BaseModel):
    DestinationLaborOfficeId: str
    DestinationSequenceNumber: str


class Body(BaseModel):
    PaymentReference: Optional[str]
    DestinationDetails: DestinationDetails
    SourceLaborerList: SourceLaborerList
    LaborersNationalitiesList: LaborersNationalitiesList
    ChangeOrTransfer: str


class SubmitChangeSponsorRequestRq(BaseModel):
    Header: Header
    Body: Body


class SubmitChangeSponsorRequestRqPayload(BaseModel):
    SubmitChangeSponsorRequestRq: SubmitChangeSponsorRequestRq
