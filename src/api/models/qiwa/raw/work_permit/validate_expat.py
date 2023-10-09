from typing import Generic, TypeVar, Optional

from pydantic import BaseModel, validator
from pydantic.generics import GenericModel

ErrorT = TypeVar("ErrorT")
ResultT = TypeVar("ResultT")


class ValidationResult(BaseModel):
    valid_twelve_months: bool
    valid_nine_months: bool
    valid_six_months: bool
    valid_three_months: bool
    valid: bool

    @validator("valid_nine_months", "valid_six_months", "valid_three_months")
    def periods_synchronization(cls, value, values):  # pylint: disable=no-self-argument
        if not any([values.values]):
            assert value is False, f"validated period is {value} but {[values]}"
        return value

    @validator("valid")
    def validation_according_to_periods(cls, value, values):  # pylint: disable=no-self-argument
        if value != any([values.values]):
            raise ValueError(f"'valid' key is {value} but {values}")
        return value


class ValidateExpat(GenericModel, Generic[ResultT, ErrorT]):
    expat_number: str
    validation_result: ResultT
    errors: Optional[ErrorT]


class Error(BaseModel):
    code: str
    message_ar: str
    message_en: str
