import allure
import pytest

from data.constants import EmployeeTransfer, Language
from data.dedicated.employee_trasfer.employee_transfer import employer, laborer
from data.dedicated.enums import ServicesAndTools
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.employee_transfer import EmployeeTransferActions
from src.ui.actions.individual_actions import IndividualActions
from src.ui.qiwa import qiwa
from utils.allure import project, TestmoProject
from utils.assertion import assert_that

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@allure.title('Verify Sent Employee Transfer Requests are shown in Home Page of ET Service')
@case_id(123656)
def test_sent_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.check_count_of_sent_request_rows()


@allure.title('Verify Received Employee Transfer Requests are shown in Home Page of ET Service')
@case_id(123657)
def test_received_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.check_count_of_received_request_rows()


@allure.title('Verify user able to submit ET request from another establishment')
@case_id(123658, 123659)
def test_user_able_to_submit_et_request_from_another_establishment():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)
    employee_transfer_actions.create_et_request_from_another_establishment(laborer)


@allure.title("If laborer already has a contract, don't show redirection to CM button another establishment")
@pytest.mark.skip("Find user with contract")
@case_id(123660)
def test_if_laborer_already_has_a_contract_do_not_show_redirection_to_cm_button_another_establishment():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.login_id) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request() \
        .check_existence_of_a_contract()


@allure.title('AS-320 Verify Laborer is able to approve the ET request')
@case_id(123663, 123664)
def test_laborer_able_to_approve_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    employee_transfer_actions.create_et_request_from_another_establishment(laborer)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.approve_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(EmployeeTransfer.LABORER_TYPE_9_STATUS_APPROVE[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(EmployeeTransfer.LABORER_TYPE_9_STATUS_APPROVE[Language.AR])


@allure.title('AS-322 Verify Laborer is able to reject the ET request')
@case_id(123663, 123662)
def test_laborer_able_to_reject_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    employee_transfer_actions.create_et_request_from_another_establishment(laborer)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    individual_actions = IndividualActions()
    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT[Language.AR])


@allure.title('AS-328 Quota (Establishment Balance) Should be decreased after submitting ET request')
@case_id(123665)
def test_quota_should_be_decreased_after_submitting_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    employee_transfer_actions.create_et_request_from_another_establishment(laborer)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.approve_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(EmployeeTransfer.LABORER_TYPE_9_STATUS_APPROVE[Language.EN])

    qiwa.header.click_on_menu_individuals(laborer.login_id).click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance - 1).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
@case_id(123666)
def test_quota_should_be_increased_after_rejection_of_et_request_by_laborer():
    EmployeeTransferApi().post_prepare_laborer_for_et_request()
    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    employee_transfer_actions.create_et_request_from_another_establishment(laborer)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    individual_actions = IndividualActions()
    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(EmployeeTransfer.LABORER_STATUS_REJECT[Language.EN])

    qiwa.header.click_on_menu_individuals(laborer.login_id).click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())
