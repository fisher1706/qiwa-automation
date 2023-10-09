from http import HTTPStatus

import pytest

from data.shareable.expected_json.work_permits.cancel_sadad_number import (
    already_canceled_transaction_error,
    successfully_canceled_transaction, incorrect_transaction_error,
)
from src.api.assertions.diff import assert_difference
from src.api.models.qiwa.raw.work_permit.cancel_sadad import SuccessfulCancelling
from src.api.models.qiwa.work_permit import cancel_sadad_ibm_error
from utils.assertion import assert_status_code

pytestmark = [pytest.mark.stage]


def test_cancelling_pending_payment_request(api, pending_payment_sadad_number):
    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=pending_payment_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = SuccessfulCancelling.parse_obj(response.json())
    expected_json_values = successfully_canceled_transaction(pending_payment_sadad_number)
    actual_json_values = response_json.dict()

    assert_difference(expected_json_values, actual_json_values)


def test_canceling_already_canceled_sadad_number(api, canceled_sadad_number):
    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=canceled_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    response_json = cancel_sadad_ibm_error.parse_obj(response.json())
    expected_json_values = already_canceled_transaction_error()
    actual_json_values = response_json.data.attributes.dict(include=set(expected_json_values.keys()))

    assert_difference(expected_json_values, actual_json_values)


def test_cancelling_incorrect_sadad_number(api):
    incorrect_sadad_number = "123456789"

    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=incorrect_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    response_json = cancel_sadad_ibm_error.parse_obj(response.json())
    expected_json_values = incorrect_transaction_error()
    actual_json_values = response_json.data.attributes.dict(include=set(expected_json_values.keys()))

    assert_difference(expected_json_values, actual_json_values)
