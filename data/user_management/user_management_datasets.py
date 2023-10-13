import dataclasses

from data.user_management.user_management_users import delegator_with_um, owner_account


@dataclasses.dataclass
class Texts:
    subscription_info = (
        "Subscription is valid for all establishments within your Establishment Group. We will inform you 30 days "
        "before its expiration."
    )
    establishment_user_details = "Establishment Delegator details"
    add_new_workspace_user = "Add new Workspace User"
    establishment_and_user_details = "Establishment and user details"


@dataclasses.dataclass
class ArabicTranslations:
    user_management_title = "إدارة صلاحيات مستخدمي المنشأة"
    add_new_user_btn = "إضافة مستخدم جديد"
    user_role = "مالك المنشأة"
    subscription_valid_until = "الاشتراك صالح لغاية"
    renew_info = "الاشتراك ساري المفعول لجميع المنشآت ضمن مجموعة المنشآت. سيتم إبلاغك قبل 30 يوم من انتهاء الاشتراك."
    how_to_renew_btn = "كيفية تجديد الاشتراك؟"


@dataclasses.dataclass
class PaymentHeaders:
    authorization = "Bearer a1671885-e44b-4a2d-bc5a-3a8756892847"


@dataclasses.dataclass
class SelfSubscriptionType:
    subscription_type = ["extend", "renew-expired", "renew-terminated"]


@dataclasses.dataclass
class UsersTypes:
    users = [owner_account, delegator_with_um]
