import dataclasses

from selene import have
from selene.support.shared.jquery_style import s

from data.dataportal.constants import EmployeesChart, EstablishmentsChart
from src.ui.pages.data_portal_pages.market_overview_page import (
    EmployeesChartLocators,
    EstablishmentsChartLocators,
)


@dataclasses.dataclass
class SectorPage:
    HERO_TITLE = s('//section[@class="hero-section"]//h3')
    EMPLOYEE_VALUES = s('(//section[@class="hero-section"]//*[@class="num-02"])[1]')
    ESTABLISH_VALUES = s('(//section[@class="hero-section"]//*[@class="num-02"])[2]')
    HERO_VALUES_DESCRIPTION = s('//span[@class="body-02-highlight xl-body-03-highlight"]')
    HERO_UPDATE = s('//section[@class="hero-section"]//p')

    """Finance sector chart"""
    CHART_EXPLORE_BUTTON = s('//div[@class="chart-block-content"]/a')
    CHART_TITLE = s('//section[@class="chart-block"]//h2')
    CHART_DESCRIPTION = s('//section[@class="chart-block"]//p')
    CHART_TITLE_HEADER = s('//div[@id="finance"]/div[1]')
    CHART_DROPDOWN = s('//ul[@class="dropdown-options"]')
    CHART_TYPE_SECTION = s('(//span[@class="body-03-short"])[1]')
    CHART_CALENDAR_SECTION = s('(//span[@class="body-03-short"])[2]')
    CHART_DROPDOWN_OPTIONS = s('//span[@class="body-03-paragraph"]')

    @staticmethod
    def define_action_from_dict(actions_dict, action):
        if action in actions_dict:
            actions_dict[action]()

    def check_incoming_data(self, element, text, action):
        if action:
            self.define_chart_action(action)
        element.should(have.text(text))

    def define_chart_action(self, arg):
        actions_dict = {
            EmployeesChart.GO_TO_GENDER_TAB: EmployeesChartLocators.GENDER_TAB.click(),
            EstablishmentsChart.PICK_UNIFIED_OPTION: self.pick_unified_option,
        }
        self.define_action_from_dict(actions_dict, arg)

    @staticmethod
    def pick_unified_option():
        EstablishmentsChartLocators.TYPE_DROPDOWN.click()
        EstablishmentsChartLocators.UNIFIED_OPTION.click()
