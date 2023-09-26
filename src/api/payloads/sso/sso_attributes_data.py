from typing import Any

from src.api.payloads.raw.data import Data
from src.api.payloads.raw.root import Root


def oauth_init(attributes: Any) -> Root:
    return Root(data=Data(type="oauth-init", attributes=attributes))


def oauth_callback(attributes: Any) -> Root:
    return Root(data=Data(type="oauth-callback", attributes=attributes))


def account_attributes(attributes: Any) -> Root:
    return Root(data=Data(type="account", attributes=attributes))


def session(attributes: Any) -> Root:
    return Root(data=Data(type="session", attributes=attributes))


def registration(attributes: Any) -> Root:
    return Root(data=Data(type="registration", attributes=attributes))


def user_email(attributes: Any) -> Root:
    return Root(data=Data(type="user-email", attributes=attributes))


def password(attributes: Any) -> Root:
    return Root(data=Data(type="password", attributes=attributes))


def login_attributes(attributes: Any) -> Root:
    return Root(data=Data(type="login", attributes=attributes))


def otp_attributes(attributes: Any) -> Root:
    return Root(data=Data(type="otp", attributes=attributes))