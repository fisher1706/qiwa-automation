from typing import Optional

from pydantic import BaseModel


class Laborer(BaseModel):
    login_id: int
    birthdate: str


class Entity(BaseModel):
    login_id: Optional[int]
    labor_office_id: Optional[int]
    sequence_number: Optional[int]
    establishment_name_ar: Optional[str]
    establishment_number: Optional[str]
