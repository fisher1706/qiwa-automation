from data.dedicated.employee_trasfer.employee_transfer_constants import (
    type_4,
    type_9,
    type_12,
)
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User

employer_old = User(
    personal_number="1016316828",
    labor_office_id="9",
    sequence_number="3212",
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد تجربة",
    establishment_number="1828954",
    name="عبدالله",
    establishment_id="23244",
)
employer = User(
    personal_number="1006783110",
    labor_office_id="11",
    sequence_number="1945041",
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد تجربة",
    establishment_number="1828954",
    name="عبدالله",
    establishment_id="23244",
)

current_sponsor = User(
    personal_number="1071480196",
    labor_office_id="4",
    sequence_number="93766",
    establishment_name_ar="شركة سراكو",
)
current_sponsor_type_12 = User(personal_number="1046395800")

laborer = Laborer(personal_number=2449079728, birthdate="11-07-1993", transfer_type=type_9)
laborer_with_sponsor = Laborer(
    personal_number=2178708182, birthdate="29-01-1958", transfer_type=type_4
)
laborer_type_12 = Laborer(
    personal_number=2493081331, birthdate="03-01-1990", transfer_type=type_12
)
laborer_type_9 = Laborer(personal_number=2021014218, birthdate="18-10-1982", transfer_type=type_9)
laborer_type_4_freedom_transfer = Laborer(
    personal_number=2283737795, birthdate="25-12-1986", transfer_type=type_4
)
laborer_type_4_direct_transfer = Laborer(
    personal_number=2198951952, birthdate="01-01-1959", transfer_type=type_4
)
laborer_type_4_absent = Laborer(
    personal_number=2145372690, birthdate="01-01-1974", transfer_type=type_4
)

laborer_between_my_establishments = Laborer(
    personal_number=2196359604, birthdate="01-01-1966", transfer_type=type_4
)
laborer_between_my_establishments_quota = Laborer(
    personal_number=2353279280, birthdate="14-01-1990", transfer_type=type_4
)
