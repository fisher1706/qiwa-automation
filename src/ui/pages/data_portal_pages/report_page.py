from selene import have
from selene.support.shared.jquery_style import s

from data.data_portal.constants import Reports


class ReportsPage:
    TITLE = s('//div[@class="reports-title"]/h3')
    TOPIC_TITLES = s('//div[@class="caption d-flex"]/p')
    TOPIC_DESCRIPTIONS = s('//div[@class="report-card-info"]/div[1]')

    INDICATORS_VIEW_MORE = s('(//div[@data-testid="report-category"]/div/a/span)[1]')
    SAUDI_ECONOMY_VIEW_MORE = s('(//div[@data-testid="report-category"]/div/a/span)[2]')
    ECONOMIC_RESEARCH_VIEW_MORE = s('(//div[@data-testid="report-category"]/div/a/span)[3]')

    MARKER_OVERVIEW_REPORT = s(
        '(//div[@class="current-report-category"][1]//button[@class="round-button dark"])[1]'
    )
    EMPLOYEE_TURNOVER_REPORT = s(
        '(//div[@class="current-report-category"][1]//button[@class="round-button dark"])[2]'
    )
    EMPLOYEE_TENURE_REPORT = s(
        '(//div[@class="current-report-category"][1]//button[@class="round-button dark"])[3]'
    )
    WORKPLACE_ENV_REPORT = s(
        '(//div[@class="current-report-category"][1]//button[@class="round-button dark"])[4]'
    )

    ESTABLISH_LABOR_REPORT = s(
        '(//div[@class="current-report-category"][2]//button[@class="round-button dark"])[1]'
    )
    ESTABLISH_SIZE_REPORT = s(
        '(//div[@class="current-report-category"][2]//button[@class="round-button dark"])[2]'
    )
    DISAGGREGATING_RATIO_REPORT = s(
        '(//div[@class="current-report-category"][2]//button[@class="round-button dark"])[3]'
    )
    GENDER_PRODUCTIVITY_REPORT = s(
        '(//div[@class="current-report-category"][3]//button[@class="round-button dark"])[1]'
    )
    SEVEN_LEVEL_REPORT = s(
        '(//div[@class="current-report-category"][3]//button[@class="round-button dark"])[2]'
    )
    ESTABLISH_SIZE_REPORT_2 = s(
        '(//div[@class="current-report-category"][3]//button[@class="round-button dark"])[3]'
    )

    def check_en_element_on_the_page(self):
        self.TITLE.should(have.text(Reports.TITLE_EN))

    def check_ar_element_on_the_page(self):
        self.TITLE.should(have.text(Reports.TITLE_AR))
