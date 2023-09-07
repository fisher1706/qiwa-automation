from selene import query
from selene.support.conditions import have
from selene.support.shared.jquery_style import browser, s, ss

from data.dataportal.constants import Links


class HeaderBlock:
    QIWA_LOGO = s('//img[@alt="Qiwa Logo"]')
    LOCALIZATION = s('//div[@class="d-flex lang-switcher align-items-center light"]')
    DARK_MODE = s('//button[@class="d-flex align-items-center justify-content-center"]')
    SECTORS = s('//span[@class="mr-3"]')
    REPORTS = s('//div[@class="d-none d-sm-flex reports"]/a')
    SECTORS_DROPDOWN = s('//div[@class="sectors-menu d-flex flex-column justify-content-center"]')
    VIEW_ALL_SECTORS = s('//div[@class="sectors-menu-body-links"]/a/span')
    ECONOMIC_ACTIVITIES = s('//div[@class="sectors-menu-body-tabs"]//div[1]/div')
    NITAQAT_ACTIVITIES = s('//div[@class="sectors-menu-body-tabs"]//div[2]/div')
    MARKET_OVERVIEW = s('//div[@class="d-flex header-left"]//a[@href="/market-overview"]')
    SECTORS_ITEM = ss('//a[@class="cta-small"]')

    def change_localization(self):
        self.LOCALIZATION.click()

    def setup_localization(self, localization):
        if self.LOCALIZATION.matching(have.text(localization)):
            self.change_localization()

    def check_element_on_the_page(self, element, element_text, open_dropdown=False):
        if open_dropdown:
            self.SECTORS.click()
        element.should(have.text(element_text))

    @staticmethod
    def check_elements_on_the_page(elements, list_text):
        elements_list = []
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text, f"{elements_list}\n{list_text}"

    def check_navigation_to_all_sectors_page(self):
        self.SECTORS.click()
        self.VIEW_ALL_SECTORS.click()
        assert browser.driver.current_url == Links.VIEW_ALL_SECTORS

    def check_navigation_to_market_overview_page(self):
        self.MARKET_OVERVIEW.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_reports_page(self):
        self.REPORTS.click()
        assert browser.driver.current_url == Links.REPORTS
