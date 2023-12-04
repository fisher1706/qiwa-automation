import dataclasses

from data.user_management import user_management_data
from data.user_management.subscriptions_price_discount import (
    SubscriptionDefaultPrice,
    SubscriptionDiscount,
)
from data.user_management.user_management_users import (
    delegator_with_um,
    establishment_discount_val_0,
    establishment_discount_val_10,
    establishment_discount_val_25,
    establishment_type_four,
    establishment_type_one,
    owner_account,
    user_with_active_subscription,
    user_with_expired_subscription,
    user_with_terminated_subscription,
    user_without_subscription,
)


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
    # # pylint: disable=anomalous-backslash-in-string
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
    groups_data = [
        {
            "title": user_management_data.EMPLOYEE_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                user_management_data.PROFESSIONAL_VERIFICATION_SERVICE,
                user_management_data.OCCUPATIONAL_HEALTH_CERTIFICATE,
                user_management_data.WAGE_PROTECTION_CERTIFICATE,
                user_management_data.CHANGE_OCCUPATION,
                user_management_data.EMPLOYEE_TRANSFER,
                user_management_data.ISSUE_AND_RENEW_WORKING_PERMITS,
                user_management_data.VISA_ISSUANCE_SERVICE,
                user_management_data.AJEER_PROGRAM,
                user_management_data.WAGE_DISBURSEMENT,
                user_management_data.EMPLOYEE_INFORMATION,
                user_management_data.CONTRACT_MANAGEMENT,
                user_management_data.TRAINING_MANAGEMENT,
                user_management_data.RECRUITMENT_SERVICE,
                user_management_data.DEBT_CERTIFICATE,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                user_management_data.SAUDIZATION_CERTIFICATE,
                user_management_data.ESTABLISHMENT_DASHBOARD,
                user_management_data.BOOK_APPOINTMENT_SERVICE,
                user_management_data.LABOR_POLICIES,
                user_management_data.ENQUIRY_AND_VIEW_ESTABLISHMENT_VIOLATIONS,
                user_management_data.SALARY_CERTIFICATE,
                user_management_data.GOVERNMENT_CONTRACTS_MANAGEMENT,
                user_management_data.ESTABLISHMENT_FILE_MANAGEMENT,
                user_management_data.CLOSE_ESTABLISHMENT_ACTIVITY,
                user_management_data.CHANGE_ESTABLISHMENT_ACTIVITY,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_PERFORMANCE_GROUP_TITLE,
            "privileges": [
                user_management_data.NITAGAT_CALCULATOR,
                user_management_data.EADVISOR,
                user_management_data.LABOR_AWARD,
                user_management_data.LABOR_MARKET_INDEX,
                user_management_data.ESTABLISHMENT_PERFORMANCE_REPORT,
            ],
        },
        {
            "title": user_management_data.WORKSPACES_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                user_management_data.USER_MANAGEMENT,
                user_management_data.QIWA_WALLET,
                user_management_data.DELEGATIONS,
            ],
        },
    ]
    default_ui_privileges = [
        user_management_data.PROFESSIONAL_VERIFICATION_SERVICE,
        user_management_data.OCCUPATIONAL_HEALTH_CERTIFICATE,
        user_management_data.WAGE_PROTECTION_CERTIFICATE,
        user_management_data.SAUDIZATION_CERTIFICATE,
        user_management_data.ESTABLISHMENT_DASHBOARD,
        user_management_data.BOOK_APPOINTMENT_SERVICE,
        user_management_data.NITAGAT_CALCULATOR,
        user_management_data.EADVISOR,
        user_management_data.LABOR_AWARD,
        user_management_data.LABOR_MARKET_INDEX,
    ]

    ineligible_ui_privileges = [
        user_management_data.USER_MANAGEMENT,
        user_management_data.QIWA_WALLET,
        user_management_data.DELEGATIONS,
    ]


@dataclasses.dataclass
class ErrorsMessage:
    user_doesnt_have_access_to_um = "Sorry! You need permission to enter this page"


@dataclasses.dataclass
class SubscriptionData:
    subscription_data = [
        (
            establishment_discount_val_0,
            SubscriptionDefaultPrice.DEFAULT_PRICE_VAL_7000,
            SubscriptionDiscount.DISCOUNT_VAL_100,
        ),
        (
            establishment_discount_val_10,
            SubscriptionDefaultPrice.DEFAULT_PRICE_VAL_7000,
            SubscriptionDiscount.DISCOUNT_VAL_10,
        ),
        (
            establishment_discount_val_25,
            SubscriptionDefaultPrice.DEFAULT_PRICE_VAL_1100,
            SubscriptionDiscount.DISCOUNT_VAL_25,
        ),
        (
            establishment_type_four,
            SubscriptionDefaultPrice.DEFAULT_PRICE_VAL_10000,
            SubscriptionDiscount.DISCOUNT_VAL_100,
        ),
        (
            establishment_type_one,
            SubscriptionDefaultPrice.DEFAULT_PRICE_VAL_1100,
            SubscriptionDiscount.DISCOUNT_VAL_100,
        ),
    ]


@dataclasses.dataclass
class DefaultVatValue:
    default_vat_value = 1.15


@dataclasses.dataclass
class SubscriptionStatuses:
    active = 1
    expired = 2
    terminated = 3


@dataclasses.dataclass
class SelfSubscriptionData:
    self_subscription_data = [
        user_without_subscription,
        user_with_active_subscription,
        user_with_expired_subscription,
        user_with_terminated_subscription,
    ]
