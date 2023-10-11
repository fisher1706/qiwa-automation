from selene import have
from selene.support.shared.jquery_style import s

from data.dedicated.enums import EmployeeTransferSuccessMsg
from src.ui.components.raw.table import Table


class SummaryPage:
    success_msg = s('[role="banner"] + div')
    table = Table()

    def check_success_msg(self):
        self.success_msg.should(have.exact_text(EmployeeTransferSuccessMsg.SUMMARY.value))

    def check_request_status(self):
        self.table.cell(row=2, column=1).should(have.exact_text(""))
