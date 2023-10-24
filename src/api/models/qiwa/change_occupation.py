from typing import Type

from src.api.models.qiwa.data import change_occupation
from src.api.models.qiwa.raw.change_occupations.establishment_validate import (
    Meta as ValidationMeta,
)
from src.api.models.qiwa.raw.change_occupations.meta import Meta
from src.api.models.qiwa.raw.root import Root

requests_data = Root[list[change_occupation.request], Type[None], Meta]
requests_laborers_data = Root[list[change_occupation.requests_laborers], Type[None], Meta]
change_occupation_count_data = Root[
    list[change_occupation.change_occupation_count], Type[None], Type[None]
]
users_data = Root[list[change_occupation.user], Type[None], Meta]
validation_data = Root[list[change_occupation.rule], Type[None], ValidationMeta]
