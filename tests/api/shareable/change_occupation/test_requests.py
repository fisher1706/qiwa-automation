from http import HTTPStatus

from src.api.models.qiwa.change_occupation import request_by_id_data
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data


def test_getting_by_request_id(api):
    request_data = api.change_occupation.get_random_request()
    laborer_data = request_data.laborers[0]

    response = api.change_occupation.get_request(request_data.request_id)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = request_by_id_data.parse_obj(response.json())
    assert_that(json.data).is_length(1)
    request_by_id = json.data[0].attributes
    assert_data(expected=request_data.dict(exclude={"id"}), actual=request_by_id.dict())
    assert_data(expected=laborer_data.dict(exclude={"request_number"}), actual=request_by_id.dict())
