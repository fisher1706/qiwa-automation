from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class Memberships(QiwaBaseModel):
    owner: int


class Permissions(QiwaBaseModel):
    saudization_certificate: bool
    change_occupation: bool
    transferring_worker: bool
    working_permits: bool
    nitaqat_calculator: bool
    visa_issuance: bool
    ajeer_program: bool
    compliance_index: bool
    company_performance_report: bool
    wage_disbursement: bool
    labor_award: bool
    subscription_service: bool
    labor_market_index: bool
    labor_policies: bool
    employee_information: bool
    establishment_dashboard: bool
    violation_service: bool
    contract_management: bool
    skill_verification: bool
    government_contracts: bool
    location_management: bool
    appointments_service: bool
    trainings_management: bool
    salary_certificate: bool
    e_wallet: bool
    delegation: bool


class AuthorizationToken(QiwaBaseModel):
    exp: int
    nbf: Optional[int]
    iss: str
    aud: str
    iat: int
    session_key: str
    lifetime: int
    account_id: str
    states: list
    user_id: str
    user_personal_number: str
    company_id: str
    memberships: Memberships
    permissions: Permissions
    language: str
    high_security_mode_start: Optional[str]
    otp_verified: Optional[str]
    login_time: Optional[str]
    company_sequence_number: str
    company_labor_office_id: str
