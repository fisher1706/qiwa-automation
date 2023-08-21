from http import HTTPStatus

import pytest

from utils.assertion import assert_status_code
from src.api import models
from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from src.api.clients.ibm_mock_api import IBMMockApi
from src.api.models.mock_mlsd.ibm import payloads

pytestmark = [pytest.mark.saudization_suite, pytest.mark.daily, pytest.mark.api, pytest.mark.ss, pytest.mark.wp]


def test_extending_certificate(create_green_nitaq_establishment):
    qiwa = QiwaApi.login_as_user(create_green_nitaq_establishment.account.personal_number).select_company()
    ibm = IBMMockApi()
    
    qiwa.saudi_api.create_certificate()
    response = qiwa.saudi_api.extend_certificate()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = response.json()
    validate_model(response_json, models.qiwa.saudi_certificate.certificate)

    payload = payloads.GetSaudiCertificateRq(
        LaborOfficeId=qiwa.authorization_token.company_labor_office_id,
        SequenceNumber=qiwa.authorization_token.company_sequence_number,
    )
    extended_certificate = ibm.get_saudization_certificate_from_ibm(payload)
    qiwa.saudi_api_assertions.assert_extended_certificate_values(response_json, extended_certificate)

    second_extend = qiwa.saudi_api.extend_certificate()
    assert_status_code(second_extend.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)
    validate_model(second_extend.json(), models.qiwa.saudi_certificate.certificate_error)

