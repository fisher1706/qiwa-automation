import allure
import pytest

from data.constants import ContractManagement, Language
from data.dedicated.employee_trasfer.employee_transfer import (
    employer,
    laborer,
    laborer_between_my_establishments, laborer_between_my_establishments_existing_contract,
)
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.actions.employee_transfer import EmployeeTransferActions
from src.ui.qiwa import qiwa


@allure.title('Verify user able to submit ET request')
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

    qiwa.contract_management_page.wait_until_title_verification_code_appears(
        ContractManagement.MOBILE_VERIFICATION, Language.EN
    ) \
        .proceed_2fa() \
        .click_btn_verify()

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
        .click_btn_submit()

    qiwa.employee_transfer_page.check_success_msg() \
        .check_request_status()


@allure.title('Verify user able to submit ET request from another establishment')
def test_user_able_to_submit_et_request_from_another_establishment():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request() \
        .click_link_create_contract_another_establishment() \
        .click_btn_proceed_to_contract_management()

    qiwa.contract_management_page.wait_until_title_verification_code_appears(
        ContractManagement.MOBILE_VERIFICATION, Language.EN
    ) \
        .proceed_2fa() \
        .click_btn_verify()

    contract_management_actions = ContractManagementActions()
    contract_management_actions.click_btn_next_step() \
        .fill_establishment_details() \
        .click_btn_next_step() \
        .fill_employee_details() \
        .click_btn_next_step() \
        .fill_contract_details(laborer.transfer_type) \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_next_step()

    qiwa.employee_transfer_page.click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit()

    qiwa.employee_transfer_page.check_success_msg() \
        .check_request_status()


@allure.title('Verify Sent Employee Transfer Requests are shown in Home Page of ET Service')
def test_sent_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.check_count_of_sent_request_rows()


@allure.title('Verify Received Employee Transfer Requests are shown in Home Page of ET Service')
def test_received_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.check_count_of_received_request_rows()


@allure.title("If laborer already has a contract, don't show redirection to CM button another establishment")
@pytest.mark.skip("Find user with contract")
def test_if_laborer_already_has_a_contract_do_not_show_redirection_to_cm_button_another_establishment():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request()\
        .check_existence_of_a_contract()


@allure.title("If laborer already has a contract, don't show redirection to CM button from my own establishment")
def test_if_laborer_already_has_a_contract_do_not_show_redirection_to_cm_button_from_my_own_establishment():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_own_establishment() \
        .click_btn_next_step() \
        .search_by_iqama_number(laborer_between_my_establishments_existing_contract.login_id) \
        .select_first_employee(laborer_between_my_establishments_existing_contract.login_id) \
        .click_btn_next_step()\
        .check_existence_of_a_contract()
