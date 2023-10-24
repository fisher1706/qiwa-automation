from typing import Literal

from pydantic import BaseModel

from src.api.models.qiwa.base import QiwaBaseModel


class _Message(BaseModel):
    message_en: str
    message_ar: str


class SuccessfulCancelling(BaseModel):
    message: _Message


class CancellingError(QiwaBaseModel):
    id: Literal[-1]
    code: str
    status: Literal["ERROR"]
    english_msg: str
    arabic_msg: str
    transaction_id: str
    service_code: Literal["CWPB0001"]
