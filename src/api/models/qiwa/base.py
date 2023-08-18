from pydantic import BaseModel  # pylint: disable = no-name-in-module


class QiwaBaseModel(BaseModel):
    class Config:
        alias_generator = lambda key: "-".join(  # pylint: disable = unnecessary-lambda-assignment
            key.split("_")
        )
        allow_population_by_field_name = True
