from pydantic.main import BaseModel


class Token(BaseModel):
    grant_type: str
    scope: str
    client_id: str
    client_secret: str
