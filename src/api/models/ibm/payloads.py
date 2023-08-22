from typing import Optional

from pydantic import BaseModel

from src.api.constants.work_permit import WorkPermitStatus


class GetWorkPermitRequestsRq(BaseModel):
    LaborOfficeId: str
    SequenceNumber: str
    PageIndex: str = "1"
    PageSize: str = "100"
    StatusId: Optional[WorkPermitStatus]


class GetSaudiCertificateRq(BaseModel):
    CertificateNumber: Optional[str] = None
    LaborOfficeId: Optional[str]
    SequenceNumber: Optional[str]
    SaudiCertStatusId: int = 1
    PageSize: int = 10
    PageIndex: int = 1


class ValidEstSaudiCertificateRq(BaseModel):
    LaborOfficeId: str
    SequenceNumber: str
