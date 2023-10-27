from data.dedicated.models.user import User

owner_account = User(
    personal_number="1001530987",
    user_id=1666054,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

delegator_for_owner_new_flow = User(
    personal_number="1615428222",
    user_id=1082,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

delegator_for_edit_flow = User(
    personal_number="1096471568",
    user_id=1666054,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

delegator_with_um = User(
    personal_number="1019865797",
    user_id=1667090,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

delegator_without_um = User(
    personal_number="1070111305",
    user_id=1668068,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

owner_for_self = User(
    personal_number="1001340536",
    user_id=963397,
    labor_office_id=4,
    sequence_number=1378802,
    unified_number_id=2099251,
)

terminated_owner = User(
    personal_number="1050705357",
    user_id=1872092,
    labor_office_id=1,
    sequence_number=59989,
    unified_number_id=121173,
)
