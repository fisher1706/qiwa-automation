from collections import namedtuple


class VisaType:  # pylint: disable=R0903
    UNKNOWN = 0
    ESTABLISHMENT = 1
    EXPANSION = 2


class UserType:  # pylint: disable=R0903
    OWNER = 1
    USER = 2


class DateFormats:  # pylint: disable=R0903
    DDMMYYYY = "%d-%m-%Y"
    YYYYMMDD = "%Y-%m-%d"
    DMYYYY = "%-d-%B-%Y"
    DDMMYY = "%d/%m/%y"
    DD_MM_YYYY = "%d/%m/%Y"


class Numbers:  # pylint: disable=R0903
    TEN_THOUSAND = 10000
    ONE_THOUSAND = 1000
    ONE_HUNDRED = 100
    NINETY_NINE = 99
    NINE_HUNDRED_NINETY_NINE = 999
    TWO = 2
    ONE = 1
    ZERO = 0
    FOUR = 4
    THREE = 3
    TEN = 10
    NINE = 9
    SIX = 6
    LAZYLOADING_PACK_SIZE = 60


class VisaUser:  # pylint: disable=R0903
    NAME = "1812066397"
    PASSWORD = "123456789aA@"
    ESTABLISHMENT_ID = "6-2273011"
    COMPANY_ID = 685181


class TIER:  # pylint: disable=R0903
    ONE = "tier 1"
    TWO = "tier 2"
    THREE = "tier 3"
    FOUR = "tier 4"


class Languages:  # pylint: disable=R0903
    ENGLISH = "EN"
    ARABIC = "عر"


class PayCardSuccess:  # pylint: disable=R0903
    HOLDER = "John Doe"
    NUMBER = "4111111111111111"
    MONTH = "05"
    YEAR = "24"
    CVV2 = "123"


class ColName:  # pylint: disable=too-few-public-methods
    REQUEST_STATUS = "Request status"
    VISA_STATUS = "Visa status"
    VISA_BORDER_NUMBER = "Border number"
    VISA_ACTIONS = "Action"


BalanceRequestStatus = namedtuple("TierRequest", ["id", "label", "refundable"])

BR_ACCEPTED = BalanceRequestStatus(1, "Accepted", True)
BR_INACTIVE = BalanceRequestStatus(2, "Accepted", True)
BR_WAITING = BalanceRequestStatus(3, "Waiting for inspection", False)
BR_REJECTED = BalanceRequestStatus(4, "Rejected", True)
BR_REFUNDED = BalanceRequestStatus(5, "Refunded", False)
BR_EXPIRED = BalanceRequestStatus(6, "Expired", False)
BR_TERMINATED = BalanceRequestStatus(7, "Terminated", False)
BR_NEW = BalanceRequestStatus(8, "Waiting for inspection", False)


ExceptionalBalanceRequestStatus = namedtuple("ExceptionRequest", ["id", "label"])

EBR_NEW = ExceptionalBalanceRequestStatus(1, "Waiting for inspection")
EBR_WAITING = ExceptionalBalanceRequestStatus(2, "Waiting for inspection")
EBR_ACTIVE = ExceptionalBalanceRequestStatus(3, "Accepted")
EBR_REJECTED = ExceptionalBalanceRequestStatus(4, "Rejected")
EBR_REFUNDED = ExceptionalBalanceRequestStatus(5, "Refunded")
EBR_EXPIRED = ExceptionalBalanceRequestStatus(6, "Expired")
EBR_TERMINATED = ExceptionalBalanceRequestStatus(7, "Terminated")


VisaRequestStatus = namedtuple("VisaRequest", ["id", "label", "expire"])

VR_NEW = VisaRequestStatus(0, "Unused", False)
VR_UNUSED = VisaRequestStatus(1, "Unused", True)
VR_CANCELED = VisaRequestStatus(2, "Canceled", False)
VR_USED = VisaRequestStatus(3, "Used", False)
VR_PENDING = VisaRequestStatus(
    4, "Pending for visa cancelation from Ministry of the interior", False
)
VR_CANCELABLE = [VR_NEW, VR_UNUSED]

CANCEL_UPGRADE_REQUEST_TITLE = "Cancel upgrade request"
CANCEL_UPGRADE_REQUEST_CONTENT = (
    "When your request is approved, the recruitment quota "
    "will reduce and your establishment funds will be returned."
)

