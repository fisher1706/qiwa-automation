from datetime import datetime

from src.api.models.qiwa.base import QiwaBaseModel


class Laborer(QiwaBaseModel):
    status_id: int
    status_name: str
    request_status_en: str
    request_status_ar: str
    current_occupation_id: str
    current_occupation_name: str
    current_occupation_en: str
    current_occupation_ar: str
    new_occupation_id: str
    new_occupation_name: str
    new_occupation_en: str
    new_occupation_ar: str
    nationality_code: str
    nationality_name: str
    rejection_description: str
    labor_office_id: str
    employee_personal_number: str
    employee_name: str
    request_number: str
    bulk_id: str
    id: str


class Request(QiwaBaseModel):
    labor_office_id: str
    sequence_number: str
    request_id: str
    type_id: int
    type_name_ar: str
    type_name_en: str
    id: str
    type_name: str
    date: datetime
    establishment_id: str
    requester_personal_number: str
    requester_id: str
    request_type: int
    requester_name: str
    laborers: list[Laborer]
