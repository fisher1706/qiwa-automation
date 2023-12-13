from datetime import datetime

from pydantic import BaseModel

from src.api.models.qiwa.base import QiwaBaseModel


class Item(BaseModel):
    code: str
    name_ar: str
    name_en: str


class OccupationCorrectionRequestAttributes(QiwaBaseModel):
    id: int
    laborer_id: str
    laborer_name: str
    request_id: str
    rejection_reason: str
    creation_date: datetime
    current_occupation: Item
    new_occupation: Item
    status: Item


class SubmitOccupationResponseAttributes(QiwaBaseModel):
    id: int
    request_id: str
