import dataclasses


@dataclasses.dataclass
class Texts:
    SUBSCRIPTION_INFO = (
        "Subscription is valid for all establishments within your establishment group. You will be "
        "informed 30 days before expiry of your subscription."
    )
    Workspace_User_Details = "Workspace User Details"
    Add_New_Workspace_User = "Add new Workspace User"
    Establishment_And_User_Details = "Establishment and user details"


@dataclasses.dataclass
class ArabicTranslations:
    User_Management_Title = "إدارة صلاحيات مستخدمي المنشأة"
    Add_New_User_Btn = "إضافة مستخدم جديد"
    Your_Subscription_Title = "اشتراكك"
    User_Role = "مالك المنشأة"
    Subscription_Valid_Until = "الاشتراك صالح لغاية"
    SUBSCRIPTION_Info_Text = (
        "الاشتراك فعال لكافة المنشآت التابعة للرقم الوطني الموحد. سيتم إعلامك خلال 30 يوم من "
        "تاريخ انتهاء الاشتراك لتجديد الاشتراك"
    )
    Extend_Subscription_Btn = "تمديد الاشتراك"
    How_To_Renew_Btn = "كيفية تجديد الاشتراك؟"
    Search = "بحث"
