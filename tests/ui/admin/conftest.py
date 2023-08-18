import pytest

from src.api.app import QiwaApi

qiwa = QiwaApi()


@pytest.fixture
def create_e_service_via_api():
    qiwa.login_as_admin().e_service.api.get_e_services(is_admin=True)
    qiwa.e_service.api.create_e_services()
    e_service_title = qiwa.e_service.api.e_service_english_title
    return e_service_title
    # self.auth_api.login_user(super_user.personal_number, super_user.password)
    # self.e_service_api.get_e_services(is_admin=True)
    # self.e_service.api.create_e_services()
    # self.e_service_title = self.e_service.api.e_service_english_title


@pytest.fixture
def delete_e_service_via_api():
    yield
    qiwa.e_service.api.delete_e_service()
    qiwa.e_service.api.get_e_services(expect_code=404)
