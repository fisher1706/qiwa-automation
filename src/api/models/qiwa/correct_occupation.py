from pydantic import BaseModel

from src.api.models.qiwa.data.correct_occupation import (
    CorrectOccupation,
    Laborer,
    OccupationCorrectionRequest,
)
from src.api.models.qiwa.raw.correct_occupation.meta import Meta


class LaborersData(BaseModel):
    data: list[Laborer]
    meta: Meta


class RequestsData(BaseModel):
    data: list[OccupationCorrectionRequest]
    meta: Meta


class CorrectOccupationsData(BaseModel):
    data: list[CorrectOccupation]
    meta: Meta
