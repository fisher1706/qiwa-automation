from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class IBMWorkPermitRequest(BaseModel):
    SubmitDate: date
    NumberOfExpats: str
    BillNumber: str
    BillStatus: str
    Status: str
    TransactionFees: str
    RemainingDays: Optional[str]


class IBMWorkPermitRequestList(BaseModel):
    WorkPermitRequests: List[IBMWorkPermitRequest]
    TotalCount: str
