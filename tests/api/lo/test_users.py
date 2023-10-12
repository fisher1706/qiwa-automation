import pytest

from data.lo.constants import LOAdmin, LOUser, UserInfo
from src.api.app import QiwaApi
from src.api.assertions.response_validator import ResponseValidator
from utils.assertion import assert_that
from utils.json_search import search_in_json


def test_get_user():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    _, content = qiwa.users_api.get_user(user_id=LOUser.ID)
    assert_that(search_in_json('data[*].id', content) == LOUser.ID)


def test_get_users():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    response, _ = qiwa.users_api.get_users()
    assert_that(ResponseValidator(response).check_response_schema('lo_users.json'))


def test_edit_user():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    last_office_id = qiwa.offices_api_action.get_last_office_id()
    qiwa.users_api.edit_user(
        user_id=LOUser.ID,
        email=UserInfo.EMAIL_EDITED,
        role_id=LOUser.LO_SYS_ADMIN_ROLE_ID,
        office_id=last_office_id
    )
    _, content = qiwa.users_api.get_user(user_id=LOUser.ID)
    assert_that(search_in_json('data[*].attributes."role-id"', content) == LOUser.LO_SYS_ADMIN_ROLE_ID)
    assert_that(search_in_json('data[*].attributes.email', content) == UserInfo.EMAIL_EDITED)
    assert_that(search_in_json('included[*].id', content) == last_office_id)


@pytest.mark.skip("Skipped due to lack of test data")
def test_add_user():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    last_office_id = qiwa.offices_api_action.get_last_office_id()
    qiwa.users_api.add_user(
        user_id=LOUser.ID,
        email=UserInfo.EMAIL_EDITED,
        role_id=LOUser.LO_SYS_ADMIN_ROLE_ID,
        office_id=last_office_id
    )
    _, content = qiwa.users_api.get_user(user_id=LOUser.ID)
    assert_that(search_in_json('data[*].attributes."role-id"', content) == LOUser.LO_SYS_ADMIN_ROLE_ID)
    assert_that(search_in_json('data[*].attributes.email', content) == UserInfo.EMAIL_EDITED)
    assert_that(search_in_json('included[*].id', content) == last_office_id)
    assert_that(search_in_json('data[*].id', content) == LOUser.ID)


def test_change_user_status():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    user_status = not qiwa.users_api.get_user_status(user_id=LOUser.ID)
    qiwa.users_api.change_user_status(user_id=LOUser.ID, status=user_status)
    updated_status = qiwa.users_api.get_user_status(user_id=LOUser.ID)
    assert_that(user_status == updated_status)

    qiwa.users_api.change_user_status(user_id=LOUser.ID, status=not updated_status)
