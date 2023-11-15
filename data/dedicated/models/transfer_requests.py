from typing import Optional

from pydantic import BaseModel


class TransferRequests(BaseModel):
    req_number: Optional[str]
    employee_name: Optional[str]
    iqama_number: Optional[str]
    current_establishment: Optional[str]
    new_establishment: Optional[str]
    status: Optional[str]
    release_date: Optional[str]
    actions: Optional[str]


request = TransferRequests(req_number="9-100216-1444")
