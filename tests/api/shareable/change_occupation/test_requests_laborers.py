from http import HTTPStatus

import pytest

from data.shareable.expected_json.change_occupation.requests_laborers import empty_data
from src.api.models.qiwa.change_occupation import requests_laborers_data
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data


@pytest.mark.parametrize("page", [-1, 0, 1, 3])
def test_getting_by_page(api, page):
    response = api.change_occupation.api.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    assert_that(json.meta.current_page).equals_to(page)
    assert_that(json.meta.pages_count).equals_to(json.meta.total_pages)
    assert_that(json.meta.total_entities).equals_to(json.meta.total.value)


def test_getting_last_page(api):
    requests_laborers = api.change_occupation.get_requests_laborers_data(per=10)
    last_page = requests_laborers.meta.pages_count

    response = api.change_occupation.api.get_requests_laborers(page=last_page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    last_page_data_count = json.meta.total_entities - json.meta.from_
    assert_that(json.data).is_length(last_page_data_count)
    assert_that(json.meta.current_page).equals_to(last_page)
    assert_that(json.meta.pages_count).equals_to(last_page)
    assert_that(json.meta.total_pages).equals_to(last_page)


def test_getting_empty_page(api):
    requests_laborers = api.change_occupation.get_requests_laborers_data(per=10)
    page = requests_laborers.meta.pages_count + 1

    response = api.change_occupation.api.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = api.change_occupation.api.get_requests_laborers(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


@pytest.mark.parametrize("per_page", list(range(1, 11)))
def test_getting_per_page(api, per_page):
    response = api.change_occupation.api.get_requests_laborers(page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    assert_that(json.data).is_length(per_page)
    assert_that(json.meta.size).equals_to(per_page)


def test_getting_total_entities(api):
    requests_laborers = api.change_occupation.get_requests_laborers_data()
    total_entities = requests_laborers.meta.total_entities
    per_page = total_entities + 1

    response = api.change_occupation.api.get_requests_laborers(page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = requests_laborers_data.parse_obj(response.json())
    assert_that(json.data).is_length(total_entities)
    assert_that(json.meta.total_entities).equals_to(total_entities)
    assert_that(json.meta.total.value).equals_to(total_entities)
    assert_that(json.meta.pages_count).equals_to(1)
    assert_that(json.meta.total_pages).equals_to(1)
    assert_that(json.meta.from_).equals_to(0)
    assert_that(json.meta.size).equals_to(per_page)


def test_getting_zero_per_page(api):
    response = api.change_occupation.api.get_requests_laborers(page=1, per=0)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
