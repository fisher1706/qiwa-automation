import allure
from selene import be, have, query
from selene.support.shared.jquery_style import s, ss

from data.constants import OtpMessage, SaudiCertificateDashboard


class LoSaudiCertificatePage:
    certificate_issuance_btn = s(".c-certificate-issuance button")
    validation_message = s(".c-summary-message")
    certification_details = ss(
        ".c-certificate-details__center span.c-certificate-details__item-value"
    )
    certificate_details_after = ss("//span[@class='c-certificate-details__item-value']")
    cer_number_after = certificate_details_after[0]
    cer_issue_date_after = certificate_details_after[1]
    cer_expiry_date_after = certificate_details_after[2]
    cer_status_after = certificate_details_after[3]
    cer_cr_number_after = certificate_details_after[4]
    cer_unified_number_after = certificate_details_after[5]

    view_certificate_btn = s(".c-certificate-details__top")
    resend_certificate_btn = s(".c-certificate-details__resend button")
    saudi_certificate_title = s(".c-certificate-details__top-title")
    back_to_est_hyper_link = s(".back-link")
    dashboard_details = {
        "header": s(".c-service-header__left-heading "),
        "sub_header": s(".c-service-header__left-subheading"),
    }
    otp_module = {
        "otp_head": s(".c-otp-modal__modal h2"),
        "otp_required": s("p.c-otp-modal__label:nth-of-type(1)"),
        "otp_to_email_details": s("p.c-otp-modal__label:nth-of-type(2)"),
        "otp_input_first_cell": s("(//div[@class='otp-input-group']//input)[1]"),
        "otp_input_second_cell": s("(//div[@class='otp-input-group']//input)[2]"),
        "otp_input_third_cell": s("(//div[@class='otp-input-group']//input)[3]"),
        "otp_input_forth_cell": s("(//div[@class='otp-input-group']//input)[4]"),
        "proceed_btn": s(".o-modal__actions > button"),
        "resend_email_btn": s("(//div[@class='o-modal__resend-buttons']//button)[1]"),
        "resend_sms_btn": s("(//div[@class='o-modal__resend-buttons']//button)[2]"),
        "otp_validation_message": s(".c-otp-modal__input p"),
    }
    certificate_details_before = ss("//section[@class='c-service-details']//span")
    cer_issue_date_before = certificate_details_before[0]
    cer_expiry_date_before = certificate_details_before[1]
    cer_number_before = certificate_details_before[2]

    @allure.step
    def issue_saudi_certificate(self):
        self.certificate_issuance_btn.click()
        return self

    @allure.step
    def check_expected_success_message(self, success_message: str):
        self.validation_message.should(be.visible).should(have.exact_text(success_message))
        return self

    @allure.step
    def validate_cr_number(self, expected_cr_number: str):
        self.cer_cr_number_after.should(be.existing).should(have.exact_text(expected_cr_number))
        return self

    @allure.step
    def validate_certificate_number(self, expected_certificate_number: str):
        self.cer_number_after.should(be.existing).should(
            have.exact_text(expected_certificate_number)
        )
        return self

    @allure.step
    def validate_unified_est_number(self, expected_uni_number):
        self.cer_unified_number_after.should(be.existing).should(
            have.exact_text(expected_uni_number)
        )
        return self

    @allure.step
    def validate_issue_date(self, expected_issue_date):
        self.cer_issue_date_after.should(be.existing).should(have.exact_text(expected_issue_date))
        return self

    @allure.step
    def validate_expiry_date(self, expected_expiry_date):
        self.cer_expiry_date_after.should(be.existing).should(
            have.exact_text(expected_expiry_date)
        )
        return self

    @allure.step
    def validate_certificate_status_to_be_active(self):
        self.cer_status_after.should(be.existing).should(have.exact_text("Active"))
        return self

    @allure.step
    def validate_otp_messages(self, exp_header: str, exp_sub_header: str, exp_email_msg: str):
        self.otp_module["otp_head"].should(have.exact_text(exp_header))
        self.otp_module["otp_required"].should(have.exact_text(exp_sub_header))
        self.otp_module["otp_to_email_details"].should(have.text(exp_email_msg))
        return self

    @allure.step
    def validate_otp_proceed_btn_is_disabled(self):
        self.otp_module["proceed_btn"].should(have.css_class("o-button--disabled"))
        return self

    @allure.step
    def validate_otp_resend_email_is_disabled(self):
        self.otp_module["resend_email_btn"].should(have.css_class("o-button--disabled"))
        return self

    @allure.step
    def validate_otp_resend_sms_is_disabled(self):
        self.otp_module["resend_sms_btn"].should(have.css_class("o-button--disabled"))
        return self

    @allure.step
    def validate_otp_fields_are_enabled(self):
        self.otp_module["otp_input_first_cell"].should(be.visible).should(be.enabled)
        self.otp_module["otp_input_second_cell"].should(be.visible).should(be.enabled)
        self.otp_module["otp_input_third_cell"].should(be.visible).should(be.enabled)
        self.otp_module["otp_input_forth_cell"].should(be.visible).should(be.enabled)
        return self

    @allure.step
    def validate_wrong_otp(self):
        self.otp_module["otp_validation_message"].should(be.visible).should(
            have.text(OtpMessage.ERROR)
        )
        return self

    @allure.step
    def validate_view_certificate_btn(self):
        self.view_certificate_btn.should(be.visible).should(be.clickable)
        return self

    @allure.step
    def validate_resend_certificate_btn(self):
        self.resend_certificate_btn.should(be.visible).should(be.clickable)
        return self

    @allure.step
    def validate_saudi_certificate_title(self):
        self.saudi_certificate_title.should(be.visible)
        return self

    @allure.step
    def validate_back_to_est_hyper_link(self):
        assert "lo-agent-system.qiwa.info/appointment" in self.back_to_est_hyper_link.get(
            query.attribute("href")
        )
        return self

    @allure.step
    def validate_dashboard_title(self):
        self.dashboard_details["header"].should(have.exact_text(SaudiCertificateDashboard.HEADER))
        return self

    @allure.step
    def validate_dashboard_sub_title(self):
        self.dashboard_details["sub_header"].should(
            have.exact_text(SaudiCertificateDashboard.SUB_HEADER)
        )
        return self

    @allure.step
    def get_certificate_issue_date(self):
        return self.cer_issue_date_before.should(be.visible).get(query.text)

    @allure.step
    def get_certificate_expiry_date(self):
        return self.cer_expiry_date_before.should(be.visible).get(query.text)

    @allure.step
    def get_certificate_number(self):
        return self.cer_number_before.should(be.visible).get(query.text)
