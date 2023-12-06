import pytest

from src.api.app import QiwaApi

qiwa = QiwaApi()


@pytest.fixture
def create_e_service_via_api():
    qiwa.login_as_admin().e_service.client.get_e_services(is_admin=True)
    qiwa.e_service.client.create_e_services()
    e_service_title = qiwa.e_service.client.e_service_english_title
    return e_service_title


@pytest.fixture
def delete_e_service_via_api():
    yield
    qiwa.e_service.client.delete_e_service()
    qiwa.e_service.client.get_e_services(expect_code=404)


@pytest.fixture
def create_category(super_user, http_client):
    qiwa.login_as_admin().e_service.client.get_e_services(is_admin=True)
    qiwa.e_service.client.create_tag()
    return qiwa.e_service.client.tag_english_name


@pytest.fixture
def create_space(http_client, request):
    qiwa.login_as_admin().spaces_api.get_spaces()
    qiwa.spaces_api.create_space()
    return qiwa.spaces_api.space_title


@pytest.fixture
def delete_spase():
    yield
    qiwa.spaces_api.delete_space_request()
