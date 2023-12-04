import pytest

from utils.assertion import assert_that
from utils.json_search import get_data_attribute, search_by_data


def test_by_laborer_name(correct_occupation):
    laborer = correct_occupation.get_any_laborer()
    name = laborer.laborer_name.split()[0]

    json = correct_occupation.get_laborers(laborer_name=name)
    assert_that(json.data).is_not_empty()
    assert_that(all(laborer.attributes.laborer_name.startswith(name) for laborer in json.data)).equals_to(True)


def test_by_laborer_id(correct_occupation):
    laborer = correct_occupation.get_any_laborer()

    json = correct_occupation.get_laborers(laborer_id=laborer.laborer_id)
    assert_that(json.data).size_is(1)
    assert_that(json.data[0].attributes).has(laborer_id=laborer.laborer_id)


@pytest.mark.parametrize("parameter", ["nationality_id", "occupation_id"])
def test_by_laborer_nationality_and_occupation(correct_occupation, parameter):
    laborer = correct_occupation.get_any_laborer()
    value = getattr(laborer, parameter)
    query_parameter = {parameter: value}

    json = correct_occupation.get_laborers(**query_parameter)
    assert_that(json.data).is_not_empty()
    assert_that(all(getattr(laborer.attributes, parameter) == value for laborer in json.data)).equals_to(True)


@pytest.mark.parametrize("value", [
    {"page": 10000},
    {"laborer_name": "Some Name"},
    {"laborer_id": "1234567890"},
    {"nationality_id": 12345},
    {"occupation_id": 12345},
], ids=lambda param: list(param.keys())[0])
def test_by_not_found_parameter_value(correct_occupation, value):
    json = correct_occupation.get_laborers(**value)

    assert_that(json.data).is_empty()
    assert_that(json.meta).has(
        pages_count=0,
        total_entities=0,
    )


class TestPagination:
    ...
