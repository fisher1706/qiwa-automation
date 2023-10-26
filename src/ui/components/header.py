from __future__ import annotations

import allure
from selene import have, be
from selene.support.shared.jquery_style import s, ss

from data.constants import Language


class Header:
    dropdown_language = ss('[data-component="MenuTrigger"] p')
    links = ss("[data-component='Menu'] a")
    language_links = {
        Language.EN: links.first,
        Language.AR: links.second,
    }
    profile = s("[data-testid='menu-trigger'] p")
    dropdown_profile = ss("[data-component='Menu'] > div")

    def _select_language(self, language: str):
        element = self.language_links[language]
        if not element.matching(have.attribute("[data-component='Icon']")):
            element.click()

    @allure.step
    def change_local(self, language: str) -> Header:
        # TODO: [dp] Adjust changing language after fix issue with different AR text
        language_tags = ['ع', 'AR'] if language == Language.EN else ['EN']
        self.dropdown_language.first.wait_until(be.visible)
        elements = [self.dropdown_language.element_by(have.exact_text(el)) for el in language_tags]
        for dropdown, tag in zip(elements, language_tags):
            if dropdown.matching(have.exact_text(tag)):
                dropdown.click()
                self._select_language(language)
        return self

    @allure.step
    def check_personal_number_or_name(self, personal_number: str) -> Header:
        self.profile.should(have.text(personal_number))
        return self

    @allure.step
    def click_on_menu(self) -> Header:
        self.profile.click()
        return self

    @allure.step
    def click_on_logout(self) -> Header:
        self.dropdown_profile.element(-1).click()
        return self
