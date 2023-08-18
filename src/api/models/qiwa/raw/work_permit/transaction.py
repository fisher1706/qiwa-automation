from datetime import date

from src.api.constants.work_permit import WorkPermitStatus, WorkPermitStatusArabic
from src.api.models.qiwa.base import QiwaBaseModel


class WorkPermitRequest(QiwaBaseModel):
    id: int
    status: WorkPermitStatusArabic
    transaction_fees: str
    bill_number: str | None = ...
    number_of_expats: str
    submit_date: date
    remaining_days: str | None = ...
    bill_status: WorkPermitStatus


class Meta(QiwaBaseModel):
    total_count: int
