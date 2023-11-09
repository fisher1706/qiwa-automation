from typing import Type

from src.api.models.qiwa.data import change_occupation
from src.api.models.qiwa.raw.change_occupations.meta import Meta
from src.api.models.qiwa.raw.change_occupations.occupations import OccupationsMeta
from src.api.models.qiwa.raw.root import Root

CreatedRequestsData = Root[list[change_occupation.created_request], Type[None], Type[None]]
requests_data = Root[list[change_occupation.request], Type[None], Meta]
request_by_id_data = Root[list[change_occupation.request_by_id], Type[None], Type[None]]
requests_laborers_data = Root[list[change_occupation.requests_laborers], Type[None], Meta]
ChangeOccupationsCountData = Root[
    list[change_occupation.ChangeOccupationCount], Type[None], Type[None]
]
users_data = Root[list[change_occupation.user], Type[None], Meta]
EstablishmentValidationData = Root[change_occupation.Establishment, Type[None], Type[None]]
OccupationsData = Root[list[change_occupation.Occupation], Type[None], OccupationsMeta]
MultiLangErrorsData = Root[list[change_occupation.MultiLangError], Type[None], Type[None]]
