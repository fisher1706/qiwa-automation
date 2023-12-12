import pytest

from src.api.app import QiwaApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.controllers.correct_occupation import CorrectOccupationController
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes


@pytest.fixture(scope="module")
def correct_occupation() -> CorrectOccupationController:
    qiwa = QiwaApi.login_as_user("1048285405").select_company(sequence_number=136401)
    return CorrectOccupationController(qiwa.client)


@pytest.fixture(scope="module")
def change_occupation(correct_occupation) -> ChangeOccupationController:
    return ChangeOccupationController(correct_occupation.api.http)


@pytest.fixture
def laborer(correct_occupation) -> LaborerAttributes:
    laborer = correct_occupation.get_any_laborer()
    correct_occupation.delete_request_in_ibm(laborer.laborer_id)
    yield laborer
    correct_occupation.delete_request_in_ibm(laborer.laborer_id)
