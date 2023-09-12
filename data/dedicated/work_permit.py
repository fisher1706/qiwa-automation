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


lo_wp_user_1 = User(
    personal_number="1009428556",
    labor_office_id="9",
    sequence_number="8800",
)
lo_wp_user_2 = User(
    personal_number="1003501564",
    labor_office_id="1",
    sequence_number="2000739",
)


class UserIqama:
    iqama_1 = "2369026089"
    iqama_2 = "2350756413"
    iqama_3 = "2426490187"
    iqama_4 = "2401631367"
    iqama_5 = "2310334475"
