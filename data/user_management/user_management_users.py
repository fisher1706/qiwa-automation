from data.dedicated.models.user import User

owner_account = User(
    personal_number="1001530987",
    user_id=1666054,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

owner_account_with_another_company = User(
    personal_number="1001530987",
    user_id=1666054,
    labor_office_id=9,
    sequence_number=11871,
    unified_number_id=9086,
)

owner_account_for_expire_subscription = User(
    personal_number="1017836568",
    user_id=2292101,
    labor_office_id=9,
    sequence_number=1196371,
    unified_number_id=1315525,
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

delegator_for_add_and_terminate_subscription_flow = User(
    personal_number="1028056867",
    user_id=91912,
    labor_office_id=9,
    sequence_number=11871,
    unified_number_id=9086,
)

delegator_for_full_terminate_flow = User(
    personal_number="1100824174",
    user_id=2082702,
    labor_office_id=9,
    sequence_number=11871,
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
    personal_number="1014157000",
    user_id=1668068,
    labor_office_id=9,
    sequence_number=1196371,
    unified_number_id=1315525,
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

user_type_three_employee = User(
    personal_number="1070111305",
    user_id=1668068,
    labor_office_id=1,
    sequence_number=1910,
    unified_number_id=9086,
)

user_type_three_employee_for_add_access = User(
    personal_number="1070111305",
    user_id=1668068,
    labor_office_id=15,
    sequence_number=2722,
    unified_number_id=9086,
)

establishment_type_one = User(
    personal_number="1023450479",
    user_id=33707906,
    labor_office_id=17,
    sequence_number=95885,
)

establishment_type_four = User(
    personal_number="1019974839",
    user_id=2291009,
    labor_office_id=9,
    sequence_number=93886,
)

establishment_discount_val_0 = User(
    personal_number="1014851610",
    user_id=2291008,
    labor_office_id=1,
    sequence_number=70289,
)

establishment_discount_val_25 = User(
    personal_number="1009999341",
    user_id=1372659,
    labor_office_id=9,
    sequence_number=77683,
)

establishment_discount_val_10 = User(
    personal_number="1019974839",
    user_id=2291009,
    labor_office_id=9,
    sequence_number=1680894,
)

user_with_active_subscription = User(
    personal_number="1055034217",
    user_id=1588485,
    labor_office_id=14,
    sequence_number=117,
)

user_with_expired_subscription = User(
    personal_number="1013051097",
    labor_office_id=25,
    sequence_number=1769868,
    unified_number_id=1849511,
)

user_with_terminated_subscription = User(
    personal_number="1039949845",
    user_id=1644420,
    labor_office_id=8,
    sequence_number=1837074,
)

user_without_subscription = User(
    personal_number="1012365118",
    labor_office_id=1,
    sequence_number=66754,
    unified_number_id=151472,
)
