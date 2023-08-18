from data.constants import EmployeeTransfer, Language
from data.enums import ServicesAndTools
from src.ui.pages.individual_page import IndividualPage


class IndividualActions(IndividualPage):
    def approve_request(self):
        self.click_btn_accept_the_request()
        self.click_btn_modal_accept_the_request()

    def reject_request(self, reason: str = EmployeeTransfer.REJECT_REASON):
        self.click_btn_reject_the_request()
        self.select_rejection_reason(reason)
        self.click_btn_modal_reject_the_request()

    def proceed_steps_for_verifying_et_request(self):
        self.change_locale(Language.EN)
        self.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value)
        self.proceed_2fa()
        self.select_first_view_request()
        self.click_agree_checkbox()
