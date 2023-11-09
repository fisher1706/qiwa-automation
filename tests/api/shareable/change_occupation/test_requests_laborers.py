from http import HTTPStatus

import pytest

from data.shareable.change_occupation import RequestStatus
from data.shareable.expected_json.change_occupation.requests_laborers import empty_data
from src.api.models.qiwa.raw.root import Root
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_data, assert_that
from utils.json_search import get_data_attribute, search_data_by_attributes


def test_getting_by_laborer_name(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_name=laborer.laborer_name, per=1000)
    assert_that(json.data).is_not_empty().size_is(json.meta.total_entities)
    assert_that(search_data_by_attributes(json, laborer_name=laborer.laborer_name)).size_is(json.meta.total_entities)


def test_getting_by_laborer_id(change_occupation):
    laborer = change_occupation.get_random_laborer()

    json = change_occupation.get_requests_laborers(laborer_id=laborer.laborer_id_no)
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
    assert_that(response).has(status_code=HTTPStatus.OK)

    json = Root.parse_obj(response.json())
    assert_that(json.data).size_is(count)
    assert_that(json.meta).has(total_entities=count)


def test_getting_empty_page(change_occupation):
    requests_laborers = change_occupation.get_requests_laborers(per=10)
    page = requests_laborers.meta.pages_count + 1

    response = change_occupation.api.get_requests_laborers(page=page, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())

    response = change_occupation.api.get_requests_laborers(page=10000, per=10)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_data(expected=empty_data(), actual=response.json())


@pytest.mark.parametrize(
    "parameter",
    [{"laborer_id": 2000000000}, {"laborer_name": "Non-exist name"}, {"request_status": 10000}],
    ids=["laborer_id", "laborer_name", "request_status"]
)
def test_getting_by_non_existent_parameter_value(change_occupation, parameter):
    response = change_occupation.api.get_requests_laborers(page=1, per=10, **parameter)
    assert_that(response).has(status_code=HTTPStatus.OK)

    json = Root.parse_obj(response.json())
    assert_that(json.data).is_empty()
    assert_that(json.meta).has(
        pages_count=0,
        total_entities=0,
        total_count=0,
        total_pages=0
    )
