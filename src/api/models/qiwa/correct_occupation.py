from pydantic import BaseModel

from src.api.models.qiwa.data.correct_occupation import Laborer
from src.api.models.qiwa.raw.correct_occupation.meta import Meta


class LaborersData(BaseModel):
    data: list[Laborer]
    meta: Meta
