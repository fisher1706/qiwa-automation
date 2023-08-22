from http import HTTPStatus

import pytest

from src.api import models
from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from utils.assertion import assert_status_code, assert_that

pytestmark = [pytest.mark.stage]


@pytest.mark.parametrize("is_regular", [True, False])
def test_validation(user, is_regular):
    qiwa = QiwaApi.login_as_user(user).select_company()
    expat_number = "2358625925"

    response = qiwa.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=is_regular
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = response.json()
    validate_model(json, model=models.qiwa.work_permit.expat_validation)
    assert_that(json).has("expat_number")(expat_number)


def test_validation_with_invalid_expat_number(user):
    qiwa = QiwaApi.login_as_user(user).select_company()
    expat_number = "0000000000"

    response = qiwa.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )

    json = response.json()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    validate_model(json, model=models.qiwa.work_permit.expat_validation_error)
    assert_that(json).has("expat_number")(expat_number)
    assert_that(json["errors"]) \
        .has("code")("WP-003") \
        .has("message_en")("Sorry, we cannot issue- renew working permit "
                           "because the border ID or border number is invalid ") \
        .has("message_ar")("عفوا، لا يمكن إصدار/تجديد رخصة عمل حيث أن رقم الإقامة/رقم الحدود للعامل غير صحيح")


def test_validation_for_expat_with_created_request(user):
    qiwa = QiwaApi.login_as_user(user).select_company()
    expat_number = "2218400451"

    response = qiwa.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )

    json = response.json()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    validate_model(json, model=models.qiwa.work_permit.expat_validation_error)
    assert_that(json).has("expat_number")(expat_number)
    assert_that(json["errors"]) \
        .has("code")("WP-010") \
        .has("message_en")("Sorry, we cannot renew working permit "
                           "since the laborer working permit is under processing ") \
        .has("message_ar")("عفوا، العامل لديه رخصة عمل قيد السداد")


def test_validation_for_expat_from_another_establishment(user):
    qiwa = QiwaApi.login_as_user(user).select_company()
    expat_number = "2393440215"

    response = qiwa.wp_request_api.validate_expat(
        expat_number=expat_number,
        regular=True
    )

    json = response.json()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    validate_model(json, model=models.qiwa.work_permit.expat_validation_error)
    assert_that(json).has("expat_number")(expat_number)
    assert_that(json["errors"]) \
        .has("code")("WP-004") \
        .has("message_en")("Sorry, we cannot issue- renew working permit "
                           "because the laborer is not listed in your establishment ") \
        .has("message_ar")("عفوا، لا يمكن إصدار/تجديد رخصة عمل حيث أن العامل غير مدرج ضمن عمالة منشأتك ")
