from data.dedicated.employee_trasfer.employee_transfer_constants import type_9
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User

employer = User(
    personal_number="1014882284",
    labor_office_id="1",
    sequence_number="4533",
)

laborer = Laborer(login_id=2449079728, birthdate="11-07-1993", transfer_type=type_9)
