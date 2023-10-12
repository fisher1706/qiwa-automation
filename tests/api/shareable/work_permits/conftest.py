import random
from http import HTTPStatus

import pytest

from data.mock_mlsd.establishment import Establishment
from src.api import models
from src.api.app import QiwaApi
from src.api.constants.work_permit import WorkPermitStatus
from src.api.models.qiwa.raw.work_permit.employees import Employee
from utils.assertion import assert_status_code
from utils.json_search import search_by_data


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
def api(request) -> QiwaApi:
    marks = [mark.name for mark in request.node.own_markers]
    user = "1470547124"
    if "stage" in marks:
        user = "1015671413"
    elif request.node.name == "test_work_permit_debts.py":
        user = "1154755065"
    return QiwaApi.login_as_user(user).select_company()


@pytest.fixture
def pending_payment_sadad_number(api) -> str:
    response = api.wp_request_api.get_wp_transactions(
        status=WorkPermitStatus.PENDING_PAYMENT, expect_code=HTTPStatus.OK
    )
    requests_list = models.qiwa.work_permit.transactions_data.parse_obj(response.json())
    return next(
        data.attributes.bill_number for data in requests_list.data if data.attributes.bill_number
    )


@pytest.fixture
def canceled_sadad_number(api) -> str:
    response = api.wp_request_api.get_wp_transactions(
        status=WorkPermitStatus.CANCELED, expect_code=HTTPStatus.OK
    )
    requests_list = models.qiwa.work_permit.transactions_data.parse_obj(response.json())
    return requests_list.data[0].attributes.bill_number


@pytest.fixture
def employee(api) -> Employee:
    response = api.wp_request_api.get_employees()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    response_json = models.qiwa.work_permit.employees_data.parse_obj(response.json())
    return Employee.parse_obj(random.choice(response_json.data).attributes)


@pytest.fixture
def employee_to_validate(api) -> Employee:
    response = api.wp_request_api.get_employees(per_page=100)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    expression = "data[?attributes.wp_status_id==`3`].attributes | [0]"
    employee = search_by_data(expression, response.json())
    return Employee.parse_obj(employee)
