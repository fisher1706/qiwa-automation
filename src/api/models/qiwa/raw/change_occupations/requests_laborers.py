from datetime import datetime

from src.api.models.qiwa.base import QiwaBaseModel


class RequestLaborer(QiwaBaseModel):
    request_id: str
    type_id: int
    type_name_ar: str
    type_name_en: str
    labor_office_id: int
    sequence_number: int
    id: int
    laborer_id_no: int
    laborer_name: str
    nationality_id: int
    nationality_en: str
    nationality_ar: str
    request_sequence: int
    request_year: int
    request_number: str
    request_date: datetime
    request_status_id: int
    request_status_en: str
    request_status_ar: str
    requester_id_no: int | None
    requester_user_id: int | None
    current_occupation_id: int
    current_occupation_en: str
    current_occupation_ar: str
    new_occupation_id: int
    new_occupation_en: str
    new_occupation_ar: str
