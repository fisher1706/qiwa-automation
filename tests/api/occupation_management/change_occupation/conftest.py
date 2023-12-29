import pytest

from src.api.payloads.raw.change_occupation import Laborer


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
