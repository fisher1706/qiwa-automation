from typing import Optional

import config
from src.api.models.qiwa.base import QiwaBaseModel


class OauthInit(QiwaBaseModel):
    state: Optional[str | dict]
    code: Optional[str]


class Auth(QiwaBaseModel):
    login: Optional[str | int]
    password: Optional[str]
    otp: Optional[str | int]


class Hsm(QiwaBaseModel):
    personal_number: Optional[str | int]
    birth_date: Optional[str] = "1430-01-01"
    otp: Optional[str]


class VerifyPhone(QiwaBaseModel):
    phone: str | int


class VerifyEmail(QiwaBaseModel):
    email: str | int


class CreateAccount(QiwaBaseModel):
    otp: str
    birth_date: str
    email: str
    password: str
    password_confirm: str


class Authorize(QiwaBaseModel):
    client_id: str = "qiwa"
    redirect_uri: str = f"{config.qiwa_urls.auth}/oauth/callback"
    response_type: str = "code"
    scope: str = "openid email phone profile"
    code_challenge_method: str = "S256"
    state: str
    code_challenge: str


class SecurityQuestion(QiwaBaseModel):
    mother_dob: str = "1-1-2011"
    mother_name: str = "Test name"


class Logout(QiwaBaseModel):
    logout_token: str
