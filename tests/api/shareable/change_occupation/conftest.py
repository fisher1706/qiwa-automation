import pytest

from src.api.app import QiwaApi
from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.models.qiwa.change_occupation import requests_laborers_data, requests_data, users_data


@pytest.fixture(scope="module")
def api() -> QiwaApi:
    qiwa = QiwaApi.login_as_user("1048285405").select_company(sequence_number=136401)
    qiwa.change_occupation.pass_ott_authorization()
    return qiwa


def pytest_generate_tests(metafunc):
    if "endpoint" in metafunc.fixturenames:
        params = [
            (ChangeOccupationApi.get_requests, requests_data, ChangeOccupationController.get_requests_data),
            (ChangeOccupationApi.get_requests_laborers, requests_laborers_data, ChangeOccupationController.get_requests_laborers_data),
            (ChangeOccupationApi.get_users, users_data, ChangeOccupationController.get_users_data)
        ]
        if metafunc.function.__name__ == "test_getting_total_items":
            params.pop(-1)  # exclude /users from test
        elif metafunc.function.__name__ == "test_getting_empty_page":
            params.pop(1)  # exclude /requests-laborers from test
        metafunc.parametrize("endpoint", params)
