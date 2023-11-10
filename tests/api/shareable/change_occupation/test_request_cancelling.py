from http import HTTPStatus

import pytest

from data.shareable.change_occupation import RequestStatus
from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_status_code, assert_that


def test_cancel_request(change_occupation, laborer):
    created_request = change_occupation.create_request(laborer)

    response = change_occupation.api.cancel_request(created_request.data[0].attributes.request_id)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_that(response.json()).has(success=True)


def test_cancel_with_invalid_request_number(change_occupation):
    response = change_occupation.api.cancel_request("11111111111")
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


@pytest.mark.parametrize("status", [
    RequestStatus.DRAFT,
    RequestStatus.REJECTED_BY_LABORER,
    RequestStatus.CANCELED_BY_EMPLOYER
])
def test_cancel_request_in_wrong_status(change_occupation, status):
    requests = change_occupation.get_requests_laborers(request_status=status)
    request_to_cancel = requests.data[0].attributes

    response = change_occupation.api.cancel_request(request_to_cancel.request_number)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
