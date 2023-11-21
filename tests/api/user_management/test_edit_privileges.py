import allure

from data.user_management.user_management_datasets import Privileges
from data.user_management.user_management_users import (
    delegator_for_edit_flow,
    owner_account,
)
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("E2e update privileges flow")
@case_id(54974)
def test_update_privileges_flow():
    owner = owner_account
    subscribed_user = delegator_for_edit_flow
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    qiwa.user_management_api.post_update_privileges(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number,
        labor_office_id=owner.labor_office_id,
        sequence_number=owner.sequence_number,
        privileges=Privileges.default_privileges,
    )


@allure.title("Check users privileges")
@case_id(7920)
def test_check_users_privileges():
    owner = owner_account
    subscribed_user = delegator_for_edit_flow
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    privileges = qiwa.user_management_api.get_user_privileges(
        cookie=subscription_cookie, users_personal_number=subscribed_user.personal_number
    )["privilegeIds"]
    assert_that(privileges).is_not_empty()


@allure.title("Check expire date")
@case_id(44515)
def test_expire_date():
    owner = owner_account
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    qiwa.user_management.compare_expired_date_in_db_and_in_endpoint(
        subscription_cookie, owner.personal_number, owner.unified_number_id
    )
