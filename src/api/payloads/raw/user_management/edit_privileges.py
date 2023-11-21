from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class Privileges(QiwaBaseModel):
    laborOfficeId: str
    sequenceNumber: str
    privilegeIds: Optional[list]
