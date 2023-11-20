import dataclasses

from data.user_management import privileges_data
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
            "title": privileges_data.EMPLOYEE_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                privileges_data.PROFESSIONAL_VERIFICATION_SERVICE,
                privileges_data.OCCUPATIONAL_HEALTH_CERTIFICATE,
                privileges_data.WAGE_PROTECTION_CERTIFICATE,
                privileges_data.CHANGE_OCCUPATION,
                privileges_data.EMPLOYEE_TRANSFER,
                privileges_data.ISSUE_AND_RENEW_WORKING_PERMITS,
                privileges_data.VISA_ISSUANCE_SERVICE,
                privileges_data.AJEER_PROGRAM,
                privileges_data.WAGE_DISBURSEMENT,
                privileges_data.EMPLOYEE_INFORMATION,
                privileges_data.CONTRACT_MANAGEMENT,
                privileges_data.TRAINING_MANAGEMENT,
                privileges_data.RECRUITMENT_SERVICE,
                privileges_data.DEBT_CERTIFICATE,
            ],
        },
        {
            "title": privileges_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                privileges_data.SAUDIZATION_CERTIFICATE,
                privileges_data.ESTABLISHMENT_DASHBOARD,
                privileges_data.BOOK_APPOINTMENT_SERVICE,
                privileges_data.LABOR_POLICIES,
                privileges_data.ENQUIRY_AND_VIEW_ESTABLISHMENT_VIOLATIONS,
                privileges_data.SALARY_CERTIFICATE,
                privileges_data.GOVERNMENT_CONTRACTS_MANAGEMENT,
                privileges_data.ESTABLISHMENT_FILE_MANAGEMENT,
                privileges_data.CLOSE_ESTABLISHMENT_ACTIVITY,
                privileges_data.CHANGE_ESTABLISHMENT_ACTIVITY,
            ],
        },
        {
            "title": privileges_data.ESTABLISHMENT_PERFORMANCE_GROUP_TITLE,
            "privileges": [
                privileges_data.NITAGAT_CALCULATOR,
                privileges_data.EADVISOR,
                privileges_data.LABOR_AWARD,
                privileges_data.LABOR_MARKET_INDEX,
                privileges_data.ESTABLISHMENT_PERFORMANCE_REPORT,
            ],
        },
        {
            "title": privileges_data.WORKSPACES_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                privileges_data.USER_MANAGEMENT,
                privileges_data.QIWA_WALLET,
                privileges_data.DELEGATIONS,
            ],
        },
    ]
    default_ui_privileges = [
        privileges_data.PROFESSIONAL_VERIFICATION_SERVICE,
        privileges_data.OCCUPATIONAL_HEALTH_CERTIFICATE,
        privileges_data.WAGE_PROTECTION_CERTIFICATE,
        privileges_data.SAUDIZATION_CERTIFICATE,
        privileges_data.ESTABLISHMENT_DASHBOARD,
        privileges_data.BOOK_APPOINTMENT_SERVICE,
        privileges_data.NITAGAT_CALCULATOR,
        privileges_data.EADVISOR,
        privileges_data.LABOR_AWARD,
        privileges_data.LABOR_MARKET_INDEX,
    ]

    ineligible_ui_privileges = [
        privileges_data.USER_MANAGEMENT,
        privileges_data.QIWA_WALLET,
        privileges_data.DELEGATIONS,
    ]


@dataclasses.dataclass
class ErrorsMessage:
    user_doesnt_have_access_to_um = "Sorry! You need permission to enter this page"


@dataclasses.dataclass
class SubscriptionData:
    subscription_data = [
        (
            establishment_discount_val_0,
            SubscriptionDefaultPrice.default_price_val_7000,
            SubscriptionDiscount.discount_val_100,
        ),
        (
            establishment_discount_val_10,
            SubscriptionDefaultPrice.default_price_val_7000,
            SubscriptionDiscount.discount_val_25,
        ),
        (
            establishment_discount_val_25,
            SubscriptionDefaultPrice.default_price_val_1100,
            SubscriptionDiscount.discount_val_10,
        ),
        (
            establishment_type_four,
            SubscriptionDefaultPrice.default_price_val_10000,
            SubscriptionDiscount.discount_val_100,
        ),
        (
            establishment_type_one,
            SubscriptionDefaultPrice.default_price_val_1100,
            SubscriptionDiscount.discount_val_100,
        ),
    ]


@dataclasses.dataclass
class DefaultVatValue:
    default_vat_value = 1.15
