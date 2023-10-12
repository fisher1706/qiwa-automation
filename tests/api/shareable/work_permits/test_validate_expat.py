from http import HTTPStatus

import pytest

from data.shareable.expected_json.work_permits.validate_expat import invalid_expat_number_error, \
    processing_work_permit_error, not_your_establishment_laborer_error
from src.api import models
from src.api.assertions.diff import assert_not_difference
from utils.assertion import assert_status_code, assert_that

pytestmark = [pytest.mark.stage]


@pytest.mark.parametrize("is_regular", [True, False])
def test_validation_result(api, employee_to_validate, is_regular):
    response = api.wp_request_api.validate_expat(
        expat_number=employee_to_validate.personal_number,
        regular=is_regular
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = models.qiwa.work_permit.expat_validation.parse_obj(response.json())
    assert_that(json.expat_number).equals_to(employee_to_validate.personal_number)


def test_validation_with_invalid_expat_number(api):
    expat_number = "0000000000"
    response = api.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = models.qiwa.work_permit.expat_validation_error.parse_obj(response.json())
    expected_json_values = invalid_expat_number_error(expat_number)
    actual_json_values = json.dict()
    assert_not_difference(expected_json_values, actual_json_values)


def test_validation_for_expat_with_created_request(api):
    expat_number = "2392007080"
    response = api.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = models.qiwa.work_permit.expat_validation_error.parse_obj(response.json())
    expected_json_values = processing_work_permit_error(expat_number)
    actual_json_values = json.dict()
    assert_not_difference(expected_json_values, actual_json_values)


def test_validation_for_expat_from_another_establishment(api):
    expat_number = "2393440215"
    response = api.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = models.qiwa.work_permit.expat_validation_error.parse_obj(response.json())
    expected_json_values = not_your_establishment_laborer_error(expat_number)
    actual_json_values = json.dict()
    assert_not_difference(expected_json_values, actual_json_values)
