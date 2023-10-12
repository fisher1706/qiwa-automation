from pydantic.generics import GenericModel  # pylint: disable = no-name-in-module


class QiwaBaseModel(GenericModel):
    class Config:
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            return "-".join(string.split("_"))
