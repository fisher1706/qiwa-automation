from typing import Literal, Type

from src.api.constants.work_permit import WorkPermitStatus, WorkPermitStatusLiterals
from src.api.models.qiwa.data import work_permits
from src.api.models.qiwa.raw.root import Root
from src.api.models.qiwa.raw.work_permits import (
    cancel_sadad,
    transaction,
    validate_expat,
    wp_debts,
)

transactions_data = Root[list[work_permits.work_permit_request], Type[None], transaction.Meta]
work_permit_debts = Root[list[work_permits.wp_dept_info], Type[None], wp_debts.Meta]
cancel_sadad_ibm_error = Root[
    work_permits.ibm_error(cancel_sadad.CancellingError), Type[None], Type[None]
]
expat_validation = validate_expat.ValidateExpat[validate_expat.ValidationResult, Type[None]]
expat_validation_error = validate_expat.ValidateExpat[Literal[False], validate_expat.Error]
employees_data = Root[list[work_permits.work_permit_employees], Type[None], transaction.Meta]


def transactions_data_with_status(status: Type[WorkPermitStatus]):
    status, status_id = WorkPermitStatusLiterals[status.name].value
    return Root[
        list[work_permits.work_permit_request_with_status(status, status_id)],
        Type[None],
        transaction.Meta,
    ]
