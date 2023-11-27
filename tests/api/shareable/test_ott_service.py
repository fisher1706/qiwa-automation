import time
from http import HTTPStatus

from src.api.clients.ott_service import OttServiceApi
from src.api.models.qiwa.raw.ott_service import GenerateToken, ValidateToken
from utils.assertion import assert_status_code, assert_that


def test_token_generation_and_validation():
    ott_service = OttServiceApi()
    sequence_number = time.time_ns()

    generate = ott_service.generate_token(sequence_number=sequence_number)
    assert_status_code(generate.status_code).equals_to(HTTPStatus.OK)
    token = GenerateToken.parse_obj(generate.json())

    validate_ott = ott_service.validate_token(token.ott)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.OK)

    token_data = ValidateToken.parse_obj(validate_ott.json())
    assert_that(token_data.payload).has(sequence_number=sequence_number)


def test_token_revalidation():
    ott_service = OttServiceApi()
    generate_ott = ott_service.generate_token(sequence_number="#@987654321", labor_office_id=2)
    assert_status_code(generate_ott.status_code).equals_to(HTTPStatus.OK)

    token = GenerateToken.parse_obj(generate_ott.json())
    validate_ott = ott_service.validate_token(token.ott)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.OK)

    re_validate_ott = ott_service.validate_token(token.ott)
    assert_status_code(re_validate_ott.status_code).equals_to(HTTPStatus.NOT_FOUND)

    token = GenerateToken.parse_obj(re_validate_ott.json())
    assert_that(token).has(ott="not_found")


def test_token_validation_without_generation():
    ott_service = OttServiceApi()
    invalid_token = time.time_ns()

    validate_ott = ott_service.validate_token(invalid_token)
    assert_status_code(validate_ott.status_code).equals_to(HTTPStatus.NOT_FOUND)

    token = GenerateToken.parse_obj(validate_ott.json())
    assert_that(token).has(ott="not_found")
