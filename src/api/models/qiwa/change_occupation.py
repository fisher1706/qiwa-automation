from typing import Type

from src.api.models.qiwa.data import change_occupation_request, request
from src.api.models.qiwa.raw.change_occupation import Meta
from src.api.models.qiwa.raw.root import Root

created_change_occupation_requests = Root[list[change_occupation_request], Type[None], Type[None]]
change_occupation_requests_list = Root[list[request], Type[None], Meta]
