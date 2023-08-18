from typing import Any, Type, TypeVar

import allure
from pydantic.main import BaseModel

Model = TypeVar("Model", bound="BaseModel")


@allure.step
def validate_model(obj: Any, model: Type[BaseModel]) -> Model:
    return model.parse_obj(obj)
