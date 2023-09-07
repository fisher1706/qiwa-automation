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
