from typing import Generic, Optional, TypeVar

from pydantic.generics import GenericModel

IdT = TypeVar("IdT")
TypeT = TypeVar("TypeT")
AttributesT = TypeVar("AttributesT")
RelationshipsT = TypeVar("RelationshipsT")


class Data(GenericModel, Generic[IdT, TypeT, AttributesT, RelationshipsT]):
    id: IdT | None = ...
    type: TypeT
    attributes: AttributesT
    relationships: Optional[RelationshipsT]
