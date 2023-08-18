from pydantic import Field

from src.api.models.qiwa.base import QiwaBaseModel


class EService(QiwaBaseModel):
    id: str = "266"


class Tag(QiwaBaseModel):
    id: str
    title_en: str


class Group(QiwaBaseModel):
    title_ar: str = "Autotest شسزرذدخحجثتباءيوهنملكقفغعظطضصىئؤةإأٱآ"
    title_en: str = "Autotest EN Title"
    e_services: list[EService] = [EService()]
    description_ar: str = "ملكقفغع"
    description_en: str = "EN description"
    rules_ar: str = "Rules AR"
    rules_en: str = "Rules EN"
    message_ar: str = "Message AR"
    message_en: str = "Message EN"
    image: str = "data:image"
    tags: list[Tag] = Field(default_factory=list)
