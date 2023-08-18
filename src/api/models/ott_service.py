from pydantic import BaseModel


class GenerateToken(BaseModel):
    ott: str


class _Payload(BaseModel):
    set_at: int


class ValidateToken(BaseModel):
    payload: _Payload
