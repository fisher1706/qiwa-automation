import pytest

from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.models.qiwa.change_occupation import (
    requests_data,
    requests_laborers_data,
    users_data,
)
from src.api.payloads.raw.change_occupation import Laborer


@pytest.fixture(scope="module")
def change_occupation() -> ChangeOccupationController:
    controller = ChangeOccupationController.pass_ott_authorization(
        labor_office_id="1", sequence_number="136401", personal_number="1048285405"
    )
    return controller


def pytest_generate_tests(metafunc):
    if "endpoint" in metafunc.fixturenames:
        params = {
            "/requests": (
                ChangeOccupationApi.get_requests,
                requests_data,
                ChangeOccupationController.get_requests,
            ),
            "/requests-laborers": (
                ChangeOccupationApi.get_requests_laborers,
                requests_laborers_data,
                ChangeOccupationController.get_requests_laborers,
            ),
            "/users": (
                ChangeOccupationApi.get_users,
                users_data,
                ChangeOccupationController.get_users,
            ),
        }
        if metafunc.function.__name__ == "test_getting_total_items":
            params.pop("/users")  # exclude /users from test
        elif metafunc.function.__name__ == "test_getting_empty_page":
            params.pop("/requests-laborers")  # exclude /requests-laborers from test
        metafunc.parametrize("endpoint", params.values(), ids=params.keys())


@pytest.fixture
def laborer(change_occupation):
    laborer = Laborer(personal_number="2037659303", occupation_code="712501")
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
    yield laborer
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
