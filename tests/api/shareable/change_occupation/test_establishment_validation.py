from http import HTTPStatus

from src.api.controllers.change_occupation import ChangeOccupationController
from src.api.models.qiwa.change_occupation import (
    EstablishmentValidationData,
    MultiLangErrorsData,
)
from utils.assertion import assert_status_code, assert_that


def test_successful_validation(change_occupation):
    response = change_occupation.api.validate_establishment()
    assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    json = EstablishmentValidationData.parse_obj(response.json())
    assert_that(json.data.attributes).has(valid=True)


def test_unsuccessful_validation():
    change_occupation = ChangeOccupationController.pass_ott_authorization(
        office_id="1", sequence_number="115892"
    )
    response = change_occupation.api.validate_establishment()
    assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    json = MultiLangErrorsData.parse_obj(response.json())
    error = json.data[0]
    assert_that(error.attributes.en_EN.details).is_not_empty()
    assert_that(error.attributes.ar_SA.details).is_not_empty()
