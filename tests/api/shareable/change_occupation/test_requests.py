from utils.assertion import assert_that
from utils.assertion.asserts import assert_data


def test_getting_by_request_id(qiwa):
    request_data = qiwa.change_occupation.get_random_request()
    laborer_data = request_data.laborers[0]

    json = qiwa.change_occupation.get_request(request_data.request_id)
    assert_that(json.data).is_length(1)
    request_by_id = json.data[0].attributes
    assert_data(expected=request_data.dict(exclude={"id"}), actual=request_by_id.dict())
    assert_data(expected=laborer_data.dict(exclude={"request_number"}), actual=request_by_id.dict())
