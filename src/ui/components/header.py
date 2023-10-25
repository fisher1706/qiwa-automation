from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s, ss

from data.constants import Language


class Header:
    # TODO: [dp] Adjust changing language
    lang_dropdown = ss('[data-component="MenuTrigger"] p').first
    links = ss("[data-component='Menu'] a")
    lang_links = {
        Language.EN: links.first,
        Language.AR: links.second,
    }
    profile = s("[data-testid='menu-trigger'] p")

    @allure.step
    def change_local(self, lang_value) -> Header:
        self.lang_dropdown.wait_until(be.visible)
        self.lang_dropdown.click()
        local = self.lang_links[lang_value]
        if not local.matching(have.attribute("[data-component='Icon']")):
            local.click()
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
    def click_on_logout(self):
        self.profile.all("a")[-1].click()
