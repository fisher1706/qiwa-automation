from pydantic import Field
from pydantic.main import BaseModel

from src.api.payloads.ibm.header import Header


# TODO: Remove this model if not in use
class GetSaudiCertificateDetailsBody(BaseModel):
    CertificateNumber: str
    LaborOfficeId: int
    SequenceNumber: int
    SaudiCertStatusId: int
    SortBy: int = Field(default=1)
    SortDirection: int = Field(default=2)
    PageSize: int = Field(default=1)
    PageIndex: int = Field(default=1)


class CertificateDetails(BaseModel):
    number: int
    status_id: int


class GetSaudiCertificateReq(BaseModel):
    Header: Header
    Body: GetSaudiCertificateDetailsBody


class GetSaudiCertificateRes(BaseModel):
    CertificateNumber: str
    CertIssueDate: str
    CertExpiryDate: str
    CertStatus: str
    CRNumber: str
    RemainingDays: str
