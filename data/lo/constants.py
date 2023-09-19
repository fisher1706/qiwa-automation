# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

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

    POLICIES_SERVICE = "Policies"
    POLICIES_SUB_SERVICE = "Submit Policies Request"

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
