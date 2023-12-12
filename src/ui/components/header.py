from __future__ import annotations

import allure
from selene.support.shared.jquery_style import s, ss

from data.constants import Language
from utils.allure import allure_steps


@allure_steps
class Header:
    def __init__(self, web_element=None):
        self.web_element = web_element if web_element else s('[data-component="Navigation"]')
        self.dropdown_language = s(
            '//*[@data-component="Navigation"]//p[contains(text(), "AR") or '
            'contains(text(), "EN") or contains(text(), "ع")]'
        )
        self.en_lang_btn = s('//p[contains(text(), "English (EN)")]')
        self.ar_lang_btn = s(
            '//p[contains(text(), "(AR) عربي") or contains(text(), "العربية (AR)")]'
        )
        self.links = ss("[data-component='Menu'] a")
        self.profile = self.web_element.s("[data-testid='menu-trigger'] p")
        self.profile_individuals = self.web_element.ss('[data-component="MenuTrigger"] p')[2]
        self.dropdown_profile = ss("[data-component='Menu'] > div > div")

    @allure.step
    def change_local(self, language: str) -> Header:
        self.dropdown_language.click()
        if language == Language.EN:
            self.en_lang_btn.click()
        elif language == Language.AR:
            self.ar_lang_btn.click()
        return self

    def click_on_menu(self) -> Header:
        self.profile.click()
        return self

    def click_on_menu_individuals(self) -> Header:
        self.profile_individuals.click()
        return self

    def click_on_logout(self) -> Header:
        self.dropdown_profile.element(-1).click()
        return self
