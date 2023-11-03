from http import HTTPStatus

import pytest

from src.api.models.qiwa import work_permits
from utils.assertion import assert_status_code, assert_that
from utils.assertion.asserts import assert_data


def test_get_employee_by_personal_number(api, employee):
    response = api.work_permits_api.get_employee_by_personal_number(employee.personal_number)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.employees_data.parse_obj(response.json())
    assert_that(json.data).size_is(1)
    assert_that(json.meta).has(total_count=1)
    assert_data(
        expected=employee.dict(exclude={"id"}),
        actual=json.data[0].attributes.dict(exclude={"id"})
    )


def test_get_employee_by_wrong_personal_number(api):
    response = api.work_permits_api.get_employee_by_personal_number("0000000000")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.employees_data.parse_obj(response.json())
    assert_that(json.data).size_is(0)
    assert_that(json.meta).has(total_count=0)


@pytest.mark.parametrize("per_page", [0, 1, 9, 11, 100, 1000])
def test_get_employees_per_page(api, per_page):
    response = api.work_permits_api.get_employees(per_page=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.employees_data.parse_obj(response.json())
    assert_that(json.data).size_is(per_page)


@pytest.mark.parametrize("page, count", [(1, 10), (11, 10), (-1, 0), (0, 0), (100000, 0)])
def test_get_employees_pagination(api, page, count):
    response = api.work_permits_api.get_employees(page=page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.employees_data.parse_obj(response.json())
    assert_that(json.data).size_is(count)
