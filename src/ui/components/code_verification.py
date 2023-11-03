from __future__ import annotations

import allure
from selene import be, have
from selene.core.entity import Element
from selene.support.shared.jquery_style import s


class CodeVerification:
    def __init__(self, web_element=None):
        self.web_element = web_element if web_element else s('[data-component="Modal"]')
        self.code_cells = self.web_element.all("input")
        self.text_rows = self.web_element.all("p")
        self.confirm_button = self.web_element.all('[data-component="Button"]').first
        self.resend_sms_code_link = self.web_element.element('[href="/registration"]')
        self.span_elements = self.web_element.all("span")

    def cell(self, index) -> Element:
        return self.code_cells.element(index=index)

    def counter(self, index: int) -> Element:
        return self.span_elements.element(index=index - 1)

    @allure.step
    def fill_in_code(self, code: str = "0000") -> CodeVerification:
        for index, digit in enumerate(code):
            self.cell(index=index).set_value(digit)
        return self

    @allure.step
    def click_resend_sms_code(self) -> CodeVerification:
        self.resend_sms_code_link.with_(timeout=60).wait_until(be.present)
        self.resend_sms_code_link.click()
        return self

    @allure.step
    def resend_sms_code_link_should_have_text(self, index: int = 5, seconds: str = 42) -> None:
        self.counter(index).should(have.exact_text(f"Resend SMS code ({seconds})"))

    @allure.step
    def click_confirm_button(self) -> CodeVerification:
        self.confirm_button.click()
        return self

    @allure.step
    def alert_message_should_have_text(self, line_index: int, message: str) -> None:
        self.text_rows.element(index=line_index + 1).should(have.exact_text(message))
