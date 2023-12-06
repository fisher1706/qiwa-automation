import allure
import pytest

from data.constants import Language, OtpMessage
from data.dedicated.enums import SearchingType
from data.dedicated.models.services import Service, saudi_certificate
from data.lo.constants import ServicesInfo
from data.shareable.saudization_certificate.saudi_certificate import *
from src.api.app import QiwaApi
from src.api.controllers.appointment import AppointmentsApiController
from src.api.controllers.ibm import IBMApiController, ibm_api_controller
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


def login(user: User, service: Service):
    # cancel current appointment
    api = QiwaApi.login_as_user(user.personal_number)
    api.visits_api.cancel_active_visit(user.personal_number)

    # create a new appointment
    booking_id = ibm_api_controller.get_appointment_id(user, service)

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
@allure.title('AS-343, AS-368, AS-376 Check if user in different nitaqat color can issue saudi certificate')
@case_id(99864, 99882, 99891)
def test_verify_user_can_issue_saudi_certificate(user: User):
    # login step
    login(user, saudi_certificate)

    qiwa.business_page.select_saudization_certificate()
    qiwa.lo_saudization_certificate_page.issue_saudi_certificate()

    # validate on UI elements in dashboard
    qiwa.lo_saudization_certificate_page.validate_back_to_est_hyper_link() \
        .validate_dashboard_title() \
        .validate_dashboard_sub_title()

    qiwa.email_popup.proceed_otp_code().click_on_proceed_button()
    qiwa.lo_saudization_certificate_page.check_expected_success_message(SUCCESSFUL_ISSUING_MESSAGE)

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
        .validate_expiry_date(date_after_90_days) \
        .validate_certificate_status_to_be_active()


@allure.title('AS-344 Verify the establishment not in Nitaqat cannot book an appointment')
@case_id(99865)
def test_if_establishment_not_included_in_nitaqat():
    AppointmentsApiController().check_invalid_response(lo_sc_nitaqat_not_included, saudi_certificate,
                                                       not_in_nitaqat_appointment_rs)

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
    qiwa.labor_office_appointments_create_page.select_service(ServicesInfo.SAUDI_CERTIFICATE_SERVICE) \
        .select_sub_service(ServicesInfo.SAUDI_CERTIFICATE_SUB_SERVICE)

    # validate on the error message
    qiwa.labor_office_appointments_create_confirmation_page.validate_error_message(
        not_in_nitaqat_appointment_rs.EnglishMsg)


@allure.title('AS-367 Verify that the establishment with red NITAQAT level cannot book the appointment')
@case_id(99866)
def test_if_establishment_has_red_nitaqat():
    AppointmentsApiController().check_invalid_response(lo_sc_red_nitaqat, saudi_certificate, red_nitaqat_appointment_rs)

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
    qiwa.labor_office_appointments_create_page.select_service(ServicesInfo.SAUDI_CERTIFICATE_SERVICE) \
        .select_sub_service(ServicesInfo.SAUDI_CERTIFICATE_SUB_SERVICE)

    # validate on the error message
    qiwa.labor_office_appointments_create_confirmation_page.validate_error_message(
        UNSUCCESSFUL_ISSUING_MESSAGE_RED_NITAQAT)


@allure.title('AS-373, AS-374 Check UI OTP modal elements')
@case_id(99888, 99890)
def test_check_otp_ui_module():
    # login step
    login(lo_sc_user, saudi_certificate)

    # validate UI elements on otp module
    qiwa.business_page.select_saudization_certificate()
    qiwa.lo_saudization_certificate_page.issue_saudi_certificate()
    qiwa.lo_saudization_certificate_page \
        .validate_otp_messages(OtpMessage.TITLE, OtpMessage.PROMPT,
                               OtpMessage.CONFIRMATION) \
        .validate_otp_proceed_btn_is_disabled() \
        .validate_otp_resend_sms_is_disabled() \
        .validate_otp_resend_email_is_disabled() \
        .validate_otp_fields_are_enabled()
    # validate invalid otp message and proceed btn is disabled
    qiwa.email_popup.proceed_otp_code("1111")
    qiwa.lo_saudization_certificate_page.validate_wrong_otp().validate_otp_proceed_btn_is_disabled()
    # user able to re-write the otp once again
    qiwa.email_popup.proceed_otp_code("2222")
