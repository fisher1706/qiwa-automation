from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class OauthInit(QiwaBaseModel):
    state: Optional[str | dict]
    code: Optional[str]
