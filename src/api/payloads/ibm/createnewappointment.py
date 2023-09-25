from typing import Optional

from pydantic import BaseModel


class UserInfo(BaseModel):
    UserId: str
    IDNumber: str


class EstablishmentDetails(BaseModel):
    SequenceNumber: str
    LaborOfficeId: str


class RequesterDetails(BaseModel):
    RequesterIdNo: str
    RequesterName: str
    RequesterUserId: str


class Header(BaseModel):
    TransactionId: str
    ChannelId: str
    SessionId: str
    RequestTime: str
    ServiceCode: str
    DebugFlag: int
    UserInfo: Optional[UserInfo]


class Body(BaseModel):
    EstablishmentDetails: EstablishmentDetails
    OfficeID: str
    ClientServiceId: str
    RequesterDetails: RequesterDetails
    Time: str
    Date: str
    RegionId: str
    RequesterTypeId: int
    SubServiceId: int
    VisitReasonId: int


class CreateNewAppointmentRq(BaseModel):
    Header: Header
    Body: Body


class CreateNewAppointmentRqPayload(BaseModel):
    CreateNewAppointmentRq: CreateNewAppointmentRq
