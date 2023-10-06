import allure

from data.shareable.expected import work_permits
from src.api.assertions.diff import assert_difference
from src.api.clients.work_permit import WorkPermitApi
from src.api.models.ibm.getworkpermitrequests import (
    IBMWorkPermitRequest,
    IBMWorkPermitRequestList,
)
from src.api.models.qiwa import work_permit as work_permit_models
from utils.assertion import assert_that


class WorkPermitApiAssertions(WorkPermitApi):
    @allure.step
    def assert_total_count(self, json: dict, expected_count: int) -> "WorkPermitApiAssertions":
        assert_that(json["meta"]).has("total_count")(expected_count)
        return self

    @allure.step
    def assert_items_count(self, json: dict, expected_count: int) -> "WorkPermitApiAssertions":
        assert_that(json["data"]).as_("data size").is_length(expected_count)
        return self

    @allure.step
    def assert_data_count(self, response: dict, expected: IBMWorkPermitRequestList):
        assert_that(response["meta"]).has("total_count")(int(expected.TotalCount))
        assert_that(response["data"]).as_("data").is_length(len(expected.WorkPermitRequests))

    @allure.step
    def assert_transaction(self, response: dict, expected: IBMWorkPermitRequest):
        assert_that(response).has("type")("work-permit-request")
        (
            assert_that(response["attributes"])
            .has("status")(expected.Status)
            .has("bill-number")(expected.BillNumber)
            .has("bill-status")(expected.BillStatus)
            .has("number-of-expats")(expected.NumberOfExpats)
            .has("remaining-days")(expected.RemainingDays)
            .has("submit-date")(str(expected.SubmitDate))
        )
        # TODO: assert transaction-fees (randomly generated in mock-mlsd for every request)

    @allure.step
    def assert_transactions(self, response: dict, expected: IBMWorkPermitRequestList):
        self.assert_data_count(response, expected)

        for item in expected.WorkPermitRequests:
            target = [
                d for d in response["data"] if d["attributes"]["bill-number"] == item.BillNumber
            ]
            try:
                actual: dict = target[0]
            except IndexError as error:
                print(f'{item.BillNumber} not in {response["data"]}')
                raise error
            self.assert_transaction(actual, item)


def assert_cancel_sadad_ibm_error(response_json: dict) -> None:
    model = work_permit_models.cancel_sadad_ibm_error.parse_obj(response_json)
    expected = work_permits.cancel_sadad_number.transaction_already_canceled()
    actual = model.data.attributes.dict(include=set(expected.keys()))
    assert_difference(expected, actual)
