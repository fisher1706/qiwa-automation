from typing import Optional

from pydantic import BaseModel

from data.constants import Occupation


class User(BaseModel):
    personal_number: str

    labor_office_id: str
    sequence_number: str

    establishment_name_ar: Optional[str]
    establishment_number: Optional[str]
    occupation: Optional[str]
    employee_name: Optional[str]


lo_co_user = User(
    personal_number='1016518225',
    labor_office_id='9',
    sequence_number='79744',
)
lo_co_user_1 = User(
    personal_number='1009428556',
    labor_office_id='9',
    sequence_number='8800',
)
employee = User(
    personal_number='2053713927',
    labor_office_id='9',
    sequence_number='79744',
    occupatiok=Occupation.SUPERVISOR,
)
employee_1 = User(
    personal_number='2002794366',
    labor_office_id='9',
    sequence_number='79744',
    occupatiok=Occupation.MANAGER_DIRECTOR,
)
