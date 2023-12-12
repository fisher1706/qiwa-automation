from pydantic import constr

from src.api.models.qiwa.base import QiwaBaseModel


class ErrorDetails(QiwaBaseModel):
    description: str | None = ...
    details: constr(strict=True, min_length=1)


class MultiLangErrorAttributes(QiwaBaseModel):
    code: str
    ar_SA: ErrorDetails
    en_EN: ErrorDetails
