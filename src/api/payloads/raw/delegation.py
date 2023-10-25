from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class GetDelegations(QiwaBaseModel):
    entityTypeId: str = "GOVERNMENT"
    page: int = 1
    size: int = 10
    sort: str = "id"
    direction: str = "DESC"
    statusEn: Optional[str]
    statusAr: Optional[str]
    entityId: Optional[str]
    search: Optional[str]


class CreateDelegation(QiwaBaseModel):
    employeeNid: str
    entityId: str = "NAFITH"
    permissionsId: list = ["NAFITH-F04"]
    durationMonth: int


class ChangeRequestStatus(QiwaBaseModel):
    status: str
    rejectReason: Optional[str]


class ResendDelegationRequest(QiwaBaseModel):
    id: int
