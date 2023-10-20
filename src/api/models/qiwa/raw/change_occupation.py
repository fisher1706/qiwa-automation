from datetime import datetime

from pydantic import Field

from src.api.models.qiwa.base import QiwaBaseModel


class RequestsCount(QiwaBaseModel):
    status_id: int
    status_en: str
    status_ar: str
    requests_count: int


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
    requester_id_no: int
    requester_user_id: int
    current_occupation_id: int
    current_occupation_en: str
    current_occupation_ar: str
    new_occupation_id: int
    new_occupation_en: str
    new_occupation_ar: str


class MetaTotal(QiwaBaseModel):
    value: int


class Meta(QiwaBaseModel):
    pages_count: int
    current_page: int
    total_entities: int
    from_: int = Field(alias="from")
    size: int
    max_score: int | None = ...
    total_pages: int
    total: MetaTotal
