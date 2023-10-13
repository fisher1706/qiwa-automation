from src.api.models.qiwa.base import QiwaBaseModel


class SelfSubscription(QiwaBaseModel):
    totalFeeAmount: int
    lang: str = "en"
    paymentMethod: str = "CARD"
