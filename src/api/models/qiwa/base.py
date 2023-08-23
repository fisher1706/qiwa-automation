from pydantic import BaseModel, ConfigDict  # pylint: disable = no-name-in-module


def camel_to_kebab_case(string: str) -> str:
    return "-".join(string.split("_"))


class QiwaBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=camel_to_kebab_case, allow_population_by_field_name=True
    )
