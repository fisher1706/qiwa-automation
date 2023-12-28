from http import HTTPStatus

import pytest

from utils.assertion import assert_that


def test_by_current_occupation_id(correct_occupation):
    laborer = correct_occupation.get_any_laborer()
    occupation_id = laborer.occupation_id

    json = correct_occupation.get_occupations(occupation_id=occupation_id)
    data = json.data
    assert_that(data).is_not_empty()


def test_by_not_found_occupation_id(correct_occupation):
    response = correct_occupation.api.get_correct_occupations(occupation_id="1234567")
    status_code = response.status_code
    assert_that(status_code).equals_to(HTTPStatus.OK)

    json = response.json()
    data = json["data"]
    data_has_list = isinstance(data, list)
    assert_that(data_has_list).equals_to(False)
    attributes = data["attributes"]
    assert_that(attributes).is_empty()


def test_by_missing_occupation_id(correct_occupation):
    response = correct_occupation.api.get_correct_occupations(occupation_id=None)
    status_code = response.status_code
    assert_that(status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)


class TestPagination:
    @pytest.mark.parametrize("page", [1, 2, 3])
    def test_by_page(self, correct_occupation, page):
        laborer = correct_occupation.get_any_laborer()
        any_occupation_id = laborer.occupation_id

        json = correct_occupation.get_occupations(page=page, per=1, occupation_id=any_occupation_id)
        data, meta = json.data, json.meta
        assert_that(data).is_not_empty()
        assert_that(meta).has(current_page=page)
        occupations = [occupation.attributes.occupation_id for occupation in data]

        next_page = page + 1
        next_page_json = correct_occupation.get_occupations(page=next_page, per=1, occupation_id=any_occupation_id)
        next_page_data = next_page_json.data
        assert_that(next_page_data).is_not_empty()
        next_page_occupations = [occupation.attributes.occupation_id for occupation in next_page_data]
        next_page_data_is_different = all(occupation not in next_page_occupations for occupation in occupations)
        assert_that(next_page_data_is_different).equals_to(True)

    @pytest.mark.parametrize("per_page", [1, 3, 5])
    def test_by_per_page(self, correct_occupation, per_page):
        laborer = correct_occupation.get_any_laborer()

        json = correct_occupation.get_occupations(per=per_page, occupation_id=laborer.occupation_id)
        assert_that(json.data).size_is(per_page)
