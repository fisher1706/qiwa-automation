from typing import Literal

from src.api.models.qiwa.base import QiwaBaseModel
from src.api.models.qiwa.raw.correct_occupation.correct_occupations import (
    CorrectOccupationAttributes,
)
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes
from src.api.models.qiwa.raw.correct_occupation.requests import (
    OccupationCorrectionRequestAttributes,
)


class Laborer(QiwaBaseModel):
    id: str
    type: Literal["laborer"]
    attributes: LaborerAttributes


class OccupationCorrectionRequest(QiwaBaseModel):
    id: str
    type: Literal["occupation-correction-request"]
    attributes: OccupationCorrectionRequestAttributes


class CorrectOccupation(QiwaBaseModel):
    id: str
    type: Literal["occupation"]
    attributes: CorrectOccupationAttributes
