from src.api.models.qiwa.base import QiwaBaseModel


class OccupationAttributes(QiwaBaseModel):
    english_name: str
    arabic_name: str
    code: str


class OccupationsMeta(QiwaBaseModel):
    current_page: int
    next_page: int | None = ...
    prev_page: int | None = ...
    total_count: int
    total_pages: int
