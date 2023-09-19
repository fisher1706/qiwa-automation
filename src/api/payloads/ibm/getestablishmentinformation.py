from pydantic.main import BaseModel


class EstablishmentInformation(BaseModel):
    LaborOfficeId: str
    EstablishmentSequenceNumber: str


class GetEstablishmentInformationRq(BaseModel):
    Header: dict
    Body: dict


class GetEstablishmentInformationPayload(BaseModel):
    GetEstablishmentInformationRq: GetEstablishmentInformationRq
