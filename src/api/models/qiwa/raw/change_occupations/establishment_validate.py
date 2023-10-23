from typing import Literal

from src.api.models.qiwa.base import QiwaBaseModel

RuleCodesT = Literal[
    "establishment_status", "work_permit_status", "nitaqat_color", "notes", "economic_activity"
]


class Rule(QiwaBaseModel):
    code: RuleCodesT
    message: str
    status: str


class Meta(QiwaBaseModel):
    valid: bool
