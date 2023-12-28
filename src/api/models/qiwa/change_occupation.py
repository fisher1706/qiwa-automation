from typing import Type

from pydantic import BaseModel

from src.api.models.qiwa.data import change_occupation
from src.api.models.qiwa.raw.change_occupations.establishment_validate import (
    EstablishmentValidateMeta,
)
from src.api.models.qiwa.raw.change_occupations.meta import Meta
from src.api.models.qiwa.raw.change_occupations.occupations import OccupationsMeta
from src.api.models.qiwa.raw.root import Root

CreatedRequestsData = Root[list[change_occupation.created_request], Type[None], Type[None]]
RequestsData = Root[list[change_occupation.request], Type[None], Meta]
RequestByIdData = Root[list[change_occupation.request_by_id], Type[None], Type[None]]
RequestsLaborersData = Root[list[change_occupation.requests_laborers], Type[None], Meta]
ChangeOccupationsCountData = Root[
    list[change_occupation.ChangeOccupationCount], Type[None], Type[None]
]
UsersData = Root[list[change_occupation.user], Type[None], Meta]
EstablishmentValidationData = Root[change_occupation.Establishment, Type[None], Type[None]]
OccupationsData = Root[list[change_occupation.Occupation], Type[None], OccupationsMeta]


class MultiLangErrorsData(BaseModel):
    data: list[change_occupation.MultiLangError]
    meta: EstablishmentValidateMeta | None
