import allure
from selene.support.shared import browser

import config
from src.api.app import QiwaApi
from src.ui.pages.lmi.dashboard_survey import DashboardSurveyPage
from src.ui.pages.lmi.dimension_details import DimensionDetailsPage
from src.ui.pages.lmi.dimension_weq import DimensionWeqPage
from src.ui.pages.lmi.lmi_landing import LandingPage
from src.ui.pages.lmi.result_detail_survey import ResultDetailsPage
from src.ui.pages.lmi.retail_sector_weq import RetailSectorWeqPage
from src.ui.pages.lmi.survey_question import SurveyQuestionPage


class Lmi:
    def __init__(self):
        super().__init__()
        self.qiwa_api = QiwaApi()
        self.cookie = {}
        self.dashboard_survey = DashboardSurveyPage()
        self.dimension_details = DimensionDetailsPage()
        self.dimension_weq = DimensionWeqPage()
        self.lmi_landing = LandingPage()
        self.result_detail_survey = ResultDetailsPage()
        self.retail_sector_weq = RetailSectorWeqPage()
        self.survey_question = SurveyQuestionPage()
        self.lmi_landing = LandingPage()

    @allure.step
    def open_surveys_page(self):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys")

        return self

    @allure.step
    def open_general_survey_tab(self, survey):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys/detail-survey/{survey}?tab=general")
        return self

    @allure.step
    def open_send_survey_tab(self, survey):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys/detail-survey/{survey}?tab=send")
        return self

    @allure.step
    def open_result_survey_tab(self, survey):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys/detail-survey/{survey}?tab=result")
        return self

    @allure.step
    def open_question_survey_tab(self, survey):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys/detail-survey/{survey}?tab=question")
        return self

    @allure.step
    def open_dimension_survey_tab(self, survey):
        browser.open(f"{config.qiwa_urls.lmi_url}/surveys/detail-survey/{survey}?tab=dimension")
        return self

    @allure.step
    def open_weq_page(self):
        browser.open(f"{config.qiwa_urls.lmi_url}/weq?tab=retail")
        return self

    @allure.step
    def open_dimensions_weq_page(self):
        browser.open(f"{config.qiwa_urls.lmi_url}/dimensions")
        return self

    @allure.step
    def open_landing_page(self):
        browser.open(config.qiwa_urls.lmi_landing_url)
        return self

    def get_cookie(self):
        cookies = browser.driver.get_cookies()
        for cookie in cookies:
            if cookie["name"] == "qiwa.authorization":
                self.cookie = {"cookie": f'qiwa.authorization={cookie["value"]}'}

    def perform_preconditions(self):
        self.get_cookie()
        self.qiwa_api.dimensions_api_actions.delete_all_dimensions(self.cookie)


lmi = Lmi()
