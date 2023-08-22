from http import HTTPStatus

import pytest

from data.mock_mlsd.establishment import Establishment
from src.api import models
from src.api.app import QiwaApi
from src.api.constants.work_permit import WorkPermitStatus


@pytest.fixture(scope="package")
def establishment() -> Establishment:
    # Init establishment
    return Establishment(
        expat_count=11,
        labor_office_id="11",
        sequence_number="2274530",
        personal_number="2670888311",
    )


@pytest.fixture(scope="module")
def user(request) -> str:
    marks = [mark.name for mark in request.node.own_markers]
    if "stage" in marks:
        return "1015671413"
    elif request.node.name == "test_work_permit_debts.py":
        return "1154755065"
    else:
        return "1470547124"


@pytest.fixture
def pending_payment_sadad_number(user) -> str:
    qiwa = QiwaApi.login_as_user(user).select_company()

    response = qiwa.wp_request_api.get_wp_transactions(
        status=WorkPermitStatus.PENDING_PAYMENT, expect_code=HTTPStatus.OK
    )

    requests_list = models.qiwa.work_permit.work_permit_requests_list.parse_obj(response.json())
    return next(
        data.attributes.bill_number for data in requests_list.data if data.attributes.bill_number
    )


@pytest.fixture
def canceled_sadad_number(user) -> str:
    qiwa = QiwaApi.login_as_user(user).select_company()

    response = qiwa.wp_request_api.get_wp_transactions(
        status=WorkPermitStatus.CANCELED, expect_code=HTTPStatus.OK
    )

    requests_list = models.qiwa.work_permit.work_permit_requests_list.parse_obj(response.json())
    return requests_list.data[0].attributes.bill_number
