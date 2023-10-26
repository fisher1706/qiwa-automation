from __future__ import annotations

import allure
from selene import have, query
from selene.support.shared.jquery_style import s

from src.ui.components.sso.birthday_box import BirthdayBoxes


class AddBirthdayPage:
    title = s(".hyJIZr")
    message = s(".kEsfaI .iPxNsA")
    birth_day_fields = BirthdayBoxes()
    add_to_your_account_button = s('button[type="submit"]')

    @allure.step
    def add_birthday_title_should_have_correct_text(self) -> AddBirthdayPage:
        self.title.should(have.exact_text("Add birthdate"))
        return self

    @allure.step
    def add_birthday_message_should_have_correct_text(self, message: str) -> AddBirthdayPage:
        self.message.get(query.text)
        self.message.should(have.exact_text(message))
        return self

    @allure.step
    def insert_birthday(self, day: str, month: str, year: str) -> AddBirthdayPage:
        self.birth_day_fields.insert_birthday(day=day, month=month, year=year)
        return self

    @allure.step
    def click_add_to_your_account_button(self) -> None:
        self.add_to_your_account_button.click()
