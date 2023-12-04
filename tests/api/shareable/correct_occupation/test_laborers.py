import pytest

from utils.assertion import assert_that
from utils.json_search import get_data_attribute, search_by_data


def test_by_laborer_name(correct_occupation):
    laborer = correct_occupation.get_any_laborer()
    name = laborer.laborer_name.split()[0]

    json = correct_occupation.get_laborers(laborer_name=name)
    assert_that(json.data).is_not_empty()
    searched_by_name_in_json = len(
        search_by_data(f"data[? starts_with(attributes.\"laborer_name\", '{name}')]", json.dict())
    )
    assert_that(json.data).size_is(searched_by_name_in_json)


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
    assert_that(set(get_data_attribute(json, parameter))).size_is(1).contains(value)


def test_not_found():
    ...


class TestPagination:
    ...
