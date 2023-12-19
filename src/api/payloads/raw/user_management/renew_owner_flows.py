from typing import List

from src.api.models.qiwa.base import QiwaBaseModel
from src.api.payloads.raw.user_management.edit_privileges import Privileges


class RenewExtendOwnerSubscription(QiwaBaseModel):
    totalFeeAmount: int
    lang: str = "en"
    idno: str
    establishments: List[Privileges]


class UpdateEstablishmentAddress(QiwaBaseModel):
    additional_no: int
    building_no: int
    city_id: int
    district_area: str
    street_name: str
    zip_code: int
