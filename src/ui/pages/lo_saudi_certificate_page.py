from selene import be, have, query
from selene.support.shared.jquery_style import s, ss


class LoSaudiCertificatePage:
    certificate_issuance_btn = s('.c-certificate-issuance button')
    validation_message = s('.c-summary-message')
    certification_details = ss('.c-certificate-details__center span.c-certificate-details__item-value')
    certificate_details_after = {
        "number": s("(//span[@class='c-certificate-details__item-value'])[1]"),
        "issue_date": s("(//span[@class='c-certificate-details__item-value'])[2]"),
        "expiry_date": s("(//span[@class='c-certificate-details__item-value'])[3]"),
        "cr_number": s("(//span[@class='c-certificate-details__item-value'])[5]"),
        "unified_number": s("(//span[@class='c-certificate-details__item-value'])[6]"),
    }
    view_certificate_btn = s('.c-certificate-details__top')
    resend_certificate_btn = s('.c-certificate-details__resend button')
    saudi_certificate_title = s('.c-certificate-details__top-title')
    back_to_est_hyper_link = s('.back-link')
    dashboard_details = {
        'header': s(".c-service-header__left-heading "),
        'sub_header': s(".c-service-header__left-subheading")
    }
    otp_module = {
        'otp_head': s('.c-otp-modal__modal h2'),
        'otp_required': s('p.c-otp-modal__label:nth-of-type(1)'),
        'otp_to_email_details': s('p.c-otp-modal__label:nth-of-type(2)'),
        'otp_input_first_cell': s("(//div[@class='otp-input-group']//input)[1]"),
        'otp_input_second_cell': s("(//div[@class='otp-input-group']//input)[2]"),
        'otp_input_third_cell': s("(//div[@class='otp-input-group']//input)[3]"),
        'otp_input_forth_cell': s("(//div[@class='otp-input-group']//input)[4]"),
        'proceed_btn': s('.o-modal__actions > button'),
        'resend_email_btn': s("(//div[@class='o-modal__resend-buttons']//button)[1]"),
        'resend_sms_btn': s("(//div[@class='o-modal__resend-buttons']//button)[2]"),
        'otp_validation_message': s('.c-otp-modal__input p')
    }
    certificate_details_before = {
        "issue_date": s("(//section[@class='c-service-details']//span)[1]"),
        "expiry_date": s("(//section[@class='c-service-details']//span)[2]"),
        "number": s("(//section[@class='c-service-details']//span)[3]")
    }

    def issue_saudi_certificate(self):
        self.certificate_issuance_btn.click()
        return self

    def get_expected_success_message(self, success_message: str):
        self.validation_message.should(be.visible).should(have.exact_text(success_message))
        return self

    def validate_cr_number(self, expected_cr_number: str):
        self.certificate_details_after['cr_number'].should(be.existing).should(have.exact_text(expected_cr_number))
        return self

    def validate_certificate_number(self, expected_certificate_number: str):
        self.certificate_details_after['number'].should(be.existing).should(have.exact_text(expected_certificate_number))
        return self

    def validate_unified_est_number(self, expected_uni_number):
        self.certificate_details_after['unified_number'].should(be.existing).should(have.exact_text(expected_uni_number))
        return self

    def validate_issue_date(self, expected_issue_date):
        self.certificate_details_after['issue_date'].should(be.existing).should(have.exact_text(expected_issue_date))
        return self

    def validate_expiry_date(self, expected_expiry_date):
        self.certificate_details_after['expiry_date'].should(be.existing).should(have.exact_text(expected_expiry_date))
        return self

    def validate_otp_messages(self, exp_header: str, exp_sub_header: str, exp_email_msg: str):
        self.otp_module['otp_head'].should(have.exact_text(exp_header))
        self.otp_module['otp_required'].should(have.exact_text(exp_sub_header))
        self.otp_module['otp_to_email_details'].should(have.text(exp_email_msg))
        return self

    def validate_otp_proceed_btn_is_disabled(self):
        self.otp_module['proceed_btn'].should(have.css_class('o-button--disabled'))
        return self

    def validate_otp_resend_email_is_disabled(self):
        self.otp_module['resend_email_btn'].should(have.css_class('o-button--disabled'))
        return self

    def validate_otp_resend_sms_is_disabled(self):
        self.otp_module['resend_sms_btn'].should(have.css_class('o-button--disabled'))
        return self

    def validate_otp_fields_are_enabled(self):
        self.otp_module['otp_input_first_cell'].should(be.visible).should(be.enabled)
        self.otp_module['otp_input_second_cell'].should(be.visible).should(be.enabled)
        self.otp_module['otp_input_third_cell'].should(be.visible).should(be.enabled)
        self.otp_module['otp_input_forth_cell'].should(be.visible).should(be.enabled)
        return self

    def validate_wrong_otp(self):
        self.otp_module['otp_validation_message'].should(be.visible).should(
            have.text("OTP is wrong. Try again or resend email to the client."))
        return self

    def validate_view_certificate_btn(self):
        self.view_certificate_btn.should(be.visible).should(be.clickable)
        return self

    def validate_resend_certificate_btn(self):
        self.resend_certificate_btn.should(be.visible).should(be.clickable)
        return self

    def validate_saudi_certificate_title(self):
        self.saudi_certificate_title.should(be.visible)
        return self

    def validate_back_to_est_hyper_link(self):
        assert "lo-agent-system.qiwa.info/appointment" in self.back_to_est_hyper_link.get(query.attribute('href'))
        return self

    def validate_dashboard_title(self):
        self.dashboard_details['header'].should(have.exact_text("Saudization Certificate"))
        return self

    def validate_dashboard_sub_title(self):
        self.dashboard_details['sub_header'].should(have.exact_text(
            "Saudization certificate states that the company has achieved the required Saudization rates based on Nitaqat."))
        return self

    def get_certificate_issue_date(self):
        return self.certificate_details_before["issue_date"].should(be.visible).get(query.text)

    def get_certificate_expiry_date(self):
        return self.certificate_details_before["expiry_date"].should(be.visible).get(query.text)

    def get_certificate_number(self):
        return self.certificate_details_before["number"].should(be.visible).get(query.text)
