from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    personal_number: str

    labor_office_id: str
    sequence_number: str

    establishment_name_ar: Optional[str]
    establishment_number: Optional[str]
    occupation: Optional[str]
    employee_name: Optional[str]
