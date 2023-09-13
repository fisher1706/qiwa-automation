from pydantic import BaseModel


class Service(BaseModel):
    client_service_id: str
    sub_service_id: str


change_occupation = Service(client_service_id="3", sub_service_id="6")

work_permit = Service(client_service_id="4", sub_service_id="12")
