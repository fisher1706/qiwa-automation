from http import HTTPStatus

import pytest

from src.api import assertions, models
from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from src.api.payloads.e_service.groups import EService, Group

pytestmark = [
    pytest.mark.e_service_suite,
    pytest.mark.daily,
    pytest.mark.api,
    pytest.mark.ss,
    pytest.mark.wp,
    pytest.mark.usefixtures("delete_groups")
]


def test_create():
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.create_e_service_group(Group())
    assert response.status_code == HTTPStatus.CREATED


def test_search():
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.groups.get_groups()
    assert response.status_code == HTTPStatus.OK


def test_find(group):
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.groups.group(group.id).find()
    assert response.status_code == HTTPStatus.OK


def test_find_group_as_user(group):
    qiwa = QiwaApi.login_as_user("1018729241").select_company()
    response = qiwa.e_service.api.groups.as_user.group(group.id).find()
    assert response.status_code == HTTPStatus.OK


def test_update(group):
    qiwa = QiwaApi.login_as_admin()
    payload = Group()
    response = qiwa.e_service.update_e_service_group(group.id, payload)
    assert response.status_code == HTTPStatus.OK


def test_delete(group):
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.groups.group(group.id).delete()
    assert response.status_code == HTTPStatus.OK


def test_created_group():
    qiwa = QiwaApi.login_as_admin()
    payload = Group()
    response = qiwa.e_service.create_e_service_group(payload)
    assert response.status_code == HTTPStatus.CREATED

    json = response.json()
    validate_model(json, models.qiwa.e_service.admin_created_group)
    assertions.e_service.assert_created_group(json, payload)


def test_group_creation_for_service_from_another_group():
    qiwa = QiwaApi.login_as_admin()
    e_service = EService()

    first_creation = qiwa.e_service.create_group_for_e_services(e_service)
    assert first_creation.status_code == HTTPStatus.CREATED

    second_creation = qiwa.e_service.create_group_for_e_services(e_service)
    assert second_creation.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_searched_group(group):
    qiwa = QiwaApi.login_as_admin()

    response = qiwa.e_service.api.groups.get_groups()
    assert response.status_code == HTTPStatus.OK

    models.qiwa.e_service.admin_groups_list.parse_obj(response.json())


def test_group_sorting_by_position():
    qiwa = QiwaApi.login_as_admin()

    response = qiwa.e_service.api.groups.get_groups()

    assert response.status_code == HTTPStatus.OK
    groups = models.qiwa.e_service.admin_groups_list.parse_obj(response.json())
    assertions.e_service.assert_sorting_by_position(groups)
