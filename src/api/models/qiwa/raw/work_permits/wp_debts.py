from datetime import date
from typing import List

from src.api.models.qiwa.base import QiwaBaseModel


class WPDebtInfo(QiwaBaseModel):
    debt_id: int
    personal_number: int
    first_name: str
    second_name: str
    third_name: str | None = ...
    fourth_name: str | None = ...
    sadad_number: str | None = ...
    employee_transfer_date: date
    wp_debit_create_date: date
    indebtedness: int
    status_ar: str
    status_en: str
    status: int
    names: List[str]


class Meta(QiwaBaseModel):
    total_count: int
    all_paid: bool
