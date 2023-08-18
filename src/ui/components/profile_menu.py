from __future__ import annotations

import allure
from selene import Element


class UserProfileMenu:
    def __init__(self, web_element: Element):
        self.web_element = web_element

    @allure.step
    def click_on_menu(self) -> UserProfileMenu:
        self.web_element.click()
        return self

    @allure.step
    def click_on_logout(self):
        self.web_element.all("a")[-1].click()
