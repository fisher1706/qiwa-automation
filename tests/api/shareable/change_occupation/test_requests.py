import pytest

from utils.assertion import assert_that
from utils.json_search import get_data_attribute

# TODO: get by partial name


def test_getting_by_employee_name(change_occupation):
    laborer = change_occupation.get_random_laborer()
    json = change_occupation.get_requests(employee_name=laborer.laborer_name, per=100)

    employee_names_from_json = get_data_attribute(json, "laborers", "[]", ".employee_name")
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
