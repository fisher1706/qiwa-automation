from http import HTTPStatus

import pytest

from src.api.constants.work_permit import WorkPermitStatus
from src.api.models.qiwa import work_permits
from utils.assertion import assert_status_code, assert_that


def test_get_transactions(api):
    response = api.work_permits_api.get_wp_transactions(per_page=1000)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.transactions_data.parse_obj(response.json())
    assert_that(json.data).is_length(json.meta.total_count)


@pytest.mark.parametrize("status", WorkPermitStatus, ids=lambda param: param.name)
def test_get_transactions_by_status(api, status):
    response = api.work_permits_api.get_wp_transactions(per_page=1000, status=status)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = work_permits.transactions_data_with_status(status).parse_obj(response.json())
    assert_that(json.data).is_length(json.meta.total_count)
