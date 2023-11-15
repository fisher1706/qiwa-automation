from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User

employer = User(personal_number="1017462894", labor_office_id="4", sequence_number="1083411")

laborer = Laborer(login_id=2289438844, birthdate="20-10-1976")
laborer_saudi = Laborer(login_id=2144197874, birthdate="01-01-1977")
laborer_saudi_not_in_the_establishment = Laborer(login_id=1061653844, birthdate="08-06-1402")
laborer_expatriate = Laborer(login_id=2243635881, birthdate="01-01-1980")
laborer_expatriate_not_in_the_establishment = Laborer(login_id=2191542147, birthdate="01-01-1978")
