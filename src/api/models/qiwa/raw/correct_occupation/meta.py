from src.api.models.qiwa.base import QiwaBaseModel


class Meta(QiwaBaseModel):
    current_page: int
    total_entities: int
    pages_count: int
