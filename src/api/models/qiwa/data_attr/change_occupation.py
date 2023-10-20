from typing import Literal, Type

from src.api.models.qiwa.raw.change_occupation import RequestLaborer
from src.api.models.qiwa.raw.data import Data

requests_laborers = Data[str, Literal["requests-laborers"], RequestLaborer, Type[None]]
