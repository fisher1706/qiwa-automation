import allure
from selene import be, have, query
from selene.support.shared.jquery_style import s

from data.lmi.constants import DimensionsInfo


class RetailSectorWeqPage:
    RECALCULATE_RESULT_BUTTON = s('//button[@data-testid="recalculate"]')
    PUBLISH_RESULT_BUTTON = s('//button[@data-testid="redirect"][text()=" Publish results "]')
    OVERALL_INDEX = s(
        '(//*[@data-testid="overall"]//span[@class="q-circle-chart__text-holder"])[1]'
    )
    SPINNER = s('//div[@class="row"]//span[@class="q-spinner-inner"]')
    WEQ_TAB = s('//*[@class="icon-services"]')
    MESSAGE = s('//div[@role="alert"]//div[@class="text"]')

    def __init__(self):
        self.overall_index = None

    def check_overall_index(self, calculated_index):
        self.overall_index = float(self.OVERALL_INDEX.get(query.text))
        assert self.overall_index == calculated_index, "Calculated Overall indexes not matched"

    @allure.step("Recalculation and compare overall index")
    def recalculation_overall_index(self):
        self.WEQ_TAB()
        self.RECALCULATE_RESULT_BUTTON.click()
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)
        self.MESSAGE.should(have.exact_text(DimensionsInfo.RECALCULATION_SUCCESS_MESSAGE))

    @allure.step("Publishing result")
    def publishing_result(self):
        self.PUBLISH_RESULT_BUTTON.should(be.clickable).click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.PUBLISHING_SUCCESS_MESSAGE))
