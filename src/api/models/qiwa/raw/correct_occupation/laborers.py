from src.api.models.qiwa.base import QiwaBaseModel


class LaborerAttributes(QiwaBaseModel):
    id: int
    laborer_id: str
    laborer_name: str
    gender_id: str
    gender: str
    nationality_name_ar: str
    nationality_name_en: str
    nationality_id: str
    occupation_id: str
    occupation_name_en: str
    occupation_name_ar: str
