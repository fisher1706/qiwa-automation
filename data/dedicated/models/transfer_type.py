from pydantic import BaseModel


class TransferType(BaseModel):
    code: str
    name_ar: str
    name_en: str

