from typing import Literal

from src.api.models.qiwa.base import QiwaBaseModel
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes


class Laborer(QiwaBaseModel):
    id: str
    type: Literal["laborer"]
    attributes: LaborerAttributes
