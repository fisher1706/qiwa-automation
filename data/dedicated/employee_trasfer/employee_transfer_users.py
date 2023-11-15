from data.dedicated.employee_trasfer.employee_transfer_constants import (
    type_4,
    type_9,
    type_12,
)
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User

employer = User(
    personal_number="1016316828",
    labor_office_id="9",
    sequence_number="3212",
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد تجربة",
    establishment_number="1828954",
    name="عبدالله المولد",
)
employer_between_my_establishments = User(
    personal_number="1029955703",
    labor_office_id="21",
    sequence_number="62148",
    establishment_name_ar="سوبر ماركت لصاحبها فائز محمد حسن",
)

current_sponsor = User(
    personal_number="1071480196",
    labor_office_id="4",
    sequence_number="93766",
    establishment_name_ar="شركة سراكو",
)
current_sponsor_type_12 = User(personal_number="1046395800")

laborer = Laborer(login_id=2449079728, birthdate="11-07-1993", transfer_type=type_9)
laborer_with_sponsor = Laborer(login_id=2178708182, birthdate="29-01-1958", transfer_type=type_4)
laborer_existing_contract = Laborer(login_id=2341193031, birthdate="15-09-1987")
laborer_type_12 = Laborer(login_id=2493081331, birthdate="03-01-1990", transfer_type=type_12)
laborer_type_9 = Laborer(login_id=2021014218, birthdate="18-10-1982", transfer_type=type_9)
laborer_type_4_freedom_transfer = Laborer(
    login_id=2283737795, birthdate="25-12-1986", transfer_type=type_4
)
laborer_type_4_direct_transfer = Laborer(
    login_id=2198951952, birthdate="01-01-1959", transfer_type=type_4
)
laborer_type_4_absent = Laborer(login_id=2468727199, birthdate="01-01-1986", transfer_type=type_4)

laborer_between_my_establishments = Laborer(
    login_id=2016254472, birthdate="01-01-1976", transfer_type=type_4
)
laborer_between_my_establishments_existing_contract = Laborer(
    login_id=2126951132, birthdate="01-03-1961", transfer_type=type_4
)
laborer_between_my_establishments_quota = Laborer(login_id=2111825226, birthdate="01-01-1976")
