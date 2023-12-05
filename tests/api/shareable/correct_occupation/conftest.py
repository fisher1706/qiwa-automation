import pytest

from src.api.app import QiwaApi
from src.api.controllers.correct_occupation import CorrectOccupationController


@pytest.fixture(scope="module")
def correct_occupation() -> CorrectOccupationController:
    qiwa = QiwaApi.login_as_user("1048285405").select_company(sequence_number=136401)
    return CorrectOccupationController(qiwa.client)
