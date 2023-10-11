from typing import Any, List, Literal, Type, Union

from pydantic import BaseModel

from src.api.constants.work_permit import WorkPermitStatusArabic, WorkPermitStatus
from src.api.models.qiwa import raw
from src.api.models.qiwa.raw.data import Data
from src.api.models.qiwa.raw.relationships import Relationships

group = Data[str, Literal["group"], raw.e_service.Group, Relationships]
service_group = Data[int, Literal["service-group"], raw.e_service.ServiceGroup, Relationships]
group_super = Data[str, Literal["group-super"], raw.e_service.GroupSuper, Relationships]
e_service = Data[Union[str, int], Literal["e-service"], raw.e_service.EService, Relationships]
e_service_super = Data[int, Literal["e-service-super"], raw.e_service.EServiceSuper, Relationships]
tag = Data[str, Literal["tag"], raw.e_service.Tag, Type[None]]
tag_super = Data[int, Literal["tag-super"], raw.e_service.TagSuper, Type[None]]
wp_dept_info = Data[str, Literal["wp-debt-info"], raw.work_permit.wp_debts.WPDebtInfo, Type[None]]
saudization_certificate = Data[
    str,
    Literal["saudization-certificate"],
    raw.saudi_certificate.SaudizationCertificate,
    Type[None],
]
encrypted_saudization_certificate = Data[
    str,
    Literal["encrypted-saudization-certificate"],
    raw.saudi_certificate.EncryptedSaudizationCertificate,
    Type[None],
]
error = Data[str, Literal["error"], raw.saudi_certificate.Error, Type[None]]
not_found = Data[Literal["-1"], Literal["not_found"], List[Any], Type[None]]
change_occupation_request = Data[
    Type[None],
    Literal["change-occupation-request"],
    raw.change_occupation.ChangeOccupationRequest,
    Type[None],
]
request = Data[str, Literal["request"], raw.change_occupation.Request, Type[None]]
work_permit_request = Data[
    str,
    Literal["work-permit-request"],
    raw.work_permit.transaction.WorkPermitRequest[WorkPermitStatusArabic, WorkPermitStatus],
    Type[None],
]


def work_permit_request_with_status(status: Type[Literal], status_id: Type[Literal]):
    return Data[
        str,
        Literal["work-permit-request"],
        raw.work_permit.transaction.WorkPermitRequest[status, status_id],
        Type[None],
    ]


work_permit_employees = Data[
    str, Literal["work_permit_employees"], raw.work_permit.employees.Employee, Type[None]
]


def ibm_error(attributes: Type[BaseModel]) -> Type[Data]:
    return Data[Literal["-1"], Literal["ibm-error"], attributes, Type[None]]
