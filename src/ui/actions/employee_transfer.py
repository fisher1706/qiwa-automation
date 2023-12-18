from __future__ import annotations

from data.constants import Language, UserInfo
from data.dedicated.enums import RequestStatus
from data.dedicated.models.laborer import Laborer
from data.dedicated.models.user import User
from src.ui.actions.contract_management import contract_management_actions
from src.ui.qiwa import qiwa
from utils.allure import allure_steps


@allure_steps
class EmployeeTransferActions:
    def navigate_to_et_service(self, user: User) -> EmployeeTransferActions:
        qiwa.login_as_user(user.personal_number)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.change_local(Language.EN)
        qiwa.workspace_page.select_company_account_with_sequence_number(user.sequence_number)

        qiwa.dashboard_page.wait_dashboard_page_to_load()
        qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
        qiwa.open_e_services_page()
        qiwa.e_services_page.select_employee_transfer()
        return self

    def navigate_to_et_service_current_sponsor(self, user: User) -> EmployeeTransferActions:
        qiwa.login_as_user(user.personal_number)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.change_local(Language.EN)
        qiwa.workspace_page.select_company_account_by_name(user.establishment_name_ar)

        qiwa.dashboard_page.wait_dashboard_page_to_load()
        qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
        qiwa.open_e_services_page()
        qiwa.e_services_page.select_employee_transfer()
        return self

    def navigate_to_individual(self, user_id: int) -> EmployeeTransferActions:
        qiwa.login_as_user(user_id, UserInfo.PASSWORD)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.change_local(Language.EN)
        qiwa.workspace_page.select_individual_account()
        return self

    def create_et_request_from_another_establishment(
        self, laborer: Laborer
    ) -> EmployeeTransferActions:
        (
            qiwa.employee_transfer_page.click_btn_transfer_employee()
            .select_another_establishment()
            .click_btn_next_step()
            .fill_employee_iqama_number(laborer.personal_number)
            .fill_date_of_birth(laborer.birthdate)
            .click_btn_find_employee()
            .click_btn_add_employee_to_transfer_request()
            .click_btn_next_step()
            .click_link_create_contract_another_establishment()
            .click_btn_proceed_to_contract_management()
        )

        qiwa.code_verification.fill_in_code().click_confirm_button()

        contract_management_actions.create_contract(laborer)

        (
            qiwa.employee_transfer_page.check_existence_of_a_contract()
            .click_btn_next_step()
            .select_terms_checkbox()
            .click_btn_submit_request()
            .check_success_msg()
            .check_request_status()
        )
        return self

    def create_et_request_between_my_establishment(
        self, laborer: Laborer
    ) -> EmployeeTransferActions:
        (
            qiwa.employee_transfer_page.click_btn_transfer_employee()
            .select_own_establishment()
            .click_btn_next_step()
            .search_by_iqama_number(laborer.personal_number)
            .select_first_employee(laborer.personal_number)
            .click_btn_next_step()
            .click_link_create_contract()
            .click_btn_proceed_to_contract_management()
        )
        qiwa.code_verification.fill_in_code().click_confirm_button()

        contract_management_actions.create_contract(laborer)

        (
            qiwa.employee_transfer_page.check_existence_of_a_contract()
            .click_btn_next_step()
            .select_terms_checkbox()
            .click_btn_submit_request()
            .check_success_msg()
            .check_request_status()
        )
        return self

    def make_a_decision_as_current_sponsor(self, status: dict):
        if status == RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value:
            qiwa.employee_transfer_page.click_btn_accept().click_btn_accept_request()
            qiwa.code_verification.fill_in_code().click_confirm_button()
        else:
            qiwa.employee_transfer_page.click_btn_reject().fill_sponsor_rejection_reason().click_btn_reject_transfer()

        return self


employee_transfer_actions = EmployeeTransferActions()
