from pydantic import BaseModel

from src.api.models.qiwa.base import QiwaBaseModel


class UMPermission(BaseModel):
    subscription_service: bool = True


class SubscriptionCookie(QiwaBaseModel):
    user_id: str
    user_personal_number: str
    exp: int = 1784759999
    company_sequence_number: str
    company_labor_office_id: str
    permissions: UMPermission = UMPermission()
