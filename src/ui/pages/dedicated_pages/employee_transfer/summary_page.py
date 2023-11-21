from __future__ import annotations

from selene import have
from selene.support.shared.jquery_style import s, ss

from data.dedicated.enums import EmployeeTransferSuccessMsg
from src.ui.components.raw.table import Table
from utils.allure import allure_steps


@allure_steps
class SummaryPage:
    success_msg = ss('[role="banner"] + div p').first
    table = Table()

    btn_back_to_employee_transfer = s("//button[.='Back to Employee Transfer']")

    def check_success_msg(self) -> SummaryPage:
        self.success_msg.should(have.text(EmployeeTransferSuccessMsg.SUMMARY.value))
        return self

    def check_request_status(self) -> SummaryPage:
        # TODO(dp): Move to test data status request
        self.table.cell(row=2, column=1).should(have.text("Pending employee’s approval"))
        return self

    def click_btn_back_to_employee_transfer(self) -> SummaryPage:
        self.btn_back_to_employee_transfer.click()
        return self
