import pytest

from data.sso import messages as messages
from data.sso import account_data_constants as users_data
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.random_manager import RandomManager

case_id = project(TestmoProject.QIWA_SSO)


@case_id(41924)
def test_user_sign_in_into_qiwa(first_account_data):
    account = first_account_data
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(first_account_data.personal_number) \
        .enter_password(first_account_data.password) \
        .click_login_button()
    qiwa.login_page.otp_pop_up.fill_in_code(first_account_data.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.workspace_page.wait_page_to_load() \
        .should_have_workspace_list_appear()


@case_id(41926)
def test_user_without_birthdate_sign_in_to_qiwa_sso(account_without_hijiri_birth_day):
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(account_without_hijiri_birth_day.personal_number) \
        .enter_password(account_without_hijiri_birth_day.password) \
        .click_login_button()
    qiwa.add_birth_day_page.add_birthday_title_should_have_correct_text() \
        .add_birthday_message_should_have_correct_text(messages.ADD_BIRTHDAY_MESSAGE) \
        .insert_birthday(day="01", month="01", year="1430") \
        .click_add_to_your_account_button()
    qiwa.login_page.otp_pop_up.fill_in_code(account_without_hijiri_birth_day.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.workspace_page.wait_page_to_load() \
        .should_have_workspace_list_appear()


@case_id(41927, 41932, 41940)
def test_user_without_phone_number_sign_in_to_qiwa_sso(account_without_phone):
    new_phone = RandomManager().random_phone_number(prefix="")
    account_with_out_phone = account_without_phone
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(account_with_out_phone.personal_number) \
        .enter_password(account_with_out_phone.password) \
        .click_login_button()
    qiwa.change_phone_number_page.insert_identity_number(account_with_out_phone.personal_number)
    qiwa.change_phone_number_page.birthdate_boxes.insert_birthday(day="01", month="01", year="1430")
    qiwa.change_phone_number_page.click_continue_button()
    qiwa.login_page.absher_pop_up.fill_in_code(code=account_with_out_phone.absher_confirmation_code) \
        .click_confirm_button()
    qiwa.change_phone_number_page.fill_new_phone_number_field(new_phone_number=new_phone) \
        .click_continue_button()
    qiwa.login_page.otp_pop_up.fill_in_code(code=account_with_out_phone.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.login_page.enter_login(account_with_out_phone.personal_number) \
        .enter_password(account_with_out_phone.password) \
        .click_login_button()
    qiwa.login_page.otp_pop_up.fill_in_code(code=account_with_out_phone.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.workspace_page.wait_page_to_load() \
        .should_have_workspace_list_appear()


@case_id(41929)
def test_user_with_unconfirmed_email_sign_into_qiwa_sso(account_with_unconfirmed_email_status):
    account = account_with_unconfirmed_email_status
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(account.personal_number) \
        .enter_password(account.password) \
        .click_login_button()
    qiwa.login_page.otp_pop_up.fill_in_code(account.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.secure_account_page.click_continue_button() \
        .verify_email_box.fill_in_code(account.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.workspace_page.wait_page_to_load() \
        .should_have_workspace_list_appear()


@case_id(41930)
def test_confirmation_code_is_resent_after_clicking_resend_sms_code_button(first_account_data):
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(first_account_data.personal_number) \
        .enter_password(first_account_data.password) \
        .click_login_button() \
        .otp_pop_up.click_resend_sms_code() \
        .resend_sms_code_link_should_have_text()


@case_id(41937)
def test_captcha_is_displayed_after_entering_incorrect_password_three_times(second_account_data):
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    account = second_account_data
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(account.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.enter_login(account.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.enter_login(account.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.recaptcha_should_be_visible()


@case_id(57505)
@pytest.mark.xfail(reasone="functionality could change")
def test_check_that_account_is_locked_after_four_times_login_with_wrong_credentials(first_account_data):
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    account_unlock = first_account_data
    for _ in range(6):
        qiwa.login_page.wait_login_page_to_load() \
            .enter_login(account_unlock.personal_number) \
            .enter_password(users_data.INVALID_PASSWORD) \
            .click_login_button()
    qiwa.login_page.enter_login(account_unlock.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.enter_login(account_unlock.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.enter_login(account_unlock.personal_number) \
        .enter_password(users_data.INVALID_PASSWORD) \
        .click_login_button()
    qiwa.login_page.unlock_account_message_should_have_text(messages.YOU_ACCOUNT_LOCK)
    qiwa.login_page.unlock_account_button_should_be_visible()


@case_id(41939)
def test_verify_user_is_change_phone_number_if_number_is_associated_with_another_account(first_account_data,
                                                                                         prepare_data_for_sign_in_with_expired_phone):
    new_phone = RandomManager().random_phone_number(prefix="")
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    user_account = prepare_data_for_sign_in_with_expired_phone
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(user_account.personal_number) \
        .enter_password(user_account.password) \
        .click_login_button()
    qiwa.change_phone_number_page.insert_identity_number(user_account.personal_number)
    qiwa.change_phone_number_page.birthdate_boxes.insert_birthday(day="01", month="01", year="1430")
    qiwa.change_phone_number_page.click_continue_button()
    qiwa.login_page.absher_pop_up.fill_in_code(code=user_account.absher_confirmation_code) \
        .click_confirm_button()
    qiwa.change_phone_number_page.fill_new_phone_number_field(new_phone_number=new_phone) \
        .click_continue_button()
    qiwa.login_page.otp_pop_up.fill_in_code(code=first_account_data.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.login_page.enter_login(first_account_data.personal_number) \
        .enter_password(first_account_data.password) \
        .click_login_button()
    qiwa.login_page.otp_pop_up.fill_in_code(code=first_account_data.otp_confirmation_code) \
        .click_confirm_button()
    qiwa.workspace_page.wait_page_to_load() \
        .should_have_workspace_list_appear()


@case_id(41947)
def test_check_functionality_when_user_enter_incorrect_otp_code_four_times_in_row(first_account_data):
    qiwa.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_page.wait_login_page_to_load() \
        .enter_login(first_account_data.personal_number) \
        .enter_password(first_account_data.password) \
        .click_login_button() \
        .otp_pop_up.fill_in_code("1234") \
        .click_confirm_button()
    qiwa.login_page.otp_pop_up.fill_in_code("1234") \
        .click_confirm_button()
    qiwa.login_page.otp_pop_up.fill_in_code("1234") \
        .click_confirm_button()
    qiwa.login_page.otp_pop_up.fill_in_code("1234") \
        .click_confirm_button() \
        .alert_message_should_have_text(line_index=2, message=messages.TOO_MANY_OTP_ATTEMPTS)
