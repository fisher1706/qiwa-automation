import allure
import pytest

from data.constants import Eligibility, EstablishmentStatus, Language, Occupation
from data.dedicated.change_occupation import (
    change_occupation,
    employee,
    employee_1,
    lo_co_user,
)
from data.dedicated.enums import RequestStatus, SearchingType
from data.constants import Eligibility, EstablishmentStatus, Language, Occupation
from data.dedicated.change_occupation import employee, employee_1, lo_co_user
from data.dedicated.enums import RequestStatus, SearchingType
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.feature('Change Occupation')
@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_co_user.personal_number)
    api.visits_api.cancel_active_visit(lo_co_user.personal_number)


@allure.title('Check if establishment and CR is active')
@case_id(32946, 32947)
def test_check_if_establishment_and_cr_is_active():
    booking_id = IBMApiController().create_new_appointment(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.check_establishment_status(EstablishmentStatus.EXISTING) \
        .check_cr_end_date()


@allure.title('Check if CR is Expired')
@case_id(32948)
@pytest.mark.skip('Todo')
def test_check_if_cr_is_expired():
    pass


@allure.title('Check if excluded activities are not able to CO')
@case_id(32949)
@pytest.mark.skip('Todo')
def test_check_if_excluded_activities_are_not_able_to_co():
    pass


@allure.title('Check if labor is employed')
@case_id(32950)
def test_check_if_labor_is_employed():
    booking_id = IBMApiController().create_new_appointment(lo_co_user,  change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .check_employee_eligibility(Eligibility.ELIGIBLE)


@allure.title('Check CO request is moved to CO request section (extra case)')
def test_check_co_request_is_moved_to_co_request_section():
    booking_id = IBMApiController().create_new_appointment(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .check_request_is_exist(employee.personal_number)


@allure.title('Check if CO is submitted (extra case)')
def test_check_if_co_is_submitted():
    booking_id = IBMApiController().create_new_appointment(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .click_agree_checkbox() \
        .click_btn_send_change_occupation_request()

    qiwa.appointment_page.set_and_confirm_otp_modal()

    qiwa.requests_page.check_request_title() \
        .expand_details() \
        .check_iqama_number(employee.personal_number) \
        .check_request_status(RequestStatus.PENDING_FOR_LABORER_APPROVAL.value)


@allure.title('Check if CO submitted while there is ST')
@case_id(32951)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_while_there_is_st():
    pass


@allure.title('Check if CO submitted while there is another CO')
@case_id(32952)
def test_check_if_co_submitted_while_there_is_another_co():
    booking_id = IBMApiController().create_new_appointment(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .click_agree_checkbox() \
        .click_btn_send_change_occupation_request()

    qiwa.appointment_page.set_and_confirm_otp_modal()

    qiwa.requests_page.check_request_title() \
        .expand_details() \
        .check_iqama_number(employee.personal_number) \
        .check_request_status(RequestStatus.PENDING_FOR_LABORER_APPROVAL.value) \
        .click_btn_return_to_the_previous_page()

    qiwa.change_occupation_page.check_change_occupation_title()\
        .find_expected_employee(employee.personal_number) \
        .check_employee_eligibility(Eligibility.NOT_ELIGIBLE)


@allure.title('Check if CO submitted for prohibited nationalities')
@case_id(32953)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_for_prohibited_nationalities():
    pass


@allure.title('Check if CO submitted on saudization occupations')
@case_id(32954)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_on_saudization_occupations():
    pass


@allure.title('Check if CO submitted on home occupations')
@case_id(32955)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_on_home_occupations():
    pass


@allure.title('Check if CO submitted to not allowed occupations')
@case_id(32956)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_to_not_allowed_occupations():
    pass


@allure.title('Check if CO submitted over occupation not allowed to transfer from')
@case_id(32957)
@pytest.mark.skip('Todo')
def test_check_if_co_submitted_over_occupation_not_allowed_to_transfer_from():
    pass


@allure.title('Check Error messages scenarios')
@case_id(32957)
@pytest.mark.skip('Todo')
def test_check_error_messages_scenarios():
    pass


@allure.title('Submit CO for multiple requests in one bulk')
@case_id(32962)
def test_submit_co_for_multiple_requests_in_one_bulk():
    booking_id = IBMApiController().create_new_appointment(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.workspace_page.select_lo_agent()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .find_expected_employee(employee_1.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation()

    qiwa.change_occupation_page.click_agree_checkbox() \
        .click_btn_send_change_occupation_request()
    qiwa.appointment_page.set_and_confirm_otp_temp()

    qiwa.requests_page.check_request_title() \
        .expand_details() \
        .check_iqama_number(employee_1.personal_number) \
        .check_request_status(RequestStatus.PENDING_FOR_LABORER_APPROVAL.value) \
        .check_iqama_number_bulk(employee.personal_number) \
        .check_request_status_bulk(RequestStatus.PENDING_FOR_LABORER_APPROVAL.value)
