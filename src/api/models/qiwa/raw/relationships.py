from typing import Literal, Optional

from src.api.models.qiwa.base import QiwaBaseModel


class Tag(QiwaBaseModel):
    id: str
    type: Literal["tag", "tag-super"]


class Tags(QiwaBaseModel):
    data: list[Tag]


class EService(QiwaBaseModel):
    id: str
    type: Literal["e-service"]


class EServices(QiwaBaseModel):
    data: list[EService]


class Relationships(QiwaBaseModel):
    e_services: Optional[EServices]
    tags: Optional[Tags]
