from pydantic.main import BaseModel


class EstablishmentInformation(BaseModel):
    LaborOfficeId: str
    # TODO: Correct after fix
    EstablishmentSequanceNumber: str


class GetEstablishmentInformationRq(BaseModel):
    Header: dict
    Body: dict


class GetEstablishmentInformationPayload(BaseModel):
    GetEstablishmentInformationRq: GetEstablishmentInformationRq
