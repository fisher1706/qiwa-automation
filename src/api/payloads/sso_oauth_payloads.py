from data.account import Account
from src.api.payloads.raw.sso_oauth import (
    Auth,
    CreateAccount,
    Hsm,
    Logout,
    OauthInit,
    SecurityQuestion,
    VerifyEmail,
    VerifyPhone,
)
from src.api.payloads.sso.sso_attributes_data import (
    account_attributes,
    login_attributes,
    oauth_callback,
    oauth_init,
    otp_attributes,
    password,
    registration,
    session,
    user_email,
)


def registration_account_payload(account: Account) -> dict:
    attributes = CreateAccount(
        otp=account.confirmation_code,
        birth_date=account.birth_day,
        email=account.email,
        password=account.password,
        password_confirm=account.password,
    )
    return account_attributes(attributes).dict(by_alias=True)


def init_sso_hsm_payload(personal_number: str | int, birth_date: str) -> dict:
    attributes = Hsm(personal_number=personal_number, birth_date=birth_date)
    return session(attributes).dict(by_alias=True, exclude_unset=True)


def activate_sso_hsm_payload(absher_code: str) -> dict:
    attributes = Hsm(otp=absher_code)
    return registration(attributes).dict(exclude_unset=True)


def phone_verification_payload(phone: str | int) -> dict:
    attributes = VerifyPhone(phone=phone)
    return registration(attributes).dict()


def email_verification_payload(email: str | int) -> dict:
    attributes = VerifyEmail(email=email)
    return user_email(attributes).dict()


def otp_code_payload(otp: str) -> dict:
    attributes = Auth(otp=otp)
    return password(attributes).dict(exclude_unset=True)


def security_question_payload() -> dict:
    attributes = SecurityQuestion()
    return account_attributes(attributes).dict(by_alias=True)


def login_payload(login: str, account_pwd: str) -> dict:
    attributes = Auth(login=login, password=account_pwd)
    return login_attributes(attributes).dict(exclude_unset=True)


def login_with_otp_payload(otp: str) -> dict:
    attributes = Auth(otp=otp)
    return otp_attributes(attributes).dict(exclude_unset=True)


def oauth_init_payload() -> dict:
    attributes = OauthInit(state={})
    return oauth_init(attributes).dict(exclude_unset=True)


def oauth_callback_payload(state: str, code: str) -> dict:
    attributes = OauthInit(state=state, code=code)
    return oauth_callback(attributes).dict(exclude_unset=True)


def logout_payload(logout_token: str) -> dict:
    attributes = Logout(logout_token=logout_token)
    return session(attributes).dict(by_alias=True)
