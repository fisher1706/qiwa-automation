from __future__ import annotations

from data.dedicated.employee_trasfer.employee_transfer_constants import REJECT_REASON
from src.ui.pages.individual_page import IndividualPage


class IndividualActions(IndividualPage):
    def approve_request(self) -> IndividualActions:
        self.click_btn_accept_the_request()
        self.click_btn_modal_accept_the_request()
        return self

    def reject_request(self, reason: str = REJECT_REASON) -> IndividualActions:
        self.click_btn_reject_the_request()
        self.select_rejection_reason(reason)
        self.click_btn_modal_reject_the_request()
        return self

    def proceed_steps_for_verifying_et_request(self) -> IndividualActions:
        return self
