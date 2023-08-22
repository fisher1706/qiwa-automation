import allure

from src.api.clients.wp_api import WorkPermitApi
from src.api.models.mock_mlsd.ibm.getworkpermitrequests import (
    IBMWorkPermitRequest,
    IBMWorkPermitRequestList,
)
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
