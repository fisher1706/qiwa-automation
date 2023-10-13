from data.constants import UserType
from data.dedicated.models.laborer import Entity, Laborer
from data.dedicated.models.user import User

employer = User(
    personal_number="1016316828",
    labor_office_id="9",
    sequence_number="3212",
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد تجربة",
    establishment_number="1828954",
    name="عبدالله المولد",
)
employer_old = Entity(
    login_id=1016316828,
    labor_office_id=9,
    sequence_number=3212,
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد تجربة",
    establishment_number="1828954",
)
employer_between_my_establishments = Entity(
    login_id=1001982204,
    labor_office_id=16,
    sequence_number=2148,
    establishment_name_ar="مؤسسة دائره العلاقات عبداللة زكريا عبداللة المولد " "تجربة",
    establishment_number="16-2148",
)

laborer = Laborer(login_id=2449079728, birthdate="11-07-1993", user_type=UserType.EXPAT)
laborer_type_12 = Laborer(login_id=2493081331, birthdate="03-01-1990")
laborer_type_9 = Laborer(login_id=2021014218, birthdate="18-10-1982")
laborer_type_4_freedom_transfer = Laborer(login_id=2283737795, birthdate="25-12-1986")
laborer_type_4_direct_transfer = Laborer(login_id=2198951952, birthdate="01-01-1959")
laborer_type_4_absent = Laborer(login_id=2468727199, birthdate="01-01-1986")

laborer_between_my_establishments = Laborer(login_id=2016254472, birthdate="01-01-1976")
laborer_between_my_establishments_quota = Laborer(login_id=2111825226, birthdate="01-01-1976")

current_sponsor = Entity(
    login_id=1070495955,
    labor_office_id=1,
    sequence_number=24636,
    establishment_name_ar="شركة منتجات التغليف",
)

current_sponsor_type_12 = Entity(login_id=1046395800)
