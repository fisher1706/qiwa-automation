from typing import Optional

from pydantic.main import BaseModel


class UserInfo(BaseModel):
    UserId: str
    IDNumber: str


class Header(BaseModel):
    TransactionId: str
    ChannelId: Optional[str]
    SessionId: Optional[str]
    RequestTime: str
    MWRequestTime: Optional[str]
    ServiceCode: str
    DebugFlag: Optional[str]
    UserInfo: Optional[UserInfo]
