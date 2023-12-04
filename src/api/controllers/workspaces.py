from __future__ import annotations

from typing import Any

import allure

from src.api.clients.workspaces import WorkspacesApi


class WorkspacesApiController(WorkspacesApi):
    @allure.step
    def select_first_company(self) -> WorkspacesApiController:
        workspace = self.__get_workspace_with("space-type", "company")
        self.select_company_by_id(workspace["company-id"])
        return self

    @allure.step
    def select_company_with_sequence_number(self, number: int) -> WorkspacesApiController:
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

    @allure.step
    def select_company_subscription_with_sequence_number(
        self, number: int
    ) -> WorkspacesApiController:
        self.__get_workspace_with("company-sequence-number", number)
        return self
