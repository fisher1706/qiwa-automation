import allure
import pytest
from selene import browser

from data.constants import EmployeeTransfer, Language
from data.dedicated.employee_trasfer.employee_transfer import (
    current_sponsor_type_12,
    laborer_type_4_absent,
    laborer_type_4_direct_transfer,
    laborer_type_4_freedom_transfer,
    laborer_type_9,
    laborer_type_12,
)
from data.dedicated.enums import ServicesAndTools
from data.validation_message import SuccessMessage
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.individual_actions import IndividualActions
from src.ui.actions.old_employee_transfer import EmployeeTransferActionsOld
from src.ui.qiwa import qiwa


@allure.feature('Employee Transfer sheet 2')
@pytest.mark.skip("Old design")
class TestEmployeeTransferSheet2:  # pylint: disable=unused-argument, duplicate-code

    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.employee_transfer_actions = EmployeeTransferActionsOld()
        self.individual_actions = IndividualActions()
        self.employee_transfer_api = EmployeeTransferApi(http_client)

    @allure.title('[Type 12] Approval by laborer and approval by current sponsor | Home Worker Transfer')
    def test_type_12_approval_by_laborer_and_approval_by_current_sponsor(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_12.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_12.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_12)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_12.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_individual(current_sponsor_type_12.login_id)
        self.individual_actions.select_service(ServicesAndTools.HOME_WORKER_TRANSFER.value)
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_APPROVE, Language.EN)
        self.individual_actions.change_locale()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_APPROVE, Language.AR)

    @allure.title('[Type 12] Approval by laborer and rejection by current sponsor | Home Worker Transfer')
    def test_type_12_approval_by_laborer_and_rejection_by_current_sponsor(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_12.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_12.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_12)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_12.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page()
        self.employee_transfer_actions.navigate_to_individual(current_sponsor_type_12.login_id)
        self.individual_actions.select_service(ServicesAndTools.HOME_WORKER_TRANSFER.value)
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.employee_transfer_actions.verify_expected_status(EmployeeTransfer.SPONSOR_STATUS_REJECT, Language.AR)

    @allure.title('[Type 12] Rejection by laborer | Home Worker Transfer')
    def test_type_12_rejection_by_laborer(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_12.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_12.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_12)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_12.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('[Type 9] Approval by laborer | Dependent Transfer')
    def test_type_9_approval_by_laborer_dependent_transfer(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_9.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_9.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_9)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_9.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_9_STATUS_APPROVE, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_9_STATUS_APPROVE, Language.AR)

    @allure.title('[Type 9] Rejection by laborer | Dependent Transfer')
    def test_type_9_rejection_by_laborer_dependent_transfer(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_9.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_9.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_9)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_9.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('[Type 4 Freedom Transfer] Verify that after Approval by Laborer status changes')
    def test_type_4_freedom_transfer_verify_that_after_approval_by_laborer_status_changes(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_freedom_transfer.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_freedom_transfer.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_freedom_transfer)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_freedom_transfer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_4_FREEDOM_TRANSFER_STATUS_APPROVE, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_4_FREEDOM_TRANSFER_STATUS_APPROVE, Language.AR)

    @allure.title('[Type 4 Freedom Transfer] Verify that after Rejection by Laborer status changes')
    def test_type_4_freedom_transfer_verify_that_after_rejection_by_laborer_status_changes_(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_freedom_transfer.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_freedom_transfer.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_freedom_transfer)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_freedom_transfer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('[Type 4 Direct Transfer] Verify that after Approval by Laborer status changes')
    def test_type_4_direct_transfer_verify_that_after_approval_by_laborer_status_changes(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_direct_transfer.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_direct_transfer.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_direct_transfer)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_direct_transfer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.approve_request()
        self.individual_actions.wait_until_popup_disappears()
        self.employee_transfer_actions.verify_message(SuccessMessage.ET_LABORER_REQUEST)
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_4_DIRECT_TRANSFER_STATUS_APPROVE,
                                                       Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_4_DIRECT_TRANSFER_STATUS_APPROVE,
                                                       Language.AR)

    @allure.title('[Type 4 Direct Transfer] Verify that after Rejection by Laborer status changes')
    def test_type_4_direct_transfer_verify_that_after_rejection_by_laborer_status_changes_(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_direct_transfer.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_direct_transfer.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_direct_transfer)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_direct_transfer.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('[Type 4 Absent Laborer] Verify that after Approval by Laborer status changes')
    def test_type_4_absent_laborer_verify_that_after_approval_by_laborer_status_changes(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_absent.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_absent.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_absent, is_verify_popup=True)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_absent.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)

    @allure.title('[Type 4 Absent Laborer] Verify that after Rejection by Laborer status changes ')
    def test_type_4_absent_laborer_verify_that_after_rejection_by_laborer_status_changes(self):
        self.employee_transfer_api.post_prepare_laborer_for_et_request(laborer_type_4_absent.login_id)
        self.employee_transfer_api.post_create_new_contract(laborer_type_4_absent.login_id)
        self.employee_transfer_actions.confirm_creation_of_contract(laborer_type_4_absent, is_verify_popup=True)
        self.employee_transfer_actions.navigate_to_individual(laborer_type_4_absent.login_id)
        self.individual_actions.proceed_steps_for_verifying_et_request()
        self.individual_actions.reject_request()
        self.individual_actions.wait_until_popup_disappears()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.EN)
        self.individual_actions.change_locale()
        self.individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT, Language.AR)
