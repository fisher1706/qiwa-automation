from http import HTTPStatus

import pytest

from src.api import models
from src.api.assertions.diff import assert_not_difference
from utils.assertion import assert_status_code, assert_that

pytestmark = [pytest.mark.stage]


def test_get_employee_by_personal_number(api, employee):
    response = api.wp_request_api.get_employee_by_personal_number(employee.personal_number)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = models.qiwa.work_permit.employees_data.parse_obj(response.json())
    assert_that(response_json.data).is_length(1)
    assert_that(response_json.meta.total_count).equals_to(1)

    expected_employee_data = employee.dict(exclude={"id"})
    actual_employee_data = response_json.data[0].attributes.dict(exclude={"id"})
    assert_not_difference(expected_employee_data, actual_employee_data)


def test_get_employee_by_wrong_personal_number(api):
    response = api.wp_request_api.get_employee_by_personal_number("0000000000")
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = models.qiwa.work_permit.employees_data.parse_obj(response.json())
    assert_that(response_json.data).is_length(0)
    assert_that(response_json.meta.total_count).equals_to(0)


@pytest.mark.parametrize("per_page", [0, 1, 9, 11, 100, 1000])
def test_get_employees_per_page(api, per_page):
    response = api.wp_request_api.get_employees(per_page=per_page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = models.qiwa.work_permit.employees_data.parse_obj(response.json())
    assert_that(response_json.data).is_length(per_page)


@pytest.mark.parametrize("page, count", [(1, 10), (11, 10), (-1, 0), (0, 0), (100000, 0)])
def test_get_employees_pagination(api, page, count):
    response = api.wp_request_api.get_employees(page=page)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = models.qiwa.work_permit.employees_data.parse_obj(response.json())
    assert_that(response_json.data).is_length(count)
