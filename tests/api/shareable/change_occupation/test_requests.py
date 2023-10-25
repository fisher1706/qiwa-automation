from http import HTTPStatus

from src.api.models.qiwa.change_occupation import requests_data
from utils.assertion import assert_status_code


def test_getting_requests(api):
    response = api.change_occupation.api.get_requests()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_data.parse_obj(response.json())
