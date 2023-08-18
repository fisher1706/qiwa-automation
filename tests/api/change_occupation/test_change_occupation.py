from http import HTTPStatus

import pytest

from helpers.assertion import assert_status_code, assert_that
from src.api import assertions, models, payloads
from src.api.app import QiwaApi
from src.api.clients.ibm_mock_api import IBMMockApi
from src.api.payloads.change_occupation import create_change_occupation_request
from src.api.payloads.raw.change_occupation import Laborer

pytestmark = [pytest.mark.change_occupation_suite, pytest.mark.daily, pytest.mark.api, pytest.mark.ss, pytest.mark.wp]


def test_create_change_occupation_request(establishment):
    ibm = IBMMockApi()
    qiwa = QiwaApi.login_as_user(establishment.personal_number).select_company()
    qiwa.change_occupation.pass_ott_authorization()

    laborer = Laborer(personal_number="2400231465", occupation_code="111011")
    payload = create_change_occupation_request(establishment.labor_office_id, establishment.sequence_number, laborer)

    create_request = qiwa.change_occupation.create_change_occupation_request(payload)
    assert_status_code(create_request.status_code).equals_to(HTTPStatus.OK)

    created_request = models.qiwa.change_occupation.created_change_occupation_requests.parse_obj(create_request.json())
    created_request_attributes = created_request.data[0].attributes
    office_id, sequence, year = created_request_attributes.request_id.split("-")
    assert_that(office_id).as_("labor_office_id").equals_to(establishment.labor_office_id)
    assert_that(created_request_attributes.personal_number).as_("personal_number").equals_to(laborer.personal_number)

    payload = payloads.ibm.search_change_occupation()
    payload.RequesterDetails.RequesterIdNo = establishment.personal_number
    payload.LaborerDetails.LaborerIdNo = laborer.personal_number
    payload.LaborerDetails.NewOccupationId = laborer.occupation_code
    payload.EstablishmentDetails.SequenceNumber = establishment.sequence_number
    payload.EstablishmentDetails.LaborOfficeId = office_id
    payload.RequestDetails.RequestSequence = sequence
    payload.RequestDetails.RequestYear = year
    ibm_response = ibm.get_change_occupation_requests_from_ibm(payload)

    assert_that(ibm_response.Body.TotalRecordsCount).as_("requests in IBM").equals_to(1)


def test_get_change_occupation_requests(establishment):
    ibm = IBMMockApi()
    qiwa = QiwaApi.login_as_user(establishment.personal_number).select_company()
    qiwa.change_occupation.pass_ott_authorization()

    response = qiwa.change_occupation.get_change_occupation_requests()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_model = models.qiwa.change_occupation.change_occupation_requests_list.parse_obj(response.json())
    actual_data = response_model.data[0]

    payload = payloads.ibm.search_change_occupation()
    payload.RequestId = actual_data.id
    ibm_response = ibm.get_change_occupation_requests_from_ibm(payload)
    expected_data = ibm_response.Body.ChangeOccupationList.ChangeOccupationItem

    assertions.change_occupation.assert_change_occupation_request(actual_data, expected_data)
