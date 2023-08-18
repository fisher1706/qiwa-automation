import datetime
from typing import List, Optional

from pydantic import BaseModel


class RequestDetails(BaseModel):
    RequestSequence: str
    RequestYear: str


class RequestInformation(BaseModel):
    RequestId: str
    RequestTypeId: int
    RequestTypeEn: str
    RequestTypeAr: str
    RequestDate: datetime.datetime


class EstablishmentDetails(BaseModel):
    LaborOfficeId: str
    SequenceNumber: str
    EstablishmentId: str
    EntityID: str


class RequesterDetails(BaseModel):
    UserId: str
    IdNo: str


class Nationality(BaseModel):
    Code: str
    Name: str


class CurrentOccupationDetails(BaseModel):
    CurrentOccupationId: str
    CurrentOccupationEn: str
    CurrentOccupationAr: str


class NewOccupationDetails(BaseModel):
    NewOccupationId: str
    NewOccupationAr: str
    NewOccupationEn: str


class StatusDetails(BaseModel):
    StatusId: int
    StatusAr: str
    StatusEn: str


class RequestDetailsItem(BaseModel):
    LaborerName: str
    LaborerIdNo: str
    LaborOfficeId: str
    RejectionDescription: Optional[str]
    RequestDetails: RequestDetails
    CurrentOccupationDetails: CurrentOccupationDetails
    NewOccupationDetails: NewOccupationDetails
    StatusDetails: StatusDetails
    Nationality: Nationality


class RequestDetailsList(BaseModel):
    RequestDetailsItem: List[RequestDetailsItem]


class ChangeOccupationItem(BaseModel):
    RequestInformation: RequestInformation
    EstablishmentDetails: EstablishmentDetails
    RequesterDetails: RequesterDetails
    LaborTransfersTotalCount: int
    PaymentReference: str
    RequestDetailsCount: int
    RequestDetailsList: RequestDetailsList


class ChangeOccupationList(BaseModel):
    ChangeOccupationItem: ChangeOccupationItem | List[ChangeOccupationItem]


class Body(BaseModel):
    ChangeOccupationList: ChangeOccupationList
    TotalRecordsCount: int
