from http import HTTPStatus

from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_status_code, assert_that


def test_with_existent_request_id(change_occupation):
    request = change_occupation.get_random_request()
    request_id = request.request_id

    json = change_occupation.get_request_by_id(request_id)
    data = json.data
    assert_that(data).is_not_empty()
    requests_have_id: bool = all(
        request.attributes.request_id == request_id for request in data
    )
    assert_that(requests_have_id).equals_to(True)


def test_with_non_existent_request_id(change_occupation):
    response = change_occupation.api.get_request_by_id(100000)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
