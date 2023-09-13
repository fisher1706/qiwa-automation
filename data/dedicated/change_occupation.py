from data.constants import Occupation
from data.dedicated.models.user import User

lo_co_user = User(
    personal_number="1016518225",
    labor_office_id="9",
    sequence_number="79744",
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
