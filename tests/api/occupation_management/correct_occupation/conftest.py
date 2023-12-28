import random

import pytest

from src.api.app import QiwaApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.controllers.correct_occupation import CorrectOccupationController
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes


@pytest.fixture(scope="module")
def correct_occupation() -> CorrectOccupationController:
    qiwa = QiwaApi.login_as_user("1020215578").select_company(sequence_number=391349)
    return CorrectOccupationController(qiwa.client)


@pytest.fixture(scope="module")
def change_occupation(correct_occupation) -> ChangeOccupationController:
    return ChangeOccupationController(correct_occupation.api.http)


@pytest.fixture
def laborer(correct_occupation) -> LaborerAttributes:
    laborers = correct_occupation.get_laborers(per=20)
    requests = correct_occupation.get_requests(per=100)

    requests_laborers = [laborer.attributes.laborer_id for laborer in requests.data]
    laborers_without_request = list(
        filter(lambda l: l.attributes.laborer_id not in requests_laborers, laborers.data)
    )
    laborer = random.choice(laborers_without_request).attributes

    yield laborer

    correct_occupation.delete_request_in_ibm(laborer.laborer_id)
