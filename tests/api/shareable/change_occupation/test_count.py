from http import HTTPStatus

from src.api.models.qiwa.change_occupation import ChangeOccupationsCountData
from utils.assertion import assert_status_code


def test_getting_count(change_occupation):
    response = change_occupation.api.get_count()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = ChangeOccupationsCountData.parse_obj(response.json())
