from src.api.models.qiwa.base import QiwaBaseModel


class ErrorDetails(QiwaBaseModel):
    description: str | None = ...
    details: str


class MultiLangErrorAttributes(QiwaBaseModel):
    code: str
    ar_SA: ErrorDetails
    en_EN: ErrorDetails
