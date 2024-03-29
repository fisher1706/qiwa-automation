# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from data.constants import Language

random_name = f"Auto Test {datetime.now().strftime('%Y.%m.%d %H.%M.%S')}"
random_email = f"email{datetime.now().strftime('%Y.%m.%d.%H.%M.%S')}@test.com"


@dataclass
class LOAgent:
    ID = "1048616450"

    ESTABLISHMENT_NAME = "مؤسسة قصر اليمامه للمقاولات"
    LABOR_OFFICE_ID = "1"
    SEQUENCE_NUMBER = 1112672

    ESTABLISHMENT_NAME_EDIT = "قصر اليمامه للوحدات السكنيه المفروشه"
    LABOR_OFFICE_ID_EDIT = "1"
    SEQUENCE_NUMBER_EDIT = 1302328


@dataclass
class LOAdmin:
    ID = "1002429940"


@dataclass
class IndividualService:
    APPOINTMENTS = {
        Language.EN: "Appointments in Labor Office",
        Language.AR: "المواعيد بمكتب العمل",
    }


@dataclass
class IndividualUser:
    ID = "1080910035"

    APPOINTMENT_TO_SEARCH_IN_HISTORY = "1260"
    APPOINTMENT_EXPIRED = "1550"
    APPOINTMENT_CANCELLED = "1248"
    APPOINTMENT_ATTENDED = "1404"
    APPOINTMENT_DONE = "2322"


@dataclass
class SubscribedUser:
    ID = "1044076196"

    APPOINTMENT_TO_SEARCH_IN_HISTORY = "35058"
    NON_EXISTING_APPOINTMENT = "0000000000"

    ESTABLISHMENT = {
        Language.EN: "شركة التصنيف الدولية للمقاولات",
        Language.AR: "شركة التصنيف الدولية للمقاولات",
    }
    OFFICE_ID = 9
    ESTABLISHMENT_SEQUENCE = "1112719"
    SEQUENCE_NUMBER = "9-1112719"


@dataclass
class UnSubscribedUser:
    ID = "1061073274"
    SEQUENCE_NUMBER = "8-1626749"

    ESTABLISHMENT = {
        Language.EN: "شركة هجر المحدودة",
        Language.AR: "شركة هجر المحدودة",
    }


@dataclass
class LOUser:
    ID = "1039682974"
    LO_SYS_ADMIN_ROLE_ID = 2


@dataclass
class UserInfo:
    INVALID_LOGIN = "0000000001"
    UNREGISTRED_USER_ID = "1000000001"
    PASSWORD = "123456789aA@"
    CHANGED_PASSWORD = "123456789aA@!#"
    INVALID_PASSWORD = "Invalid"
    EXPIRED_DATE = "2023-05-10"
    DEFAULT_OTP_CODE = "0000"
    PHONE = "+966000000000"
    EMAIL = random_email
    EMAIL_EDITED = f"edited{random_email}"
    INVALID_EMAIL = "invalid@email"
    CALENDAR = "hijiri"


@dataclass
class LOSysAdmin:
    ID = "1002429940"
    ID_NEW = "1027331956"
    LABOR_OFFICE_ID = "4"
    SEQUENCE_NUMBER = 8134

    LABOR_OFFICE_ID_EDIT = "11"
    SEQUENCE_NUMBER_EDIT = 1049676


@dataclass
class AppointmentsHistoryStatus:
    SHOW_ALL = {"index": 0, "value": "Show all"}
    EXPIRED = {"index": 1, "value": "Expired"}
    CANCELLED = {"index": 2, "value": "Cancelled"}
    ATTENDED = {"index": 3, "value": "Attended"}
    DONE = {"index": 4, "value": "Done"}
    UNDER_PROGRESS = {"index": 5, "value": "Under Progress"}
    PENDING = {"index": 6, "value": "Pending"}
    CLOSED = {"index": 7, "value": "Closed"}


