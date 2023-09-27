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
    ONE_HUNDRED = 100
    NINTY_NINE = 99
    TWO = 2
    ONE = 1
    ZERO = 0
    FOUR = 4


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


ERROR_CODE = "ODM0024"
WORK_VISA_CARD_ZERO_QUOTA_ERROR = "You cannot issue Work Visas because your Allowed quota is 0."
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
WORK_VISA_CARD_WARNING = (
    "You have already used your Allowed quota in the current tier. "
    "To request more work visas, you need to upgrade your tier."
)
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
INCREASE_ABSHER_MODAL_TITLE = "Increase the Ministry of Interior fund"
SERVICE_PAGE_BUTTON_TEXT = "Go to service page"
INCREASE_RECRUITMENT_QUOTA_TEXT = "Increase recruitment quota"
ISSUE_VISA_TEXT = "Issue Visa"
ISSUE_VISA_REQUEST_TITLE = "Issue visa"
VISA_REQUEST_PAGE_TITLE_TEXT = "Visa request details"
