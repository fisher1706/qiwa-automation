from dataclasses import dataclass

from data.constants import UserInfo


@dataclass
class Entity:  # pylint: disable=duplicate-code
    personal_number: str
    password: str
    user_id: int


@dataclass
class EntityUser(Entity):  # pylint: disable=duplicate-code
    labor_office_id: int
    sequence_number: int
    unified_number_id: int


UM_OWNER = EntityUser(
    personal_number="1020872030",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=10,
    sequence_number=1525921,
    unified_number_id=423722,
)

OWNER_FOR_INVOICE = EntityUser(
    personal_number="1000807006",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=1,
    sequence_number=0,
    unified_number_id=0,
)

OWNER = EntityUser(
    personal_number="1040521757",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=6,
    sequence_number=63,
    unified_number_id=166,
)

OWNER_TERM = EntityUser(
    personal_number="1077493508",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=2,
    sequence_number=0,
    unified_number_id=0,
)

ADMIN = EntityUser(
    personal_number="1077493508",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=0,
    unified_number_id=1290380,
)

ADMIN_NOT_EMPLOYEE = EntityUser(
    personal_number="1108959485",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=0,
    unified_number_id=1124274,
)

USER_ADMIN = EntityUser(
    personal_number="1035661949",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=1,
    sequence_number=0,
    unified_number_id=0,
)

USER = EntityUser(
    personal_number="1048924474",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=0,
    unified_number_id=1235074,
)

USER_EXPIRED = EntityUser(
    personal_number="1070204233",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=0,
    unified_number_id=423722,
)

USER_TO_SUBSCRIBE1 = EntityUser(
    personal_number="1028655841",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=2,
    sequence_number=0,
    unified_number_id=0,
)

USER_TO_SUBSCRIBE2 = EntityUser(
    personal_number="1005832199",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=4,
    sequence_number=0,
    unified_number_id=0,
)

USER_MANY_COMPANIES = EntityUser(
    personal_number="1031732579",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=34,
    sequence_number=0,
    unified_number_id=382632,
)

OWNER_EXP = EntityUser(
    personal_number="1009442136",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=9,
    sequence_number=0,
    unified_number_id=1686257,
)

OWNER_FOR_RENEW = EntityUser(
    personal_number="1048398877",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=1,
    sequence_number=0,
    unified_number_id=0,
)

USER_FOR_RENEW = EntityUser(
    personal_number="1004020473",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=11,
    sequence_number=0,
    unified_number_id=1626370,
)

USER_UM = EntityUser(
    personal_number="1106495433",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=10,
    unified_number_id=0,
)

USER_UM2 = EntityUser(
    personal_number="1008426114",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=4,
    sequence_number=0,
    unified_number_id=0,
)

UM2_COMPANY_ID = "4-5524"

OWNER_WITHOUT_SUBSCRIPTION = EntityUser(
    personal_number="1028471850",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=9,
    sequence_number=14536,
    unified_number_id=118676,
)

OWNER_SECOND_SUBS = EntityUser(
    personal_number="1037078068",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=1,
    sequence_number=232562,
    unified_number_id=0,
)

OWNER_THIRD_SUBS = EntityUser(
    personal_number="1019626694",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=1,
    sequence_number=56150,
    unified_number_id=0,
)

OWNER_SELF_SUBS = EntityUser(
    personal_number="1035497096",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=23,
    sequence_number=19679,
    unified_number_id=560309,
)
OWNER_SELF_SUBS_COMPANY = "23-19679"

COMPANY_OWNER = EntityUser(
    personal_number="1009823517",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=9,
    sequence_number=0,
    unified_number_id=0,
)
EXPIRED_DATE = "2023-05-10"
COMPANY_NAME = "15-1944459"
