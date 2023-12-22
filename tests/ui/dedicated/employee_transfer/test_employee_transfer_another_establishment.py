import allure
import pytest

from data.constants import Language
from data.dedicated.employee_trasfer.employee_transfer_users import (
    current_sponsor,
    employer,
    employer_old,
    laborer,
    laborer_with_sponsor,
)
from data.dedicated.enums import RequestStatus, ServicesAndTools
from src.api.clients.employee_transfer import employee_transfer_api
from src.api.clients.ibm import ibm_api
from src.ui.actions.employee_transfer import employee_transfer_actions
from src.ui.actions.individual_actions import individual_actions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.EMPLOYEE_TRANSFER)


@allure.title('Verify Sent Employee Transfer Requests are shown in Home Page of ET Service')
@case_id(123656, 123657)
def test_sent_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    employee_transfer_actions.navigate_to_et_service(employer_old)

    qiwa.employee_transfer_page.check_count_of_sent_request_rows()


@allure.title('Verify Received Employee Transfer Requests are shown in Home Page of ET Service')
@case_id(123657)
def test_received_employee_transfer_requests_are_shown_in_home_page_of_et_service():
    employee_transfer_actions.navigate_to_et_service(employer_old)

    qiwa.employee_transfer_page.check_count_of_received_request_rows()


@allure.title('Verify user able to submit ET request from another establishment')
@case_id(123658, 123659, 123660)
def test_user_able_to_submit_et_request_from_another_establishment():
    employee_transfer_api.post_prepare_laborer_for_et_request()

    employee_transfer_actions.navigate_to_et_service(employer) \
        .create_et_request_from_another_establishment(laborer)


@pytest.mark.parametrize(
    'status',
    [
        RequestStatus.PENDING_FOR_CURRENT_EMPLOYER_APPROVAL.value,
        RequestStatus.REJECTED_BY_LABORER.value
    ],
    ids=[
        'AS-320 Verify Laborer is able to approve the ET request',
        'AS-322 Verify Laborer is able to reject the ET request'
    ]
)
@case_id(123661, 123662, 123663, 123664)
def test_laborer_able_to_make_a_decision_for_et_request(status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_with_sponsor.personal_number)
    ibm_api.create_new_contract(employer, laborer_with_sponsor)
    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)

    employee_transfer_actions.navigate_to_individual(laborer_with_sponsor.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
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


@pytest.mark.parametrize(
    'status',
    [
        RequestStatus.PENDING_COMPLETING_TRANSFER_IN_ABSHER_BY_NEW_EMPLOYER.value,
        RequestStatus.REJECTED_BY_CURRENT_EMPLOYER.value
    ],
    ids=[
        'Verify Current Sponsor Able to approve the ET request',
        'Verify Current Sponsor Able to reject the ET request'
    ]
)
@case_id(123667, 123668, 123670, 123671)
def test_current_sponsor_able_to_make_a_decision_for_get_request(status):
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_with_sponsor.personal_number)
    ibm_api.create_new_contract(employer, laborer_with_sponsor)
    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)

    employee_transfer_actions.navigate_to_individual(laborer_with_sponsor.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request()

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service_current_sponsor(current_sponsor)

    qiwa.employee_transfer_page.search_received_request(laborer_with_sponsor.personal_number)

    employee_transfer_actions.make_a_decision_as_current_sponsor(status)

    qiwa.employee_transfer_page.check_sponsor_request_status(status[Language.EN])
    qiwa.header.change_local(Language.AR)
    qiwa.employee_transfer_page.check_sponsor_request_status(status[Language.AR])


@allure.title('AS-328 Quota (Establishment Balance) Should be decreased after submitting ET request')
@case_id(123665)
def test_quota_should_be_decreased_after_submitting_et_request():
    employee_transfer_api.post_prepare_laborer_for_et_request()
    ibm_api.create_new_contract(employer, laborer_with_sponsor)

    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(RequestStatus.PENDING_FOR_CURRENT_EMPLOYER_APPROVAL.value[Language.EN])

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance - 1).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Quota (Establishment Balance) increased after rejection of ET request by Laborer')
@case_id(123666)
def test_quota_should_be_increased_after_rejection_of_et_request_by_laborer():
    employee_transfer_api.post_prepare_laborer_for_et_request()
    ibm_api.create_new_contract(employer, laborer_with_sponsor)
    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)
    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    individual_actions.reject_request() \
        .wait_until_popup_disappears() \
        .verify_expected_status(RequestStatus.REJECTED_BY_LABORER[Language.EN])

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())


@allure.title('Quota (Establishment Balance) increased after rejection of ET request by current sponsor')
@case_id(123669)
def test_quota_should_be_increased_after_rejection_of_et_request_current_sponsor():
    employee_transfer_api.post_prepare_laborer_for_et_request(laborer_with_sponsor.personal_number)
    ibm_api.create_new_contract(employer, laborer_with_sponsor)

    employee_transfer_actions.navigate_to_et_service(employer)

    establishment_balance = qiwa.employee_transfer_page.get_recruitment_quota()

    ibm_api.create_employee_transfer_request_ae(employer, laborer_with_sponsor)

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)

    employee_transfer_actions.navigate_to_individual(laborer_with_sponsor.personal_number)

    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
    qiwa.code_verification.fill_in_code() \
        .click_confirm_button()

    # TODO(dp): Remove after fixing an issue with changing the language
    qiwa.header.change_local(Language.EN)

    qiwa.individual_page.select_service(ServicesAndTools.EMPLOYEE_TRANSFERS.value[Language.EN]) \
        .click_agree_checkbox()

    individual_actions.approve_request()

    qiwa.header.click_on_menu_individuals().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()

    employee_transfer_actions.navigate_to_et_service_current_sponsor(current_sponsor)

    qiwa.employee_transfer_page.search_received_request(laborer_with_sponsor.personal_number) \
        .click_btn_reject() \
        .fill_rejection_reason() \
        .click_btn_reject_request()

    qiwa.employee_transfer_page.check_sponsor_request_status(RequestStatus.REJECTED_BY_CURRENT_EMPLOYER.value[Language.EN])

    qiwa.header.click_on_menu().click_on_logout()

    employee_transfer_actions.navigate_to_et_service(employer)

    assert_that(establishment_balance).equals_to(qiwa.employee_transfer_page.get_recruitment_quota())
