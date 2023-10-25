from pydantic import BaseModel


class GetUserEstablishmentsMLSDLORqBody(BaseModel):
    IdNo: str


class GetUserEstablishmentsMLSDLORq(BaseModel):
    Header: dict
    Body: GetUserEstablishmentsMLSDLORqBody


class GetUserEstablishmentsMLSDLORqPayload(BaseModel):
    GetUserEstablishmentsMLSDLORq: GetUserEstablishmentsMLSDLORq
