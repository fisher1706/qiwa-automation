from data.dedicated.models.user import User

establishment_owner_with_two_partners = User(
    personal_number="1006434144", labor_office_id="1", sequence_number="1467826"
)

establishment_owner_with_one_partner = User(
    personal_number="1049956129", labor_office_id="1", sequence_number="85206"
)

establishment_owner_without_partners = User(
    personal_number="1052708888", labor_office_id="35", sequence_number="1566616"
)
