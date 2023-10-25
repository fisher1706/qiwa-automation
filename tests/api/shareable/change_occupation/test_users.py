from http import HTTPStatus

from src.api.models.qiwa.change_occupation import users_data
from utils.assertion import assert_status_code


def test_getting_users(api):
    response = api.change_occupation.get_users(page=1, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = users_data.parse_obj(response.json())
