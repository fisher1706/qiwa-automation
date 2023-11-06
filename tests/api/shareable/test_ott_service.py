import time
from http import HTTPStatus

from src.api.clients.ott_service import OttServiceApi
from src.api.models.qiwa.raw.ott_service import GenerateToken, ValidateToken
from utils.assertion import assert_status_code, assert_that


def test_token_generation_and_validation():
    ott_service = OttServiceApi()
    data = {"sequence-number": time.time_ns()}

    generate_ott = ott_service.generate_token(data)
    assert_status_code(generate_ott.status_code).equals_to(HTTPStatus.OK)

    token = generate_ott.json()
    GenerateToken.parse_obj(token)
    validate_ott = ott_service.validate_token(token)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.OK)

    token_data = validate_ott.json()
    ValidateToken.parse_obj(token_data)
    assert_that("sequence-numberr").as_("sequence-numberr").in_(list(token_data["payload"].keys()))
    assert_that(token_data["payload"]).has(**{"sequence-number": data["sequence-number"]})


def test_token_revalidation():
    ott_service = OttServiceApi()
    data = {
        "labor-office-id": 2,
        "sequence-number": "#@987654321",
    }
    generate_ott = ott_service.generate_token(data)
    assert_status_code(generate_ott.status_code).equals_to(HTTPStatus.OK)

    token = generate_ott.json()
    validate_ott = ott_service.validate_token(token)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.OK)

    re_validate_ott = ott_service.validate_token(token)
    assert_status_code(re_validate_ott.status_code).equals_to(HTTPStatus.NOT_FOUND)

    token = re_validate_ott.json()
    GenerateToken.parse_obj(token)
    assert_that(token).has(ott="not_found")


def test_token_validation_without_generation():
    ott_service = OttServiceApi()
    invalid_token = {"ott": time.time_ns()}

    validate_ott = ott_service.validate_token(invalid_token)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.NOT_FOUND)

    token = validate_ott.json()
    GenerateToken.parse_obj(token)
    assert_that(token).has(ott="not_found")
