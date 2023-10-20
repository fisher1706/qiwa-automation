from typing import Literal, Type

from src.api.models.qiwa.raw.change_occupation import RequestLaborer, RequestsCount, Request
from src.api.models.qiwa.raw.data import Data

request = Data[str, Literal["request"], Request, Type[None]]
requests_laborers = Data[str, Literal["requests-laborers"], RequestLaborer, Type[None]]
change_occupation_count = Data[str, Literal["change-occupation-count"], RequestsCount, Type[None]]
