import allure
from selene import be, have
from selene.support.shared.jquery_style import s

from data.lmi.constants import QuestionActions, SurveysInfo


class DashboardSurveyPage:
    FAVORITE_SURVEY_CHECKBOX = s("#favorite")
    QUESTION_CODE = s('//*[@class="code"]')
    MAX_ANSWER_SCORE = s('//*[@class="code has-tooltip"]')
    QUESTION_TITLE = s('//span[@class="holder"]')
    SPINNER_SYNC = s('//*[@class="fas fa-sync-alt fa-spin"]')
    EMPTY_COLUMN = s('//*[@class="is-empty"]')

    SYNC_DROPDOWN = s('//*[@data-testid="label"][ text()=" Sync survey "]')
    SYNC_SURVEY_OPTION = '(//*[@data-testid="item"][ text()=" {0} "])[2]'
    SURVEY_ID = '//td[@data-label="Id"]//*[text()=" {0} "]'
    DETAILS_BUTTON = '//span[text()=" {0} "]/../../td[@data-label="Actions"]'
    QUESTION_TAB = s('//a/span[contains(text(), "Question")]')
    DASHBOARD_TAB = s('//*[@class="icon-dashboard"]')
    SPINNER = s('//div[@class="row"]//span[@class="q-spinner-inner"]')
    FAVORITE_BLOCK = '(//div[@class="q-page-box__content"])[1]//span[text()=" {0} "]'

    def perform_sync_survey(self, survey_resource):
        self.SYNC_DROPDOWN.click()
        s(self.SYNC_SURVEY_OPTION.format(survey_resource)).click()
        self.SPINNER_SYNC.wait_until(be.visible)
        self.SPINNER_SYNC.with_(timeout=600).wait_until(be.not_.visible)
        self.EMPTY_COLUMN.wait_until(be.visible)
        self.EMPTY_COLUMN.wait_until(be.not_.visible)

    def check_sync_survey_and_question(self, survey_id):
        s(self.SURVEY_ID.format(survey_id)).should(be.visible)
        s(self.DETAILS_BUTTON.format(survey_id)).click()
        self.QUESTION_TAB.wait_until(be.visible)
        self.QUESTION_TAB.click()
        self.QUESTION_TITLE.should(have.text(QuestionActions.TEST_QUESTION))

    def setup_to_individual_page(self):
        pass

    def check_favorite_checkbox(self):
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)
        self.FAVORITE_SURVEY_CHECKBOX.click()
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)

    @allure.step("Add survey to Favorite option")
    def add_survey_to_favorite_option(self, survey_id):
        survey_name = (
            SurveysInfo.SURVEY_SS_NAME
            if survey_id == SurveysInfo.SURVEYS_SS_ID
            else SurveysInfo.SURVEY_QPRO_NAME
        )
        self.check_favorite_checkbox()
        self.FAVORITE_SURVEY_CHECKBOX.should(have.attribute("data-test", "checked"))
        self.DASHBOARD_TAB.click()
        self.SPINNER.with_(timeout=2).wait_until(be.visible)
        s(self.FAVORITE_BLOCK.format(survey_name)).should(be.visible)

    @allure.step("Remove survey from Favorite option")
    def remove_survey_from_favorite_option(self, survey_id):
        survey_name = (
            SurveysInfo.SURVEY_SS_NAME
            if survey_id == SurveysInfo.SURVEYS_SS_ID
            else SurveysInfo.SURVEY_QPRO_NAME
        )
        self.check_favorite_checkbox()
        self.FAVORITE_SURVEY_CHECKBOX.should(have.attribute("data-test", "unchecked"))
        self.DASHBOARD_TAB.click()
        self.SPINNER.with_(timeout=2).wait_until(be.visible)
        s(self.FAVORITE_BLOCK.format(survey_name)).should(be.not_.visible)

    def add_survey_to_target_group(self):
        pass

    def remove_survey_from_target_group(self):
        pass
