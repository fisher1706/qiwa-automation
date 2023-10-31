import allure
import pytest

from data.constants import Language
from data.dedicated.enums import SearchingType
from data.dedicated.models.services import Service, saudi_certificate
from data.shareable.saudization_certificate.saudi_certificate import *
from src.api.app import QiwaApi
from src.api.controllers.ibm import IBMApiController
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


def login(user: User, service: Service):
    # cancel current appointment
    api = QiwaApi.login_as_user(user.personal_number)
    api.visits_api.cancel_active_visit(user.personal_number)

    # create a new appointment
    booking_id = IBMApiController().create_new_appointment(user, service)

    # login in UI
    qiwa.login_as_user(lo_sc_agent.personal_number)
    qiwa.header.check_personal_number_or_name(lo_sc_agent.name).change_local(Language.EN)
    qiwa.workspace_page.select_lo_agent()
    qiwa.appointment_page.set_and_confirm_otp() \
        .set_search_by(SearchingType.ID, booking_id) \
        .search_visit()
    qiwa.footer.click_on_lang_button(Language.EN)
    qiwa.visits_page.click_on_proceed_button()


@pytest.mark.parametrize("user", [
    lo_sc_low_green_nitaqat, lo_sc_med_green_nitaqat, lo_sc_high_green_nitaqat, lo_sc_platinum_nitaqat])
@allure.title('Check if user in different nitaqat color can issue saudi certificate')
@case_id(99864, 99882, 99891, 99889)
def test_verify_user_can_issue_saudi_certificate(user: User):
    # login step
    login(user, saudi_certificate)

    qiwa.business_page.select_saudization_certificate()
    qiwa.lo_saudization_certificate_page.issue_saudi_certificate()

    # validate on UI elements in dashboard
    qiwa.lo_saudization_certificate_page.validate_back_to_est_hyper_link() \
        .validate_dashboard_title() \
        .validate_dashboard_sub_title()

    qiwa.email_popup.proceed_otp_code("0000").click_on_proceed_button()
    qiwa.lo_saudization_certificate_page.get_expected_success_message(successful_issuing_message)

    # get cr and unified number for an establishment
    est_details = IBMApiController().get_cr_unified_numbers_for_establishment(user)

    # validate saudi certificate details element on UI
    qiwa.lo_saudization_certificate_page.validate_saudi_certificate_title() \
        .validate_view_certificate_btn() \
        .validate_resend_certificate_btn() \
        .validate_back_to_est_hyper_link()

    # validate on the saudi certificate elements after issuing it
    qiwa.lo_saudization_certificate_page.validate_unified_est_number(est_details.unified_number_id) \
        .validate_cr_number(est_details.cr_number) \
        .validate_issue_date(today_date) \
        .validate_expiry_date(date_after_90_days)


@allure.title('AS-344 Verify the establishment not in Nitaqat cannot book an appointment')
@case_id(99865)
def test_if_establishment_not_included_in_nitaqat():
    create_new_appointment_rs = IBMApiController().get_response_book_an_appointment(lo_sc_nitaqat_not_included,
                                                                                    saudi_certificate)

    # backend validation on the response in arabic and english
    appointment_rs = AppointmentStatus.validate(create_new_appointment_rs)
    assert appointment_rs == not_in_nitaqat_appointment_rs

    # validation on the UI
    qiwa.login_as_user(lo_sc_nitaqat_not_included.personal_number)
    qiwa.header.check_personal_number_or_name(lo_sc_nitaqat_not_included.name).change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(lo_sc_nitaqat_not_included.sequence_number)
    qiwa.dashboard_page.wait_dashboard_page_to_load()

    # selecting e-services then lo
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.dashboard_page.select_e_services_menu_item()
    qiwa.e_services_page.select_lo()

    # book an appointment and add needed details
    qiwa.labor_office_appointments_page.switch_to_appointment_booking_tab()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_establishment_by_seq_number(
        lo_sc_nitaqat_not_included.labor_office_id, lo_sc_nitaqat_not_included.sequence_number) \
        .click_next_step_button()

    qiwa.labor_office_appointments_create_page.select_in_person_appointments().click_next_step_button()
    qiwa.labor_office_appointments_create_page.select_service("Saudization Certificate") \
        .select_sub_service("Create Saudi Certificate")

    # validate on the error message
    qiwa.labor_office_appointments_create_confirmation_page.validate_error_message(
        not_in_nitaqat_appointment_rs.EnglishMsg)


