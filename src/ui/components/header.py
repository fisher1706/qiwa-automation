from __future__ import annotations

import allure
from selene import have
from selene.support.shared.jquery_style import s, ss

from data.constants import Language


class Header:
    # TODO: [dp] Adjust changing language
    dropdown_lang = ss('[data-component="MenuTrigger"] p')
    links = ss("[data-component='Menu'] a")
    lang_links = {
        Language.EN: links.first,
        Language.AR: links.second,
    }
    profile = s("[data-testid='menu-trigger'] p")
    dropdown_profile = ss("[data-component='Menu'] > div")

    def _select_language(self, lang_value: str):
        local = self.lang_links[lang_value]
        if not local.matching(have.attribute("[data-component='Icon']")):
            local.click()

    @allure.step
    def change_local(self, lang_value: str) -> Header:
        language = 'ع' if lang_value == Language.EN else 'EN'
        dropdown = self.dropdown_lang.element_by(have.exact_text(language))
        if dropdown.matching(have.exact_text(language)):
            dropdown.click()
            self._select_language(lang_value)
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
