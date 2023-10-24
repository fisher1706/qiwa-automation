from typing import Literal, Type, TypeVar

from pydantic import BaseModel

from src.api.constants.work_permit import WorkPermitStatus, WorkPermitStatusArabic
from src.api.models.qiwa.raw.data import Data
from src.api.models.qiwa.raw.work_permit.employees import Employee
from src.api.models.qiwa.raw.work_permit.transaction import WorkPermitRequest
from src.api.models.qiwa.raw.work_permit.wp_debts import WPDebtInfo

StatusLiteralT = TypeVar("StatusLiteralT", bound=WorkPermitStatus)
StatusIdLiteralT = TypeVar("StatusIdLiteralT", bound=WorkPermitStatusArabic)


work_permit_request = Data[
    str,
    Literal["work-permit-request"],
    WorkPermitRequest[WorkPermitStatusArabic, WorkPermitStatus],
    Type[None],
]

work_permit_employees = Data[str, Literal["work_permit_employees"], Employee, Type[None]]
wp_dept_info = Data[str, Literal["wp-debt-info"], WPDebtInfo, Type[None]]


def work_permit_request_with_status(status: StatusLiteralT, status_id: StatusIdLiteralT):
    return Data[
        str,
        Literal["work-permit-request"],
        WorkPermitRequest[status, status_id],
        Type[None],
    ]


def ibm_error(attributes: Type[BaseModel]) -> Type[Data]:
    return Data[Literal["-1"], Literal["ibm-error"], attributes, Type[None]]
