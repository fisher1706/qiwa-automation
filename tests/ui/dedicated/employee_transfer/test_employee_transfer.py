import allure
import pytest as pytest

from data.constants import ContractManagement, Language
from data.dedicated.employee_transfer import employer, laborer
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.contract_management import ContractManagementActions
from src.ui.qiwa import qiwa


@pytest.fixture(autouse=True)
def prepare_laborer_for_et_request():
    employee_transfer_api = EmployeeTransferApi()
    employee_transfer_api.post_prepare_laborer_for_et_request()


@allure.title('Verify user able to submit ET request')
@pytest.skip('Need to debug and add extra verifications')
def test_user_able_to_submit_et_request_from_my_own_establishment():
    qiwa.login_as_user(employer.personal_number)
    qiwa.workspace_page.wait_page_to_load()
    qiwa.header.check_personal_number_or_name(employer.name)\
        .change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(employer.sequence_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.open_e_services_page()
    qiwa.e_services_page.select_employee_transfer()

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_own_establishment() \
        .click_btn_next_step() \
        .search_by_iqama_number("2136118060") \
        .select_first_employee() \
        .click_btn_next_step() \
        .click_link_create_contract_own_establishment() \
        .click_btn_proceed_to_contract_management()

    qiwa.employee_transfer_page.click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit_request()


@allure.title('Verify user able to submit ET request from another establishment')
def test_user_able_to_submit_et_request_from_another_establishment():
    qiwa.login_as_user(employer.personal_number)
    qiwa.workspace_page.wait_page_to_load()
    qiwa.header.check_personal_number_or_name(employer.name)\
        .change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(employer.sequence_number)

    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.open_e_services_page()
    qiwa.e_services_page.select_employee_transfer()

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee()\
        .click_btn_add_employee_to_transfer_request()\
        .click_link_create_contract_another_establishment()\
        .click_btn_proceed_to_contract_management()

    qiwa.contract_management_page.wait_until_title_verification_code_appears(
        ContractManagement.MOBILE_VERIFICATION, Language.EN
    )\
        .proceed_2fa()\
        .click_btn_verify()

    contract_management_actions = ContractManagementActions()
    contract_management_actions.click_btn_next_step()\
        .fill_establishment_details(laborer.user_type)\
        .click_btn_next_step()\
        .fill_employee_details()\
        .click_btn_next_step()\
        .fill_contract_details(laborer.user_type)\
        .click_btn_next_step()\
        .select_terms_checkbox()\
        .click_btn_next_step()

    qiwa.employee_transfer_page.click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit()

    qiwa.employee_transfer_page.check_success_msg()\
        .check_request_status()
