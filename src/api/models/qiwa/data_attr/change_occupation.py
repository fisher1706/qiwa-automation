from typing import Literal, Type

from src.api.models.qiwa.raw.change_occupations.count import RequestsCount
from src.api.models.qiwa.raw.change_occupations.establishment_validate import (
    Rule,
    RuleCodesT,
)
from src.api.models.qiwa.raw.change_occupations.requests import Request
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.change_occupations.users import User
from src.api.models.qiwa.raw.data import Data

request = Data[str, Literal["request"], Request, Type[None]]
requests_laborers = Data[str, Literal["requests-laborers"], RequestLaborer, Type[None]]
change_occupation_count = Data[str, Literal["change-occupation-count"], RequestsCount, Type[None]]
user = Data[Type[None], Literal["user"], User, Type[None]]
rule = Data[RuleCodesT, Literal["rule"], Rule, Type[None]]
