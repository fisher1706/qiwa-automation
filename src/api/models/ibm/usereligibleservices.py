from typing import List

from pydantic import BaseModel

from src.api.models.ibm.header import IBMResponseHeader


class Status(BaseModel):
    StatusId: str
    StatusEn: str
    StatusAr: str


class Service(BaseModel):
    Service: str
    ServiceNameEn: str
    ServiceNameAr: str


class EligibleServicesListItem(BaseModel):
    IdNo: str
    UserId: str
    Name: str
    LaborOfficeId: str
    SequenceNumber: str
    Status: Status
    Service: Service


class EligibleServicesItem(BaseModel):
    EligibleServicesItem: List[EligibleServicesListItem]


class Body(BaseModel):
    TotalRecordsCount: int
    EligibleServicesList: EligibleServicesItem


class GetUserEligibleServicesRs(BaseModel):
    Header: IBMResponseHeader
    Body: Body


class ResponseUserEligibleServices(BaseModel):
    GetUserEligibleServicesRs: GetUserEligibleServicesRs
