from pydantic import HttpUrl

from src.api.models.qiwa.base import QiwaBaseModel


class EstablishmentValidateAttributes(QiwaBaseModel):
    valid: bool


class EstablishmentValidateMeta(QiwaBaseModel):
    contract_management_url: HttpUrl
