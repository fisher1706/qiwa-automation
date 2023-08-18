from typing import Dict, Generic, TypeVar

from pydantic.generics import GenericModel

from src.api.constants.ibm import IBMServicesResponse
from src.api.models.mock_mlsd.ibm.header import IBMResponseHeader

IBMDataBodyT = TypeVar("IBMDataBodyT")


class IBMResponseData(GenericModel, Generic[IBMDataBodyT]):
    Header: IBMResponseHeader
    Body: IBMDataBodyT


class IBMResponse(GenericModel, Generic[IBMDataBodyT]):
    __root__: Dict[IBMServicesResponse, IBMResponseData[IBMDataBodyT]]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]
