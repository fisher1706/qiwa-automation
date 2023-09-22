from selene.api import be, s
from selene.support.shared import browser

from data.visa.constants import Languages


class BasePage:
    LANGUAGE_MENU_BUTTON = (
        '//button[contains(@class, "MenuTrigger") or contains(@class, "lang-switcher__trigger")]'
        '//p[contains(text(), "{}") or contains(text(), "{}")]'
    )
    LANGUAGE_MENU = '//button[contains(@class, "MenuTrigger")]//p[contains(text(), "{}")]'
    SWITCH_LANGUAGE_BOX = '//div[@class="tippy-box"]'
    SWITCH_LANGUAGE_BUTTON = './/p[contains(text(), "{}")]'
    current_language_english = s(LANGUAGE_MENU.format(Languages.ENGLISH))
    current_language_arabic = s(LANGUAGE_MENU.format(Languages.ARABIC))
    english_button = s(SWITCH_LANGUAGE_BOX).s(SWITCH_LANGUAGE_BUTTON.format(Languages.ENGLISH))
    arabic_button = s(SWITCH_LANGUAGE_BOX).s(SWITCH_LANGUAGE_BUTTON.format(Languages.ARABIC))
    quiz_popup_close_button = s('//div[contains(@class, "demo__shutter")]')
    quiz_popup_window = s('//div[contains(@class,"animation-content")]')
    quiz_popup = s('[title="iframe"]')

    def refresh_page(self):
        browser.driver.refresh()
        self.select_language(Languages.ENGLISH)
        return self

    def select_language(self, language):
        s(self.LANGUAGE_MENU_BUTTON.format(Languages.ENGLISH, Languages.ARABIC)).should(be.visible)
        if self.selected_language() == language:
            return
        self.current_language_box().click()
        self.english_button.should(be.visible)
        self.arabic_button.should(be.visible)
        if language == Languages.ENGLISH:
            self.english_button.click()
            return
        self.arabic_button.click()

    def selected_language(self):
        if self.current_language_arabic.with_(timeout=1).wait_until(be.visible):
            return Languages.ARABIC
        return Languages.ENGLISH

    def current_language_box(self):
        return s(self.SWITCH_LANGUAGE_BUTTON.format(self.selected_language()))

    def close_quiz_popup(self):
        if self.quiz_popup.with_(timeout=10).wait_until(be.visible):
            self.quiz_popup.wait_until(be.visible)
            browser.switch_to.frame(self.quiz_popup())
            self.quiz_popup_close_button.click()
            browser.switch_to.default_content()
            self.quiz_popup_window.should(be.hidden)
