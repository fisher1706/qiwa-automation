from __future__ import annotations

from typing import Optional

import allure

from data.constants import UserInfo
from src.api.assertions.saudization_certificate import SaudizationApiAssertions
from src.api.clients.lo.users import UsersApi
from src.api.clients.payment import PaymentApi
from src.api.clients.saudization_certificate import SaudizationCertificateApi
from src.api.clients.spaces import SpacesApi
from src.api.clients.user_management import UserManagementApi
from src.api.clients.work_permit import WorkPermitsApi
from src.api.clients.wp_debts import WPDebtsApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.controllers.delegation import DelegationApiController
from src.api.controllers.e_service import EServiceApiController
from src.api.controllers.lmi.dashboard_api_actions import DashboardApiAction
from src.api.controllers.lmi.dimensions_api_actions import DimensionsApiAction
from src.api.controllers.lmi.survey_questions_api_actions import (
    SurveyQuestionsApiAction,
)
from src.api.controllers.lmi.survey_result_api_actions import SurveyResultApiAction
from src.api.controllers.lmi.weq_api_actions import WeqApiAction
from src.api.controllers.lo.offices_api_actions import OfficesApiActions
from src.api.controllers.lo.services_api_actions import ServiceApiActions
from src.api.controllers.lo.visits_api_actions import VisitsApiActions
from src.api.controllers.sso.sso_auth import AuthApiSSOController
from src.api.controllers.user_management import UserManagementControllers
from src.api.controllers.visits import VisitsApiController
from src.api.controllers.workspaces import WorkspacesApiController
from src.api.http_client import HTTPClient
from src.api.models.qiwa.raw.token import AuthorizationToken
from utils.crypto_manager import decode_authorization_token


class QiwaApi:  # pylint: disable=too-many-instance-attributes
    saudi_api_assertions = SaudizationApiAssertions()

    def __init__(self) -> None:
        self.client = HTTPClient()
        self.auth = WorkspacesApiController(self.client)
        self.sso = AuthApiSSOController(self.client)
        # APIs
        self.saudi_api = SaudizationCertificateApi(self.client)
        self.wp_debts_api = WPDebtsApi(self.client)
        self.work_permits_api = WorkPermitsApi(self.client)
        self.offices_api_action = OfficesApiActions(self.client)
        self.services_api_actions = ServiceApiActions(self.client)
        self.visits_api_actions = VisitsApiActions(self.client)
        self.users_api = UsersApi(self.client)
        self.spaces_api = SpacesApi(self.client)
        self.user_management_api = UserManagementApi(self.client)
        self.payment = PaymentApi(self.client)
        # Controllers
        self.change_occupation = ChangeOccupationController(self.client)
        self.visits_api = VisitsApiController(self.client)
        self.e_service = EServiceApiController(self.client)
        self.dashboard_api_actions = DashboardApiAction(self.client)
        self.dimensions_api_actions = DimensionsApiAction(self.client)
        self.survey_questions_api_actions = SurveyQuestionsApiAction(self.client)
        self.survey_result_api_actions = SurveyResultApiAction(self.client)
        self.weq_api_actions = WeqApiAction(self.client)
        self.delegation_api = DelegationApiController(self.client)
        self.user_management = UserManagementControllers(self.client)

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

    @allure.step
    def select_company_subscription(self, sequence_number: int) -> QiwaApi:
        self.auth.select_company_subscription_with_sequence_number(sequence_number)
        return self
