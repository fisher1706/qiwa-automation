from http import HTTPStatus

from data.shareable.expected_json.change_occupation.requests_laborers import empty_data
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_data


def test_getting_empty_page(api):
    requests_laborers = api.change_occupation.get_requests_laborers_data(per=10)
    page = requests_laborers.meta.pages_count + 1

    response = api.change_occupation.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = api.change_occupation.get_requests_laborers(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())
