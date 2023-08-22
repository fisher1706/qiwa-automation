import allure

from src.api import models
from utils.assertion import assert_that


@allure.step
def assert_change_occupation_request(
    actual: models.qiwa.data.request,
    expected: src.api.models.ibm.searchchangeoccupation.ChangeOccupationItem,
) -> None:
    assert_that(actual.id).as_("id").equals_to(expected.RequestInformation.RequestId)
    assert_that(actual.type).as_("type").equals_to("request")
    assert_request_attributes(actual.attributes, expected)
    assert_request_laborer(actual.attributes.laborers[0], expected)


@allure.step
def assert_request_attributes(
    actual: models.qiwa.raw.change_occupation.Request,
    expected: src.api.models.ibm.searchchangeoccupation.ChangeOccupationItem,
) -> None:
    assert_that(actual.request_id).as_("request-id").equals_to(
        expected.RequestInformation.RequestId
    )
    assert_that(actual.type_id).as_("type-id").equals_to(expected.RequestInformation.RequestTypeId)
    assert_that(actual.type_name).as_("type-name").equals_to(
        expected.RequestInformation.RequestTypeEn
    )
    assert_that(actual.date).as_("date").equals_to(
        expected.RequestInformation.RequestDate.strftime("%Y-%m-%dT%H:%M:%S.%f").strip("0")
    )
    assert_that(actual.labor_office_id).as_("labor-office-id").equals_to(
        expected.EstablishmentDetails.LaborOfficeId
    )
    assert_that(actual.sequence_number).as_("sequance-number").equals_to(
        expected.EstablishmentDetails.SequenceNumber
    )
    assert_that(actual.establishment_id).as_("establishment-id").equals_to(
        expected.EstablishmentDetails.EstablishmentId
    )
    assert_that(actual.requester_personal_number).as_("requester-personal-number").equals_to(
        expected.RequesterDetails.IdNo
    )
    assert_that(actual.requester_id).as_("requester-id").equals_to(
        expected.RequesterDetails.UserId
    )
    assert_that(actual.request_type).as_("request-type").equals_to(
        expected.RequestInformation.RequestTypeId
    )
    assert_that(actual.id).as_("id").equals_to(expected.RequestInformation.RequestId)


@allure.step
def assert_request_laborer(
    actual: models.qiwa.raw.change_occupation.Laborer,
    expected: src.api.models.ibm.searchchangeoccupation.ChangeOccupationItem,
) -> None:
    details = expected.RequestDetailsList.RequestDetailsItem[0]
    assert_that(actual.status_id).as_("status_id").equals_to(details.StatusDetails.StatusId)
    assert_that(actual.status_name).as_("status_name").equals_to(details.StatusDetails.StatusEn)
    assert_that(actual.current_occupation_id).as_("current_occupation_id").equals_to(
        details.CurrentOccupationDetails.CurrentOccupationId
    )
    assert_that(actual.current_occupation_name).as_("current_occupation_name").equals_to(
        details.CurrentOccupationDetails.CurrentOccupationEn
    )
    assert_that(actual.new_occupation_id).as_("new_occupation_id").equals_to(
        details.NewOccupationDetails.NewOccupationId
    )
    assert_that(actual.new_occupation_name).as_("new_occupation_name").equals_to(
        details.NewOccupationDetails.NewOccupationEn
    )
    assert_that(actual.nationality_code).as_("nationality_code").equals_to(
        details.Nationality.Code
    )
    assert_that(actual.nationality_name).as_("nationality_name").equals_to(
        details.Nationality.Name
    )
    assert_that(actual.rejection_description).as_("rejection_description").equals_to(
        details.RejectionDescription
    )
    assert_that(actual.labor_office_id).as_("labor_office_id").equals_to(details.LaborOfficeId)
    assert_that(actual.employee_personal_number).as_("employee_personal_number").equals_to(
        details.LaborerIdNo
    )
    assert_that(actual.employee_name).as_("employee_name").equals_to(details.LaborerName)
    assert_that(actual.request_sequence).as_("request_sequence").equals_to(
        details.RequestDetails.RequestSequence
    )
    assert_that(actual.request_year).as_("request_year").equals_to(
        details.RequestDetails.RequestYear
    )
    assert_that(actual.request_number).as_("request_number").equals_to(
        f"{details.LaborOfficeId}-{details.RequestDetails.RequestSequence}-{details.RequestDetails.RequestYear}"
    )
    assert_that(actual.bulk_id).as_("bulk_id").equals_to(expected.RequestInformation.RequestId)
    assert_that(actual.id).as_("id").equals_to(
        f"{expected.RequestInformation.RequestId}-{details.LaborerIdNo}"
    )
