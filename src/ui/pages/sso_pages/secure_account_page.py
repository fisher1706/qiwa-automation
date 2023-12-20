from __future__ import annotations

import allure
from selene import have
from selene.support.shared.jquery_style import s, ss

from src.ui.components.code_verification import CodeVerification
from src.ui.components.raw.dropdown import Dropdown


class SecureAccountPage:
    title = s(".hyJIZr")
    message = s(".kEsfaI .iPxNsA")
    continue_button = s(".jkFNbI")
    first_question_dropdown = Dropdown(
        element=ss('input[id="test-id-0"]').first, option_element_locator='[id=":r3:-list"]'
    )
    verify_email_box = CodeVerification(s(".eOPJMF"))

    @allure.step
    def secure_account_page_should_have_title(self, title: str) -> SecureAccountPage:
        self.title.should(have.exact_text(title))
        return self

    @allure.step
    def click_continue_button(self) -> SecureAccountPage:
        self.continue_button.click()
        return self

    @allure.step
    def select_mothers_first_name_question(self):
        self.first_question_dropdown.select_by_index(index=1)
