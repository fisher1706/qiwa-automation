from typing import Type

from src.api.models.qiwa.data_attr import change_occupation
from src.api.models.qiwa.raw.change_occupation import Meta
from src.api.models.qiwa.raw.root import Root

requests_laborers_data = Root[list[change_occupation.requests_laborers], Type[None], Meta]
