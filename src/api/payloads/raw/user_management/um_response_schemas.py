from pydantic import BaseModel


class SubscriptionNumberOfUsers(BaseModel):
    totalFeeAmount: float
    includeVat: float
