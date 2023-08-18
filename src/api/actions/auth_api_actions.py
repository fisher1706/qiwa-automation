from __future__ import annotations

from typing import Any

import allure

from src.api.clients.auth_api import AuthApi


class AuthApiActions(AuthApi):
    @allure.step("Login via API")
    def login_user(self, login, password):
        self.api.session.cookies.clear()
        self.login(login=login, password=password)
        self.two_factor_auth(login=login, password=password)

    @allure.step("Create prepared user account via API")
    def create_account_via_api(self, account):
        self.api.session.cookies.clear()
        self.init_hsm_with_birthday(account.personal_number)
        self.enable_hsm(account.personal_number)
        self.phone_verification(account.phone_number)
        self.create_account(account)
        self.disable_hsm_session()
        self.api.session.cookies.clear()

    @allure.step
    def select_first_company(self) -> AuthApiActions:
        workspace = self.__get_workspace_with("space-type", "company")
        self.select_company_by_id(workspace["company-id"])
        return self

    @allure.step
    def select_company_with_sequence_number(self, number: int) -> AuthApiActions:
        workspace = self.__get_workspace_with("company-sequence-number", number)
        self.select_company_by_id(workspace["company-id"])
        return self

    def __get_workspace_with(self, attribute: str, value: Any) -> dict:
        get_workspaces = self.get_workspaces()
        workspaces = get_workspaces.json()
        workspace = next(
            workspace["attributes"]
            for workspace in workspaces["data"]
            if workspace["attributes"][attribute] == value
            and workspace["attributes"]["company-id"]
        )
        return workspace
