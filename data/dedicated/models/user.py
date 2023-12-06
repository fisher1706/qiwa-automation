from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    personal_number: str

    labor_office_id: Optional[str]
    sequence_number: Optional[str]

    office_id: Optional[str]
    establishment_name_ar: Optional[str]
    establishment_number: Optional[str]
    occupation: Optional[str]
    name: Optional[str]

    user_id: Optional[int]
    unified_number_id: Optional[int]

    establishment_id: Optional[str]
