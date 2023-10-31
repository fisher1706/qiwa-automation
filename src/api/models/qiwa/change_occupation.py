from typing import Type

from src.api.models.qiwa.data import change_occupation
from src.api.models.qiwa.raw.change_occupations import establishment_validate
from src.api.models.qiwa.raw.change_occupations.meta import Meta
from src.api.models.qiwa.raw.root import Root

CreatedRequestsData = Root[list[change_occupation.created_request], Type[None], Type[None]]
requests_data = Root[list[change_occupation.request], Type[None], Meta]
request_by_id_data = Root[list[change_occupation.request_by_id], Type[None], Type[None]]
requests_laborers_data = Root[list[change_occupation.requests_laborers], Type[None], Meta]
change_occupation_count_data = Root[
    list[change_occupation.change_occupation_count], Type[None], Type[None]
]
users_data = Root[list[change_occupation.user], Type[None], Meta]
validation_data = Root[list[change_occupation.rule], Type[None], establishment_validate.Meta]
