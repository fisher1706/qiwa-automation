import allure
from selene import be, query
from selene.support.shared.jquery_style import s, ss

from data.lmi.constants import LandingInfo


class LandingPage:
    BLOCK_ON_LANDING = '//div[@class="card"]//h3[@class="card--headline"][text()="{0}"]'
    RETAIL_SECTOR_BLOCK = s(
        '//h5[@class="report-card--headline"][contains (text(),"The Retail Sector")]'
    )
    VIEW_FULL_REPORT_BUTTON = s('//button[@class="report-button"]')
    COMPANY_LIST = s(
        '//div[@class="environment-result"]//*[text()="All Retail Establishments results"]'
    )
    TOP_COMPANIES_BLOCK = s('//div[@class="overall-main"]//div[@selecteddimension="totalIndex"]')
    COMPANY = s('//*[@class="company-link"]')
    ENVIRONMENT_RANKING = s('//div[@class="environment-ranking"]')
    INDEXES_VALUES = ss('//span[@class="ep-legend--value__counter"]//span')

    def __init__(self):
        self.indexes_value = []

    def get_retail_indexes_value(self, overall_index):
        self.RETAIL_SECTOR_BLOCK.click()
        for indexes_value in self.INDEXES_VALUES:
            self.indexes_value.append(indexes_value.get(query.text))
        assert overall_index == self.indexes_value[0], "Published Overall indexes not matched"

    @allure.step("Check unhidden Labor Market Statistics Block")
    def check_labor_market_statistics_block(self):
        s(self.BLOCK_ON_LANDING.format(LandingInfo.LABOR_MARKET_STATISTICS_BLOCK)).should(
            be.visible
        )

    @allure.step("Check unhidden All Retail Establishments results Block")
    def check_company_list(self):
        s(self.BLOCK_ON_LANDING.format(LandingInfo.WORK_ENVIRONMENT_QUALITY_INDEX_BLOCK)).click()
        self.VIEW_FULL_REPORT_BUTTON.click()
        self.COMPANY_LIST.should(be.visible)

    @allure.step("Check unhidden Labor Market Top companies Block")
    def check_top_companies_block(self):
        s(self.BLOCK_ON_LANDING.format(LandingInfo.WORK_ENVIRONMENT_QUALITY_INDEX_BLOCK)).click()
        self.VIEW_FULL_REPORT_BUTTON.click()
        self.TOP_COMPANIES_BLOCK.should(be.visible)

    @allure.step("Check unhidden Ranking for company")
    def check_ranking_block(self):
        s(self.BLOCK_ON_LANDING.format(LandingInfo.WORK_ENVIRONMENT_QUALITY_INDEX_BLOCK)).click()
        self.VIEW_FULL_REPORT_BUTTON.click()
        self.COMPANY.click()
        self.ENVIRONMENT_RANKING.should(be.visible)
