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
    owner_with_active_subscription,
    owner_with_expired_subscription_always,
    owner_without_subscription_always,
)


@dataclasses.dataclass
class Texts:
    subscription_info = (
        "Subscription is valid for all establishments within your Establishment Group. We will inform you 30 days "
        "before its expiration."
    )
    establishment_user_details = "Establishment Delegator details"
    add_new_workspace_user = "Add new Establishment Delegator"
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
    allowed_access = "توجد صلاحية"
    establishment_name = "اسم المنشأة"
    establishment_id = "رقم المنشأة"
    privileges = "الصلاحيات"
    actions = "الإجراءات"
    establishment_delegator_details_breadcrumbs = "تفاصيل مفوض المنشأة"
    add_access_btn = "إضافة الصلاحية"
    title_on_add_access_modal = "اختيار صلاحيات المستخدم على المنشآت المختارة"
    selected_establishment_text_on_add_access_modal = "المنشآت المختارة"
    all_privileges = "جميع الصلاحيات"
    hide_privileges = "إخفاء الصلاحيات الغير مختارة"
    show_more_privileges_for_2nd_group = "إظهار {} الصلاحيات الغير مختارة"
    occupation_management_description = (
        "إذا قمت باختيار هذه الصلاحية, سيتم اختيارصلاحية معلومات الموظفين تلقائياً"
    )
    employee_transfer_description = (
        "إذا قمت باختيار هذه الصلاحية, سيتم اختيارصلاحية معلومات الموظفين و إدارة العقود تلقائياً"
    )
    issue_working_permits_description = (
        "إذا قمت باختيار هذه الصلاحية, سيتم اختيارصلاحية معلومات الموظفين تلقائياً"
    )
    edit_user_privileges_btn = "تعديل صلاحيات المستخدم"
    title_on_edit_privileges_modal = "تعديل صلاحيات المستخدم على المنشأة"
    remove_access_btn = "إزالة المستخدم"
    save_and_close_btn = "حفظ وإغلاق"


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
                user_management_data.WAGE_PROTECTION_CERTIFICATE,
                user_management_data.OCCUPATION_MANAGEMENT,
                user_management_data.EMPLOYEE_TRANSFER,
                user_management_data.ISSUE_AND_RENEW_WORKING_PERMITS,
                user_management_data.VISA_ISSUANCE_SERVICE,
                user_management_data.WAGE_DISBURSEMENT,
                user_management_data.EMPLOYEE_INFORMATION,
                user_management_data.CONTRACT_MANAGEMENT,
                user_management_data.TRAININGS_MANAGEMENT,
                user_management_data.RECRUITMENT_SERVICE,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE,
            "privileges": [
                user_management_data.NATIONALIZATION_CERTIFICATE,
                user_management_data.ESTABLISHMENT_DASHBOARD,
                user_management_data.BOOK_APPOINTMENT_SERVICE,
                user_management_data.INTERNAL_WORK_POLICY,
                user_management_data.ENQUIRY_AND_VIEW_ESTABLISHMENT_VIOLATIONS,
                user_management_data.SALARY_CERTIFICATE,
                user_management_data.NATIONALIZATION_OF_OPERATION,
                user_management_data.ESTABLISHMENT_FILE_MANAGEMENT,
                user_management_data.CLOSE_ESTABLISHMENT_ACTIVITY,
                user_management_data.CHANGE_ESTABLISHMENT_ACTIVITY,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_PERFORMANCE_GROUP_TITLE,
            "privileges": [
                user_management_data.NITAGAT_CALCULATOR,
                user_management_data.INDICATORS,
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
    groups_data_ar = [
        {
            "title": user_management_data.EMPLOYEE_MANAGEMENT_GROUP_TITLE_AR,
            "privileges": [
                user_management_data.WAGE_PROTECTION_CERTIFICATE_AR,
                user_management_data.OCCUPATION_MANAGEMENT_AR,
                user_management_data.EMPLOYEE_TRANSFER_AR,
                user_management_data.ISSUE_AND_RENEW_WORKING_PERMITS_AR,
                user_management_data.VISA_ISSUANCE_SERVICE_AR,
                user_management_data.WAGE_DISBURSEMENT_AR,
                user_management_data.EMPLOYEE_INFORMATION_AR,
                user_management_data.CONTRACT_MANAGEMENT_AR,
                user_management_data.TRAININGS_MANAGEMENT_AR,
                user_management_data.RECRUITMENT_SERVICE_AR,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE_AR,
            "privileges": [
                user_management_data.NATIONALIZATION_CERTIFICATE_AR,
                user_management_data.ESTABLISHMENT_DASHBOARD_AR,
                user_management_data.BOOK_APPOINTMENT_SERVICE_AR,
                user_management_data.INTERNAL_WORK_POLICY_AR,
                user_management_data.ENQUIRY_AND_VIEW_ESTABLISHMENT_VIOLATIONS_AR,
                user_management_data.SALARY_CERTIFICATE_AR,
                user_management_data.NATIONALIZATION_OF_OPERATION_AR,
                user_management_data.ESTABLISHMENT_FILE_MANAGEMENT_AR,
                user_management_data.CLOSE_ESTABLISHMENT_ACTIVITY_AR,
                user_management_data.CHANGE_ESTABLISHMENT_ACTIVITY_AR,
            ],
        },
        {
            "title": user_management_data.ESTABLISHMENT_PERFORMANCE_GROUP_TITLE_AR,
            "privileges": [
                user_management_data.NITAGAT_CALCULATOR_AR,
                user_management_data.INDICATORS_AR,
                user_management_data.LABOR_MARKET_INDEX_AR,
                user_management_data.ESTABLISHMENT_PERFORMANCE_REPORT_AR,
            ],
        },
        {
            "title": user_management_data.WORKSPACES_MANAGEMENT_GROUP_TITLE_AR,
            "privileges": [
                user_management_data.USER_MANAGEMENT_AR,
                user_management_data.QIWA_WALLET_AR,
                user_management_data.DELEGATIONS_AR,
            ],
        },
    ]

    default_ui_privileges = [
        user_management_data.WAGE_PROTECTION_CERTIFICATE,
        user_management_data.NATIONALIZATION_CERTIFICATE,
        user_management_data.ESTABLISHMENT_DASHBOARD,
        user_management_data.BOOK_APPOINTMENT_SERVICE,
        user_management_data.NITAGAT_CALCULATOR,
        user_management_data.INDICATORS,
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
    no_access_error_description = "You have no permission to access this part of the platform."


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
    all_users = [
        ("active", owner_with_active_subscription),
        ("without", owner_without_subscription_always),
        ("expired", owner_with_expired_subscription_always),
    ]


@dataclasses.dataclass
class RenewPageData:
    COUNT_GROUP_MANAGER_CONTENT = 4
    COUNT_ESTABLISHMENT_GROUP_DETAILS_CONTENT = 2
    COUNT_ESTABLISHMENT_SUBSCRIPTION_CONTENT_NEW = 5
    COUNT_ESTABLISHMENT_SUBSCRIPTION_CONTENT_EXPIRED = 5
    COUNT_SUMMARY_CONTENT = 6


@dataclasses.dataclass
class ThankYouPageData:
    COUNT_EXPIRED_SUBSCRIPTION = 11
    COUNT_NEW_SUBSCRIPTION = 12


@dataclasses.dataclass
class EstablishmentAddresses:
    initial_address = [7492, 2899, 8, "حي الشرفية", "ذو النورين", 23218]
    updated_address = [4594, 7551, 392, "الربوة", "الحميدات", 12814]
    country = user_management_data.COUNTRY
    district_en = "Al Rayan Dist."
    street_en = "Kharis Branch Rd"
    final_updated_address = [
        user_management_data.UPDATED_BUILDING_NUMBER,
        user_management_data.UPDATED_STREET,
        user_management_data.UPDATED_STREET,
        user_management_data.UPDATED_CITY_AR,
        user_management_data.UPDATED_CITY,
        user_management_data.UPDATED_DISTRICT,
        user_management_data.UPDATED_DISTRICT,
        user_management_data.UPDATED_ADDITIONAL_NUMBER,
    ]
    vat_number = "300559557700003"

    update_address_data_on_ui = [
        user_management_data.UPDATED_CITY,
        user_management_data.UPDATED_DISTRICT,
        user_management_data.UPDATED_STREET,
        user_management_data.UPDATED_BUILDING_NUMBER,
        user_management_data.UPDATED_ADDITIONAL_NUMBER,
    ]
    updated_address_data_on_thank_you_popup = [
        user_management_data.COUNTRY,
        user_management_data.UPDATED_CITY,
        user_management_data.UPDATED_DISTRICT,
        user_management_data.UPDATED_BUILDING_NUMBER,
        user_management_data.UPDATED_STREET,
        str(user_management_data.UPDATED_ADDITIONAL_NUMBER),
    ]

    updated_address_data_on_confirmation_page = [
        user_management_data.COUNTRY,
        user_management_data.UPDATED_CITY,
        user_management_data.UPDATED_DISTRICT,
        user_management_data.UPDATED_STREET,
        user_management_data.UPDATED_BUILDING_NUMBER,
        str(user_management_data.UPDATED_ADDITIONAL_NUMBER),
    ]
