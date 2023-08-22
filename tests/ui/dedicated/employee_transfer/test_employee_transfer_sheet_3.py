import allure
import pytest
from selene import browser

from data.constants import EmployeeTransfer, Language
from data.dedicated.employee_transfer import (
    employer,
    employer_between_my_establishments,
    laborer_between_my_establishments,
)
from data.dedicated.enums import TransferType
from data.validation_message import ErrorMessage, SuccessMessage
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.employee_transfer import EmployeeTransferActions
from src.ui.actions.individual_actions import IndividualActions
from src.ui.actions.sign_in import LoginActions


@allure.feature('Employee Transfer sheet 3')
@pytest.mark.usefixtures("go_to_auth_page")
class TestEmployeeTransferSheet3:  # pylint: disable=unused-argument

    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.employee_transfer_actions = EmployeeTransferActions()
        self.login_action = LoginActions()
        self.individual_actions = IndividualActions()
        self.employee_transfer_api = EmployeeTransferApi(http_client)
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_between_my_establishments.login_id)

    @pytest.fixture()
    def create_contract(self, http_client):
        self.employee_transfer_actions.confirm_creation_of_contract(entity_laborer=laborer_between_my_establishments,
                                                                    transfer_type=TransferType.
                                                                    BETWEEN_MY_ESTABLISHMENTS)

    @pytest.fixture()
    def create_contract_with_quota(self, http_client):
        self.employee_transfer_actions.confirm_creation_of_contract(entity_laborer=laborer_between_my_establishments,
                                                                    transfer_type=TransferType.
                                                                    BETWEEN_MY_ESTABLISHMENTS,
                                                                    is_get_balance_value=True)

    @pytest.fixture()
    def quota_same_unfied_number(self, http_client):
        self.employee_transfer_actions.confirm_creation_of_contract(entity_laborer=laborer_between_my_establishments,
                                                                    entity=employer_between_my_establishments,
                                                                    transfer_type=TransferType.
                                                                    BETWEEN_MY_ESTABLISHMENTS,
                                                                    is_get_balance_value=True)

    @allure.title('Verify user able to submit ET request between my establishments')
    def test_user_able_to_submit_et_request_between_my_establishments(self, create_contract):
        pass

    @allure.title('Verify Laborer is able to approve the ET request')
    def test_bme_laborer_able_to_approve_et_request(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)

    @allure.title('ET Request status changes after Laborer approval')
    def test_bme_et_request_status_changes_after_laborer_approval(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_APPROVE, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_APPROVE, Language.AR)

    @allure.title('Verify Laborer is able to reject the ET request')
    def test_bme_laborer_able_to_reject_et_request(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(ErrorMessage.ET_LABORER_REQUEST)

    @allure.title('Verify request status changes when Laborer rejected the ET request')
    def test_bme_et_request_status_changes_after_laborer_rejected(self, create_contract):
        self.employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('Quota (Establishment Balance) Should be decreased after submitting ET request')
    def test_bme_quota_should_be_decreased_after_submitting_et_request(self, create_contract_with_quota):
        self.employee_transfer_actions.navigate_to_employee_transfer_by_link()
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value()

    @allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
    def test_bme_quota_should_be_increased_after_rejection_of_et_request_by_laborer(self, create_contract_with_quota):
        self.employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(ErrorMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        self.login_action.visit()
        self.employee_transfer_actions.navigate_to_et_service(employer)
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value(is_decreased=False)

    @allure.title('Verify Quota does not decrease when transferring between my establishments same unfied number')
    def test_quota_not_decrease_between_my_establishments_same_unfied_number(self, quota_same_unfied_number):
        self.employee_transfer_actions.navigate_to_employee_transfer_by_link()
        self.employee_transfer_actions.click_btn_request_employee_transfer().click_btn_approve()
        self.employee_transfer_actions.click_check_balance()
        self.employee_transfer_actions.verify_balance_value(is_decreased=False)
