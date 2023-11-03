from http import HTTPStatus

from data.shareable.expected_json.change_occupation.requests_laborers import empty_data
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_data, assert_that
from utils.json_search import search_data_by_attributes


def test_getting_empty_page(qiwa):
    requests_laborers = qiwa.change_occupation.get_requests_laborers(per=10)
    page = requests_laborers.meta.pages_count + 1

    response = qiwa.change_occupation.api.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = qiwa.change_occupation.api.get_requests_laborers(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


def test_getting_by_laborer_name(qiwa):
    laborer = qiwa.change_occupation.get_random_laborer()

    json = qiwa.change_occupation.get_requests_laborers(laborer_name=laborer.laborer_name)
    assert_that(json.data).is_not_empty().size_is(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_name=laborer.laborer_name)).size_is(json.meta.total_entities)


def test_getting_by_non_existent_laborer_name(qiwa):
    response = qiwa.change_occupation.api.get_requests_laborers(page=1, per=10, laborer_name="Non-exist name")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


def test_getting_by_laborer_id(qiwa):
    laborer = qiwa.change_occupation.get_random_laborer()

    json = qiwa.change_occupation.get_requests_laborers(laborer_id=laborer.laborer_id_no)
    assert_that(json.data).is_not_empty().size_is(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_id_no=laborer.laborer_id_no)).size_is(json.meta.total_entities)


def test_getting_by_non_existent_laborer_id(qiwa):
    response = qiwa.change_occupation.api.get_requests_laborers(page=1, per=10, laborer_name="Non-exist name")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())
