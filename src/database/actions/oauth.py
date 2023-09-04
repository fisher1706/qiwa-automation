import allure
from sqlalchemy import DateTime
from sqlalchemy.orm import Session

from src.api.features.application import Application
from src.database.sql_requests.oauth_applications import (
    create_applications_request,
    expired_temporary_token_request,
    get_application_id_request,
)


@allure.step
def create_application(session: Session, account_id: str, application: Application) -> None:
    create_applications_request(
        session=session, account_id=account_id, application_add=application
    )


@allure.step
def expired_temporary_token(
    session: Session, temporary_token: str, expired_time: DateTime
) -> None:
    expired_temporary_token_request(
        session=session, temporary_token=temporary_token, expired_time=expired_time
    )


@allure.step
def get_application_id(session: Session, account_id: str, name: str) -> str:
    return get_application_id_request(session=session, account_id=account_id, name=name)
