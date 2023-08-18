from typing import Generic, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class Data(GenericModel, Generic[DataT]):
    type: str
    attributes: DataT


class Root(GenericModel, Generic[DataT]):
    data: Data[DataT]
