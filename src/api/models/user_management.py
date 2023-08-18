from dataclasses import dataclass

from data.constants import UserInfo


@dataclass
class Entity:
    personal_number: str
    password: str
    user_id: int


@dataclass
class EntityUser(Entity):
    labor_office_id: int
    sequence_number: int
    unified_number_id: int


class EntityOwner:
    def __init__(self, labor_office_id=None, sequence_number=None, unified_number_id=None):
        self.account = None
        self.labor_office_id = labor_office_id
        self.sequence_number = sequence_number
        self.unified_number_id = unified_number_id

    def build_account(self, personal_number: str, password: str, user_id: int):
        self.account = Entity(personal_number, password, user_id)
        return self


owner_main = EntityOwner(
    labor_office_id=1, sequence_number=1329851, unified_number_id=1655833
).build_account(personal_number="1113805822", password=UserInfo.PASSWORD, user_id=2290655)

owner_for_free_flow = EntityOwner(
    labor_office_id=3, sequence_number=8901, unified_number_id=145458
).build_account(personal_number="1000238269", password=UserInfo.PASSWORD, user_id=0)

owner_one_subscription = EntityOwner(
    labor_office_id=5, sequence_number=8112, unified_number_id=384302
).build_account(personal_number="1016989954", password=UserInfo.PASSWORD, user_id=1953660)

owner_without_confirmed_email = EntityOwner(
    labor_office_id=15, sequence_number=1545426, unified_number_id=1221774
).build_account(personal_number="1010407490", password=UserInfo.PASSWORD, user_id=1238032)

owner_unsubscribed = EntityOwner(
    labor_office_id=1, sequence_number=1839687, unified_number_id=1334704
).build_account(personal_number="1000366151", password=UserInfo.PASSWORD, user_id=2283373)

owner_expired = EntityOwner(
    labor_office_id=1, sequence_number=57247, unified_number_id=116427
).build_account(personal_number="2467037269", password=UserInfo.PASSWORD, user_id=1211087)

owner_without_vat = EntityOwner(
    labor_office_id=3, sequence_number=1677128, unified_number_id=1808274
).build_account(personal_number="1076532652", password=UserInfo.PASSWORD, user_id=1993901)

owner_for_terminate = EntityOwner(
    labor_office_id=13, sequence_number=3945, unified_number_id=98270
).build_account(personal_number="1012836118", password=UserInfo.PASSWORD, user_id=1679084)

owner_with_subscription_and_without_email = EntityOwner(
    labor_office_id=4, sequence_number=1765278, unified_number_id=1484330
).build_account(personal_number="1012957096", password=UserInfo.PASSWORD, user_id=2176069)

soon_expired_owner = EntityOwner(
    labor_office_id=6, sequence_number=1703232, unified_number_id=844798
).build_account(personal_number="1057996801", password=UserInfo.PASSWORD, user_id=1317147)

soon_expired_admin = EntityUser(
    personal_number="1040158725",
    password=UserInfo.PASSWORD,
    user_id=1314327,
    labor_office_id=6,
    sequence_number=1703232,
    unified_number_id=844798,
)

admin_main = EntityUser(
    personal_number="1010259115",
    password=UserInfo.PASSWORD,
    user_id=2290654,
    labor_office_id=1,
    sequence_number=1672686,
    unified_number_id=1655833,
)

admin_unsubscribed = EntityUser(
    personal_number="1075733129",
    password=UserInfo.PASSWORD,
    user_id=2283302,
    labor_office_id=1,
    sequence_number=1892017,
    unified_number_id=1919009,
)

admin_for_terminate = EntityUser(
    personal_number="1029204029",
    password=UserInfo.PASSWORD,
    user_id=1665765,
    labor_office_id=1,
    sequence_number=1665765,
    unified_number_id=325106,
)

user_subscribed = EntityUser(
    personal_number="1005717192",
    password=UserInfo.PASSWORD,
    user_id=1921851,
    labor_office_id=1,
    sequence_number=8370,
    unified_number_id=0,
)

user_subscribed_2 = EntityUser(
    personal_number="1030792319",
    password=UserInfo.PASSWORD,
    user_id=1921851,
    labor_office_id=1,
    sequence_number=8370,
    unified_number_id=0,
)

user_for_free_flow = EntityUser(
    personal_number="1050093960",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=3,
    sequence_number=28200,
    unified_number_id=145458,
)

user_unsubscribed = EntityUser(
    personal_number="1063269912",
    password=UserInfo.PASSWORD,
    user_id=1019286,
    labor_office_id=3,
    sequence_number=1677128,
    unified_number_id=0,
)

user_unsubscribed_2 = EntityUser(
    personal_number="1086015417",
    password=UserInfo.PASSWORD,
    user_id=1185412,
    labor_office_id=1,
    sequence_number=1673532,
    unified_number_id=0,
)

user_not_registered = EntityUser(
    personal_number="1119936712",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=3,
    sequence_number=28200,
    unified_number_id=145458,
)

terminated_user = EntityUser(
    personal_number="1126654399",
    password=UserInfo.PASSWORD,
    user_id=1903117,
    labor_office_id=1,
    sequence_number=1905512,
    unified_number_id=325106,
)

terminated_user_2 = EntityUser(
    personal_number="1027551009",
    password=UserInfo.PASSWORD,
    user_id=1469836,
    labor_office_id=1,
    sequence_number=1905512,
    unified_number_id=325106,
)

expired_user = EntityUser(
    personal_number="1038008577",
    password=UserInfo.PASSWORD,
    user_id=0,
    labor_office_id=0,
    sequence_number=0,
    unified_number_id=0,
)

test_owner = EntityOwner(
    labor_office_id=9, sequence_number=21652, unified_number_id=157601
).build_account(personal_number="1032601518", password=UserInfo.PASSWORD, user_id=686399)


test_account_um_2 = EntityOwner(
    labor_office_id=1, sequence_number=1722642, unified_number_id=622323
).build_account(personal_number="1058873835", password=UserInfo.PASSWORD, user_id=465611)
