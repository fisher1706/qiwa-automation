import allure
import pytest
from selene import browser

from data.constants import Language
from data.dedicated.employee_trasfer.employee_transfer_users import (
    employer,
    laborer_between_my_establishments,
    laborer_between_my_establishments_quota, )
from data.dedicated.enums import RequestStatus, ServicesAndTools, TransferType
from src.api.clients.employee_transfer import employee_transfer_api
from src.api.clients.ibm import ibm_api
from src.ui.actions.employee_transfer import employee_transfer_actions
from src.ui.actions.individual_actions import IndividualActions, individual_actions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@allure.title('Verify user able to submit ET request from my own establishment')
@case_id(123677, 123678)
def test_bme_user_able_to_submit_et_request():
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments.personal_number)

    employee_transfer_actions.navigate_to_et_service(employer) \
        .create_et_request_between_my_establishment(laborer_between_my_establishments)


@pytest.mark.parametrize(
    'status', [RequestStatus.PENDING_FOR_CURRENT_EMPLOYER_APPROVAL.value, RequestStatus.REJECTED_BY_LABORER.value],
    ids=[
        'Verify Laborer is able to approve the ET request',
        'Verify Laborer is able to reject the ET request'
    ]
)
@case_id(123679, 123680, 123681, 123682)
def test_bme_laborer_able_to_make_a_decision_for_et_request(status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments.personal_number)
    ibm_api.create_new_contract(employer, laborer_between_my_establishments)
    ibm_api.create_employee_transfer_request_bme(employer,
                                                 laborer_between_my_establishments,
                                                 TransferType.BETWEEN_MY_ESTABLISHMENTS.value)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    if status == RequestStatus.PENDING_FOR_CURRENT_EMPLOYER_APPROVAL.value:
        individual_actions.approve_request()
    else:
        individual_actions.reject_request()

    individual_actions.wait_until_popup_disappears() \
        .verify_expected_status(status[Language.EN])
    qiwa.header.change_local(Language.AR)
    individual_actions.verify_expected_status(status[Language.AR])


@allure.title('Quota (Establishment Balance) Should be decreased after submitting ET request')
@case_id(123683)
def test_bme_quota_should_be_decreased_after_submitting_et_request():
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments.personal_number)
    ibm_api.create_new_contract(employer, laborer_between_my_establishments)

    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_bme(employer,
                                                 laborer_between_my_establishments,
                                                 TransferType.BETWEEN_MY_ESTABLISHMENTS.value)

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.personal_number)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.approve_request() \
        .wait_until_popup_disappears()

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance - 1).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
@case_id(123684)
def test_bme_quota_should_be_increased_after_rejection_of_et_request_by_laborer():
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments.personal_number)
    ibm_api.create_new_contract(employer, laborer_between_my_establishments)

    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_bme(employer,
                                                 laborer_between_my_establishments,
                                                 TransferType.BETWEEN_MY_ESTABLISHMENTS.value)

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_between_my_establishments.personal_number)

    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions = IndividualActions()
    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(RequestStatus.REJECTED_BY_LABORER.value[Language.EN])

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Verify Quota does not decrease when transferring between my establishments same unified number')
@case_id(123685)
def test_quota_not_decrease_between_my_establishments_same_unified_number():
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_between_my_establishments_quota.personal_number)
    ibm_api.create_new_contract(employer, laborer_between_my_establishments_quota)

    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_bme(employer,
                                                 laborer_between_my_establishments_quota,
                                                 TransferType.BETWEEN_MY_ESTABLISHMENTS.value)

    browser.driver.refresh()

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())
