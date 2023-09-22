from dataclasses import dataclass

HEADERS = {
    "X-IBM-Client-Id": "514c55d8eb39044a69c1e9ab434ff616",
    "X-IBM-Client-Secret": "4e2b5e46d09fec6775177730e3b44aaf",
    "Content-Type": "application/json",
}


@dataclass
class Language:
    EN = "en"
    AR = "ar"


class UserType:  # pylint: disable=too-few-public-methods
    SAUDI = "saudi"
    EXPAT = "expat"
    BORDER = "border"
    USER = "user"
    MEMBER = "member"


@dataclass
class EmailConst:  # pylint: disable=too-few-public-methods
    INBOX_FOLDER = '"Inbox"'
    UNSEEN_EMAILS = "UNSEEN"
    IMAP_SESSION_ACTIVE = "SELECTED"
    EMAIL_FORMAT = "(RFC822)"
    IMAP_DOMAIN = "imap.gmail.com"
    STATUS_OK = "OK"
    FLAG_SEEN = r"\Seen"
    ADD_FLAG = "+FLAGS"


@dataclass
class UserInfo:
    PASSWORD = "123456789aA@"
    CHANGED_PASSWORD = "123456789aA@!#"
    INVALID_PASSWORD = "Invalid"
    EXPIRED_DATE = "2023-05-10"


@dataclass
class EServiceAction:
    TRANSFER_TO_COMPANY = "Transfer to company"
    TRANSFER_BETWEEN_BRANCHES = "Transfer between branches"
    SUBMIT_REQUEST = "Submit request"
    VIEW_REQUEST = "View requests"
    ESTABLISHMENTS_USERS = "Establishment Users"
    SUBSCRIBE_NEW_USER = "Subscribe New User"
    CONTRACT_MANAGEMENT = "Request Service"


@dataclass
class EService:
    CHANGE_OCCUPATION = "Change Occupation"
    NITAQAT_CALCULATOR = "Nitaqat calculator"
    WORK_PERMIT = "Issue & Renew Working Permits"
    TRANSFER_WORKER = "Transferring worker"
    SAUDIZATION_CERTIFICATE = "Saudization certificate"
    USER_MANAGEMENT = "User Management"
    VALIDATION_CERTIFICATE = "Validation Certificate"
    EMPLOYEE_TRANSFER = "Employee Transfer"
    CONTRACT_MANAGEMENT = "Contract Management"
    ALL_SERVICES = [
        "Contract Management",
        "Issue & Renew Working Permits New",
        "Issue & Renew Working Permits",
        "Labor Award",
        "Delegation",
        "Wage Protection System Certificate",
        "Seasonal Visa",
        "Ajeer Program",
        "Compliance Index",
        "Wage Disbursement",
        "Violation Service",
        "Visa Issuance Service",
        "Company Performance Report",
        "Nitaqat Calculator",
        "Saudization Certificate",
        "User Management",
        "Object Exit Visa Service",
        "Change Occupation",
        "Validation Certificate",
        "Labor Policies",
    ]


@dataclass
class EmployeeTransfer:
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
    LABORER_STATUS_REJECT = {Language.EN: "Rejected by Laborer", Language.AR: "مرفوض من الموظف"}
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


@dataclass
class ContractManagement:
    VERIFICATION_CODE = {Language.EN: "Verification Code", Language.AR: "رمز التحقق"}
    TITLE = {Language.EN: "Contract Management", Language.AR: "إدارة العقود"}
    DESCRIPTION = {
        Language.EN: "A service provided to establishments on Qiwa platform to create and authenticate employee "
        "contracts digitally. After the contract gets created and submitted, it will be sent to the "
        "employee’s account on Qiwa for approval or rejection.",
        Language.AR: "خدمة تتيح للمنشآت إنشاء وتوثيق وإنهاء عقود الموظفين إلكترونيًا، وبعد إنشاء العقد الوظيفي يمكن "
        "للموظف الموافقة على العقد أو رفضه أو طلب تعديله عبر حسابه في قوى أفراد. وفي حال موافقة الطرفين "
        "يعتبر العقد موثق من وزارة الموارد البشرية والتنمية الاجتماعية",
    }
    CONTRACT_AUTHENTICATION_SCORE_FOR_SAUDI_EMPLOYEES = {
        Language.EN: "Contract Authentication Score for Saudi Employees",
        Language.AR: "مؤشر توثيق العقود للموظفين السعوديين",
    }
    CONTRACT_AUTHENTICATION_SCORE_FOR_EXPATS_EMPLOYEES = {
        Language.EN: "Contract Authentication Score for Expats Employees",
        Language.AR: "مؤشر توثيق العقود للموظفين المقيمين",
    }
    TOTAL_CONTRACT_AUTHENTICATION = {
        Language.EN: "Total Contract Authentication",
        Language.AR: "مؤشر توثيق العقود لجميع الموظفين",
    }
    AUTHENTICATED_CONTRACTS = {Language.EN: "Authenticated Contracts", Language.AR: "عقود موثقة"}
    UNAUTHENTICATED_CONTRACTS = {
        Language.EN: "Unauthenticated Contracts",
        Language.AR: "عقود غير موثقة",
    }
    MSG_SUCCESS_CONTRACT_CREATION = {
        Language.EN: "The contract was created! ( please submit an employee transfer request to proceed )",
        Language.AR: "تم إنشاء العقد بنجاح! ( الرجاء اكمال إجراء النقل من خدمة نقل الخدمات )",
    }
    MSG_SUCCESS_CONTRACT_CREATION_SAUDI_NOT_IN_ESTABLISHMENT = {
        Language.EN: "The contract has been sent successfully! Please inform the employee to login to Qiwa platform and"
        " accept the contract.",
        Language.AR: "تم ارسال العقد بنجاح! الرجاء إبلاغ الموظف بالدخول على منصة قوى والموافقة على العقد.",
    }
    CONTRACT_TYPE = {Language.EN: "Contract Type", Language.AR: "نوع العقد"}
    MSG_SUCCESS_TEMPLATE_CREATION = {
        Language.EN: "Template was created successfully!",
        Language.AR: "عقود غير موثقة",
    }
    MSG_SUCCESS_TEMPLATE_REMOVING = "The contract template has been deleted successfully"


@dataclass
class SupportedBrowser:
    version = {"chrome": "102.0", "firefox": "93.0", "opera": "80.0"}


@dataclass
class EstablishmentStatus:
    EXISTING = "قائمة"


@dataclass
class Occupation:
    SUPERVISOR = "مشرف عمال"
    MANAGER_DIRECTOR = "مدير الادارة"
    INFORMATION_TECHNOLOGY_OPERATIONS_TECHNICIAN = "فني عمليات تقنية معلومات"
    SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION = "أمين عام منظمة ذات اهتمامات خاصة"
    PERSONAL_CARE_WORKER = "عامل عناية شخصية"
    ACCOUNTANT = "محاسب قانوني"
    GENERAL_DIRECTOR = "مدير عام"


@dataclass
class Label:
    ACTIONS = "Actions"
    ELIGIBILITY = "Eligibility"
    IQAMA_NUMBER = "Iqama number"


@dataclass
class Eligibility:
    ELIGIBLE = "Eligible"
    NOT_ELIGIBLE = "Not Eligible"


@dataclass
class Titles:
    CHANGE_OCCUPATION_REQUEST = "Change occupation requests"
    CHANGE_OCCUPATION = "Change Occupation"
    LABOR_OFFICE_APPOINTMENTS = "Labor Office Appointments"
    WORK_PERMIT = "WORK PERMITS - Select employees for issuing or renewal of work permit"
