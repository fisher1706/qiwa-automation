from http import HTTPStatus

import pytest

from src.api import assertions
from src.api.app import QiwaApi
from src.api.models.qiwa.e_service import admin_e_services, user_e_services

pytestmark = [
    pytest.mark.e_service_suite,
    pytest.mark.daily,
    pytest.mark.api,
    pytest.mark.ss,
    pytest.mark.wp,
]


def test_search_e_services_as_user():
    qiwa = QiwaApi.login_as_user("1452151361").select_company()
    e_services = qiwa.e_service.api.get_e_services()

    assert e_services.status_code == HTTPStatus.OK
    user_e_services.parse_obj(e_services.json())


def test_search_e_services_as_admin():
    qiwa = QiwaApi.login_as_admin()
    e_services = qiwa.e_service.api.as_admin.get_e_services()

    assert e_services.status_code == HTTPStatus.OK
    admin_e_services.parse_obj(e_services.json())


def test_e_service_crud():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.as_admin.create_e_services()
    qiwa.e_service.api.as_admin.find_e_service_by_id()
    update = qiwa.e_service.api.as_admin.update_e_service()
    assert update.status_code == HTTPStatus.OK
    delete = qiwa.e_service.api.as_admin.delete_e_service()
    assert delete.status_code == HTTPStatus.OK


def test_get_e_services_without_super_user():
    qiwa = QiwaApi.login_as_user("1452151361").select_company()
    qiwa.e_service.api.as_admin.get_e_services(expect_code=HTTPStatus.FORBIDDEN)


def test_create_e_service_with_empty_body():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.as_admin.create_e_services(body=False, expect_code=HTTPStatus.UNPROCESSABLE_ENTITY)


def test_find_non_existing_e_service():
    qiwa = QiwaApi.login_as_admin()
    qiwa.e_service.api.as_admin.find_e_service_by_id(expected_code=HTTPStatus.NOT_FOUND)


def test_update_non_existing_e_service():
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.as_admin.update_e_service()
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_non_existing_e_service():
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.as_admin.delete_e_service()
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_e_services_sorting():
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.as_admin.get_e_services()

    assert response.status_code == HTTPStatus.OK
    e_services = admin_e_services.parse_obj(response.json())
    assertions.e_service.assert_sorting_by_position(e_services)
