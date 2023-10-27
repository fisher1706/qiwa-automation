from __future__ import annotations

import allure

from data.constants import Language, UserInfo
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.pages.dedicated_pages.employee_transfer.employee_transfer_page import (
    EmployeeTransferPage,
)
from src.ui.qiwa import qiwa


class EmployeeTransferActions(EmployeeTransferPage):
    @allure.step
    def navigate_to_et_service(self, user: User) -> EmployeeTransferActions:
        qiwa.login_as_user(user.personal_number)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.check_personal_number_or_name(user.name)
        qiwa.workspace_page.select_company_account_with_sequence_number(user.sequence_number)

        qiwa.dashboard_page.wait_dashboard_page_to_load()
        qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
        qiwa.open_e_services_page()
        qiwa.e_services_page.select_employee_transfer()
        return self

    @allure.step
    def navigate_to_individual(self, user_id: int) -> EmployeeTransferActions:
        qiwa.header.click_on_menu().click_on_logout()
        qiwa.login_page.wait_login_page_to_load()
        qiwa.header.change_local(Language.EN)
        qiwa.login_as_user(user_id, UserInfo.PASSWORD)
        qiwa.header.check_personal_number_or_name(str(user_id)).change_local(Language.EN)
        qiwa.workspace_page.select_individual_account()
        return self

    @allure.step
    def create_et_request_from_another_establishment(
        self, laborer: Laborer
    ) -> EmployeeTransferActions:
        (
            qiwa.employee_transfer_page.click_btn_transfer_employee()
            .select_another_establishment()
            .click_btn_next_step()
            .fill_employee_iqama_number(laborer.login_id)
            .fill_date_of_birth(laborer.birthdate)
            .click_btn_find_employee()
            .click_btn_add_employee_to_transfer_request()
            .click_link_create_contract_another_establishment()
            .click_btn_proceed_to_contract_management()
        )

        qiwa.code_verification.fill_in_code().click_confirm_button()

        contract_management_actions = ContractManagementActions()
        (
            contract_management_actions.click_btn_next_step()
            .fill_establishment_details()
            .click_btn_next_step()
            .fill_employee_details()
            .click_btn_next_step()
            .fill_contract_details(laborer.transfer_type)
            .click_btn_next_step()
            .select_terms_checkbox()
            .click_btn_next_step()
        )

        qiwa.employee_transfer_page.click_btn_next_step().select_terms_checkbox().click_btn_submit()

        qiwa.employee_transfer_page.check_success_msg().check_request_status()
        return self
