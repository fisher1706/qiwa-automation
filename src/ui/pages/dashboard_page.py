from __future__ import annotations

import allure
from selene import be, by
from selene.support.shared.jquery_style import s


class DashboardPage:
    switch_account_link = by.css(".dropdown-menu div:nth-child(1) > a")
    e_services_menu = by.xpath('//a[@href="https://e-services.qiwa.info/e-services"]')
    nitaqat_level = s('[data-component="NitaqatLevel"]')

    def click_on_switch_account_link(self) -> DashboardPage:
        s(self.switch_account_link).should(be.clickable).click()
        return self

    @allure.step
    def select_e_services_menu_item(self) -> DashboardPage:
        s(self.e_services_menu).click()
        return self

    @allure.step
    def wait_dashboard_page_to_load(self) -> DashboardPage:
        s('//p[.="Nitaqat Level"]').wait_until(be.visible)
        return self
