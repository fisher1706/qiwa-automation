from http import HTTPStatus

import pytest

from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from src.api.models.qiwa.raw.work_permit.cancel_sadad import SuccessfulCancelling
from src.api.models.qiwa.work_permit import cancel_sadad_ibm_error
from utils.assertion import assert_status_code, assert_that

pytestmark = [pytest.mark.stage]


def test_cancelling_pending_payment_request(user, pending_payment_sadad_number):
    qiwa = QiwaApi.login_as_user(user).select_company()

    response = qiwa.wp_request_api.cancel_sadad_number(
        sadad_number=pending_payment_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = response.json()
    validate_model(json, model=SuccessfulCancelling)
    assert_that(json["message"])\
        .has("message_en")(f"SADAD bill {pending_payment_sadad_number} has been canceled successfully")\
        .has("message_ar")(f"تم إلغاء معاملة سداد رقم {pending_payment_sadad_number} بنجاح")


def test_cancelling_canceled_request(user, canceled_sadad_number):
    qiwa = QiwaApi.login_as_user(user).select_company()

    response = qiwa.wp_request_api.cancel_sadad_number(
        sadad_number=canceled_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = response.json()
    validate_model(json, model=cancel_sadad_ibm_error)
    assert_that(json["data"]["attributes"])\
        .has("code")("MOF00005")\
        .has("english-msg")("Cannot be canceled, the payment entry transaction is canceled")\
        .has("arabic-msg")("لا يمكن الإلغاء، معاملة سداد المدخلة ملغاة")


def test_cancelling_incorrect_sadad_number(user):
    qiwa = QiwaApi.login_as_user(user).select_company()
    incorrect_sadad_number = "123456789"

    response = qiwa.wp_request_api.cancel_sadad_number(
        sadad_number=incorrect_sadad_number
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = response.json()
    validate_model(json, model=cancel_sadad_ibm_error)
    assert_that(json["data"]["attributes"])\
        .has("code")("MOF00008")\
        .has("english-msg")("Cannot be canceled, payment entry is incorrect")\
        .has("arabic-msg")("لا يمكن الإلغاء، معاملة سداد المدخلة غير صحيحة")
