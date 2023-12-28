import pytest

from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.payloads.raw.change_occupation import Laborer


@pytest.fixture(scope="module")
def change_occupation() -> ChangeOccupationController:
    controller = ChangeOccupationController.pass_ott_authorization(
        office_id="1", sequence_number="391349", personal_number="1020215578"
    )
    return controller


@pytest.fixture
def laborer(change_occupation):
    user = change_occupation.get_random_user(eligible=True)
    laborer = Laborer(personal_number=user.personal_number)

    yield laborer

    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])


@pytest.fixture
def laborer2(change_occupation):
    user = change_occupation.get_random_user(eligible=True)
    laborer = Laborer(personal_number=user.personal_number)

    yield laborer

    requests = change_occupation.get_requests_by_laborer(laborer.personal_number)
    for request in requests:
        change_occupation.api.cancel_request(request["request_number"])
