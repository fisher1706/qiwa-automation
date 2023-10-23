from pydantic import Field

from src.api.models.qiwa.base import QiwaBaseModel


class Total(QiwaBaseModel):
    value: int


class Meta(QiwaBaseModel):
    pages_count: int
    current_page: int
    total_entities: int
    from_: int = Field(alias="from")
    size: int
    max_score: int | None = ...
    total_pages: int
    total: Total