@dataclass
class OfficesInfo:
    HOURLY_CAPACITY = 500
    WORKING_HOURS_FROM = "07:00"
    WORKING_HOURS_TO = "17:00"
    ADDRESS = "مكتب التشغيل الآلي"
    NAJRAN_REGION_ID = 13
    LATITUDE = "27.2578957"
    LONGITUDE = "33.8116067"
    IS_ELECTRONIC_OFFICE = False

    OFFICES_NAME = random_name
    OFFICE_NAME_TEST_OFFICE = "office 3216"
    OFFICE_NAME_VEUM_HANE = "Veum - Hane"
    OFFICE_NAME_VIRTUAL = "Alina_Virtual"
    OFFICE_NAME_EDIT = "Voffgh"
    INACTIVE_TEST_OFFICE = "INACTIVE TEST OFFICE"
    INACTIVE_TEST_OFFICE_ID = 2389
    INVALID_OFFICE = "INVALID OFFICE"
    AUTO_TEST_OFFICE = "AUTO TEST OFFICE"
    AUTO_TEST_OFFICE_ID = 1712
    INDIVIDUAL_OFFICE = "TEST OFFICE INDIVIDUAL"
    INDIVIDUAL_OFFICE_ID = 1960
    AUTO_TEST_EDITED_OFFICE = "AUTO TEST EDITED OFFICE"
    AUTO_TEST_OFFICE_EDITED_ID = 1713

    VIRTUAL = "AUTO TEST VIRTUAL"
    VIRTUAL_ID = 3153

    SEQUENCE_NUMBER_AGENT = "1-1302328"
    SEQUENCE_NUMBER_2_AGENT = "1-1448204"

    HOURLY_CAPACITY_EDITED = 400
    WORKING_HOURS_FROM_EDITED = "06:00"
    WORKING_HOURS_TO_EDITED = "18:00"
    ADDRESS_EDITED = "قسم ثان الغردقة، مصر"
    TABUK_REGION_ID = 12
    LATITUDE_EDITED = "27.2578958"
    LONGITUDE_EDITED = "33.8116067"

    REGION_NAJRAN = "Najran"
    REGION_TABUK = "Tabuk"
    REGION_MADINAH = {Language.EN: "Madinah", Language.AR: "المدينة المنورة"}
    REGION_RIYADH = {Language.EN: "Riyadh", Language.AR: "الرياض"}
    REGION_HAIL_WITHOUT_OFFICES = "Hail"

    REGION_ITEM_EDITED = "Riyadh"

    CREATE_OFFICE_SUCCESS_MESSAGE = "Office added successfully"
    EDIT_OFFICE_SUCCESS_MESSAGE = "Office details edited successfully"
    OFFICE_STATUS_SUCCESS_MESSAGE = "Office status changed successfully"
    SERVICE_ADDED_SUCCESS_MESSAGE = "Service added successfully"


@dataclass
class ServicesInfo:
    SERVICE_RANDOM_NAME_AR = "اختبار الأتمتة" + f" {datetime.now().strftime('%Y.%m.%d %H.%M.%S')}"
    SERVICE_RANDOM_NAME_EN = random_name

    SERVICE_NAME_INDIVIDUALS = {Language.EN: "Individuals_10/08", Language.AR: "Individuals_10/08"}
    SUB_SERVICE_NAME_INDIVIDUALS = {
        Language.EN: "subservices_10/08",
        Language.AR: "subservices_10/08",
    }
    SERVICE_NAME_VIRTUAL = {
        Language.EN: "Alina_Individuals_Virtual",
        Language.AR: "Alina_ndividualVirtual",
    }
    SUB_SERVICE_NAME_VIRTUAL = {
        Language.EN: "Alina_New_Individuals",
        Language.AR: "Alina_New_Individuals",
    }
    POLICIES_SERVICE = "Policies"
    POLICIES_SUB_SERVICE = "Submit Policies Request"

    SERVICE_NAME_EDIT = {
        Language.EN: "Alina_Individuals_",
        Language.AR: "",
    }

    SUB_SERVICE_NAME_EDIT = {
        Language.EN: "Alina",
        Language.AR: "",
    }

    SERVICE_NAME_WORK_PERMITS = {Language.EN: "Work Permits", Language.AR: "رخص العمل"}
    SUB_SERVICE_NAME_RENEW_WORK_PERMITS = {
        Language.EN: "Renew Work Permits",
        Language.AR: "تجديد رخص العمل",
    }

    SERVICE_NAME_POLICIES = {Language.EN: "Policies", Language.AR: "لوائح تنظيم العمل"}
    SUB_SERVICE_NAME_POLICIES = {
        Language.EN: "Submit Policies Request",
        Language.AR: "تقديم لوائح تنظيم العمل",
    }

    EMPLOYEE_TRANSFER_SERVICE = "Employee Transfer"
    EMPLOYEE_TRANSFER_SUB_SERVICE = "Employee Transfer"

    VISAS_SERVICE = "Visas"
    VISAS_SERVICE_AR = "التأشيرات"
    VISAS_SUB_SERVICE = "Submit Expansion Visa Request"
    VISAS_SUB_SERVICE_AR = "تقديم طلب تأشيرة توسع"

    INDIVIDUAL_SERVICE = "Anna2507"
    INDIVIDUAL_SUB_SERVICE = "Anna2507Anna"
    INDIVIDUAL_SUB_SERVICE_2 = "Anna2507Anna1"

    VIRTUAL = "VIRTUAL"
    VIRTUAL_SUB = "VIRTUAL SUB"

    CHANGE_OCCUP_SERVICE = "Change Occupation"
    CHANGE_OCCUP_SUB_SERVICE = "Submit Change Occupation"

    CREATE_SERVICE_SUCCESS_MESSAGE = "The service has been added successfully"
    CREATE_SUB_SERVICE_SUCCESS_MESSAGE = "Subservice added successfully"
    EDIT_SERVICE_SUCCESS_MESSAGE = "Service edited successfully"
    EDIT_SUB_SERVICE_SUCCESS_MESSAGE = "Subservice edited successfully"
    SERVICE_STATUS_SUCCESS_MESSAGE = "Service status changed successfully"

    SAUDI_CERTIFICATE_SERVICE = "Saudization Certificate"
    SAUDI_CERTIFICATE_SUB_SERVICE = "Create Saudi Certificate"


