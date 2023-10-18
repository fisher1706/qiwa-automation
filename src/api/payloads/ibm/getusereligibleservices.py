from pydantic import BaseModel


class GetUserEligibleServicesRqBody(BaseModel):
    IdNo: str
    LaborOfficeId: str
    EstablishmentSequence: str
    PageSize: int = 100
    PageIndex: int = 1


class GetUserEligibleServicesRq(BaseModel):
    Header: dict
    Body: GetUserEligibleServicesRqBody


class GetUserEligibleServicesRqPayload(BaseModel):
    GetUserEligibleServicesRq: GetUserEligibleServicesRq
