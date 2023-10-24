from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared import browser

from data.delegation import general_data


class DelegationToast:
    toast = browser.element('div[data-component="Toast"]')
    icon_on_toast = browser.element(
        'div[data-component="Toast"] > span[data-component="Icon"] > svg'
    )

    @allure.step
    def should_message_be_displayed(self, message: str, toast_color: str) -> DelegationToast:
        self.toast.should(have.text(message))
        self.icon_on_toast.should(be.visible)
        self.toast.should(
            have.css_property(name=general_data.BACKGROUND_COLOR_NAME, value=toast_color)
        )
        return self