@dataclass
class RequesterTypeId:
    INDIVIDUAL = 1
    ESTABLISHMENT = 2


class BasePageInfo:
    STATE_TRIGGER_COLOR_ACTIVE = "rgba(204, 204, 204, 1)"
    STATE_TRIGGER_COLOR_INACTIVE = "rgba(204, 204, 204, 1)"
    ESTABLISH_REQUEST_TYPE = "establishment"
    INDIVID_REQUEST_TYPE = "individual"


class ServiceIds:
    VISA_SERVICE_ID = 1
    EMPLOYEE_TRANSFER_ID = 2
    POLICIES_SERVICE_ID = 6
    INDIVIDUAL_SERVICE_ID = 99
    CHANGE_OCCUPATION_ID = 3
    VIRTUAL_ID = None


class SubServiceIds:
    SUBMIT_CHANGE_SPONSOR_REQUEST = 1
    APPROVE_REJECT_CHANGE_SPONSOR_REQUEST = 2
    CANCEL_CHANGE_SPONSOR_REQUEST = 3
    UPDATE_RELEASE_DATE = 4

    SUBMIT_CHANGE_OCCUPATION = 6

    SUBMIT_ESTABLISH_VISA_REQUEST = 8
    SUBMIT_EXPANSION_VISA_REQUEST = 9
    CANCEL_ISSUED_VISA_REQUEST = 10
    TERMINATE_ESTABLISH_PERIOD = 11

    SUBMIT_POLICIES_REQUEST = 13

    INDIVIDUAL_SUB_SERVICE_ID = 52
    INDIVIDUAL_SUB_SERVICE_ID_2 = 56
    VIRTUAL_SUB_ID = None


class UserAnyRole:
    ID = "1039682974"

    LABOR_OFFICE_ID = "1"
    SEQUENCE_NUMBER = 100521

    LABOR_OFFICE_ID_EDIT = "1"
    SEQUENCE_NUMBER_EDIT = 179760


class VisitInfo:
    CANCEL_VISIT_SUCCESS_MESSAGE = "The visit is cancelled"
    VISIT_CONFIRMED_MESSAGE = "Visit confirmed"
    VISIT_EDITED_MESSAGE = "Visit edited"


class VisitReason:
    REQUEST_NEW_SERVICE = "Request new service"
    REQUEST_NEW_SERVICE_API = "1"


class RegionFront(str, Enum):
    REGION_NAJRAN = "Najran"
    REGION_TABUK = "Tabuk"
    REGION_HAIL_WITHOUT_OFFICES = "Hail"


class OfficesFront:
    AUTO_TEST_OFFICE = "AUTO TEST OFFICE"
    AUTO_TEST_OFFICE_EDITED = "API TEST OFFICE EDITED"
    TEST_OFFICE_INDIVIDUAL = "TEST OFFICE INDIVIDUAL"


class ServicesFront(str, Enum):
    EMPLOYEE_TRANSFER = "Employee Transfer"
    VISA_SERVICES = "Visas"
    POLICES = "Policies"
    INDIVIDUAL_SERVICE = "Individual service"


class VisitStatus(str, Enum):
    ACTIVE = "Active"
    DONE = "Done"
    CANCELED = "Cancelled"
    EXPIRED = "Expired"


class InfoAboutVisit(str, Enum):
    VISIT_CONFIRMED = "Visit confirmed"
    VISIT_EDITED = "Visit edited"
    VISIT_CANCELED = "The visit is cancelled"


class SubServicesFront(str, Enum):
    SUBMIT_CHANGE_SPONSOR_REQUEST = "Submit Change Sponsor Request"
    APPROVE_REJECT_CHANGE_SPONSOR_REQUEST = "Approve Reject Change Sponsor Request"
    CANCEL_CHANGE_SPONSOR_REQUEST = "Cancel Change Sponsor Request"
    UPDATE_RELEASE_DATE = "Update Release Date"

    SUBMIT_EXPANSION_VISA_REQUEST = "Submit Expansion Visa Request"
    SUBMIT_VISIT_VISA_REQUEST = "Submit Visit Visa Request"
    SUBMIT_SEASONAL_VISA_REQUEST = "Submit Seasonal Visa Request"
    CANCEL_ISSUED_VISA = "Cancel Issued Visa"


