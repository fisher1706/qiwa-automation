from pydantic import BaseModel


class SubscriptionItem(BaseModel):
    SubscriptionId: str
    Duration: str = "5"
    LaborOfficeId: str
    SequenceNumber: str
    EstablishmentId: str


class SubscriptionsList(BaseModel):
    SubscriptionItem: SubscriptionItem


class Body(BaseModel):
    SubscriptionsList: SubscriptionsList
