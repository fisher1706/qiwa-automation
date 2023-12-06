from datetime import date, timedelta
from http import HTTPStatus

import allure
import pytest

from data.shareable.change_occupation import RequestStatus
from src.api.models.qiwa.change_occupation import RequestsLaborersData
from src.api.models.qiwa.raw.root import Root
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_that
from utils.json_search import get_data_attribute


def test_getting_by_laborer_name(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_name=laborer.laborer_name)
    assert_that(json.data).is_not_empty()
    names = get_data_attribute(json, "laborer_name")
    assert_that(set(names)).size_is(1).contains(laborer.laborer_name)


def test_getting_by_laborer_id(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_id=laborer.laborer_id_no)
    assert_that(json.data).is_not_empty()

    laborer_ids_from_json = get_data_attribute(json, "laborer_id_no")
    assert_that(set(laborer_ids_from_json)).size_is(1).contains(laborer.laborer_id_no)


@pytest.mark.parametrize("status", [
    RequestStatus.DRAFT,
    RequestStatus.REJECTED_BY_LABORER,
    RequestStatus.CANCELED_BY_EMPLOYER
])
def test_getting_by_status_id(change_occupation, status):
    json = change_occupation.get_requests_laborers(request_status=status)
    status_ids_from_json = get_data_attribute(json, "request_status_id")

    assert_that(set(status_ids_from_json)).size_is(1).contains(status.value)


@pytest.mark.parametrize("status", list(RequestStatus))
def test_getting_by_status_id_according_to_count(change_occupation, status):
    count = change_occupation.get_requests_count_by_status(status).requests_count

    response = change_occupation.api.get_requests_laborers(page=1, per=100, request_status=status.value)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = Root.parse_obj(response.json())
    assert_that(json.meta).has(total_entities=count)


def test_getting_by_request_date(change_occupation):
    laborer = change_occupation.get_random_laborer()
    from_date = laborer.request_date.date()
    to_date = from_date + timedelta(weeks=4)
    date_range = (from_date, to_date)

    json = change_occupation.get_requests_laborers(date_range=date_range)
    requests_dates = [laborer.attributes.request_date.date() for laborer in json.data]
    assert_that(min(requests_dates)).is_greater_or_equal(from_date)
    assert_that(max(requests_dates)).is_less_or_equal(to_date)


@pytest.mark.parametrize(
    "parameter",
    [
        {"page": 1000},
        {"laborer_id": 2000000000},
        {"laborer_name": "Non-exist name"},
        {"request_status": 10000},
        {"date_range": (date.today() + timedelta(days=1), date.today() + timedelta(days=2))},
        {"date_range": (date.today() + timedelta(days=2), date.today() + timedelta(days=1))},
    ],
    ids=["page", "laborer_id", "laborer_name", "request_status", "future_date_range", "invalid_date_range"]
)
def test_getting_by_invalid_parameter_value(change_occupation, parameter):
    response = change_occupation.api.get_requests_laborers(**parameter)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = Root.parse_obj(response.json())
    assert_that(json.data).is_empty()
    assert_that(json.meta).has(
        pages_count=0,
        total_entities=0,
        total_count=0,
        total_pages=0,
        current_page=0,
        next_page=0,
        prev_page=0
    )


class TestPagination:
    @pytest.mark.parametrize("page", [-1, 0, 1])
    def test_getting_by_page(self, change_occupation, page):
        response = change_occupation.api.get_requests_laborers(page=page, per=10)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsLaborersData.parse_obj(response.json())
        assert_that(json.meta).has(
            current_page=page,
            pages_count=json.meta.total_pages,
            total_entities=json.meta.total.value
        )

    def test_getting_last_page(self, change_occupation):
        requests_laborers = change_occupation.get_requests_laborers(per=10)
        last_page = requests_laborers.meta.pages_count

        response = change_occupation.api.get_requests_laborers(page=last_page, per=10)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsLaborersData.parse_obj(response.json())
        last_page_data_count = json.meta.total_entities - json.meta.from_
        assert_that(json.data).size_is(last_page_data_count)
        assert_that(json.meta).has(
            current_page=last_page,
            pages_count=last_page,
            total_pages=last_page
        )

    @pytest.mark.parametrize("per_page", list(range(1, 11)))
    def test_getting_per_page(self, change_occupation, per_page):
        response = change_occupation.api.get_requests_laborers(page=1, per=per_page)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsLaborersData.parse_obj(response.json())
        assert_that(json.data).size_is(per_page)
        assert_that(json.meta).has(size=per_page)

    @pytest.mark.xfail(strict=True)
    @allure.issue("https://employeesgate.atlassian.net/browse/QSS-2676")
    def test_getting_max_items(self, change_occupation):
        max_items = 100
        data = change_occupation.get_requests_laborers()
        total_entities = data.meta.total_entities

        response = change_occupation.api.get_requests_laborers(page=1, per=total_entities)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

        json = RequestsLaborersData.parse_obj(response.json())
        assert_that(json.data).size_is(max_items)
        assert_that(json.meta).has(current_page=1)
        assert_that(json.meta.pages_count).is_greater(1)
        assert_that(json.meta.total_pages).equals_to(json.meta.pages_count)

    def test_getting_zero_per_page(self, change_occupation):
        response = change_occupation.api.get_requests_laborers(page=1, per=0)
        assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
