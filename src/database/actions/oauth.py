import allure
from sqlalchemy import DateTime

from data.sso.application import Application
from src.database.sql_requests.sso_requests.oauth_applications import AppRequest


@allure.step
def create_application(account_id: str, application: Application) -> None:
    AppRequest().create_applications_request(account_id=account_id, application_add=application)


@allure.step
def expired_temporary_token(temporary_token: str, expired_time: DateTime) -> None:
    AppRequest().expired_temporary_token_request(
        temporary_token=temporary_token, expired_time=expired_time
    )


@allure.step
def get_application_id(account_id: str, name: str) -> str:
    return AppRequest().get_application_id_request(account_id=account_id, name=name)
