from collections import namedtuple


class VisaType:  # pylint: disable=R0903
    UNKNOWN = 0
    ESTABLISHMENT = 1
    EXPANSION = 2


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


class VisaUser:  # pylint: disable=R0903
    NAME = "1812066397"
    PASSWORD = "123456789aA@"
    ESTABLISHMENT_ID = "6-2273011"


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


BalanceRequestStatus = namedtuple("TierRequest", ["id", "label"])

BR_ACCEPTED = BalanceRequestStatus(1, "Accepted")
BR_INACTIVE = BalanceRequestStatus(2, "Accepted")
BR_WAITING = BalanceRequestStatus(3, "Waiting for inspection")
BR_REJECTED = BalanceRequestStatus(4, "Rejected")
BR_REFUNDED = BalanceRequestStatus(5, "Refunded")
BR_EXPIRED = BalanceRequestStatus(6, "Expired")
BR_TERMINATED = BalanceRequestStatus(7, "Terminated")
BR_NEW = BalanceRequestStatus(8, "Waiting for inspection")


ERROR_CODE = "ODM0024"
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
# env variables:
IS_SEASONAL_VISA_AVAILABLE = "IS_SEASONAL_VISA_AVAILABLE"
IS_BALANCE_FLOW_AVAILABLE = "IS_BALANCE_FLOW_AVAILABLE"
FIRST_TIER_ACTIVE = "FIRST_TIER_ACTIVE"
IS_INSPECTOR_VISIT_FLOW_AVAILABLE = "IS_INSPECTOR_VISIT_FLOW_AVAILABLE"
ENV_VARIABLES = [
    IS_SEASONAL_VISA_AVAILABLE,
    IS_BALANCE_FLOW_AVAILABLE,
    FIRST_TIER_ACTIVE,
    IS_INSPECTOR_VISIT_FLOW_AVAILABLE,
]
