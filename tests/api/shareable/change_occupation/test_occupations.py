from http import HTTPStatus

import pytest

from utils.assertion import assert_that


def test_by_english_name(change_occupation):
    occupation = change_occupation.get_random_occupation()
    english_name = occupation.english_name

    json = change_occupation.get_occupations(english_name=english_name)
    data = json.data
    assert_that(data).is_not_empty()
    occupations_match_english_name: bool = all(
        english_name in occupation.attributes.english_name for occupation in data
    )
    assert_that(occupations_match_english_name).equals_to(True)


def test_by_arabic_name(change_occupation):
    occupation = change_occupation.get_random_occupation()
    arabic_name = occupation.arabic_name

    json = change_occupation.get_occupations(arabic_name=arabic_name)
    data = json.data
    assert_that(data).is_not_empty()
    occupations_match_arabic_name: bool = all(
        arabic_name in occupation.attributes.arabic_name for occupation in data
    )
    assert_that(occupations_match_arabic_name).equals_to(True)


@pytest.mark.parametrize("name", [
    {"english_name": "Some Name"},
    {"arabic_name": "بعض الاسم"},
], ids=lambda param: list(param.keys())[0])
def test_by_not_found_occupation_name(change_occupation, name):
    json = change_occupation.get_occupations(**name)

    data, meta = json.data, json.meta
    assert_that(data).is_empty()
    assert_that(meta).has(
        total_count=0,
        total_pages=0,
    )


@pytest.mark.parametrize("page", [1, 10, 100])
def test_getting_page(change_occupation, page):
    json = change_occupation.get_occupations(page=page, per=1)
    assert_that(json.meta).has(
        current_page=page,
        next_page=page + 1
    )


@pytest.mark.parametrize("per_page", [1, 10, 100])
def test_getting_per_page(change_occupation, per_page):
    json = change_occupation.get_occupations(per=per_page)
    assert_that(json.data).size_is(per_page)


def test_getting_last_page(change_occupation):
    occupations = change_occupation.get_occupations()
    last_page = occupations.meta.total_pages

    json = change_occupation.get_occupations(page=last_page)
    assert_that(json.data).is_not_empty()
    assert_that(json.meta).has(
        current_page=last_page,
        next_page=None,
        prev_page=last_page - 1,
        total_pages=last_page
    )


def test_getting_next_after_last_page(change_occupation):
    occupations = change_occupation.get_occupations()
    last_page = occupations.meta.total_pages
    next_after_last_page = last_page + 1

    json = change_occupation.get_occupations(page=next_after_last_page)
    assert_that(json.data).is_empty()
    assert_that(json.meta).has(
        current_page=next_after_last_page,
        next_page=None,
        prev_page=last_page,
        total_pages=last_page
    )


def test_getting_more_than_total_per_page(change_occupation):
    occupations = change_occupation.get_occupations()
    total_count = occupations.meta.total_count

    json = change_occupation.get_occupations(per=total_count + 1)
    assert_that(json.data).size_is(total_count)
    assert_that(json.meta).has(
        total_count=total_count,
        current_page=1,
        total_pages=1,
        next_page=None,
        prev_page=None
    )


def test_getting_zero_per_page(change_occupation):
    response = change_occupation.api.get_occupations(page=1, per=0)
    assert_that(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)


@pytest.mark.parametrize("page", [0, -1])
def test_getting_zero_and_negative_page(page, change_occupation):
    response = change_occupation.api.get_occupations(page=page, per=10)
    assert_that(response.status_code).equals_to(HTTPStatus.OK)
    assert_that(response.json()).has(data=None)
