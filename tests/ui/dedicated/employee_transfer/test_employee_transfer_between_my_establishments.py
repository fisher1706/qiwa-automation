import allure

from data.dedicated.employee_trasfer.employee_transfer import (
    employer,
    laborer_between_my_establishments,
    laborer_between_my_establishments_existing_contract,
)
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.actions.employee_transfer import EmployeeTransferActions
from src.ui.qiwa import qiwa


@allure.title('Verify user able to submit ET request from my own establishment')
def test_user_able_to_submit_et_request_from_my_own_establishment():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_own_establishment() \
        .click_btn_next_step() \
        .search_by_iqama_number(laborer_between_my_establishments.login_id) \
        .select_first_employee(laborer_between_my_establishments.login_id) \
        .click_btn_next_step() \
        .click_link_create_contract() \
        .click_btn_proceed_to_contract_management()

    qiwa.code_verification.fill_in_code().click_confirm_button()

    contract_management_actions = ContractManagementActions()
    contract_management_actions.click_btn_next_step() \
        .fill_establishment_details() \
        .click_btn_next_step() \
        .fill_employee_details() \
        .click_btn_next_step() \
        .fill_contract_details(laborer_between_my_establishments.transfer_type) \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_next_step()

    qiwa.employee_transfer_page.click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit_request()

    qiwa.employee_transfer_page.check_success_msg() \
        .check_request_status()


@allure.title("If laborer already has a contract, don't show redirection to CM button from my own establishment")
def test_if_laborer_already_has_a_contract_do_not_show_redirection_to_cm_button_from_my_own_establishment():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_own_establishment() \
        .click_btn_next_step() \
        .search_by_iqama_number(laborer_between_my_establishments_existing_contract.login_id) \
        .select_first_employee(laborer_between_my_establishments_existing_contract.login_id) \
        .click_btn_next_step() \
        .check_existence_of_a_contract()
