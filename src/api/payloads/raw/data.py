from typing import Generic, TypeVar

from pydantic.generics import GenericModel

TypeT = TypeVar("TypeT")
AttributesT = TypeVar("AttributesT")


class Data(GenericModel, Generic[TypeT, AttributesT]):
    type: TypeT
    attributes: AttributesT
