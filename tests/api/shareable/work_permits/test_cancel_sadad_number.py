from http import HTTPStatus

from data.shareable.expected_json.work_permits.cancel_sadad_number import (
    already_canceled_transaction_error,
    incorrect_transaction_error,
    successfully_canceled_transaction,
)
from src.api.models.qiwa.raw.work_permits.cancel_sadad import SuccessfulCancelling
from src.api.models.qiwa.work_permits import cancel_sadad_ibm_error
from utils.assertion import assert_status_code
from utils.assertion.asserts import assert_data


def test_cancelling_pending_payment_request(api, pending_payment_sadad_number):
    response = api.work_permits_api.cancel_sadad_number(
        sadad_number=pending_payment_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = SuccessfulCancelling.parse_obj(response.json())
    assert_data(
        expected=successfully_canceled_transaction(pending_payment_sadad_number),
        actual=json.dict()
    )


def test_canceling_already_canceled_sadad_number(api, canceled_sadad_number):
    response = api.work_permits_api.cancel_sadad_number(
        sadad_number=canceled_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = cancel_sadad_ibm_error.parse_obj(response.json())
    assert_data(
        expected=already_canceled_transaction_error(),
        actual=json.data.attributes.dict()
    )


def test_cancelling_incorrect_sadad_number(api):
    incorrect_sadad_number = "123456789"

    response = api.work_permits_api.cancel_sadad_number(
        sadad_number=incorrect_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = cancel_sadad_ibm_error.parse_obj(response.json())
    assert_data(
        expected=incorrect_transaction_error(),
        actual=json.data.attributes.dict()
    )
