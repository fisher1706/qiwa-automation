import pytest

from src.api.app import QiwaApi
from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.controllers.correct_occupation import CorrectOccupationController


@pytest.fixture(scope="module")
def change_occupation() -> ChangeOccupationController:
    controller = ChangeOccupationController.pass_ott_authorization(
        office_id="1", sequence_number="391349", personal_number="1020215578"
    )
    return controller


@pytest.fixture(scope="module")
def correct_occupation() -> CorrectOccupationController:
    qiwa = QiwaApi.login_as_user("1020215578").select_company(sequence_number=391349)
    return CorrectOccupationController(qiwa.client)
