import pytest


@pytest.mark.parametrize("page", [1, 2])
def test_total_count(api, page, establishment):
    response = api.wp_request_api.get_employees(page)
    api.wp_request_api.assert_total_count(response.json(), expected_count=establishment.expat_count)


@pytest.mark.parametrize("page, count", [(1, 10), (2, 1)])
def test_items_count(api, page, count):
    response = api.wp_request_api.get_employees(page)
    api.wp_request_api.assert_total_count(response.json(), expected_count=count)


def test_empty_page_count(api):
    response = api.wp_request_api.get_employees(page=100)
    json = response.json()
    api.wp_request_api\
        .assert_total_count(json, expected_count=0)\
        .assert_items_count(json, expected_count=0)


def test_search_by_personal_number(api, establishment):
    response = api.wp_request_api.get_employee_by_personal_number(establishment.personal_number)
    json = response.json()
    api.wp_request_api \
        .assert_total_count(json, expected_count=1) \
        .assert_items_count(json, expected_count=1)


def test_search_by_wrong_personal_number(api):
    response = api.wp_request_api.get_employee_by_personal_number('1234567890')
    json = response.json()
    api.wp_request_api \
        .assert_total_count(json, expected_count=0) \
        .assert_items_count(json, expected_count=0)
