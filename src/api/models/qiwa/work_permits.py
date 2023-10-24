from typing import Literal, Type

from src.api.constants.work_permit import WorkPermitStatus, WorkPermitStatusLiterals
from src.api.models.qiwa.data_attr import work_permits
from src.api.models.qiwa.raw import work_permit
from src.api.models.qiwa.raw.root import Root
from src.api.models.qiwa.raw.work_permit import validate_expat

transactions_data = Root[
    list[work_permits.work_permit_request], Type[None], work_permit.transaction.Meta
]
work_permit_debts = Root[list[work_permits.wp_dept_info], Type[None], work_permit.wp_debts.Meta]
cancel_sadad_ibm_error = Root[
    work_permits.ibm_error(work_permit.cancel_sadad.CancellingError), Type[None], Type[None]
]
expat_validation = validate_expat.ValidateExpat[validate_expat.ValidationResult, Type[None]]
expat_validation_error = validate_expat.ValidateExpat[Literal[False], validate_expat.Error]
employees_data = Root[
    list[work_permits.work_permit_employees], Type[None], work_permit.transaction.Meta
]


def transactions_data_with_status(status: Type[WorkPermitStatus]):
    status, status_id = WorkPermitStatusLiterals[status.name].value
    return Root[
        list[work_permits.work_permit_request_with_status(status, status_id)],
        Type[None],
        work_permit.transaction.Meta,
    ]
