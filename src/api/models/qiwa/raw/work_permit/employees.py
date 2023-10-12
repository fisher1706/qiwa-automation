from datetime import date
from typing import Annotated

from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    personal_number: str
    id_release_date: date
    passport_no: str
    name: Annotated[list[str | None], 4]
    first_name: str
    second_name: str | None = ...
    third_name: str | None = ...
    fourth_name: str
    establishment_name: str
    job_id: int
    job_name: str
    nationality_id: int
    nationality_name: str
    gender_id: int
    gender_name: str
    service_start_date: date
    service_end_date: date | None = ...
    kingdom_entry_date: date
    wp_fees: int | None = ...
    extra_fees: int | None = ...
    total_laborer_wp_fees: int | None = ...
    transaction_status_id: int
    transaction_status: str
    transaction_number: str | None = ...
    transaction_date: date
    work_permit_type_id: int
    work_permit_type: str
    wp_number: str | None = ...
    iqama_expiration_date: str
    wp_expiration_date: date | None = ...
    is_regular: bool
    wp_status_id: int
    wp_status_en: str
    wp_status_ar: str
