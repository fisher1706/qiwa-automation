from data.constants import Language
from data.dedicated.models.transfer_type import TransferType

type_4 = TransferType(
    code="4",
    name_ar="نقل عامل من منشأة اخرى",
    name_en="Transfer laborer from another establishment",
)
type_9 = TransferType(code="9", name_ar="نقل تابع", name_en="Dependent transfer")
type_12 = TransferType(code="12", name_ar="نقل عامل منزلي", name_en="Home Worker Transfer")

TRANSFER_REQUESTS = {Language.EN: "TRANSFER REQUESTS", Language.AR: "طلبات النقل"}
DASHBOARD = {Language.EN: "Dashboard", Language.AR: "لوحة المعلومات"}
EMPLOYEE_TRANSFER = {Language.EN: "Employee transfer", Language.AR: "نقل الخدمات"}
DESCRIPTION = {
    Language.EN: "You can request an employee transfer between your establishments & another business owner.",
    Language.AR: "باستطاعتك طلب نقل خدمات الموظف بين منشآتك أو من صاحب عمل آخر.",
}
ESTABLISHMENT_ID_LABEL = {Language.EN: "Establishment ID", Language.AR: "رقم المنشأة"}
ESTABLISHMENT_NAME_LABEL = {Language.EN: "Establishment name", Language.AR: "اسم المنشأة"}
SENT_REQUESTS = {Language.EN: "Sent Requests", Language.AR: "الطلبات المرسلة"}
RECEIVED_REQUESTS = {Language.EN: "Received requests", Language.AR: "الطلبات المستلمة"}
TERMS_POPUP_TITLE = {Language.EN: "TERMS & CONDITIONS", Language.AR: "الشروط والأحكام"}
TERMS_POPUP_DESCRIPTION = [
    {
        Language.EN: "Acknowledge the possibility of the transfer application being rejected by the Ministry of "
        "Interior for any reason.",
        Language.AR: "أقر بعلمي باحتمالية رفض وزارة الداخلية طلب النقل لأي سبب.",
    },
    {
        Language.EN: "I acknowledge and undertake to treat the transferred employee based on the Labor Law and "
        "its Executive Regulation and the decrees issued in implementation thereof.",
        Language.AR: "أتعهد بمعاملة الموظف المنقول وفقاً لنظام العمل ولائحته التنفيذية والقرارات الصادرة تنفيذاً "
        "له. ",
    },
    {
        Language.EN: "To benefit from the Freedom of transfer initiative, the establishment must be committed to "
        "the following:"
        "\n"
        "1. Authenticating all non Saudi employees contracts in QIWA by 20% ("
        "Contract Management Service)",
        Language.AR: "يجب أن تكون المنشأة مقدمة الطلب ملتزمة بالتالي لتتمكن من طلب نقل الموظف:"
        "\n"
        "1- توثيق جميع عقود العاملين في المنشأة بنسبة ٪؜20 في منصة قوى (خدمة توثيق عقود الموظفين)",
    },
]
TERMS_POPUP_BTN_APPROVE = {Language.EN: "Approve", Language.AR: "موافق"}
TITLE_FROM_ANOTHER_BUSINESS_OWNER = "FROM ANOTHER BUSINESS OWNER"
TITLE_TRANSFER_LABORER_BETWEEN_MY_ESTABLISHMENTS = "TRANSFER LABORER BETWEEN MY ESTABLISHMENTS"
POPUP_REDIRECTION_TITLE = "YOU WILL BE REDIRECTED"
POPUP_REDIRECTION_BODY = (
    "You will be redirected to Contracts Management service to edit the employee’s contract"
)
LABORER_STATUS_APPROVE = {
    Language.EN: "Pending For Current Employer Approval",
    Language.AR: "بانتظار موافقة صاحب العمل الحالي",
}
LABORER_TYPE_9_STATUS_APPROVE = {
    Language.EN: "Pending Completing Transfer in Absher by New Employer",
    Language.AR: "بانتظار استكمال عملية النقل في وزارة الداخلية بواسطة صاحب العمل الجديد",
}
LABORER_TYPE_4_FREEDOM_TRANSFER_STATUS_APPROVE = {
    Language.EN: "Pending for Notice Period Completion",
    Language.AR: "بانتظار إكمال فترة الإشعار",
}
LABORER_TYPE_4_DIRECT_TRANSFER_STATUS_APPROVE = {
    Language.EN: "Pending Completing Transfer in Absher by New Employer",
    Language.AR: "بانتظار استكمال عملية النقل في وزارة الداخلية بواسطة صاحب العمل الجديد",
}
LABORER_STATUS_REJECT = {Language.EN: "Rejected by Employee", Language.AR: "مرفوض من الموظف"}
SPONSOR_STATUS_APPROVE = {
    Language.EN: "Pending Completing Transfer in Absher by New Employer",
    Language.AR: "بانتظار استكمال عملية النقل في وزارة الداخلية بواسطة صاحب العمل الجديد",
}
SPONSOR_STATUS_REJECT = {
    Language.EN: "Rejected by Current Employer",
    Language.AR: "مرفوض من صاحب العمل الحالي",
}
REJECT_REASON = "I don’t want to be transferred"
HEADER_REQ_NUMBER = {Language.EN: "Req number", Language.AR: "رقم الطلب"}
HEADER_EMPLOYEE_NAME = {Language.EN: "Employee name", Language.AR: "اسم الموظف"}
HEADER_IQAMA_NUMBER = {Language.EN: "IQAMA number", Language.AR: "رقم الإقامة"}
HEADER_CURRENT_ESTABLISHMENT = {
    Language.EN: "Current establishment",
    Language.AR: "صاحب العمل الحالي",
}
HEADER_NEW_ESTABLISHMENT = {Language.EN: "New establishment", Language.AR: "المنشأة الجديدة"}
HEADER_STATUS = {Language.EN: "Status", Language.AR: "الحالة"}
HEADER_RELEASE_DATE = {
    Language.EN: "Release date",
    Language.AR: "تاريخ نهاية العلاقة التعاقدية",
}
HEADER_ACTIONS = {Language.EN: "Actions", Language.AR: "الإجراءات"}
HEADER_TITLES_LIST = [
    HEADER_REQ_NUMBER,
    HEADER_EMPLOYEE_NAME,
    HEADER_IQAMA_NUMBER,
    HEADER_CURRENT_ESTABLISHMENT,
    HEADER_NEW_ESTABLISHMENT,
    HEADER_STATUS,
    HEADER_RELEASE_DATE,
    HEADER_ACTIONS,
]
PLACEHOLDER_SEARCH = {Language.EN: "Search", Language.AR: "البحث"}
REQUEST_SUBMITTED = {Language.EN: "Request submitted", Language.AR: "البحث"}
REQUEST_CONFIRMED_BY_EMPLOYEE = {
    Language.EN: "Request confirmed by employee",
    Language.AR: "البحث",
}
REQUEST_CONFIRMED_BY_CURRENT_EMPLOYER = {
    Language.EN: "Request confirmed by current employer",
    Language.AR: "البحث",
}
REQUEST_CONFIRMED_BY_NIC = {Language.EN: "Request confirmed by NIC", Language.AR: "البحث"}
EXPECTED_DATE = [
    "Date: 20/09/2022",
    "Date: 20/09/2022",
    "Date: 21/09/2022",
    "Date: 22/09/2022",
]
