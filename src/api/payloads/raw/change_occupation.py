from typing import List, Optional

from src.api.models.qiwa.base import QiwaBaseModel


class Laborer(QiwaBaseModel):
    personal_number: Optional[str]
    occupation_code: Optional[str]


class CreateRequest(QiwaBaseModel):
    labor_office_id: Optional[str]
    sequence_number: Optional[str]
    laborers: List[Laborer]
