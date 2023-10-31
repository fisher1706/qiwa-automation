from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s

from data.delegation import general_data


class ResendModal:
    resend_modal = s('div[data-testid="ResendModal"]')
    title_on_modal = s('p[data-testid="ResendModalTitle"]')
    description_on_modal = s('p[data-testid="ResendModalDescription"]')
    message_on_resend_modal = s('div[data-component="Message"]')
    resend_button_on_modal = s('button[data-testid="ResendModalAction"]')
    cancel_button_on_resend_modal = s('button[data-testid="ResendModalClose"]')
    close_button_on_modal = s('button[aria-label="Close modal"]')

    @allure.step
    def should_resend_confirmation_modal_be_displayed(
        self,
    ) -> ResendModal:
        self.resend_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.RESEND_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.RESEND_MODAL_DESCRIPTION))
        self.message_on_resend_modal.should(have.exact_text(general_data.RESEND_MODAL_MESSAGE))
        self.resend_button_on_modal.should(have.exact_text(general_data.RESEND_BUTTON))
        self.cancel_button_on_resend_modal.should(have.exact_text(general_data.CANCEL_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_resend_request_button(self) -> ResendModal:
        self.resend_button_on_modal.click()
        return self

    @allure.step
    def click_cancel_button_on_resend_modal(self) -> ResendModal:
        self.cancel_button_on_resend_modal.click()
        return self

    @allure.step
    def should_resend_confirmation_modal_be_hidden(self) -> ResendModal:
        self.resend_modal.should(be.not_.visible)
        return self
