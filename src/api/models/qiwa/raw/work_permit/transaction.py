from datetime import date
from typing import Generic, TypeVar

from src.api.models.qiwa.base import QiwaBaseModel

StatusT = TypeVar("StatusT")
BillStatusT = TypeVar("BillStatusT")


class WorkPermitRequest(QiwaBaseModel, Generic[StatusT, BillStatusT]):
    id: int
    status: StatusT
    transaction_fees: str
    bill_number: str | None = ...
    number_of_expats: str
    submit_date: date
    remaining_days: str | None = ...
    bill_status: BillStatusT


class Meta(QiwaBaseModel):
    total_count: int
