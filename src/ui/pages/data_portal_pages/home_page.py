import dataclasses

from selene import be, browser, have, query
from selene.support.shared.jquery_style import s, ss

from data.data_portal.constants import Links, Variables


@dataclasses.dataclass
class TrendingStatsBlockLocators:
    TITLE = s('//div[@class="description-block-content"]//h2')
    DESCRIPTION = ss('//div[@class="description-block-content"]/div[2]')
    EXPLORE_STATS_TITLE = s('//div[@class="description-block-card"]/div[1]')
    EXPLORE_CARD_TITLE = s('//div[@class="description-block-card"]/div[2]/div[1]')
    MARKET_OVERVIEW = s('//button[@class="round-button dark"]')


@dataclasses.dataclass
class InsightBlockLocators:
    TITLE = s('(//h3[@class="heading-03 md-heading-02"])[1]')
    DESCRIPTION = s('//p[@class="body-01-paragraph md-body-large-paragraph dark_sub-title"]')
    EXPLORE_BUTTON = s('(//a[@class="button button-secondary button-regular"])[1]')
    SLIDER_VALUES = s('//div[@class="num-01 md-num-01"]')

    SLIDER_LIST_DESCRIPTIONS = ss('//div[@class="insights-slider-list"]//p')
    VIEW_REPORT_BUTTON = '(//a[@class="large primary link d-flex align-items-center underline font-weight-500"])[{0}]'
    FORWARD_BUTTON_NAV = s('(//div[@class="navigation-buttons d-flex"]//button)[2]')
    BACK_BUTTON_NAV = s('(//div[@class="navigation-buttons d-flex"]//button)[1]')


@dataclasses.dataclass
class SolutionBlockLocators:
    TITLE = s('//section[@id="solution-block"]/div/div[2]')
    DESCRIPTION = s('//section[@id="solution-block"]//p')
    ITEM_TITLE = ss('//div[@class="tiles-item"]//h3')
    ITEM_DESCRIPTION = ss('//div[@class="tiles-item"]//p')


@dataclasses.dataclass
class TrustBlockLocators:
    TITLE = s("#trust-block h3")
    DESCRIPTION = s('//div[@class="trust-info"]//p')
    INFO_DATA = ss('//span[@class="body-02-highlight"]')
    SECTOR_DATA = s('(//span[@class="num-02 lg-num-01"])[1]')
    USER_OF_QIWA_DATA = s('(//span[@class="num-02 lg-num-01"])[2]')
    VOLUME_DATA = s('(//span[@class="num-02 lg-num-01"])[3]')
    PROVIDED = ss('//div[@class="provided-block-title d-flex flex-column"]/span')


@dataclasses.dataclass
class SubscribeBlockLocators:
    TITLE = s('//section[@class="subscription"]//h4')
    DESCRIPTION = s('//section[@class="subscription"]//p')
    EMAIL_FIELD = s('//div[@class="subscription-content-form"]//input')
    BUTTON = s('//div[@class="subscription-content-form"]//button')
    MESSAGE = s('//div[@class="snackbar snackbar-advanced"]//span')


class HomePage:
    QIWA_LOGO = s('//img[@alt="Qiwa Logo"]')
    HERO_TITLE = ss('//section[@class="hero"]//h1')
    HERO_DESCRIPTION = s('//section[@class="hero"]//p')
    MARKET_OVERVIEW = s('//section[@class="hero"]//a')

    BLOCK_DATA_HERO_1 = s("a:nth-child(1) > div.body-02-highlight")
    BLOCK_DATA_HERO_2 = s('(//span[@class="d-block d-sm-none d-xl-block"])[1]')
    BLOCK_DATA_HERO_3 = s('(//span[@class="d-block d-sm-none d-xl-block"])[2]')

    EXPLORE_BUTTON_1 = s('(//div[contains(@class, "link underline")])[1]')
    EXPLORE_BUTTON_2 = s('(//div[contains(@class, "link underline")])[2]')
    EXPLORE_BUTTON_3 = s('(//div[contains(@class, "link underline")])[3]')

    VIEW_ALL_SECTORS_BUTTON = s('//a[@class="button button-regular button-secondary"]')
    CONTACT_US_BUTTON = s('//section[@class="request-block "]//a')

    CHART_EXPLORE_BUTTON = s('//div[@class="chart-block-content"]/a')
    SECTORS_LIST = s('[class*="flex sector-list"]')

    def check_navigation_to_market_overview_from_hero(self):
        self.MARKET_OVERVIEW.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_market_overview_from_growth_block(self):
        self.BLOCK_DATA_HERO_1.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_market_overview_from_empl_block(self):
        self.BLOCK_DATA_HERO_2.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_market_overview_from_estab_block(self):
        self.BLOCK_DATA_HERO_3.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    @staticmethod
    def check_navigation_to_market_overview_from_trending_block():
        TrendingStatsBlockLocators.MARKET_OVERVIEW.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_finance_sector(self):
        self.CHART_EXPLORE_BUTTON.click()
        assert browser.driver.current_url == Links.FINANCE_SECTOR

    def check_navigation_to_all_sectors_page(self):
        self.VIEW_ALL_SECTORS_BUTTON.click()
        assert browser.driver.current_url == Links.VIEW_ALL_SECTORS

    @staticmethod
    def check_navigation_to_market_overview_from_insight():
        InsightBlockLocators.EXPLORE_BUTTON.click()
        assert browser.driver.current_url == Links.MARKET_OVERVIEW

    def check_navigation_to_contact_us_page(self):
        self.CONTACT_US_BUTTON.click()
        assert browser.driver.current_url == Links.CONTACT_US

    def check_elements_on_the_page(self, elements, list_text, navigation_button=None):
        elements_list = []
        self.SECTORS_LIST.should(be.visible)
        for element in elements:
            elements_list.append(element.get(query.text))
            if navigation_button:
                navigation_button.click()
        assert elements_list == list_text, f"{elements_list}\n{list_text}"

    def check_insight_block_navigation(self):
        for i in range(1, 5):
            s(InsightBlockLocators.VIEW_REPORT_BUTTON.format(i)).click()
            assert browser.driver.current_url == Links.MARKET_OVERVIEW
            self.QIWA_LOGO.click()
            for _ in range(i):
                InsightBlockLocators.FORWARD_BUTTON_NAV.click()

    @staticmethod
    def check_subscribe_request(message):
        SubscribeBlockLocators.EMAIL_FIELD.set_value(Variables.EMAIL)
        SubscribeBlockLocators.BUTTON.click()
        SubscribeBlockLocators.MESSAGE.should(have.text(message))