@allure.title('AS-367 Verify that the establishment with red NITAQAT level cannot book the appointment')
@case_id(99866)
def test_if_establishment_has_red_nitaqat():
    create_new_appointment_rs = IBMApiController().get_response_book_an_appointment(lo_sc_red_nitaqat,
                                                                                    saudi_certificate)

    # backend validation on the response in arabic and english
    appointment_rs = AppointmentStatus.validate(create_new_appointment_rs)
    assert appointment_rs == red_nitaqat_appointment_rs

    # validation on the UI
    qiwa.login_as_user(lo_sc_red_nitaqat.personal_number)
    qiwa.header.check_personal_number_or_name(lo_sc_red_nitaqat.name).change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(lo_sc_red_nitaqat.sequence_number)
    qiwa.dashboard_page.wait_dashboard_page_to_load()

    # selecting e-services then lo
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
    qiwa.dashboard_page.select_e_services_menu_item()
    qiwa.e_services_page.select_lo()

    # book an appointment and add needed details
    qiwa.labor_office_appointments_page.switch_to_appointment_booking_tab()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.select_establishment_by_seq_number(
        lo_sc_red_nitaqat.labor_office_id, lo_sc_red_nitaqat.sequence_number) \
        .click_next_step_button()

    qiwa.labor_office_appointments_create_page.select_in_person_appointments().click_next_step_button()
    qiwa.labor_office_appointments_create_page.select_service("Saudization Certificate") \
        .select_sub_service("Create Saudi Certificate")

    # validate on the error message
    qiwa.labor_office_appointments_create_confirmation_page.validate_error_message(
        red_nitaqat_appointment_rs.EnglishMsg)


@allure.title('Check UI OTP modal elements')
@case_id(99888, 99890)
def test_check_otp_ui_module():
    # login step
    login(lo_sc_user, saudi_certificate)

    # validate UI elements on otp module
    qiwa.business_page.select_saudization_certificate()
    qiwa.lo_saudization_certificate_page.issue_saudi_certificate()
    qiwa.lo_saudization_certificate_page \
        .validate_otp_messages("Confirmation", "Please enter the OTP to proceed",
                               "Please inform client that the OTP is sent to the email") \
        .validate_otp_proceed_btn_is_disabled() \
        .validate_otp_resend_sms_is_disabled() \
        .validate_otp_resend_email_is_disabled() \
        .validate_otp_fields_are_enabled()
    # validate invalid otp message and proceed btn is disabled
    qiwa.email_popup.proceed_otp_code("1111")
    qiwa.lo_saudization_certificate_page.validate_wrong_otp().validate_otp_proceed_btn_is_disabled()
    # user able to re-write the otp once again
    qiwa.email_popup.proceed_otp_code("2222")


@allure.title('user can reissue the certificate with the same details')
@case_id(99886, 99887)
def test_reissue_certificate_with_same_old_certificate_number():
    # login step
    login(lo_sc_user, saudi_certificate)

    qiwa.business_page.select_saudization_certificate()
    expected_certificate_number = qiwa.lo_saudization_certificate_page.get_certificate_number()
    expected_issue_date = qiwa.lo_saudization_certificate_page.get_certificate_issue_date()
    expected_expiry_date = qiwa.lo_saudization_certificate_page.get_certificate_expiry_date()
    qiwa.lo_saudization_certificate_page.issue_saudi_certificate()

    # validate on UI elements in dashboard
    qiwa.lo_saudization_certificate_page.validate_back_to_est_hyper_link() \
        .validate_dashboard_title() \
        .validate_dashboard_sub_title()

    qiwa.email_popup.proceed_otp_code("0000").click_on_proceed_button()
    qiwa.lo_saudization_certificate_page.get_expected_success_message(successful_issuing_message)

    # validate saudi certificate details element on UI
    qiwa.lo_saudization_certificate_page.validate_saudi_certificate_title() \
        .validate_view_certificate_btn() \
        .validate_resend_certificate_btn() \
        .validate_back_to_est_hyper_link()

    qiwa.lo_saudization_certificate_page.validate_issue_date(expected_issue_date) \
        .validate_expiry_date(expected_expiry_date) \
        .validate_certificate_number(expected_certificate_number)
