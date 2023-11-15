from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import add_delegation_data, general_data
from src.ui.components.code_verification import CodeVerification
from utils.random_manager import RandomManager


class PartnerApprovalPage:
    page_title = s('p[data-testid="SendCodeTitle"]')
    title_on_unavailable_flow = s('p[data-testid="RequestNoValidTitle"]')
    subtitle_on_unavailable_flow = s('p[data-testid="RequestNoValidSubTitle"]')
    description_on_unavailable_flow = s('p[data-testid="RequestNoValidDescription"]')
    send_verification_code_button = s('button[data-testid="SendCodeAction"]')
    verification_code_modal = CodeVerification(s('[data-testid="AbsherVerificationModal"]'))
    title_on_verification_code_modal = s('p[data-testid="AbsherVerificationModalTitle"]')
    description_on_verification_code_modal = s('p[data-testid="AbsherVerificationModalSubTitle"]')
    phone_number_text_on_verification_code_modal = s(
        'p[data-testid="AbsherVerificationModalPhoneNumber"]'
    )
    sms_code_text = s("label#sms-code-label")
    verification_code_modal.resend_sms_code_link = s(
        'a[data-testid="AbsherVerificationModalResend"]'
    )
    cancel_button = s('button[data-testid="AbsherVerificationModalClose"]')
    text_after_resend_sms = s("p.fLOcEJ")
    title_on_delegation_request = s('p[data-testid="PartnerApprovalFlowTitle"]')
    delegation_request_details = s('p[data-testid="PartnerApprovalFlowSubTitle"]')
    message_on_delegation_request = s('div[data-component="Message"]')
    approve_button = ss('div[data-component="ButtonGroup"] button').first
    reject_button = ss('div[data-component="ButtonGroup"] button').second
    buttons = ss('div[data-component="ButtonGroup"] button')
    confirmation_modal = s("div.kKXbuO")
    title_on_reject_modal = s("p.gkqahJ")
    reason_label_on_reject_modal = s('label[for="reason"]')
    description_on_reject_modal = s("p.gBHkze")
    reason_input = s("textarea#reason")
    close_button = s('button[aria-label="Close modal"]')
    reject_request_button = s("button.kFdvBb")
    go_back_button = s("button.jFDBnQ")
    reject_reason_characters_counter = s('[data-component="TextArea"] div.fWzNNl p')
    title_on_approve_modal = s("p.kmUukb")
    approve_request_button = s("div.kKXbuO button.bVUOtX")
    title_on_result_screen = s("p.hyJIZr")
    description_on_result_screen = s("p.dEyufF")

    @allure.step
    def wait_partner_approval_page_to_load(self) -> PartnerApprovalPage:
        self.page_title.should(have.exact_text(general_data.TITLE_ON_PARTNER_APPROVAL))
        return self

    @allure.step
    def should_partner_approval_flow_be_not_available(self) -> PartnerApprovalPage:
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/request-no-valid"))
        self.title_on_unavailable_flow.should(
            have.exact_text(general_data.TITLE_ON_UNAVAILABLE_FLOW)
        )
        self.subtitle_on_unavailable_flow.should(
            have.exact_text(general_data.SUBTITLE_ON_UNAVAILABLE_FLOW)
        )
        self.description_on_unavailable_flow.should(
            have.exact_text(general_data.DESCRIPTION_ON_UNAVAILABLE_FLOW)
        )
        return self

    @allure.step
    def click_send_verification_code_button(self) -> PartnerApprovalPage:
        self.send_verification_code_button.click()
        return self

    @allure.step
    def should_verification_code_modal_be_displayed(
        self, phone_number: str
    ) -> PartnerApprovalPage:
        self.should_verification_code_modal_be_opened()
        self.title_on_verification_code_modal.should(
            have.exact_text(general_data.TITLE_ON_PARTNER_APPROVAL)
        )
        self.description_on_verification_code_modal.should(
            have.exact_text(general_data.DESCRIPTION_ON_VERIFICATION_CODE_MODAL)
        )
        self.phone_number_text_on_verification_code_modal.should(have.text(phone_number))
        self.sms_code_text.should(
            have.exact_text(general_data.SMS_CODE_TEXT_ON_VERIFICATION_CODE_MODAL)
        )
        return self

    @allure.step
    def should_verification_code_modal_be_opened(self) -> PartnerApprovalPage:
        self.verification_code_modal.web_element.should(be.visible)
        return self

    @allure.step
    def should_verification_code_modal_be_hidden(self) -> PartnerApprovalPage:
        self.verification_code_modal.web_element.should(be.not_.visible)
        return self

    @allure.step
    def should_delegation_request_screen_be_opened(self) -> PartnerApprovalPage:
        self.title_on_delegation_request.should(
            have.exact_text(general_data.TITLE_ON_DELEGATION_REQUEST)
        )
        return self

    @allure.step
    def should_delegation_request_screen_be_displayed(self, duration: str) -> PartnerApprovalPage:
        self.should_delegation_request_screen_be_opened()
        self.message_on_delegation_request.should(
            have.exact_text(general_data.MESSAGE_ON_DELEGATION_REQUEST.format(duration))
        )
        return self

    @allure.step
    def should_delegation_request_data_be_correct(
        self,
        employee_name: str,
        employee_job: str,
        employee_nid: str,
        establishment_name: str,
        cr_number: str,
    ):
        self.delegation_request_details.should(
            have.exact_text(
                general_data.DELEGATION_REQUEST_TEXT.format(
                    employee_name,
                    employee_job,
                    employee_nid,
                    establishment_name,
                    cr_number,
                    add_delegation_data.PERMISSION.lower(),
                    add_delegation_data.ENTITY_NAME,
                )
            )
        )

    @allure.step
    def should_text_after_resend_sms_be_displayed(self) -> PartnerApprovalPage:
        self.text_after_resend_sms.should(have.exact_text(general_data.TEXT_AFTER_RESEND_SMS))
        return self

    @allure.step
    def click_cancel_button_on_verification_code_modal(self) -> PartnerApprovalPage:
        self.cancel_button.click()
        return self

    @allure.step
    def click_reject_button(self) -> PartnerApprovalPage:
        self.reject_button.click()
        return self

    @allure.step
    def click_approve_button(self) -> PartnerApprovalPage:
        self.approve_button.click()
        return self

    @allure.step
    def should_reject_confirmation_modal_be_opened(self) -> PartnerApprovalPage:
        self.confirmation_modal.should(be.visible)
        self.title_on_reject_modal.should(
            have.exact_text(
                general_data.TITLE_ON_CONFIRMATION_MODAL_PARTNER_FLOW.format(
                    general_data.REJECT_TEXT.lower()
                )
            )
        )
        self.reason_label_on_reject_modal.should(have.exact_text(general_data.REASON_TEXT))
        self.description_on_reject_modal.should(
            have.exact_text(general_data.REJECT_REASON_DESCRIPTION)
        )
        return self

    @allure.step
    def should_approve_confirmation_modal_be_opened(self) -> PartnerApprovalPage:
        self.confirmation_modal.should(be.visible)
        self.title_on_approve_modal.should(
            have.exact_text(
                general_data.TITLE_ON_CONFIRMATION_MODAL_PARTNER_FLOW.format(
                    general_data.APPROVE_TEXT.lower()
                )
            )
        )
        return self

    @allure.step
    def should_approve_confirmation_modal_be_closed(self) -> PartnerApprovalPage:
        self.confirmation_modal.should(be.not_.visible)
        return self

    @allure.step
    def click_close_button(self) -> PartnerApprovalPage:
        self.close_button.click()
        return self

    @allure.step
    def click_go_back_button(self) -> PartnerApprovalPage:
        self.go_back_button.click()
        return self

    @allure.step
    def enter_reject_reason(
        self, characters_number: int, counter_text: str
    ) -> PartnerApprovalPage:
        reject_reason = RandomManager().random_eng_string(letters_quantity=characters_number)
        self.reason_input.clear().type(reject_reason)
        self.reject_reason_characters_counter.should(
            have.exact_text(counter_text.format(characters_number))
        )
        self.reject_request_button.should(be.enabled)
        return self

    @allure.step
    def click_reject_request_button(self) -> PartnerApprovalPage:
        self.reject_request_button.click()
        return self

    @allure.step
    def click_approve_request_button(self) -> PartnerApprovalPage:
        self.approve_request_button.click()
        return self

    @allure.step
    def check_redirect_to_final_page(self, status: str) -> PartnerApprovalPage:
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/{status}"))
        return self

    @allure.step
    def should_content_be_displayed_on_final_page(self, title_text: str) -> PartnerApprovalPage:
        self.title_on_result_screen.should(have.exact_text(title_text))
        self.description_on_result_screen.should(
            have.exact_text(general_data.DESCRIPTION_AFTER_PARTNER_FLOW)
        )
        return self
