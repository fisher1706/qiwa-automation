from typing import List

import allure

from utils.assertion import assert_that


@allure.step("Verify workspace establishments response contains eligible workspaces")
def assert_eligible_workspace_establishments(workspace_establishments: dict) -> None:
    assert_that("EligibleEstablishmentsList" in workspace_establishments)


@allure.step("Verify workspace establishments response contains non-eligible workspaces")
def assert_non_eligible_workspace_establishments(workspace_establishments: dict) -> None:
    assert_that("NonEligibleEstablishmentsList" in workspace_establishments)


@allure.step("Verify user eligible services response contains required ids")
def assert_user_eligible_services_contains_required_ids(actual: List[str], expected: List["str"]):
    assert_that(all(x in actual for x in expected))
