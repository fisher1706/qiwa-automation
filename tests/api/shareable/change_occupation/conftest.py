import pytest

from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.models.qiwa.change_occupation import (
    RequestsData,
    RequestsLaborersData,
    UsersData,
)
from src.api.payloads.raw.change_occupation import Laborer


@pytest.fixture(scope="module")
def change_occupation() -> ChangeOccupationController:
    controller = ChangeOccupationController.pass_ott_authorization(
        labor_office_id="1", sequence_number="136401"
    )
    return controller


def pytest_generate_tests(metafunc):
    if "endpoint" in metafunc.fixturenames:
        params = {
            "/requests": (
                ChangeOccupationApi.get_requests,
                RequestsData,
                ChangeOccupationController.get_requests,
            ),
            "/requests-laborers": (
                ChangeOccupationApi.get_requests_laborers,
                RequestsLaborersData,
                ChangeOccupationController.get_requests_laborers,
            ),
            "/users": (
                ChangeOccupationApi.get_users,
                UsersData,
                ChangeOccupationController.get_users,
            ),
        }
        if metafunc.function.__name__ == "test_getting_empty_page":
            params.pop("/requests-laborers")  # exclude /requests-laborers from test
        metafunc.parametrize("endpoint", params.values(), ids=params.keys())


@pytest.fixture
def laborer(change_occupation):  # TODO: select randomly
    laborer = Laborer()
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
    yield laborer
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])


@pytest.fixture
def laborer2(change_occupation):  # TODO: select randomly
    laborer = Laborer(personal_number="2037659303")
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
    yield laborer
    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
