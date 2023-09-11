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
    personal_number="1016518225",
    labor_office_id="9",
    sequence_number="79744",
)
lo_co_user_1 = User(
    personal_number="1009428556",
    labor_office_id="9",
    sequence_number="8800",
)
lo_co_user_2 = User(
    personal_number="1003501564",
    labor_office_id="1",
    sequence_number="2000739",
)
employee = User(
    personal_number="2053713927",
    labor_office_id="9",
    sequence_number="79744",
    occupatiok=Occupation.SUPERVISOR,
)
employee_1 = User(
    personal_number="2002794366",
    labor_office_id="9",
    sequence_number="79744",
    occupatiok=Occupation.MANAGER_DIRECTOR,
)


class Service(BaseModel):
    client_service_id: str
    sub_service_id: str


change_occupation = Service(
    client_service_id="3",
    sub_service_id="6"
)


work_permit = Service(
    client_service_id="4",
    sub_service_id="12"
)