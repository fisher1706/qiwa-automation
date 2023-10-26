from http import HTTPStatus
import pytest

from data.shareable.expected_json.change_occupation.common import empty_data
from src.api.models.qiwa.change_occupation import requests_data, request_by_id_data
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


@pytest.mark.parametrize("page", [-1, 0, 1, 3])
def test_getting_by_page(api, page):
    response = api.change_occupation.get_requests(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_data.parse_obj(response.json())
    assert_that(json.meta.current_page).equals_to(page)
    assert_that(json.meta.pages_count).equals_to(json.meta.total_pages)
    assert_that(json.meta.total_entities).equals_to(json.meta.total.value)


def test_getting_last_page(api):
    requests = api.change_occupation.get_requests_data(per=10)
    last_page = requests.meta.pages_count

    response = api.change_occupation.get_requests(page=last_page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_data.parse_obj(response.json())
    last_page_data_count = json.meta.total_entities - json.meta.from_
    assert_that(json.data).is_length(last_page_data_count)
    assert_that(json.meta.current_page).equals_to(last_page)
    assert_that(json.meta.pages_count).equals_to(last_page)
    assert_that(json.meta.total_pages).equals_to(last_page)


def test_getting_empty_page(api):
    requests = api.change_occupation.get_requests_data(per=10)
    page = requests.meta.pages_count + 1

    response = api.change_occupation.get_requests(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = api.change_occupation.get_requests(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


@pytest.mark.parametrize("per_page", list(range(1, 11)))
def test_getting_per_page(api, per_page):
    response = api.change_occupation.get_requests(page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_data.parse_obj(response.json())
    assert_that(json.data).is_length(per_page)
    assert_that(json.meta.size).equals_to(per_page)


def test_getting_total_entities(api):
    requests = api.change_occupation.get_requests_data()
    total_entities = requests.meta.total_entities
    per_page = total_entities + 1

    response = api.change_occupation.get_requests(page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_data.parse_obj(response.json())
    assert_that(json.data).is_length(total_entities)
    assert_that(json.meta.total_entities).equals_to(total_entities)
    assert_that(json.meta.total.value).equals_to(total_entities)
    assert_that(json.meta.pages_count).equals_to(1)
    assert_that(json.meta.total_pages).equals_to(1)
    assert_that(json.meta.from_).equals_to(0)
    assert_that(json.meta.size).equals_to(per_page)


def test_getting_zero_per_page(api):
    response = api.change_occupation.get_requests(page=1, per=0)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
