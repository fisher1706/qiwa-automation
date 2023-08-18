from http import HTTPStatus

import pytest

from src.api import models
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.e_service import Group
from src.api.payloads.e_service.groups import Group


@pytest.fixture
def delete_groups():
    yield
    qiwa = QiwaApi.login_as_admin()
    response = qiwa.e_service.api.groups.get_groups()
    assert response.status_code == HTTPStatus.OK
    groups = response.json()
    for group in groups["data"]:
        if group["attributes"]["title-en"].startswith("Autotest"):
            qiwa.e_service.api.groups.group(group["id"]).delete()
    qiwa.e_service.api.groups.get_groups()


@pytest.fixture
def group() -> Group:
    qiwa = QiwaApi.login_as_admin()

    create = qiwa.e_service.create_e_service_group(Group())
    assert create.status_code == HTTPStatus.CREATED
    model = models.qiwa.e_service.admin_created_group.parse_obj(create.json())

    return model.data.attributes
