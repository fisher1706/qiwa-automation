from http import HTTPStatus

import pytest

from data.shareable.expected_json.change_occupation.common import empty_data
from src.api.models.qiwa.change_occupation import RequestsData
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data
from utils.json_search import get_data_attribute

# TODO: get by partial name


def test_getting_by_employee_name(change_occupation):
    laborer = change_occupation.get_random_laborer()
    json = change_occupation.get_requests(employee_name=laborer.laborer_name, per=100)

    employee_names_from_json = get_data_attribute(json, "laborers", "[0]", ".employee_name")
    assert_that(set(employee_names_from_json)).size_is(1).contains(laborer.laborer_name)


def test_getting_by_request_id(change_occupation):
    request = change_occupation.get_random_request()
    json = change_occupation.get_requests(request_id=request.request_id)

    assert_that(json.data).size_is(1)
    assert_that(json.data[0]).has(id=request.request_id)


@pytest.mark.parametrize("value", [
    {"employee_name": "Some name"},
    {"request_id": "100000"}
], ids=["employee_name", "request_id"])
def test_getting_with_non_existent_value(change_occupation, value):
    json = change_occupation.get_requests(**value)

    assert_that(json.data).is_empty()
    assert_that(json.meta).has(
        pages_count=0,
        total_entities=0,
    )


class TestPagination:
    @pytest.mark.parametrize("page", [-1, 0, 1])
    def test_getting_by_page(self, change_occupation, page):
        response = change_occupation.api.get_requests(page=page, per=10)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsData.parse_obj(response.json())
        assert_that(json.meta).has(
            current_page=page,
            pages_count=json.meta.total_pages,
            total_entities=json.meta.total.value
        )

    def test_getting_last_page(self, change_occupation):
        requests = change_occupation.get_requests(per=10)
        last_page = requests.meta.pages_count

        response = change_occupation.api.get_requests(page=last_page, per=10)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsData.parse_obj(response.json())
        last_page_data_count = json.meta.total_entities - json.meta.from_
        assert_that(json.data).size_is(last_page_data_count)
        assert_that(json.meta).has(
            current_page=last_page,
            pages_count=last_page,
            total_pages=last_page
        )

    def test_getting_empty_page(self, change_occupation):
        requests = change_occupation.get_requests(per=10)
        page = requests.meta.pages_count + 1

        response = change_occupation.api.get_requests(page=page, per=10)
        json = RequestsData.parse_obj(response.json())
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        assert_data(expected=empty_data(), actual=json.dict())

        response = change_occupation.api.get_requests(page=10000, per=10)
        json = RequestsData.parse_obj(response.json())
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        assert_data(expected=empty_data(), actual=json.dict())

    @pytest.mark.parametrize("per_page", list(range(1, 11)))
    def test_getting_per_page(self, change_occupation, per_page):
        response = change_occupation.api.get_requests(page=1, per=per_page)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsData.parse_obj(response.json())
        assert_that(json.data).size_is(per_page)
        assert_that(json.meta).has(size=per_page)

    def test_getting_max_items(self, change_occupation):
        max_items = 100
        data = change_occupation.get_requests()
        total_entities = data.meta.total_entities

        response = change_occupation.api.get_requests(page=1, per=total_entities)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsData.parse_obj(response.json())
        assert_that(json.data).size_is(max_items)
        assert_that(json.meta).has(current_page=1)
        assert_that(json.meta.pages_count).is_greater(1)
        assert_that(json.meta.total_pages).equals_to(json.meta.pages_count)

    def test_getting_zero_per_page(self, change_occupation):
        response = change_occupation.api.get_requests(page=1, per=0)
        assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
