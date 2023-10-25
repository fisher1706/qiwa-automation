import allure
import pytest
from selene import browser

from data.constants import EmployeeTransfer, Language
from data.dedicated.employee_trasfer.employee_transfer import (
    current_sponsor,
    employer_old,
    laborer,
)
from data.dedicated.enums import TransferType
from data.validation_message import ErrorMessage, SuccessMessage
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.individual_actions import IndividualActions
from src.ui.actions.old_contract_management import OldContractManagementActions
from src.ui.actions.old_employee_transfer import EmployeeTransferActionsOld
from src.ui.components.footer import Footer
from src.ui.qiwa import qiwa


@allure.feature('Employee Transfer sheet 1')
@pytest.mark.skip("Old design")
class TestEmployeeTransferSheet1:  # pylint: disable=unused-argument, duplicate-code

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.employee_transfer_actions = EmployeeTransferActionsOld()
        self.contract_management_actions = OldContractManagementActions()
        self.individual_actions = IndividualActions()
        self.footer = Footer()

    @pytest.fixture()
    def prepare_laborer_for_et_request(self, http_client):
        self.employee_transfer_api = EmployeeTransferApi(http_client)
        self.employee_transfer_api.post_prepare_laborer_for_et_request()

    @pytest.fixture()
    def create_contract(self, http_client):
        self.employee_transfer_api = EmployeeTransferApi(http_client)
        self.employee_transfer_api.post_prepare_laborer_for_et_request()
        self.employee_transfer_api.post_create_new_contract()
        self.employee_transfer_actions.confirm_creation_of_contract(laborer)

    @pytest.fixture()
    def create_contract_with_quota(self, http_client):
        self.employee_transfer_api = EmployeeTransferApi(http_client)
        self.employee_transfer_api.post_prepare_laborer_for_et_request()
        self.employee_transfer_api.post_create_new_contract()
        self.employee_transfer_actions.confirm_creation_of_contract(laborer, is_get_balance_value=True)

    @allure.title('Redirection from ET service to CM service in case no contract were created for the Laborer before')
    def test_navigate_to_redirection_popup(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.request_new_contract(transfer_type=TransferType.FROM_ANOTHER_BUSINESS_OWNER,
                                                            establishment_number=employer_old.establishment_number,
                                                            entity_laborer=laborer)
        self.employee_transfer_actions.click_btn_next()
        self.employee_transfer_actions.click_btn_create_contract()
        self.employee_transfer_actions.verify_redirections_popup()

    @allure.title('Verify Current Sponsor is able to approve the ET request')
    def test_current_sponsor_able_to_approve_et_request(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(current_sponsor)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.click_btn_accept()
        self.employee_transfer_actions.click_btn_accept_request()
        self.employee_transfer_actions.fill_verification_code()
        self.employee_transfer_actions.click_btn_verify()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_SPONSOR_REQUEST)

    @allure.title('Request status changes after Current Sponsor approval')
    def test_request_status_changes_after_current_sponsor_approval(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(current_sponsor)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.click_btn_accept()
        self.employee_transfer_actions.click_btn_accept_request()
        self.employee_transfer_actions.fill_verification_code()
        self.employee_transfer_actions.click_btn_verify()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_APPROVE, Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_APPROVE, Language.AR)

    @allure.title('Verify Current Sponsor is able to reject the ET request')
    def test_current_sponsor_able_to_reject_et_request(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(current_sponsor)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.click_btn_reject()
        self.employee_transfer_actions.fill_field_rejection_reason()
        self.employee_transfer_actions.click_btn_reject_request()
        self.employee_transfer_actions.verify_message(ErrorMessage.ET_SPONSOR_REQUEST)

    @allure.title('Request status changes after Current Sponsor rejection')
    def test_request_status_changes_after_current_sponsor_rejected(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(current_sponsor)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.click_btn_reject()
        self.employee_transfer_actions.fill_field_rejection_reason()
        self.employee_transfer_actions.click_btn_reject_request()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_REJECT, Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_REJECT, Language.AR)

    @allure.title('Quota (Establishment Balance) Should be decreased after submitting ET request')
    def test_quota_should_be_decreased_after_submitting_et_request(self, create_contract_with_quota):
        self.employee_transfer_actions.navigate_to_employee_transfer_by_link()
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value()

    @allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
    def test_quota_should_be_increased_after_rejection_of_et_request_by_laborer(self, create_contract_with_quota):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(ErrorMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value(is_decreased=False)

    @allure.title('Quota (Establishment Balance) increased after rejection of ET request by current sponsor')
    def test_quota_should_be_increased_after_rejection_of_et_request_current_sponsor(self, create_contract_with_quota):
        self.employee_transfer_actions.navigate_to_individual(laborer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_et_service(current_sponsor)
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.click_btn_reject()
        self.employee_transfer_actions.fill_field_rejection_reason()
        self.employee_transfer_actions.click_btn_reject_request()
        self.employee_transfer_actions.verify_message(ErrorMessage.ET_SPONSOR_REQUEST)
        qiwa.header.click_on_menu().click_on_logout()
        browser.close_current_tab()
        browser.switch_to_tab(0)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value(is_decreased=False)
