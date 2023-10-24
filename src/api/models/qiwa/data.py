from typing import Any, List, Literal, Type, Union

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
saudization_certificate = Data[
    str,
    Literal["saudization-certificate"],
    raw.saudi_certificate.SaudizationCertificate,
    Type[None],
]
encrypted_saudization_certificate = Data[
    str,
    Literal["encrypted-saudization-certificate"],
    raw.saudi_certificate.EncryptedSaudizationCertificate,
    Type[None],
]
error = Data[str, Literal["error"], raw.saudi_certificate.Error, Type[None]]
not_found = Data[Literal["-1"], Literal["not_found"], List[Any], Type[None]]
