from typing import Optional

from pydantic import BaseModel


class Nationality(BaseModel):
    Code: Optional[int]
    Name: Optional[str]


class EstablishmentDetails(BaseModel):
    LaborOfficeId: Optional[int]
    SequenceNumber: Optional[str]
    EstablishmentId: Optional[int]


class RequesterDetails(BaseModel):
    RequesterUserid: Optional[int]
    RequesterIdNo: Optional[str]


class LaborerDetails(BaseModel):
    LaborerIdNo: Optional[str]
    LaborerName: Optional[str]
    CurrentOccupationId: Optional[int]
    NewOccupationId: Optional[int]
    CurrentOccupationName: Optional[str]
    NewOccupationName: Optional[str]
    Nationality: Optional[Nationality]


class RequestDetails(BaseModel):
    RequestSequence: Optional[str]
    RequestYear: Optional[str]


class Body(BaseModel):
    RequestId: Optional[int]
    RequestTypeId: Optional[int]
    EstablishmentDetails: EstablishmentDetails = EstablishmentDetails()
    RequesterDetails: RequesterDetails = RequesterDetails()
    LaborerDetails: LaborerDetails = LaborerDetails()
    RequestDetails: RequestDetails = RequestDetails()
    StatusId: Optional[int]
    IncludeDraft: Optional[int]
    PageSize: Optional[int] = 10
    PageIndex: Optional[int] = 1
