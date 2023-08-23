from typing import Optional

from pydantic import BaseModel

from src.api.constants import nitaq
from src.api.constants.subscription import Subscription


class Establishment(BaseModel):
    managers: int = 1
    users: int = 2
    owners: int = 1
    expat_count: int = 1
    saudi_count: int = 1
    branches: int = 3
    nitaq_color_id: nitaq.ColorID = nitaq.ColorID.GREEN
    nitaq_color_name: nitaq.ColorName = nitaq.ColorName.GREEN
    nitaq_color_code: nitaq.ColorCode = nitaq.ColorCode.GREEN
    economic_activity: int = "1"
    sub_economic_activity: str = "10"
    e_status_id: int = "6"
    activity_id: int = 1
    note_status_id: str = "1"
    note_type_id: str = "2"
    note_source_id: str = "16"
    size_id: int = 1
    have_subscription: Subscription = Subscription.HAVE
    cr_number: Optional[str] = None
    personal_number: Optional[str] = None
    labor_office_id: Optional[str] = None
    sequence_number: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        use_enum_values = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            return "-".join(string.split("_")) if string != "cr_number" else string
