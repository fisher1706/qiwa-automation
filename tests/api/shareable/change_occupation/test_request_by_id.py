from http import HTTPStatus

from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_status_code, assert_that


def test_with_existent_request_id(change_occupation):
    request_data = change_occupation.get_random_request()

    json = change_occupation.get_request_by_id(request_data.request_id)
    assert_that(json.data).size_is(1)
    assert_that(json.data[0].attributes).has(request_id=request_data.request_id)


def test_with_non_existent_request_id(change_occupation):
    response = change_occupation.api.get_request_by_id(100000)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    MultiLangErrorsData.parse_obj(response.json())
