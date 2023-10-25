from __future__ import annotations

from data.constants import Language
from data.dedicated.models.user import User
from src.ui.qiwa import qiwa


class EmployeeTransferActions:
    def navigate_to_et_service(self, user: User) -> EmployeeTransferActions:
        qiwa.login_as_user(user.personal_number)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.check_personal_number_or_name(user.name).change_local(Language.EN)
        qiwa.workspace_page.select_company_account_with_sequence_number(user.sequence_number)

        qiwa.dashboard_page.wait_dashboard_page_to_load()
        qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
        qiwa.open_e_services_page()
        qiwa.e_services_page.select_employee_transfer()
        return self
