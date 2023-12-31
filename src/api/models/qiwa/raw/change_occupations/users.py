from datetime import datetime

from src.api.models.qiwa.base import QiwaBaseModel


class Reason(QiwaBaseModel):
    code: str
    ar_description: str
    en_description: str


class User(QiwaBaseModel):
    personal_number: str
    name: str
    status_code: str
    pk_laborer_id: str
    establishment_number: str
    establishment_name: str
    id_expire_date: datetime
    nationality_code: str
    nationality_name_en: str
    nationality_name_ar: str
    occupation_code: str
    occupation_name_en: str
    occupation_name_ar: str
    entry_date: datetime | None
    eligibility: str
    iqama_border_number: str
    reasons: list[Reason] | None
