from src.api.models.qiwa.base import QiwaBaseModel


class Laborer(QiwaBaseModel):
    personal_number: str
    occupation_code: str
