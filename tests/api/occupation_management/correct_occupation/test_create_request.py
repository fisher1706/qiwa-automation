from datetime import date
from http import HTTPStatus

from data.shareable.correct_occupation import RequestStatus
from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes
from utils.assertion import assert_that


def test_create_correct_occupation_request(correct_occupation, laborer: LaborerAttributes):
    new_occupation = correct_occupation.get_any_occupation(laborer.occupation_id)

    json = correct_occupation.create_request(laborer, new_occupation.occupation_id)
    submit_response = json.data.attributes

    requests = correct_occupation.get_requests(
        laborer_id=laborer.laborer_id,
        laborer_name=laborer.laborer_name
    )
    requests_list = requests.data
    assert_that(requests_list).size_is(1)

    request = requests_list[0].attributes
    request_date = request.creation_date.date()
    request_current_occupation = request.current_occupation
    request_new_occupation = request.new_occupation
    request_status = request.status
    assert_that(request).has(request_id=submit_response.request_id)
    assert_that(request_date).equals_to(date.today())
    assert_that(request_status).has(code=RequestStatus.APPROVED_BY_NIC.value)  # TODO: assert not only code value
    assert_that(request_current_occupation).has(
        code=laborer.occupation_id,
        name_ar=laborer.occupation_name_ar,
        name_en=laborer.occupation_name_en,
    )
    assert_that(request_new_occupation).has(
        code=new_occupation.occupation_id,
        name_ar=new_occupation.occupation_ar,
        name_en=new_occupation.occupation_en,
    )


def test_by_laborer_has_correct_request(correct_occupation):
    laborer = correct_occupation.get_any_request()

    response = correct_occupation.api.create_request(
        laborer.laborer_id,
        laborer.laborer_name,
        laborer.current_occupation.code,
        laborer.new_occupation.code
    )
    status_code = response.status_code
    assert_that(status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    errors_list = json.data
    assert_that(errors_list).size_is(1)


def test_by_new_occupation_not_match_with_current(correct_occupation, change_occupation, laborer: LaborerAttributes):
    occupation = change_occupation.get_random_occupation()

    response = correct_occupation.api.create_request(
        laborer.laborer_id,
        laborer.laborer_name,
        laborer.occupation_id,
        occupation.code,
    )
    status_code = response.status_code
    assert_that(status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    errors_list = json.data
    assert_that(errors_list).size_is(1)


