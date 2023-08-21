from __future__ import annotations

from functools import cached_property
from typing import Optional

import allure

from data.constants import UserInfo
from src.api.actions.workspaces_api_actions import WorkspacesApiActions
from src.api.actions.e_service_controller import EServiceController
from src.api.actions.sso_auth_api_action import AuthApiLaborerSSOActions
from src.api.actions.saudization_api_actions import SaudizationApiActions
from src.api.actions.wp_api_actions import WorkPermitApiActions
from src.api.clients.change_occupation_api import ChangeOccupationApi
from src.api.clients.saudization_api import SaudizationCertificateApi
from src.api.clients.wp_debts_api import WPDebtsApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.raw.token import AuthorizationToken
from utils.crypto_manager import decode_authorization_token


class QiwaApi:
    saudi_api_assertions = SaudizationApiActions()

    def __init__(self) -> None:
        self.client = HTTPClient()
        self.auth = WorkspacesApiActions(self.client)
        self.sso = AuthApiLaborerSSOActions(self.client)
        # APIs
        self.saudi_api = SaudizationCertificateApi(self.client)
        self.wp_debts_api = WPDebtsApi(self.client)
        self.wp_request_api = WorkPermitApiActions(self.client)
        # Controllers
        self.e_service = EServiceController(self.client)

    @cached_property
    def change_occupation(self) -> ChangeOccupationApi:
        return ChangeOccupationApi(self.client, self.authorization_token)

    @property
    def authorization_token(self) -> AuthorizationToken:
        encoded_jwt = self.client.session.cookies.get("qiwa.authorization")
        decoded_jwt = decode_authorization_token(encoded_jwt)
        return AuthorizationToken.parse_obj(decoded_jwt)

    @classmethod
    @allure.step
    def login_as_user(
        cls,
        personal_number: str,
        password: str = UserInfo.PASSWORD,
    ) -> QiwaApi:
        api = cls()
        api.sso.login_user(personal_number, password)
        return api

    @classmethod
    @allure.step
    def login_as_admin(cls) -> QiwaApi:  # Review for a case of several admins
        return cls.login_as_user("1215113732")

    @allure.step
    def select_company(self, sequence_number: Optional[int] = None) -> QiwaApi:
        if sequence_number:
            self.auth.select_company_with_sequence_number(sequence_number)
        else:
            self.auth.select_first_company()
        return self
