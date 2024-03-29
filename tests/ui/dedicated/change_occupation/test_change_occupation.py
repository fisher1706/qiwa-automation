import allure
import pytest

from data.constants import EService, Language
from data.dedicated.change_occupation.change_occupation_constants import (
    Eligibility,
    EstablishmentStatus,
    Occupation,
)
from data.dedicated.change_occupation.change_occupation_users import (
    employee,
    employee_1,
    employee_ho,
    employee_po,
    laborer,
    lo_co_expired_user,
    lo_co_ho_user,
    lo_co_user,
)
from data.dedicated.employee_trasfer.employee_transfer_users import employer
from data.dedicated.enums import (
    RequestStatus,
    SearchingType,
    SubServiceChangeOccupation,
    SubServiceErrors,
)
from data.dedicated.models.services import change_occupation
from data.lo.constants import AppointmentReason
from src.api.app import QiwaApi
from src.api.clients.employee_transfer import employee_transfer_api
from src.api.clients.ibm import ibm_api
from src.api.controllers.ibm import ibm_api_controller
from src.ui.actions.employee_transfer import employee_transfer_actions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@pytest.fixture(autouse=True)
def pre_test():
    api = QiwaApi.login_as_user(lo_co_user.personal_number)
    api.visits_api.cancel_active_visit(lo_co_user.personal_number)


@pytest.fixture()
def remove_co_requests():
    request_number = ibm_api_controller.get_request_numbers(employee)
    if request_number:
        ibm_api.cancel_change_occupation_request(request_number[0])


@pytest.fixture()
def remove_co_requests_bulk(remove_co_requests):
    request_number = ibm_api_controller.get_request_numbers(employee_1)
    if request_number:
        ibm_api.cancel_change_occupation_request(request_number[0])


@pytest.fixture()
def create_et_request():
    employee_transfer_api.post_prepare_laborer_for_et_request()
    ibm_api.create_new_contract(employer, laborer)

    employee_transfer_actions.navigate_to_et_service(employer)

    qiwa.employee_transfer_page.click_btn_transfer_employee() \
        .select_another_establishment() \
        .click_btn_next_step() \
        .fill_employee_iqama_number(laborer.personal_number) \
        .fill_date_of_birth(laborer.birthdate) \
        .click_btn_find_employee() \
        .click_btn_add_employee_to_transfer_request() \
        .click_btn_next_step() \
        .check_existence_of_a_contract() \
        .click_btn_next_step() \
        .select_terms_checkbox() \
        .click_btn_submit() \
        .check_request_status() \
        .click_btn_back_to_employee_transfer()

    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    qiwa.header.change_local(Language.EN)


@pytest.fixture()
def login():
    booking_id = ibm_api_controller.get_appointment_id(lo_co_user, change_occupation)

    qiwa.login_as_user(lo_co_user.personal_number)
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .click_btn_process_appointments() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()


@pytest.fixture()
def navigate_to_co(login):
    qiwa.business_page.select_change_occupation()


@allure.title('AS-280 Check if establishment and CR is active')
@case_id(32946, 32947)
def test_check_if_establishment_and_cr_is_active(login):
    qiwa.business_page.check_establishment_status(EstablishmentStatus.EXISTING) \
        .check_cr_end_date()


@allure.title('AS-283 Check if CR is Expired')
@case_id(32948)
def test_check_if_cr_is_expired():
    qiwa.login_as_user(lo_co_expired_user.personal_number)
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(lo_co_expired_user.sequence_number)
    qiwa.open_labor_office_appointments_page()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_establishment(lo_co_expired_user.establishment_name_ar) \
        .select_appointment_reason(AppointmentReason.IN_PERSON) \
        .select_service(EService.CHANGE_OCCUPATION) \
        .select_sub_service(SubServiceChangeOccupation.SUBMIT_CHANGE_OCCUPATION.value) \
        .check_sub_service_error(SubServiceErrors.EXPIRED.value)


@allure.title('AS-284 Check if excluded activities are not able to CO')
@case_id(32949)
def test_check_if_excluded_activities_are_not_able_to_co(navigate_to_co):
    economic_activity_id = ibm_api_controller.get_economic_activity_id(employee)
    first_unrelated_occupation_ar = ibm_api_controller.get_first_unrelated_occupation(economic_activity_id)

    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .search_occupation(first_unrelated_occupation_ar) \
        .check_blank_occupation_list()


