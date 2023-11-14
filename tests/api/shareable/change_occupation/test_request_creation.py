from http import HTTPStatus

import pytest

from data.shareable.change_occupation import RequestStatus
from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from src.api.payloads.raw.change_occupation import Laborer
from utils.assertion import assert_status_code, assert_that


def test_create_request(change_occupation, laborer):
    json = change_occupation.create_request(laborer)
    assert_that(json.data).size_is(1)

    request_attributes = json.data[0].attributes
    assert_that(request_attributes).has(personal_number=laborer.personal_number)

    requests = change_occupation.get_requests_by_request_number(request_attributes.request_id)
    assert_that(requests).size_is(1)
    assert_that(requests[0]).has(
        status_id=RequestStatus.PENDING_LABORER_APPROVAL.value,
        employee_personal_number=laborer.personal_number,
        new_occupation_id=laborer.occupation_code
    )


def test_create_for_two_laborers(change_occupation, laborer, laborer2):
    json = change_occupation.create_request(laborer, laborer2)
    assert_that(json.data).size_is(2)

    request1, request2 = json.data

    for request, laborer in ((request1, laborer), (request2, laborer2)):
        assert_that(request.attributes).has(personal_number=laborer.personal_number)

        requests = change_occupation.get_requests_by_request_number(request.attributes.request_id)
        assert_that(requests).size_is(1)
        assert_that(requests[0]).has(
            status_id=RequestStatus.PENDING_LABORER_APPROVAL.value,
            employee_personal_number=laborer.personal_number,
            new_occupation_id=laborer.occupation_code
        )


def test_create_for_two_laborers_but_one_not_eligible(change_occupation, laborer):
    user = change_occupation.get_random_user(eligible=False)
    laborer2 = Laborer(personal_number=user.personal_number)

    response = change_occupation.api.create_request(laborer, laborer2)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_create_for_laborer_with_processing_request(change_occupation, laborer):
    change_occupation.create_request(laborer)

    response = change_occupation.api.create_request(laborer)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


@pytest.mark.parametrize(
    "laborer",
    [
        Laborer(personal_number="2000879565"),
        Laborer(personal_number="200000000"),
        Laborer(occupation_code="111111"),
    ],
    ids=["laborer_from_another_establishment", "invalid_personal_number", "invalid_occupation"]
)
def test_create_with_invalid_values(change_occupation, laborer):
    response = change_occupation.api.create_request(laborer)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
