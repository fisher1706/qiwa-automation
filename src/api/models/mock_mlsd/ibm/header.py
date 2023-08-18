from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ResponseHeaderStatus(BaseModel):
    Status: str
    Code: str
    ArabicMsg: str
    EnglishMsg: str


class IBMResponseHeader(BaseModel):
    TransactionId: Optional[str]
    ChannelId: Optional[str]
    SessionId: Optional[str]
    RequestTime: Optional[datetime]
    MWRequestTime: Optional[datetime]
    MWResponseTime: Optional[datetime]
    ServiceCode: Optional[str]
    DebugFlag: Optional[str]
    ResponseStatus: ResponseHeaderStatus