class EmployeeTransferStatuses(str, Enum):
    CANCELED_BY_NEW_EMPLOYEE = "Cancelled by New Employer"


class AppointmentsView:
    PAGINATION = {Language.EN: "Appointment details", Language.AR: "تفاصيل الموعد"}
    APPOINTMENT_REFERENCE_NUMBER_TEXT = {
        Language.EN: "Appointment reference number",
        Language.AR: "الرقم المرجعي للموعد:",
    }
    INFO_ROW_TEXT = {
        Language.EN: "For a seamless experience at the Labor Office, "
        "please make sure to arrive at the requested location on the "
        "scheduled date and time.",
        Language.AR: "للحصول على تجربة أفضل في مكتب العمل،"
        " يرجى التأكد من الوصول للموقع في التاريخ والوقت المحددين.",
    }
    INFO_ROW_VIRTUAL_TEXT = {
        Language.EN: "A Labor Office agent will meet you virtually over video call, "
        "please join the virtual appointment session on exact time you chose for the appointment in case "
        "of no show or delay, unfortunately, the appointment will get canceled.",
        Language.AR: "ستكون جلسة الموعد عبر الاتصال المرئي ، الرجاء الدخول الى جلسة"
        " الموعد حسب الوقت المحدد في الموعد، في حال عدم دخول الجلسة أو التأخير سيتم الغاء الموعد.",
    }
    GENERAL_INFO_REASON_TEXT = {
        Language.EN: "Appointment reason",
        Language.AR: "سبب الموعد",
    }
    GENERAL_INFO_DATA_TEXT = {Language.EN: "Date", Language.AR: "التاريخ"}
    GENERAL_INFO_TIME_TEXT = {Language.EN: "Time", Language.AR: "الوقت"}
    GENERAL_INFO_SERVICE_TEXT = {Language.EN: "Service name", Language.AR: "اسم الخدمة"}
    GENERAL_INFO_SUB_SERVICE_TEXT = {Language.EN: "Subservice name", Language.AR: "الخدمة الفرعية"}
    GENERAL_INFO_OFFICE_TEXT = {Language.EN: "Office", Language.AR: "المكتب"}
    GENERAL_INFO_LOCATION_TEXT = {Language.EN: "Location", Language.AR: "موقع"}
    GENERAL_INFO_TYPE_TEXT = {Language.EN: "Type", Language.AR: "النوع"}
    GENERAL_INFO_STATUS_TEXT = {Language.EN: "Status", Language.AR: "الحالة"}
    REQUESTER_TYPE = {Language.EN: "Account type", Language.AR: "نوع الحساب"}
    REQUESTER_ID = {Language.EN: "National ID", Language.AR: "الهوية الوطنية"}
    MAP_TITLE = {Language.EN: "Appointment location", Language.AR: "موقع الموعد"}
    MAP_TEXT = {
        Language.EN: "Click on the blue pin to view your appointment’s location details.",
        Language.AR: "اختر علامة الدبوس الأزرق لعرض تفاصيل موقع موعدك.",
    }
    COPY_MAP_TEXT = {
        Language.EN: "Location link was successfully copied to the clipboard.",
        Language.AR: "تم نسخ الرابط بنجاح",
    }


class AppointmentsCancel:
    TITLE_TEXT = {
        Language.EN: "Are you sure you want to cancel this appointment?",
        Language.AR: "هل أنت متأكد من إلغاء الموعد؟",
    }
    REASON_TEXT = {Language.EN: "Appointment reason", Language.AR: "سبب الموعد"}
    DATE_TEXT = {Language.EN: "Date", Language.AR: "التاريخ"}
    TIME_TEXT = {Language.EN: "Time", Language.AR: "الوقت"}
    OFFICE_TEXT = {Language.EN: "Office", Language.AR: "المكتب"}
    TYPE_TEXT = {Language.EN: "Type", Language.AR: "النوع"}
    STATUS_TEXT = {Language.EN: "Status", Language.AR: "الحالة"}


class AppointmentReason:
    VIRTUAL = {"id": 0, "text": {Language.EN: "New request - virtual", Language.AR: ""}}
    IN_PERSON = {
        "id": 3,
        "text": {
            Language.EN: "Request new service - in person",
            Language.AR: "طلب خدمة جديدة - موعد حضوري",
        },
    }


class AppointmentType:
    IN_PERSON = {
        Language.EN: "In-person",
        Language.AR: "حضوري",
    }
