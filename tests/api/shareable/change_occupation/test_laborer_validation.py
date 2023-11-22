from http import HTTPStatus

from src.api.models.qiwa.change_occupation import MultiLangErrorsData
from utils.assertion import assert_status_code, assert_that


def test_validation_for_laborer_registered_in_portal(change_occupation, laborer):
    response = change_occupation.api.validate_laborer(laborer.personal_number, laborer.occupation_code)
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
    assert_that(response.json()).has(valid=True)


def test_validation_for_laborer_not_registered_in_portal(change_occupation, laborer2):
    response = change_occupation.api.validate_laborer(
        laborer2.personal_number,
        laborer2.occupation_code
    )
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = MultiLangErrorsData.parse_obj(response.json())
    assert_that(json.data).size_is(1)

    error = json.data[0]
    assert_that(error).has(id="WARNING")
    assert_that(error.attributes).has(code="WARNING")


def test_validation_laborer_not_eligible(change_occupation):
    not_eligible_user = change_occupation.get_random_user(eligible=False)

    response = change_occupation.api.validate_laborer(not_eligible_user.personal_number, occupation_code=216101)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_for_laborer_with_request(change_occupation, laborer):
    change_occupation.create_request(laborer)
    response = change_occupation.api.validate_laborer(laborer.personal_number, laborer.occupation_code)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_with_non_existent_personal_number(change_occupation):
    response = change_occupation.api.validate_laborer(personal_number=12341512312, occupation_code=712501)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()


def test_validation_with_non_existent_occupation_code(change_occupation, laborer):
    response = change_occupation.api.validate_laborer(laborer.personal_number, occupation_code=11111)
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
