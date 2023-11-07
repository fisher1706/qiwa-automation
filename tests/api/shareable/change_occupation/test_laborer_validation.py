from http import HTTPStatus

from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_status_code, assert_that


def test_successful_validation_without_warning(change_occupation, laborer):
    response = change_occupation.api.validate_laborer(laborer.personal_number, laborer.occupation_code)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_that(response.json()).has(valid=True)


def test_successful_validation_with_warning(change_occupation):
    response = change_occupation.api.validate_laborer(personal_number=2037659303, occupation_code=712501)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = MultiLangErrorsData.parse_obj(response.json())
    assert_that(json.data).size_is(1)

    error = json.data[0]
    assert_that(error).has(id="WARNING")
    assert_that(error.attributes).has(code="WARNING")


def test_unsuccessful_validation(change_occupation, laborer):
    response = change_occupation.api.validate_laborer(laborer.personal_number, occupation_code=213201)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_for_employee_with_request(change_occupation, laborer):
    change_occupation.create_request(laborer)
    response = change_occupation.api.validate_laborer(laborer.personal_number, laborer.occupation_code)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_for_non_existent_laborer(change_occupation):
    response = change_occupation.api.validate_laborer(personal_number=12341512312, occupation_code=712501)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_for_non_existent_occupation(change_occupation, laborer):
    response = change_occupation.api.validate_laborer(laborer.personal_number, occupation_code=11111)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
