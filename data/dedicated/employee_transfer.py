from data.dedicated.users_types import Entity, Laborer

employer = Entity(
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

laborer = Laborer(login_id=2289438844, birthdate="1976-10-20")
laborer_type_12 = Laborer(login_id=2493081331, birthdate="1990-01-03")
laborer_type_9 = Laborer(login_id=2021014218, birthdate="1982-10-18")
laborer_type_4_freedom_transfer = Laborer(login_id=2283737795, birthdate="1986-12-25")
laborer_type_4_direct_transfer = Laborer(login_id=2198951952, birthdate="1959-01-01")
laborer_type_4_absent = Laborer(login_id=2468727199, birthdate="1986-01-01")

laborer_between_my_establishments = Laborer(login_id=2016254472, birthdate="1976-01-01")
laborer_between_my_establishments_quota = Laborer(login_id=2111825226, birthdate="1976-01-01")

current_sponsor = Entity(
    login_id=1070495955,
    labor_office_id=1,
    sequence_number=24636,
    establishment_name_ar="شركة منتجات التغليف",
)

current_sponsor_type_12 = Entity(login_id=1046395800)
