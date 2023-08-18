from typing import Literal, Type

from src.api.models.qiwa.raw.data import Data
from src.api.models.qiwa.raw.e_service import IncludedEService

e_service = Data[str, Literal["e-service"], IncludedEService, Type[None]]
