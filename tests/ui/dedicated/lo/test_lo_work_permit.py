import allure
import pytest

from data.constants import Language
from data.dedicated.enums import SearchingType
from data.dedicated.lo_work_permit import (
    lo_wp_iqama_1,
    lo_wp_iqama_2,
    lo_wp_iqama_3,
    lo_wp_iqama_4,
    lo_wp_iqama_5,
    lo_wp_user_1,
)
from data.dedicated.models.services import lo_work_permit
from src.api.app import QiwaApi
from src.api.controllers.ibm import ibm_api_controller
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_wp_user_1.personal_number)
    api.visits_api.cancel_active_visit(lo_wp_user_1.personal_number)


@allure.title('AS-271 Verify that search functionality works with both Iqama and BorderNo')
@case_id(32964)
def test_verify_search_functionality_with_iqama_and_border_number():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_1.personal_number)


@allure.title('AS-274 Verify that user return the 12-months WP period option when iqama is expired for slighly'
              ' less than a whole number of years')
@case_id(32967)
def test_verify_wp_period_when_iqama_expired():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_2.personal_number) \
        .check_available_periods()


@allure.title('AS-272 Verify that laborer with unfit job returns an error')
@case_id(32965)
def test_verify_laborer_with_unfit_job_returns_an_error():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_3.personal_number) \
        .verify_unfit_job_error()


@allure.title('AS-273 Verify that this user return all WP periods when iqama is expired slighlty more than a whole '
              'number of years')
@case_id(32966)
def test_verify_that_all_wp_returns_with_expired_iqama():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_4.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_redirect_to_overview()


@allure.title('AS-275 Verify that selected employees tab shows only the selected employees')
@case_id(32968)
def test_verify_that_selected_employees_tab_shows_only_the_selected_employees():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_4.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .click_on_show_only_selected_employees_btn() \
        .verify_selected_employees(lo_wp_iqama_4.personal_number)


@allure.title('AS-276 Verify that the selected employees all have WP Fees = (25 per each 3 months from selected '
              'WP period) on calculation page')
@case_id(32969)
def test_verify_that_the_selected_employees_all_have_wp_fees():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_4.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_total_amount_is_displayed() \
        .verify_wp_fees_is_displayed() \
        .verify_extra_fees_is_displayed() \
        .verify_late_years_extra_fees()


@allure.title('AS-277 Verify that only the selected employees (with no error in validation step) are moved to the'
              'calculation page')
@case_id(32970)
def test_selected_employees_moved_to_calculation_page():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_4.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_iqama_is_displayed()


@allure.title('AS-278 Verify that a penalty user will have fees > 0 in either (or both) of the "fees for late '
              'years" columns')
@case_id(32971)
def test_verify_that_a_penalty_user_will_have_fees_less_than_null():
    appointment_id = ibm_api_controller.get_appointment_id(lo_wp_user_1, lo_work_permit)
    qiwa.login_as_user(login=lo_wp_user_1.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, appointment_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.business_page.select_work_permit()
    qiwa.lo_work_permit_page.verify_search_by_border_or_iqama(lo_wp_iqama_5.personal_number) \
        .check_available_periods() \
        .choose_wp_period_12() \
        .verify_continue_with_wp_request_btn_active() \
        .verify_total_amount_is_displayed() \
        .verify_wp_fees_is_displayed() \
        .verify_extra_fees_is_displayed() \
        .verify_late_years_extra_fees()
