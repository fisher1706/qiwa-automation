from http import HTTPStatus
from json import dumps
from pprint import pprint

import pytest

from src.api.assertions.diff import assert_difference
from src.api.assertions.model import validate_model
from src.api.models.qiwa.raw.work_permit.cancel_sadad import SuccessfulCancelling
from src.api.models.qiwa.work_permit import cancel_sadad_ibm_error
from utils.assertion import assert_status_code, assert_that

pytestmark = [pytest.mark.stage]


def test_cancelling_pending_payment_request(api, pending_payment_sadad_number):
    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=pending_payment_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = response.json()

    model = SuccessfulCancelling.parse_obj(json)

    expected_json = {
        "message_en": f"SADAD bill {pending_payment_sadad_number} has been canceled successfully",
        "message_ar": f"تم إلغاء معاملة سداد رقم {pending_payment_sadad_number} بنجاح"
    }

    assert_difference(expected_json, )




    validate_model(json, model=SuccessfulCancelling)
    assert_that(json["message"]) \
        .has("message_en")(f"SADAD bill {pending_payment_sadad_number} has been canceled successfully") \
        .has("message_ar")(f"تم إلغاء معاملة سداد رقم {pending_payment_sadad_number} بنجاح")





def test_cancelling_canceled_request(api, canceled_sadad_number):
    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=canceled_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    assert_cancel_sadad_ibm_error(response.json())


def test_cancelling_incorrect_sadad_number(api):
    incorrect_sadad_number = "123456789"

    response = api.wp_request_api.cancel_sadad_number(
        sadad_number=incorrect_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = response.json()
    validate_model(json, model=cancel_sadad_ibm_error)
    assert_that(json["data"]["attributes"]) \
        .has("code")("MOF00008") \
        .has("english-msg")("Cannot be canceled, payment entry is incorrect") \
        .has("arabic-msg")("لا يمكن الإلغاء، معاملة سداد المدخلة غير صحيحة")
