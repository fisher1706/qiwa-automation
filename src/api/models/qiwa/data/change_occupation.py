from typing import Literal, Type

from src.api.models.qiwa.raw.change_occupations.count import (
    ChangeOccupationCountAttributes,
)
from src.api.models.qiwa.raw.change_occupations.create_request import CreatedRequest
from src.api.models.qiwa.raw.change_occupations.error import MultiLangErrorAttributes
from src.api.models.qiwa.raw.change_occupations.establishment_validate import (
    EstablishmentValidateAttributes,
)
from src.api.models.qiwa.raw.change_occupations.occupations import OccupationAttributes
from src.api.models.qiwa.raw.change_occupations.requests import Request, RequestByID
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.change_occupations.users import User
from src.api.models.qiwa.raw.data import Data

created_request = Data[
    Type[None], Literal["change-occupation-request"], CreatedRequest, Type[None]
]
request = Data[str, Literal["request"], Request, Type[None]]
request_by_id = Data[str, Literal["request"], RequestByID, Type[None]]
requests_laborers = Data[str, Literal["requests-laborers"], RequestLaborer, Type[None]]
ChangeOccupationCount = Data[
    str, Literal["change-occupation-count"], ChangeOccupationCountAttributes, Type[None]
]
user = Data[Type[None], Literal["user"], User, Type[None]]
Establishment = Data[str, Literal["establishment"], EstablishmentValidateAttributes, Type[None]]
Occupation = Data[Type[None], Literal["occupation"], OccupationAttributes, Type[None]]
MultiLangError = Data[str, Literal["multi-lang-error"], MultiLangErrorAttributes, Type[None]]
