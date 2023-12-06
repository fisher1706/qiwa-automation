from datetime import datetime, timedelta

import pytest

from data.shareable.correct_occupation import RequestStatus
from utils.assertion import assert_that

today = datetime.today()


def test_by_laborer_name(correct_occupation):
    request = correct_occupation.get_any_request()

    json = correct_occupation.get_requests(laborer_name=request.laborer_name)

    data = json.data
    assert_that(data).size_is(1)

    request_attributes = json.data[0].attributes
    assert_that(request_attributes).has(laborer_name=request.laborer_name)


def test_by_laborer_id(correct_occupation):
    request = correct_occupation.get_any_request()

    json = correct_occupation.get_requests(laborer_id=request.laborer_id)

    data = json.data
    assert_that(data).size_is(1)

    request_attributes = json.data[0].attributes
    assert_that(request_attributes).has(laborer_id=request.laborer_id)


def test_by_approved_request_status(correct_occupation):
    status = RequestStatus.APPROVED_BY_NIC
    json = correct_occupation.get_requests(request_status=status)

    requests_have_appropriate_status: bool = all(
        request.attributes.status.code == status.value for request in json.data
    )
    assert_that(requests_have_appropriate_status).equals_to(True)


@pytest.mark.parametrize("status", [
    RequestStatus.PENDING,
    RequestStatus.REJECTED_BY_NIC,
    RequestStatus.NIC_FAILURE,
    RequestStatus.AUTO_TERMINATED,
])
def test_by_not_found_status(correct_occupation, status):
    json = correct_occupation.get_requests(request_status=status)

    data, meta = json.data, json.meta
    assert_that(data).is_empty()
    assert_that(meta).has(
        total_entities=0,
        pages_count=0,
    )


def test_by_request_date(correct_occupation):
    request = correct_occupation.get_any_request()
    from_date = request.creation_date.date()
    to_date = from_date + timedelta(weeks=4)
    date_range = (from_date, to_date)

    json = correct_occupation.get_requests(date_range=date_range)

    requests_dates = [request.attributes.creation_date.date() for request in json.data]
    min_request_date = min(requests_dates)
    max_request_date = max(requests_dates)
    assert_that(min_request_date).is_greater_or_equal(from_date)
    assert_that(max_request_date).is_less_or_equal(to_date)


@pytest.mark.parametrize(
    "parameter",
    [
        {"page": 1000},
        {"laborer_id": 2000000000},
        {"laborer_name": "Non-exist name"},
        {"date_range": (today + timedelta(days=1), today + timedelta(days=2))},
        {"date_range": (today + timedelta(days=2), today + timedelta(days=1))},
    ],
    ids=["page", "laborer_id", "laborer_name", "future_date_range", "invalid_date_range"]
)
def test_by_not_found_value(correct_occupation, parameter):
    json = correct_occupation.get_requests(**parameter)

    data, meta = json.data, json.meta
    assert_that(data).is_empty()
    assert_that(meta).has(
        total_entities=0,
        pages_count=0,
    )
