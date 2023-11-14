from src.api.models.qiwa.base import QiwaBaseModel


class ChangeOccupationCountAttributes(QiwaBaseModel):
    status_id: int
    status_en: str
    status_ar: str
    requests_count: int
