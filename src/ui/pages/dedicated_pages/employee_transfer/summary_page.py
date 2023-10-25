from __future__ import annotations

from selene import have
from selene.support.shared.jquery_style import ss

from data.dedicated.enums import EmployeeTransferSuccessMsg
from src.ui.components.raw.table import Table


class SummaryPage:
    success_msg = ss('[role="banner"] + div p').first
    table = Table()

    def check_success_msg(self) -> SummaryPage:
        self.success_msg.should(have.text(EmployeeTransferSuccessMsg.SUMMARY.value))
        return self

    def check_request_status(self) -> SummaryPage:
        # todo: [dp] Move to test data status request
        self.table.cell(row=2, column=1).should(have.text("Pending employee’s approval"))
        return self
