from typing import Type

from src.api.models.qiwa import data
from src.api.models.qiwa.raw import work_permit
from src.api.models.qiwa.raw.root import Root

work_permit_requests_list = Root[
    list[data.work_permit_request], Type[None], work_permit.transaction.Meta
]
work_permit_debts = Root[list[data.wp_dept_info], Type[None], work_permit.wp_debts.Meta]
cancel_sadad_ibm_error = Root[
    data.ibm_error(work_permit.cancel_sadad.CancellingError), Type[None], Type[None]
]
expat_validation = work_permit.validate_expat.ValidateExpat  # pylint: disable = invalid-name
expat_validation_error = work_permit.validate_expat.ValidateExpat[work_permit.validate_expat.Error]
