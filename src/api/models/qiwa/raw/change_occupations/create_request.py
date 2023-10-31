from src.api.models.qiwa.base import QiwaBaseModel


class CreatedRequest(QiwaBaseModel):
    request_id: str
    personal_number: str