BRRefundMessages = namedtuple("RefundStatus", ["id", "title", "content", "success"])

BR_SUCCESS = BRRefundMessages(
    1, CANCEL_UPGRADE_REQUEST_TITLE, CANCEL_UPGRADE_REQUEST_CONTENT, True
)
BR_LIMIT = BRRefundMessages(
    2,
    "Unfortunately, you cannot return the requested balance",
    "Sorry, you have exceeded the 30 days limit of refunding requested balance.",
    False,
)
BR_USED = BRRefundMessages(
    3,
    "Unfortunately, you cannot return the requested balance",
    "Sorry, you cannot refund this balance request as you have used it for either employee transfer or issuing visas.",
    False,
)
BR_CANNOT = BRRefundMessages(
    4,
    "Unfortunately, you cannot return the requested balance",
    "Sorry, you cannot refund this balance request.",
    False,
)
BR_ERROR = BRRefundMessages(5, CANCEL_UPGRADE_REQUEST_TITLE, CANCEL_UPGRADE_REQUEST_CONTENT, False)
CAN_BE_REFUNDED = [1, 5]

ERROR_CODE = "ODM0024"
EXP_PERMIT_ERROR_CODE = "ED000020"
WORK_VISA_CARD_ZERO_QUOTA_ERROR = (
    "You cannot issue Work Visas because your recruitment quota is 0."
)
PERM_WORK_VISA_TITLE = "Permanent work visas"
TEMPORARY_WORK_VISA_TITLE = "Temporary work visas"
SEASONAL_WORK_VISA_TITLE = "Seasonal work visas"
TRANSITIONAL_CARDS_TITLE_TEXT = [
    PERM_WORK_VISA_TITLE,
    TEMPORARY_WORK_VISA_TITLE,
    SEASONAL_WORK_VISA_TITLE,
]
PERM_WORK_VISA_DESCRIPTION = (
    "For hiring non-Saudi employees for long-term employment contracts (more than 3 months)."
)
TEMP_WORK_VISA_DESCRIPTION = (
    "For hiring non-Saudi employees for short-term employment contracts (3 months or less)."
)
SEASONAL_WORK_VISA_DESCRIPTION = (
    "For hiring employees during the Hajj season (only granted upon "
    "request by the Ministry of Human Resources and Social Development)."
)
SEASONAL_WORK_VISA_BLOCKED_TEXT = "This service will be available soon."
INCREASE_ALLOWED_QUOTA = "Increase recruitment quota"
WORK_VISA_CARD_WARNING = "You have already used your recruitment quota in the current tier."
WORK_VISA_PAGE_TITLE_TEXT = "Permanent work visas"
OTHER_VISAS_TITLE = "Other Visas"
FILTERS = "Filters"
OTHER_VISAS_NO_RESULTS = (
    "Here you will see the list of closed establishment visas, "
    "visas issued outside Qiwa and others."
)
PERMANENT_VISAS_TITLE = "Permanent work visas requests"
PERMANENT_VISAS_NO_RESULTS = (
    "You have no history of visa requests yet. "
    "Here you will see the list of your Permanent work visa requests."
)
INCREASE_ABSHER_MODAL_TITLE = "Increase establishment funds"
SERVICE_PAGE_BUTTON_TEXT = "Go to service page"
INCREASE_RECRUITMENT_QUOTA_TEXT = "Increase recruitment quota"
ISSUE_VISA_TEXT = "Issue Visa"
ISSUE_VISA_REQUEST_TITLE = "Issue visa"
VISA_REQUEST_PAGE_TITLE_TEXT = "Visa request details"
BALANCE_REQUESTS_WAITING_STATUS = "waiting_for_payment"
BALANCE_REQUESTS_SUBMIT_FAILED_STATUS = "submit_failed"
TRANSACTIONID = "transactionId"
PERM_WORK_VISA_ELIGIBILITY_ERRORS = (
    "You cannot issue visas because you don’t meet the {} mandatory requirements.\n"
    "See unmet requirements"
)
PERM_WORK_VISA_ELIGIBILITY_ERRORS_LINK = "See unmet requirements"
ESTABLISHMENT_FUND = "Establishment fund"
RECRUITMENT_QUOTA = "Recruitment quota"
ESTABLISHMENT_PHASE = "Establishment phase"
EXPANSION = "Expansion"
RECRUITMENT_QUOTA_TIER = "Recruitment quota tier"
ALLOWANCE_PERIOD_START_DATE = "Allowance period start date"
ALLOWANCE_PERIOD_END_DATE = "Allowance period end date"
ESTIMATED_RECRUITMENT_QUOTA = "Estimated recruitment quota after allowance period ends"
ESTABLISHING = "Establishing"
ISSUE_VISA_MODAL_TITLE_TEXT = "Sorry, currently you cannot issue Permanent work visas"
ISSUE_VISA_MODAL_CONTENT_ESTABLISHING_TEXT = (
    "You have already used your recruitment quota in the current tier."
)
ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT = "You have already used your recruitment quota."
ISSUE_VISA_MODAL_CONTENT_HIGHEST_TIER_TEXT = (
    "You have already used your recruitment quota in the highest tier. "
    "Please wait for the allowance period to end."
)
HOW_TO_INCREASE_ESTABLISHMENT_FUNDS = "How to increase establishment funds?"
CANCEL_VISA = "Cancel visa"
YOUR_REQUEST_HAS_BEEN_SENT = "Your request has been sent"
FIRST_NAME = "John"
LAST_NAME = "Doe"
REFUND_SUCCESS_MODAL_TITLE = "Your request has been sent"
REFUND_SUCCESS_MODAL_CONTENT = (
    "We’ve received and approved your request to cancel the tier upgrade. Your "
    "recruitment quota will be reduced and your establishment funds will be returned."
)
REFUND_ERROR_MODAL_MESSAGE = "Sorry, something went wrong"
USER_CANNOT_SIGN_AGREEMENT_TITLE_EST = "Sorry, currently you cannot increase recruitment quota"
USER_CANNOT_SIGN_AGREEMENT_CONTENT_EST = (
    "Establishing tiers are available when unified number "
    "owner agrees on establishing program agreement"
)
USER_CANNOT_SIGN_AGREEMENT_TITLE_EXP = (
    "Sorry, currently you cannot request exceptional recruitment quota"
)
USER_CANNOT_SIGN_AGREEMENT_CONTENT_EXP = (
    "Exceptional expansion balance are only available for unified "
    "number owner to agree on exceptional program agreement"
)
GENERIC_EXP_WORK_PERMIT_ERROR_TEXT = (
    "Sorry, the service is not available for establishments that have "
    "employees without valid work permits in any of the unified number "
    "establishments. Please issue / renew the necessary licenses through "
    "the Work Permits Service and then try again."
)
GENERIC_EXP_WORK_PERMIT_ERROR_LINK = "Review expired work permits details"
GENERIC_EXP_WORK_PERMIT_ERROR_TITLE = "Sorry, you are not eligible to issue a Work Visa"
PERM_VISA_EXP_WORK_PERMIT_ERROR = "Validation Error: card isn't enabled"
PERM_VISA_EXP_WORK_PERMIT_ERROR_LINK = "Review expired work permits details"
SEASONAL_VISA_ZERO_BALANCE_ERROR = (
    "You can't issue Seasonal work visas because your remaining balance for this season is 0."
)
SEASONAL_VISA_ZERO_BALANCE_ERROR_TITLE = (
    "Sorry, you are not eligible to issue a Seasonal work visa"
)
# env variables:
IS_SEASONAL_VISA_AVAILABLE = "IS_SEASONAL_VISA_AVAILABLE"
IS_BALANCE_FLOW_AVAILABLE = "IS_BALANCE_FLOW_AVAILABLE"
FIRST_TIER_ACTIVE = "IS_AUTOMATIC_FIRST_TIER_ENABLED"
IS_INSPECTOR_VISIT_FLOW_AVAILABLE = "IS_INSPECTOR_VISIT_FLOW_AVAILABLE"
ENV_VARIABLES = [
    IS_SEASONAL_VISA_AVAILABLE,
    IS_BALANCE_FLOW_AVAILABLE,
    FIRST_TIER_ACTIVE,
    IS_INSPECTOR_VISIT_FLOW_AVAILABLE,
]

KNOWLEDGE_CENTER_URL = "knowledge-center.qiwa.info"
ESTABLISHMENT_LOCATION_MANAGEMENT_URL = "establishment-location-management"
WORK_PERMIT_URL = "working-permits.qiwa.info"
ISSUE_VISA_URL = "issue-visa"