@allure.title('AS-285 Check if labor is employed')
@case_id(32950)
def test_check_if_labor_is_employed(navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .check_employee_eligibility(Eligibility.ELIGIBLE)


@allure.title('AS-282 Check CO request is moved to CO request section (extra case)')
def test_check_co_request_is_moved_to_co_request_section(navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .check_request_is_exist(employee.personal_number)


@allure.title('AS-298 Check if CO is submitted (extra case)')
def test_check_if_co_is_submitted(remove_co_requests, navigate_to_co):
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


@allure.title('AS-286 Check if CO submitted while there is ST')
@case_id(32951)
@pytest.mark.skip('The ST (service transfer) is determined by PO as Employee Transfer')
def test_check_if_co_submitted_while_there_is_st(navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(laborer.personal_number) \
        .check_employee_eligibility(Eligibility.NOT_ELIGIBLE)


@allure.title('AS-287 Check if CO submitted while there is another CO')
@case_id(32952)
def test_check_if_co_submitted_while_there_is_another_co(remove_co_requests, navigate_to_co):
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

    qiwa.change_occupation_page.check_change_occupation_title() \
        .find_expected_employee(employee.personal_number) \
        .check_employee_eligibility(Eligibility.NOT_ELIGIBLE)


@allure.title('AS-288 Check if CO submitted for prohibited nationalities')
@case_id(32953)
def test_check_if_co_submitted_for_prohibited_nationalities(remove_co_requests, navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(employee_po.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.SECRETARY_GENERAL_OF_A_SPECIAL_INTEREST_ORGANIZATION) \
        .click_create_change_occupation() \
        .click_agree_checkbox() \
        .click_btn_send_change_occupation_request()

    qiwa.appointment_page.set_and_confirm_otp_modal()

    qiwa.requests_page.check_request_title() \
        .expand_details() \
        .check_iqama_number(employee_po.personal_number) \
        .check_request_status(RequestStatus.PENDING_FOR_LABORER_APPROVAL.value)


@allure.title('AS-289 Check if CO submitted on saudization occupations')
@case_id(32954)
def test_check_if_co_submitted_on_saudization_occupations(navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .search_occupation(Occupation.ACCOUNTANT) \
        .check_blank_occupation_list()


@allure.title('AS-290 Check if CO submitted on home occupations')
@case_id(32955)
def test_check_if_co_submitted_on_home_occupations():
    api = QiwaApi.login_as_user(lo_co_ho_user.personal_number)
    api.visits_api.cancel_active_visit(lo_co_ho_user.personal_number)
    booking_id = ibm_api_controller.get_appointment_id(lo_co_ho_user, change_occupation)
    qiwa.login_as_user(lo_co_ho_user.personal_number)
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .click_btn_process_appointments() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()

    qiwa.business_page.select_change_occupation()

    qiwa.change_occupation_page.find_expected_employee(employee_ho.personal_number) \
        .click_btn_change_occupation() \
        .search_occupation(Occupation.PERSONAL_CARE_WORKER) \
        .check_blank_occupation_list()


@allure.title('AS-291 Check if CO submitted to not allowed occupations')
@case_id(32956)
def test_check_if_co_submitted_to_not_allowed_occupations(navigate_to_co):
    qiwa.change_occupation_page.find_expected_employee(employee.personal_number) \
        .click_btn_change_occupation() \
        .select_occupation(Occupation.GENERAL_DIRECTOR) \
        .click_create_change_occupation() \
        .check_warning_msg()


@allure.title('AS-292 Check if CO submitted over occupation not allowed to transfer from')
@case_id(32957)
def test_check_if_co_submitted_over_occupation_not_allowed_to_transfer_from(navigate_to_co):
    employee_personal_number = ibm_api_controller.get_first_expected_employee(lo_co_user)
    qiwa.change_occupation_page.find_expected_employee(employee_personal_number) \
        .check_employee_eligibility(Eligibility.NOT_ELIGIBLE)


@allure.title('AS-293 Check Error messages scenarios')
@case_id(32957)
@pytest.mark.skip('Todo')
def test_check_error_messages_scenarios():
    pass


@allure.title('AS-294 Submit CO for multiple requests in one bulk')
@case_id(32962)
def test_submit_co_for_multiple_requests_in_one_bulk(remove_co_requests_bulk, navigate_to_co):
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
