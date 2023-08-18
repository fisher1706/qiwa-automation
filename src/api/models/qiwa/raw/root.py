from typing import Generic, Optional, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")
IncludedT = TypeVar("IncludedT")
MetaT = TypeVar("MetaT")


class Root(GenericModel, Generic[DataT, IncludedT, MetaT]):
    data: DataT
    included: Optional[IncludedT]
    meta: Optional[MetaT]
