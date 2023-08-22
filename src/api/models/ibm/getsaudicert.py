from typing import Literal, Optional

from pydantic import BaseModel


class SaudiCertStatus(BaseModel):
    SaudiCertStatusId: Literal["1"]
    SaudiCertStatusEn: Literal["Active"]
    SaudiCertStatusAr: Literal["نشط"]


class SCDetailsItem(BaseModel):
    CertificateNumber: str
    NationalUnifiedNumber: dict
    SaudiCertIssueDate: str
    SaudiCertExpiryDate: str
    SaudiCertStatus: SaudiCertStatus
    LaborOfficeId: int
    SequenceNumber: int
    EstablishmentName: str
    CRNumber: str
    RenewalStartDate: dict | str
    RequesterIdNo: Optional[str]
    RequesterUserId: Optional[str]


class SCDetailsList(BaseModel):
    SCDetailsItem: SCDetailsItem


class GetSaudiCertificateRsBody(BaseModel):
    SCDetailsList: Optional[SCDetailsList]
    TotalRecordsCount: Optional[int]
