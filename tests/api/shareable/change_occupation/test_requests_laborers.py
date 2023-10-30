from http import HTTPStatus

from data.shareable.expected_json.change_occupation.requests_laborers import empty_data
from src.api.models.qiwa.change_occupation import requests_laborers_data
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_data, assert_that
from utils.json_search import search_data_by_attributes


def test_getting_empty_page(api):
    requests_laborers = api.change_occupation.get_requests_laborers_data(per=10)
    page = requests_laborers.meta.pages_count + 1

    response = api.change_occupation.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = api.change_occupation.get_requests_laborers(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


def test_getting_by_laborer_name(api):
    laborer = api.change_occupation.get_random_laborer()

    response = api.change_occupation.get_requests_laborers(page=1, per=100, laborer_name=laborer.laborer_name)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    assert_that(len(json.data)).not_equals_to(0)
    assert_that(json.data).is_length(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_name=laborer.laborer_name)).is_length(json.meta.total_entities)


def test_getting_by_non_existent_laborer_name(api):
    response = api.change_occupation.get_requests_laborers(page=1, per=100, laborer_name="Non-exist name")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


def test_getting_by_laborer_id(api):
    laborer = api.change_occupation.get_random_laborer()

    response = api.change_occupation.get_requests_laborers(page=1, per=100, laborer_id=laborer.laborer_id_no)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    assert_that(len(json.data)).not_equals_to(0)
    assert_that(json.data).is_length(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_id_no=laborer.laborer_id_no)).is_length(json.meta.total_entities)


def test_getting_by_non_existent_laborer_id(api):
    response = api.change_occupation.get_requests_laborers(page=1, per=100, laborer_name="Non-exist name")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())
