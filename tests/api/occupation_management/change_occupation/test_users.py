from http import HTTPStatus

import allure
import pytest

from data.shareable.expected_json.change_occupation.common import empty_data
from src.api.models.qiwa.change_occupation import UsersData
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data


@pytest.mark.parametrize("page", [-1, 0, 1])
def test_getting_by_page(change_occupation, page):
    response = change_occupation.api.get_users(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = UsersData.parse_obj(response.json())
    assert_that(json.meta).has(
        current_page=page,
        pages_count=json.meta.total_pages,
        total_entities=json.meta.total.value
    )


def test_getting_last_page(change_occupation):
    users = change_occupation.get_users(per=10)
    last_page = users.meta.pages_count

    response = change_occupation.api.get_users(page=last_page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = UsersData.parse_obj(response.json())
    last_page_data_count = json.meta.total_entities - json.meta.from_
    assert_that(json.data).size_is(last_page_data_count)
    assert_that(json.meta).has(
        current_page=last_page,
        pages_count=last_page,
        total_pages=last_page
    )


def test_getting_empty_page(change_occupation):
    users = change_occupation.get_users(per=10)
    page = users.meta.pages_count + 1

    response = change_occupation.api.get_users(page=page, per=10)
    json = UsersData.parse_obj(response.json())
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=json.dict())

    response = change_occupation.api.get_users(page=10000, per=10)
    json = UsersData.parse_obj(response.json())
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=json.dict())


@pytest.mark.parametrize("per_page", list(range(1, 11)))
def test_getting_per_page(change_occupation, per_page):
    response = change_occupation.api.get_users(page=1, per=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = UsersData.parse_obj(response.json())
    assert_that(json.data).size_is(per_page)
    assert_that(json.meta).has(size=per_page)


@pytest.mark.xfail(strict=True)
@allure.issue("https://employeesgate.atlassian.net/browse/QSS-2676")
def test_getting_max_items(change_occupation):
    max_items = 100
    data = change_occupation.get_users()
    total_entities = data.meta.total_entities

    response = change_occupation.api.get_users(page=1, per=total_entities)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = UsersData.parse_obj(response.json())
    assert_that(json.data).size_is(max_items)
    assert_that(json.meta).has(current_page=1)
    assert_that(json.meta.pages_count).is_greater(1)
    assert_that(json.meta.total_pages).equals_to(json.meta.pages_count)


def test_getting_zero_per_page(change_occupation):
    response = change_occupation.api.get_users(page=1, per=0)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
