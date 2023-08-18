from datetime import date
from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class SaudizationCertificate(QiwaBaseModel):
    id: int
    saudi_certificate_number: str
    national_unified_number: Optional[dict]
    labor_office_id: int
    sequence_number: int
    company_id: int
    saudi_cert_status_id: int
    saudi_cert_status_en: str
    saudi_cert_status_ar: str
    establishment_name: str
    cr_number: int
    requester_user_id: int
    requester_personal_number: int
    renew_start_date: Optional[date]
    cert_issue_date: date
    cert_expiry_date: date


class EncryptedSaudizationCertificate(QiwaBaseModel):
    id: int
    certificate: str


class Error(QiwaBaseModel):
    id: int
    code: str
    ar_message: str
    en_message: str
