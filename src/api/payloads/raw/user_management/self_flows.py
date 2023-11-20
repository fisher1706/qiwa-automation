from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class SelfSubscription(QiwaBaseModel):
    totalFeeAmount: float
    lang: str = "en"
    paymentMethod: Optional[str]
