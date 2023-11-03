import allure
import pytest

from data.constants import Language
from data.dedicated.employee_trasfer.employee_transfer_constants import LABORER_TYPE_9_STATUS_APPROVE, \
    LABORER_STATUS_REJECT
from data.dedicated.employee_trasfer.employee_transfer_users import (
    employer,
    employer_between_my_establishments,
    laborer_between_my_establishments,
    laborer_between_my_establishments_existing_contract,
)
from data.dedicated.enums import ServicesAndTools
from src.api.clients.employee_transfer import EmployeeTransferApi
from src.ui.actions.employee_transfer import EmployeeTransferActions
from src.ui.actions.individual_actions import IndividualActions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@allure.title('Verify user able to submit ET request from my own establishment')
@case_id(123677)
def test_bme_user_able_to_submit_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer) \
        .create_et_request_between_my_establishment(laborer_between_my_establishments)


@allure.title("If laborer already has a contract, don't show redirection to CM button from my own establishment")
@case_id(123678)
def test_bme_if_laborer_already_has_a_contract_do_not_show_redirection_to_cm():
    EmployeeTransferActions().navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_own_establishment() \
        .click_btn_next_step() \
        .search_by_iqama_number(laborer_between_my_establishments_existing_contract.login_id) \
        .select_first_employee(laborer_between_my_establishments_existing_contract.login_id) \
        .click_btn_next_step() \
        .check_existence_of_a_contract()


@allure.title('Verify Laborer is able to approve the ET request')
@case_id(123679, 123680)
def test_bme_laborer_able_to_approve_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer) \
        .create_et_request_between_my_establishment(laborer_between_my_establishments)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.approve_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(LABORER_TYPE_9_STATUS_APPROVE[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(LABORER_TYPE_9_STATUS_APPROVE[Language.AR])


@allure.title('Verify Laborer is able to reject the ET request')
@case_id(123681, 123682)
def test_bme_laborer_able_to_reject_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer) \
        .create_et_request_between_my_establishment(laborer_between_my_establishments)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    individual_actions = IndividualActions()
    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(LABORER_STATUS_REJECT[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(LABORER_STATUS_REJECT[Language.AR])


@allure.title('Quota (Establishment Balance) Should be decreased after submitting ET request')
@case_id(123683)
def test_bme_quota_should_be_decreased_after_submitting_et_request():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    employee_transfer_actions.create_et_request_between_my_establishment(laborer_between_my_establishments)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFER.value) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.approve_request() \
        .wait_until_popup_disappears()

    qiwa.header.click_on_menu_individuals().click_on_logout()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance - 1).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
@case_id(123684)
def test_bme_quota_should_be_increased_after_rejection_of_et_request_by_laborer():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    employee_transfer_actions.create_et_request_between_my_establishment(laborer_between_my_establishments)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.login_id)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    individual_actions = IndividualActions()
    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(LABORER_STATUS_REJECT[Language.EN])

    qiwa.header.click_on_menu_individuals().click_on_logout()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Verify Quota does not decrease when transferring between my establishments same unified number')
@case_id(123685)
@pytest.mark.skip("Renew laborers work permits for employer and find laborer with same unified number")
def test_quota_not_decrease_between_my_establishments_same_unified_number():
    EmployeeTransferApi().post_prepare_laborer_for_et_request(laborer_between_my_establishments.login_id)

    employee_transfer_actions = EmployeeTransferActions()
    employee_transfer_actions.navigate_to_et_service(employer_between_my_establishments)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    employee_transfer_actions.create_et_request_between_my_establishment(laborer_between_my_establishments)

    qiwa.employee_transfer_page.click_btn_back_to_employee_transfer()

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())
