from pydantic import BaseModel


class GetWorkspaceEstablishmentsRqBody(BaseModel):
    IdNo: str


class GetWorkspaceEstablishmentsRq(BaseModel):
    Header: dict
    Body: GetWorkspaceEstablishmentsRqBody


class GetWorkspaceEstablishmentsRqPayload(BaseModel):
    GetQiwaWorkspaceEstablishmentsRq: GetWorkspaceEstablishmentsRq
