import dataclasses

from data.user_management.user_management_users import delegator_with_um, owner_account, \
    user_1380, user_1265, user_11500


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

    establishment_user_details = "تفاصيل مفوض المنشأة"
    full_name = "الاسم الكامل"
    subscription_period = "مدة الاشتراك"
    national_id = "رقم الهوية"
    subscription_expiry_date = "تاريخ انتهاء الاشتراك"
    terminate_btn = "إنهاء اشتراك المستخدم من جميع المنشآت"
    terminate_text = "سيتم إزالة هذا المستخدم من جميع المنشآت التابعة للرقم الموحد, وسيتم إنهاء الاشتراك الخاص به"
    search = "بحث"
    establishment_table_title = "جميع المنشآت التابعة للرقم الموحد"
    establishment_table_text = (
        "الرجاء اختيار المنشأة\المنشآت التي سيتم تعديل صلاحيات المستخدم عليها"
    )
    no_access = "لا توجد صلاحية"
    establishment_name = "اسم المنشأة"
    establishment_id = "رقم المنشأة"
    privileges = "الصلاحيات"
    actions = "الإجراءات"
    establishment_delegator_details_breadcrumbs = "تفاصيل مفوض المنشأة"


@dataclasses.dataclass
class PaymentHeaders:
    authorization = "Bearer a1671885-e44b-4a2d-bc5a-3a8756892847"


@dataclasses.dataclass
class SelfSubscriptionType:
    subscription_type = ["extend", "renew-expired", "renew-terminated"]


@dataclasses.dataclass
class UsersTypes:
    users = [owner_account, delegator_with_um]


@dataclasses.dataclass
class Privileges:
    default_privileges = [1, 5, 8, 11, 13, 16, 20, 23, 29, 31]


@dataclasses.dataclass
class ErrorsMessage:
    user_doesnt_have_access_to_um = "Sorry! You need permission to enter this page"


@dataclasses.dataclass
class SubscriptionUsers:
    subscription_users = [user_1380, user_1265, user_11500]


@dataclasses.dataclass
class DefaultPercentValue:
    percent_value = 1.15
