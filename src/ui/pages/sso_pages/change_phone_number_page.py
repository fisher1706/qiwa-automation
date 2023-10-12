from __future__ import annotations

import allure
from selene import have
from selene.support.shared.jquery_style import s

from src.ui.components.sso.bithday_box import BirthdayBoxes


class ChangePhoneNumberPage:
    title = s(".hyJIZr")
    identity_number_field = s("#absherId")
    birthdate_boxes = BirthdayBoxes()
    continue_button = s('button[type="submit"]')
    new_phone_number = s("#username")

    @allure.step
    def change_phone_title_should_have_correct_text(self, title: str) -> ChangePhoneNumberPage:
        self.title.should(have.exact_text(title))
        return self

    @allure.step
    def insert_identity_number(self, identity_number: str) -> ChangePhoneNumberPage:
        self.identity_number_field.set_value(identity_number)
        return self

    @allure.step
    def fill_in_birthdate_boxes(self, day: str, month: str, year: str):
        self.birthdate_boxes.insert_birthday(day, month, year)

    @allure.step
    def click_continue_button(self):
        self.continue_button.click()

    @allure.step
    def fill_new_phone_number_field(self, new_phone_number: str) -> ChangePhoneNumberPage:
        self.new_phone_number.set_value(new_phone_number)
        return self
