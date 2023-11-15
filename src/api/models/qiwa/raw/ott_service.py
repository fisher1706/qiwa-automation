from src.api.models.qiwa.base import QiwaBaseModel


class GenerateToken(QiwaBaseModel):
    ott: str


class _Payload(QiwaBaseModel):
    sequence_number: int
    set_at: int


class ValidateToken(QiwaBaseModel):
    payload: _Payload
