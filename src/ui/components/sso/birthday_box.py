from __future__ import annotations

import allure
from selene.support.shared.jquery_style import s


class BirthdayBoxes:
    day_box = s("#birth-date-0")
    month_box = s("#birth-date-1")
    year_box = s('input[id="birth-date-2"]')

    @allure.step
    def insert_birthday(self, day: str, month: str, year: str) -> BirthdayBoxes:
        self.day_box.set_value(day)
        self.month_box.set_value(month)
        self.year_box.set_value(year)
        return self
