from src.api.models.qiwa.base import QiwaBaseModel


class CallBack(QiwaBaseModel):
    transId: str
    status: str
