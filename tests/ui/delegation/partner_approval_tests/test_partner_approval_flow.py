import allure

from data.delegation import general_data
from data.delegation.users import establishment_owner_with_one_partner
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import (
    check_sms_after_sending_otp_code,
    get_delegation_request,
    login_as_establishment_owner,
)
from tests.ui.delegation.partner_approval_tests.conftest import (
    check_updated_delegation_status,
    prepare_data_for_partner_approval_flow,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Verify 'Send verification code' modal")
@case_id(71541, 71543)
def test_send_verification_code_modal():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button() \
        .should_verification_code_modal_be_displayed(phone_number=prepared_data["formattedPhoneNumber"]) \
        .verification_code_modal.resend_sms_code_link_should_have_text(index=2, seconds=50)
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    check_sms_after_sending_otp_code(phone_number=prepared_data["partnerPhoneNumber"], otp_code=otp_code)
    qiwa.delegation_partner_approval_page.verification_code_modal.fill_in_code(otp_code).click_confirm_button()
    qiwa.delegation_partner_approval_page.should_delegation_request_screen_be_opened()


@allure.title("Verify resend SMS")
@case_id(71548)
def test_resend_sms_on_verification_code_modal():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button() \
        .verification_code_modal.click_resend_sms_code()
    qiwa.delegation_partner_approval_page.should_text_after_resend_sms_be_displayed() \
        .verification_code_modal.resend_sms_code_link_should_have_text(index=2, seconds=50)
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    check_sms_after_sending_otp_code(phone_number=prepared_data["partnerPhoneNumber"], otp_code=otp_code)


@allure.title("Verify 'Cancel' button on the Verification code modal")
@case_id(71549)
def test_verification_code_modal_is_closed():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button() \
        .should_verification_code_modal_be_opened().click_cancel_button_on_verification_code_modal() \
        .should_verification_code_modal_be_hidden() \
        .click_send_verification_code_button().should_verification_code_modal_be_opened()


@allure.title("Verify data on the delegation request")
@case_id(71504)
def test_delegation_request_data():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button()
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    qiwa.delegation_partner_approval_page.verification_code_modal.fill_in_code(otp_code).click_confirm_button()
    qiwa.delegation_partner_approval_page.should_delegation_request_screen_be_displayed(
        duration=general_data.TWELVE_MONTHS_DURATION_STR) \
        .should_delegation_request_data_be_correct(employee_name=prepared_data["employeeName"],
                                                   employee_job=prepared_data["employeeJob"],
                                                   employee_nid=prepared_data["employeeNid"],
                                                   establishment_name=general_data.ESTABLISHMENT_NAME,
                                                   cr_number=general_data.ESTABLISHMENT_CR_NUMBER)


@allure.title("Verify approval flow by partner")
@case_id(71493)
def test_approval_flow_by_partner():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button()
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    qiwa.delegation_partner_approval_page.verification_code_modal.fill_in_code(otp_code).click_confirm_button()
    qiwa.delegation_partner_approval_page.should_delegation_request_screen_be_opened() \
        .click_approve_button().should_approve_confirmation_modal_be_opened() \
        .click_approve_request_button().check_redirect_to_final_page(status=general_data.APPROVED.lower()) \
        .should_content_be_displayed_on_final_page(general_data.TITLE_AFTER_APPROVE_FLOW)
    check_updated_delegation_status(qiwa_api=qiwa_api, delegation_id=prepared_data["delegationId"],
                                    expected_status=general_data.ACTIVE)


@allure.title("Verify confirmation modal is closed")
@case_id(71550)
def test_delegation_request_confirmation_modal_is_closed():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button()
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    qiwa.delegation_partner_approval_page.verification_code_modal.fill_in_code(otp_code).click_confirm_button()
    qiwa.delegation_partner_approval_page.should_delegation_request_screen_be_opened() \
        .click_approve_button().should_approve_confirmation_modal_be_opened() \
        .click_close_button().should_approve_confirmation_modal_be_closed() \
        .click_approve_button().should_approve_confirmation_modal_be_opened() \
        .click_go_back_button().should_approve_confirmation_modal_be_closed()


@allure.title("Verify reject flow by partner")
@case_id(71551)
def test_reject_flow_by_partner():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    prepared_data = prepare_data_for_partner_approval_flow(
        qiwa_api=qiwa_api, employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
        duration=general_data.TWELVE_MONTHS_DURATION)
    qiwa.delegation_partner_approval_page.click_send_verification_code_button()
    otp_code = get_delegation_request(delegation_id=prepared_data["delegationId"],
                                      status=general_data.PENDING).otp_code
    qiwa.delegation_partner_approval_page.verification_code_modal.fill_in_code(otp_code).click_confirm_button()
    qiwa.delegation_partner_approval_page.should_delegation_request_screen_be_opened() \
        .click_reject_button().should_reject_confirmation_modal_be_opened() \
        .enter_reject_reason(characters_number=254, counter_text=general_data.CHARACTERS_COUNTER) \
        .enter_reject_reason(characters_number=255, counter_text=general_data.CHARACTERS_LIMIT_REACHED_COUNTER) \
        .click_reject_request_button().check_redirect_to_final_page(status=general_data.REJECTED.lower()) \
        .should_content_be_displayed_on_final_page(general_data.TITLE_AFTER_REJECT_FLOW)
    check_updated_delegation_status(qiwa_api=qiwa_api, delegation_id=prepared_data["delegationId"],
                                    expected_status=general_data.REJECTED)
