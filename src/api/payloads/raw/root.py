from typing import Generic, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Root(GenericModel, Generic[DataT]):
    data: DataT
