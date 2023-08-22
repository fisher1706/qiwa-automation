import pytest

from src.api.app import QiwaApi

pytestmark = [
    pytest.mark.usefixtures("delete_service_categories")
]


def test_positive_tag():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.get_admin_tags()
    qiwa.e_service.api.create_tag()
    qiwa.e_service.api.update_tag()
    qiwa.e_service.api.delete_tag()


def test_get_tags_as_simple_user():
    qiwa = QiwaApi.login_as_user("1018729241").select_company()
    qiwa.e_service.api.get_admin_tags(expect_code=403)


def test_create_tag_with_empty_payload():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.create_tag(body=False)


def test_update_tag_with_non_existent_id():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.update_tag()


def test_delete_tag():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.delete_tag()
