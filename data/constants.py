from collections import namedtuple
from dataclasses import dataclass

from src.api.models.qiwa.base import QiwaBaseModel


@dataclass
class Language:
    EN = "en"
    AR = "ar"


@dataclass
class UserInfo:
    PASSWORD = "123456789aA@"
    CHANGED_PASSWORD = "123456789aA@!#"


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
class SupportedBrowser:
    version = {"chrome": "114.0", "firefox": "93.0"}


@dataclass
# TODO: [dp] Compare with services and adjust class Tittles
class Titles:
    CHANGE_OCCUPATION_REQUEST = "Change occupation requests"
    CHANGE_OCCUPATION = "Change Occupation"
    LABOR_OFFICE_APPOINTMENTS = "Labor Office Appointments"
    WORK_PERMIT = "WORK PERMITS - Select employees for issuing or renewal of work permit"


@dataclass
class Workspaces:
    BUSINESS_ACCOUNT_CARD = {Language.EN: "Business Account", Language.AR: "حساب الأعمال"}


@dataclass
class OtpMessage:
    TITLE = "Confirmation"
    PROMPT = "Please enter the OTP to proceed"
    CONFIRMATION = "Please inform client that the OTP is sent to the email"
    ERROR = "OTP is wrong. Try again or resend email to the client."


@dataclass
class SaudiCertificateDashboard:
    HEADER = "Saudization Certificate"
    SUB_HEADER = (
        "Saudization certificate states that the company has achieved the required Saudization rates based "
        "on Nitaqat."
    )


class CardDetails(QiwaBaseModel):
    Holder: str = "Jane Jones"
    Number: str = "4111111111111111"
    ExpiryMonth: str = "05"
    ExpiryYear: str = "2034"
    CVV: str = "123"


class PaymentRequest(QiwaBaseModel):
    paymentBrand: str = "VISA"
    card: CardDetails = CardDetails()


PaymentTypes = namedtuple("PaymentTypes", ["name", "submit_button"])

SADAD = PaymentTypes("sadad", "Pay")  # need to correct when is available
WALLET = PaymentTypes("wallet", "Pay")  # need to correct when is available
APPLE = PaymentTypes("apple", "Pay")
CARD = PaymentTypes("card", "Submit and pay")


class PaymentResult(QiwaBaseModel):
    AUTHENTICATED = "AUTHENTICATED"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    CANCELLED_AUTHENTICATION = "CANCELLED_AUTHENTICATION"
    AUTHENTICATION_NOT_AVAILABLE = "AUTHENTICATION_NOT_AVAILABLE"
    AUTHENTICATION_REJECTED = "AUTHENTICATION_REJECTED"
    API_GW_ASM_POLICY_ERROR = "API_GW_ASM_POLICY_ERROR"
    successful_results = [AUTHENTICATION_NOT_AVAILABLE, AUTHENTICATED]
