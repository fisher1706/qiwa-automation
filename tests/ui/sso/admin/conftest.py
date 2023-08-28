import pytest

from src.api.app import QiwaApi

qiwa = QiwaApi()


@pytest.fixture
def create_e_service_via_api():
    qiwa.login_as_admin().e_service.api.get_e_services(is_admin=True)
    qiwa.e_service.api.create_e_services()
    e_service_title = qiwa.e_service.api.e_service_english_title
    return e_service_title


@pytest.fixture
def delete_e_service_via_api():
    yield
    qiwa.e_service.api.delete_e_service()
    qiwa.e_service.api.get_e_services(expect_code=404)


@pytest.fixture
def create_category(self, super_user, http_client):
    qiwa.login_as_admin().e_service.api.get_e_services(is_admin=True)
    qiwa.e_service.api.create_tag()
    return qiwa.e_service.api.tag_english_name
