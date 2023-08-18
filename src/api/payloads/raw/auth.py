from typing import Optional

from src.api.models.qiwa.base import QiwaBaseModel


class Birthday(QiwaBaseModel):
    year: str = "1430"
    month: str = "01"
    day: str = "01"


class RestorePassword(QiwaBaseModel):
    personal_number: Optional[str | int]
    token: Optional[str]
    new_password: Optional[str]
    new_password_confirmation: Optional[str]


class Auth(QiwaBaseModel):
    login: str | int
    password: str
    otp_code: Optional[str | int]


class Hsm(QiwaBaseModel):
    personal_number: Optional[str | int]
    birthday: Optional[Birthday] = Birthday()
    sms_code: Optional[str]


class VerifyPhone(QiwaBaseModel):
    phone_number: str | int
    locale: str
    personal_number: Optional[str | int]


class CreateAccount(QiwaBaseModel):
    personal_number: str | int
    email: str
    password: str
    password_confirmation: str
    phone_number: Optional[str]
    confirmation_code: str
    language: str = "en"


class ConfirmationToken(QiwaBaseModel):
    confirmation_token: str
