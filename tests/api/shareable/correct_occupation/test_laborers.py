import pytest

from utils.assertion import assert_that


def test_by_laborer_name(correct_occupation):
    laborer = correct_occupation.get_any_laborer()
    name = laborer.laborer_name.split()[0]

    json = correct_occupation.get_laborers(laborer_name=name)
    assert_that(json.data).is_not_empty()
    assert_that(all(laborer.attributes.laborer_name.startswith(name) for laborer in json.data))\
        .as_(f"laborer names start with {name}").equals_to(True)


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
    assert_that(all(getattr(laborer.attributes, parameter) == value for laborer in json.data))\
        .as_("laborers are with attribute").equals_to(True)


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
    @pytest.mark.parametrize("page", [1, 2, 3])
    def test_by_page(self, correct_occupation, page):
        json = correct_occupation.get_laborers(page=page, per=5)
        data, meta = json.data, json.meta
        assert_that(data).is_not_empty()
        assert_that(meta).has(current_page=page)
        laborers = [laborer.attributes.laborer_id for laborer in data]

        next_page = page + 1
        next_page_json = correct_occupation.get_laborers(page=next_page, per=5)
        next_page_data = next_page_json.data
        assert_that(next_page_data).is_not_empty()
        next_page_laborers = [laborer.attributes.laborer_id for laborer in next_page_data]
        next_page_data_is_different = all(laborer not in next_page_laborers for laborer in laborers)
        assert_that(next_page_data_is_different).equals_to(True)

    @pytest.mark.parametrize("per_page", [1, 5, 10, 15])
    def test_by_per_page(self, correct_occupation, per_page):
        json = correct_occupation.get_laborers(per=per_page)
        data = json.data

        assert_that(data).size_is(per_page)
