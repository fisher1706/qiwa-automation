import allure
import pytest

from data.constants import Language
from data.dedicated.enums import SearchingType, WorkPermitRequestStatus
from data.dedicated.lo_work_permit import (
    lo_wp_iqama_6,
    lo_wp_iqama_7,
    lo_wp_iqama_8,
    lo_wp_iqama_9,
    lo_wp_user_2,
)
from data.dedicated.services import lo_work_permit
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_wp_user_2.personal_number)
    api.visits_api.cancel_active_visit(lo_wp_user_2.personal_number)


@allure.title('AS-300 Verify that new SADAD bill is issued after a successful flow in issue/renew')
@case_id(32972)
def test_verify_that_new_sadad_bill_is_issued_after_a_successful_flow_in_issue_renew():
    appointment_id = IBMApiController().create_new_appointment(lo_wp_user_2, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_6.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_redirect_to_overview() \
        .click_on_confirm_and_finish_btn() \
        .click_on_confirm_and_send_email_btn()
    qiwa.email_popup.proceed_otp_code("0000") \
        .click_on_confirm_and_proceed()
    bill = str(qiwa.lo_work_permit_page.get_bill_number())
    qiwa.lo_work_permit_page.click_back_to_establishment_page()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_wp_requests_service()
    qiwa.lo_work_permit_page.check_pending_status(bill_number=bill, status=WorkPermitRequestStatus.PENDING_PAYMENT)


@allure.title('AS-301 Verify that only the SADAD bills with status "pending payment" are cancellable')
@case_id(32973)
def test_verify_that_only_the_sadad_bills_with_status_pending_payment_are_cancellable():
    appointment_id = IBMApiController().create_new_appointment(lo_wp_user_2, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_wp_requests_service()
    sadad = str(qiwa.lo_work_permit_page.get_sadad_number())
    qiwa.lo_work_permit_page.click_on_cancel_sadad_number_btn()
    qiwa.lo_work_permit_page.enter_otp() \
        .click_on_proceed_btn() \
        .navigate_to_last_page() \
        .check_canceled_status(bill_number=sadad, status=WorkPermitRequestStatus.CANCELED)


@allure.title('AS-302 Verify that the details of the newly issued WP request contains only the employees used in its'
              ' flow and with the correctly selected periods')
@case_id(32974)
def test_verify_that_wp_request_contains_only_the_employees_used_in_its_flow_and_with_the_correctly_selected_periods():
    appointment_id = IBMApiController().create_new_appointment(lo_wp_user_2, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_7.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .click_on_clear_btn() \
        .verify_search_by_border_or_iqama(lo_wp_iqama_8.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_redirect_to_overview() \
        .click_on_confirm_and_finish_btn() \
        .click_on_confirm_and_send_email_btn()
    qiwa.email_popup.proceed_otp_code("0000") \
        .click_on_confirm_and_proceed()
    qiwa.lo_work_permit_page.click_back_to_establishment_page()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_wp_requests_service() \
        .click_on_view_details() \
        .verify_requested_period(period="12")


@allure.title('AS-303 Verify that the total amount in the sadad bill is equal to the total amount mentioned in the '
              'calculation page during issue/renew flow')
@case_id(32975)
def test_verify_that_the_total_amount_in_the_sadad_bill_is_equal_to_the_total_amount_mentioned_in_the_calculation_page_during_issue_renew_flow():
    appointment_id = IBMApiController().create_new_appointment(lo_wp_user_2, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_2.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_9.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_redirect_to_overview()
    amount = str(qiwa.lo_work_permit_page.get_total_amount())
    qiwa.lo_work_permit_page.click_on_confirm_and_finish_btn() \
        .click_on_confirm_and_send_email_btn()
    qiwa.email_popup.proceed_otp_code("0000") \
        .click_on_confirm_and_proceed()
    qiwa.lo_work_permit_page.compare_total_amounts(amount)
