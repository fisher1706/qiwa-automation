from selene.support.conditions import be, have
from selene.support.shared.jquery_style import browser, s, ss

from data.data_portal.constants import Links


class HeaderBlock:
    QIWA_LOGO = s('//img[@alt="Qiwa Logo"]')
    LOCALIZATION = s('//div[@class="d-flex lang-switcher align-items-center light"]')
    DARK_MODE = s('//button[@class="d-flex align-items-center justify-content-center"]')
    SECTORS = s('//span[@class="mr-3"]')
    REPORTS = s('//div[@class="d-none d-sm-flex reports"]/a')
    SECTORS_DROPDOWN = s('//div[@class="sectors-menu d-flex flex-column justify-content-center"]')
    VIEW_ALL_SECTORS = s('//div[@class="sectors-menu-body-links"]/a/span')
    ISIC_4_CLASSIFICATION = s('[class^="sectors-menu-body-tabs"]>div:nth-child(1)>div')
    NITAQAT_CLASSIFICATION = s('[class^="sectors-menu-body-tabs"]>div:nth-child(2)>div')
    MARKET_OVERVIEW = s('//div[@class="d-flex header-left"]//a[@href="/market-overview"]')
    SECTORS_ITEM = ss('[class^="sectors-menu-body-links-link"]>a')
    SECTORS_BLOCK = s('[class^="flex align-items-baseline"]')

    def change_localization(self):
        self.LOCALIZATION.click()

    def setup_localization(self, localization):
        if self.LOCALIZATION.matching(have.text(localization)):
            self.change_localization()

    def check_element_on_the_page(self, element, element_text, open_dropdown=False):
        if open_dropdown:
            self.SECTORS.click()
        element.should(have.text(element_text))

    def check_navigation_to_all_sectors_page(self):
        self.VIEW_ALL_SECTORS.click()
        assert browser.driver.current_url == Links.VIEW_ALL_SECTORS

    def check_navigation_to_market_overview_page(self):
        self.MARKET_OVERVIEW.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_reports_page(self):
        self.REPORTS.click()
        assert browser.driver.current_url == Links.REPORTS

    def open_sectors_dropdown(self):
        self.SECTORS.click()
        self.SECTORS_BLOCK.should(be.visible)
