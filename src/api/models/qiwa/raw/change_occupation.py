from typing import List, Optional

from pydantic import Field

from src.api.models.qiwa.base import QiwaBaseModel


class Value(QiwaBaseModel):
    value: int


class Meta(QiwaBaseModel):
    from_: int = Field(..., alias="from")
    size: int
    max_score: Optional[int]
    total: Value


class Laborer(QiwaBaseModel):
    status_id: int
    status_name: str
    current_occupation_id: str
    current_occupation_name: str
    new_occupation_id: str
    new_occupation_name: str
    nationality_code: str
    nationality_name: str
    rejection_description: str
    labor_office_id: str
    employee_personal_number: str
    employee_name: str
    request_sequence: str
    request_year: str
    request_number: str
    bulk_id: str
    id: str


class Request(QiwaBaseModel):
    request_id: str
    type_id: int
    type_name: str
    date: str
    labor_office_id: str
    sequence_number: str
    establishment_id: str
    requester_personal_number: str
    requester_id: str
    request_type: int
    id: str
    requester_name: str
    laborers: List[Laborer]


class ChangeOccupationRequest(QiwaBaseModel):
    request_id: str
    personal_number: str
