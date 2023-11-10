from http import HTTPStatus

from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_that
from utils.assertion.asserts import assert_data, assert_status_code


def test_getting_by_request_id(change_occupation):
    request_data = change_occupation.get_random_request()
    laborer_data = request_data.laborers[0]

    json = change_occupation.get_request(request_data.request_id)
    assert_that(json.data).size_is(1)
    request_by_id = json.data[0].attributes
    assert_data(
        expected=request_data.dict(exclude={"id"}), actual=request_by_id.dict(), title="request data"
    )
    assert_data(
        expected=laborer_data.dict(exclude={"request_number"}), actual=request_by_id.dict(), title="laborer data"
    )


def test_getting_by_non_existent_request_id(change_occupation):
    response = change_occupation.api.get_request(100000)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_creating_request(change_occupation, laborer):
    json = change_occupation.create_request(laborer)
    assert_that(json.data).size_is(1)

    request_attributes = json.data[0].attributes
    assert_that(request_attributes).has(personal_number=laborer.personal_number)

    requests = change_occupation.get_requests_by_request_number(request_attributes.request_id)
    assert_that(requests).size_is(1)
    assert_that(requests[0]).has(
        status_id=3,
        employee_personal_number=laborer.personal_number,
        new_occupation_id=laborer.occupation_code
    )
