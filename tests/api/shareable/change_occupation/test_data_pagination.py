from http import HTTPStatus

import pytest

from data.shareable.expected_json.change_occupation.common import empty_data
from src.api.models.qiwa.change_occupation import users_data
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data


@pytest.mark.parametrize("page", [-1, 0, 1])
def test_getting_by_page(qiwa, endpoint, page):
    tested_endpoint, validation_model, data = endpoint

    response = tested_endpoint(qiwa.change_occupation.api, page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validation_model.parse_obj(response.json())
    assert_that(json.meta.current_page).equals_to(page)
    assert_that(json.meta.pages_count).equals_to(json.meta.total_pages)
    assert_that(json.meta.total_entities).equals_to(json.meta.total.value)


def test_getting_last_page(qiwa, endpoint):
    tested_endpoint, validation_model, data = endpoint

    requests_laborers = data(qiwa.change_occupation, per=10)
    last_page = requests_laborers.meta.pages_count

    response = tested_endpoint(qiwa.change_occupation.api, page=last_page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validation_model.parse_obj(response.json())
    last_page_data_count = json.meta.total_entities - json.meta.from_
    assert_that(json.data).is_length(last_page_data_count)
    assert_that(json.meta.current_page).equals_to(last_page)
    assert_that(json.meta.pages_count).equals_to(last_page)
    assert_that(json.meta.total_pages).equals_to(last_page)


def test_getting_empty_page(qiwa, endpoint):
    tested_endpoint, validation_model, data = endpoint

    requests_laborers = data(qiwa.change_occupation, per=10)
    page = requests_laborers.meta.pages_count + 1

    response = tested_endpoint(qiwa.change_occupation.api, page=page, per=10)
    json = validation_model.parse_obj(response.json())
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=json)

    response = tested_endpoint(qiwa.change_occupation.api, page=10000, per=10)
    json = validation_model.parse_obj(response.json())
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=json)


@pytest.mark.parametrize("per_page", list(range(1, 11)))
def test_getting_per_page(qiwa, endpoint, per_page):
    tested_endpoint, validation_model, data = endpoint

    response = tested_endpoint(qiwa.change_occupation.api, page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validation_model.parse_obj(response.json())
    assert_that(json.data).is_length(per_page)
    assert_that(json.meta.size).equals_to(per_page)


def test_getting_max_items(qiwa):
    total_users = 103
    max_items = 100

    response = qiwa.change_occupation.api.get_users(page=1, per=total_users)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = users_data.parse_obj(response.json())
    assert_that(json.data).is_length(max_items)
    assert_data(actual=json.meta.dict(), expected=dict(pages_count=2, total_pages=2, size=max_items))


def test_getting_total_items(qiwa, endpoint):
    tested_endpoint, validation_model, data = endpoint

    data = data(qiwa.change_occupation)
    total_entities = data.meta.total_entities
    per_page = total_entities + 1

    response = tested_endpoint(qiwa.change_occupation.api, page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = validation_model.parse_obj(response.json())
    assert_that(json.data).is_length(total_entities)
    assert_that(json.meta.total_entities).equals_to(total_entities)
    assert_that(json.meta.total.value).equals_to(total_entities)
    assert_that(json.meta.pages_count).equals_to(1)
    assert_that(json.meta.total_pages).equals_to(1)
    assert_that(json.meta.from_).equals_to(0)


def test_getting_zero_per_page(qiwa, endpoint):
    tested_endpoint, validation_model, data = endpoint

    response = tested_endpoint(qiwa.change_occupation.api, page=1, per=0)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
