from __future__ import annotations

import allure
from selene import Element, be
from selene.support.shared import browser


class FeedbackPopup:
    popup = browser.element(".modal")

    def __init__(self):
        self._iframe = None

    @property
    def iframe(self) -> Element:
        if not self._iframe:
            browser.switch_to.frame(self.popup.element("iframe").should(be.visible)())
            self._iframe = browser.element("body")
        return self._iframe

    @allure.step
    def close_feedback(self):
        self.iframe.element(".demo__shutter").click()
        browser.switch_to.default_content()
