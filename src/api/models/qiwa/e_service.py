from typing import Type

from src.api.models.qiwa import raw
from src.api.models.qiwa.data import e_service as data
from src.api.models.qiwa.raw.root import Root

user_e_services = Root[
    list[data.service_group], list[data.e_service | data.tag], raw.e_service.Meta
]
admin_e_services = Root[
    list[data.e_service_super], list[data.group_super | data.tag_super], raw.e_service.MetaSuper
]
admin_groups_list = Root[list[data.group_super], list[data.included_e_service], Type[None]]
admin_created_group = Root[data.group, list[data.e_service], Type[None]]
