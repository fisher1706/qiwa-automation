from __future__ import annotations

from selene import be, by
from selene.support.shared.jquery_style import s


class DashboardPage:
    switch_account_link = by.css(".dropdown-menu div:nth-child(1) > a")
    e_services_menu = by.css('.q-navigation__list_item img[alt="E-services"]')
    nitaqat_level = s('[data-component="NitaqatLevel"]')

    def click_on_switch_account_link(self) -> DashboardPage:
        s(self.switch_account_link).should(be.clickable).click()
        return self

    def select_e_services_menu_item(self):
        s(self.e_services_menu).click()
        return self

    def wait_dashboard_page_to_load(self) -> DashboardPage:
        self.nitaqat_level.should(be.visible)
