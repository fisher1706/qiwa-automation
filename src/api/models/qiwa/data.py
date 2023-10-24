from typing import Literal, Type, Union

from src.api.models.qiwa import raw
from src.api.models.qiwa.raw.data import Data
from src.api.models.qiwa.raw.relationships import Relationships

group = Data[str, Literal["group"], raw.e_service.Group, Relationships]
service_group = Data[int, Literal["service-group"], raw.e_service.ServiceGroup, Relationships]
group_super = Data[str, Literal["group-super"], raw.e_service.GroupSuper, Relationships]
e_service = Data[Union[str, int], Literal["e-service"], raw.e_service.EService, Relationships]
e_service_super = Data[int, Literal["e-service-super"], raw.e_service.EServiceSuper, Relationships]
tag = Data[str, Literal["tag"], raw.e_service.Tag, Type[None]]
tag_super = Data[int, Literal["tag-super"], raw.e_service.TagSuper, Type[None]]
