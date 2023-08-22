from http import HTTPStatus

from src.api import models
from src.api.app import QiwaApi
from src.api.assertions.model import validate_model
from src.api.controllers.ibm import IBMApiController
from src.api.models.ibm import payloads
from utils.assertion import assert_status_code, assert_that
from utils.crypto_manager import decrypt_saudization_certificate


def test_with_green_nitaq(green_nitaq_establishment):
    qiwa = QiwaApi.login_as_user(green_nitaq_establishment.personal_number).select_company()
    ibm = IBMApiController()

    response = qiwa.saudi_api.get_certificate_details()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    response_json = response.json()
    validated_response = validate_model(response_json, models.qiwa.saudi_certificate.encrypted_certificate)

    decrypted_certificate = decrypt_saudization_certificate(validated_response.data.attributes.certificate)
    validate_model(decrypted_certificate, models.qiwa.raw.certificate.SaudizationCertificate)

    payload = payloads.GetSaudiCertificateRq(
        LaborOfficeId=green_nitaq_establishment.labor_office_id,
        SequenceNumber=green_nitaq_establishment.sequence_number,
    )
    ibm_response = ibm.get_saudization_certificate_from_ibm(payload)
    qiwa.saudi_api_assertions.assert_certificate_values(decrypted_certificate, ibm_response)


def test_with_red_nitaq(red_nitaq_establishment):
    qiwa = QiwaApi.login_as_user(red_nitaq_establishment.personal_number).select_company()
    ibm = IBMApiController()

    qiwa_response = qiwa.saudi_api.get_certificate_details()
    assert_status_code(qiwa_response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    response_json = qiwa_response.json()
    validate_model(response_json, models.qiwa.saudi_certificate.certificate_error)

    payload = payloads.ValidEstSaudiCertificateRq(
        LaborOfficeId=red_nitaq_establishment.labor_office_id,
        SequenceNumber=red_nitaq_establishment.sequence_number,
    )
    ibm_response = ibm.validate_establishment_saudization_in_ibm(payload)
    qiwa.saudi_api_assertions.assert_error(response_json, ibm_response)


def test_no_certificate_found(no_certificate_establishment):
    qiwa = QiwaApi.login_as_user(no_certificate_establishment.personal_number).select_company()

    response = qiwa.saudi_api.get_certificate_details()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = response.json()
    validate_model(json, models.qiwa.saudi_certificate.certificate_not_found)
    assert_that(json["data"])\
        .has("id")("-1")\
        .has("type")("not_found")\
        .has("attributes")([])
