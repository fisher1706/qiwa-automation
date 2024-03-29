from enum import Enum

from data.constants import Language


class RowsPerPage(Enum):
    TEN = "10"
    FIFTEEN = "15"
    TWENTY_FIVE = "25"

    @staticmethod
    def get_list_of_variable_values() -> list:
        return [var.value for var in RowsPerPage]


class RequestStatus(Enum):
    ALL = "All"
    DRAFT = "Draft"
    PENDING_FOR_CURRENT_EMPLOYER_APPROVAL = {
        Language.EN: "Pending For Current Employer Approval",
        Language.AR: "بانتظار موافقة صاحب العمل الحالي",
    }
    PENDING_FOR_LABORER_APPROVAL = "Pending for Laborer Approval"
    PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER = {
        Language.EN: "Pending Completing Transfer in Absher by New Employer",
        Language.AR: "بانتظار استكمال عملية النقل في وزارة الداخلية بواسطة صاحب العمل الجديد",
    }
    APPROVED = "Approved"
    REJECTED_BY_NIC = "Rejected By NIC"
    PENDING_FOR_NOTICE_PERIOD_COMPLETION = {
        Language.EN: "Pending notice period completion",
        Language.AR: "بانتظار إكمال فترة الإشعار",
    }
    AUTO_CANCELLED_FOR_MORE_THAN_14_DAYS = (
        "Auto Cancelled Due To Not Approve Or Reject The Request For More Than 14 Days"
    )
    REJECTED_BY_LABORER = {Language.EN: "Rejected by Employee", Language.AR: "مرفوض من الموظف"}
    REJECTED_BY_CURRENT_EMPLOYER = {
        Language.EN: "Rejected by Current Employer",
        Language.AR: "مرفوض من صاحب العمل الحالي",
    }
    CANCELLED_BY_NEW_EMPLOYER = "Cancelled By New Employer"
    EXPIRED_BECAUSE_OF_NOT_COMPLETING_THE_REQUEST_BY_THE_NEW_EMPLOYER = (
        "Expired Because Of Not Completing The Request By The New Employer"
    )
    UNDER_PROCESSING = "Under Processing"
    EXPIRED_DUE_TO_NIC_FAILURE = "Expired Due To NIC Failure"
    CANCELLED_BY_LABORER = "Cancelled By Laborer"

    @staticmethod
    def get_list_of_variable_values() -> list:
        return [var.value for var in RequestStatus]


class ServicesAndTools(dict, Enum):
    HOME_WORKERS_TRANSFER = {Language.EN: "Home Workers Transfer", Language.AR: "نقل عامل منزلي"}
    EMPLOYEE_TRANSFERS = {Language.EN: "Employee Transfers", Language.AR: "نقل عامل منزلي"}
    DEPENDENT_TRANSFER = {Language.EN: "Dependent transfer", Language.AR: "نقل تابع"}
    TRANSFER_LABORER_FROM_ANOTHER_ESTABLISHMENT = {
        Language.EN: "Transfer laborer from another establishment",
        Language.AR: "نقل عامل من منشأة اخرى",
    }


class TransferType(int, Enum):
    FROM_DIFFERENT_UNIFIED_NUMBER = 0
    BETWEEN_MY_ESTABLISHMENTS = 1


class SearchingType(str, Enum):
    VISIT_REFERENCE_NUMBER = "Visit Reference Number"
    ID = "Id"
    ESTABLISHMENT_NUMBER = "Establishment Number"


class SubServiceChangeOccupation(str, Enum):
    SUBMIT_CHANGE_OCCUPATION = "Submit Change Occupation"


class SubServiceErrors(str, Enum):
    EXPIRED = (
        "Sorry, the establishment’s commercial registration is not valid, to benefit from the service, "
        "please renew the commercial registration with the Ministry of Commerce."
    )


class ChangeOccupationWarning(str, Enum):
    NOT_ALLOWED = "Sorry, it is not allowed to change to the chosen occupation."


class WorkPermitRequestStatus(str, Enum):
    PENDING_PAYMENT = "Pending payment"
    CANCELED = "Canceled"


class EmployeeTransferSuccessMsg(str, Enum):
    SUMMARY = (
        "The request has been sent to the employees for approval via the Qiwa Individuals platform. To ensure "
        "the completion of the transfer, please ask the employees to log in to the Qiwa platform and accept the "
        "Employee Transfer request."
    )
