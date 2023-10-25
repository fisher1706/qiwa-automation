from data.delegation import general_data
from src.api.clients.delegation import DelegationAPI
from utils.assertion import assert_that


class DelegationApiController(DelegationAPI):
    def get_otp_code(self, headers: dict, request_id: str):
        self.check_delegation_request_status(headers=headers, request_id=request_id)
        self.set_delegation_request_otp_code(headers=headers, request_id=request_id)

    def reject_delegation_request(self, headers: dict, request_id: str):
        self.get_delegation_request_details(headers=headers, request_id=request_id)
        request_change = self.reject_delegation_request_status(
            headers=headers, request_id=request_id
        )
        assert_that(request_change["status"]).equals_to(general_data.REJECTED)
