from data.dedicated.change_occupation.change_occupation_constants import Occupation
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User

lo_co_user = User(
    personal_number="1016518225",
    labor_office_id="9",
    sequence_number="79744",
    name="عبدالله النهدي",
    office_id="1413",
)
lo_co_ho_user = User(
    personal_number="2139807230",
    labor_office_id="1",
    sequence_number="59670",
    name="عبدالله النهدي",
    office_id="1250",
)
lo_co_expired_user = User(
    personal_number="1036149837",
    labor_office_id="11",
    sequence_number="76326",
    establishment_name_ar="بيع خرداوات عيسى احمد عامر عسيري",
    office_id="1250",
)
employee = User(
    personal_number="2053713927",
    labor_office_id="9",
    sequence_number="79744",
    occupation=Occupation.SUPERVISOR,
)
employee_1 = User(
    personal_number="2002794366",
    labor_office_id="9",
    sequence_number="79744",
    occupation=Occupation.MANAGER_DIRECTOR,
)
employee_ho = User(
    personal_number="2004423279",
    labor_office_id="1",
    sequence_number="59670",
    occupation=Occupation.INFORMATION_TECHNOLOGY_OPERATIONS_TECHNICIAN,
)
employee_po = User(
    personal_number="2033807609",
    labor_office_id="1",
    sequence_number="59670",
    occupation=Occupation.ACCOUNTANT,
)
laborer = Laborer(personal_number=2289438844, birthdate="20-10-1976")
