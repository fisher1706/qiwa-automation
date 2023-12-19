from src.api.models.qiwa.base import QiwaBaseModel


class CorrectOccupationAttributes(QiwaBaseModel):
    id: int
    occupation_id: str
    occupation_ar: str
    occupation_en: str
