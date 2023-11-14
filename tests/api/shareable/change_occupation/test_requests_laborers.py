from datetime import date, timedelta
from http import HTTPStatus

import pytest

from data.shareable.change_occupation import RequestStatus
from src.api.models.qiwa.change_occupation import RequestsLaborersData
from src.api.models.qiwa.raw.root import Root
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_that
from utils.json_search import get_data_attribute, search_data_by_attributes


def test_getting_by_laborer_name(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_name=laborer.laborer_name, per=1000)
    assert_that(json.data).is_not_empty().size_is(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_name=laborer.laborer_name)).size_is(json.meta.total_entities)


def test_getting_by_laborer_id(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_id=laborer.laborer_id_no, per=100)
    assert_that(json.data).is_not_empty().size_is(json.meta.total_entities)

    laborer_ids_from_json = get_data_attribute(json, "laborer_id_no")
    assert_that(set(laborer_ids_from_json)).size_is(1).contains(laborer.laborer_id_no)


@pytest.mark.parametrize("status", [
    RequestStatus.DRAFT,
    RequestStatus.PENDING_LABORER_APPROVAL,
    RequestStatus.REJECTED_BY_LABORER,
    RequestStatus.CANCELED_BY_EMPLOYER
])
def test_getting_by_status_id(change_occupation, status):
    json = change_occupation.get_requests_laborers(request_status=status, per=100)
    status_ids_from_json = get_data_attribute(json, "request_status_id")

    assert_that(set(status_ids_from_json)).size_is(1).contains(status.value)


@pytest.mark.parametrize("status", list(RequestStatus))
def test_getting_by_status_id_according_to_count(change_occupation, status):
    count = change_occupation.get_requests_count_by_status(status).requests_count

    response = change_occupation.api.get_requests_laborers(page=1, per=100, request_status=status.value)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = Root.parse_obj(response.json())
    assert_that(json.data).size_is(count)
    assert_that(json.meta).has(total_entities=count)


def test_getting_by_request_date(change_occupation):
    today = date.today()
    yesterday = today - timedelta(weeks=2)
    date_range = (yesterday, today)

    response = change_occupation.api.get_requests_laborers(page=1, per=100, date_range=date_range)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = RequestsLaborersData.parse_obj(response.json())
    request_dates_from_json = get_data_attribute(json, "request_date")
    assert_that(min(request_dates_from_json).date()).is_greater_or_equal(yesterday)
    assert_that(max(request_dates_from_json).date()).is_less_or_equal(today)


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
