import random
from datetime import datetime

import allure
from selene import be, browser, have, query
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import Keys

from data.lmi.constants import DimensionsInfo, QuestionActions


class SurveyQuestionPage:
    QUESTION_WEIGHT_FIELD = s('//input[@data-testid="input"]')
    QUESTION_CODE = s('//*[@class="code"]')
    MAX_ANSWER_SCORE = s('//*[@class="code has-tooltip"]')
    ANSWER_WEIGHT_FIELD = '//input[@data-testid="input"][@data-child-weight]'
    RESET_WEIGHTS_BUTTON = s('//button[@data-testid="reset"]')
    CONFIRM_BUTTON = s('//button[@data-testid="confirm"]')
    BLUR_STATE = s('[class^="blur"]')
    QUESTION_OPTIONS = s('//h3[@class="tab-title d-flex align-items-center"]')
    SAVE_BUTTON = s('//*[@data-testid="save"]')
    NAME_FIELD_MODAL = s('//input[@type="text"]')
    SUBMIT_BUTTON = s('//button[@type="submit"]')
    MESSAGE = s('//div[@role="alert"]//div[@class="text"]')
    QUESTION_MESSAGE = s('//span[@class="ml-1"]')
    QUESTION_CODE_MESSAGE = s('//div[@class="mt-2 validation-error"]/b')

    def __init__(self):
        self.answer_weight = []
        self.configured_answers_scores = []
        self.gotten_answers_weight = []
        self.max_answer_score = None
        self.random_value = f"Test {datetime.now().strftime('%M.%S')}"
        self.random_float = random.uniform(1, 8)

    def add_question_weight(self, invalid_question_value=None):
        question_weight = invalid_question_value if invalid_question_value else self.random_float
        self.QUESTION_WEIGHT_FIELD.set_value(question_weight)
        self.SAVE_BUTTON.click()

    def add_answers_weight(self, invalid_answer_score=None):
        value = invalid_answer_score if invalid_answer_score else self.random_float
        self.QUESTION_OPTIONS.click()
        for answer_weight in ss(self.ANSWER_WEIGHT_FIELD):
            answer_weight.set_value(value)
            self.configured_answers_scores.append(value)
            value += 0.1
        self.max_answer_score = max(self.configured_answers_scores)
        self.SAVE_BUTTON.click()
        return self

    def get_answers_scores(self):
        gotten_answers_weight = []
        for answer_weight in ss(self.ANSWER_WEIGHT_FIELD):
            gotten_answers_weight.append(float(answer_weight.get(query.value)))
        return gotten_answers_weight

    def check_reset_values(self):
        self.QUESTION_OPTIONS.click()
        answer_score = self.get_answers_scores()[0]
        assert float(self.QUESTION_WEIGHT_FIELD.get(query.value)) == 0.0 and answer_score == 1.0

    def setup_question_weight(self):
        self.add_question_weight()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.UPDATE_WEIGHT_SUCCESS))
        self.MESSAGE.wait_until(be.not_.visible)
        assert (
            float(self.QUESTION_WEIGHT_FIELD.get(query.value)) == self.random_float
        ), "Question weight not matched"

    @allure.step("Setup answer weight")
    def setup_answer_weights(self):
        self.configured_answers_scores = []
        self.add_answers_weight()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.UPDATE_WEIGHT_SUCCESS))
        self.MESSAGE.wait_until(be.not_.visible)
        self.QUESTION_OPTIONS.click()
        assert (
            self.get_answers_scores() == self.configured_answers_scores
        ), "Answers scores not matched"

    @allure.step("Calculation max answer score")
    def calculation_max_answer_score(self):
        self.setup_answer_weights()
        assert self.max_answer_score == float(
            self.MAX_ANSWER_SCORE.get(query.text)
        ), "Answer score not matched"

    @allure.step("Change question code")
    def setup_question_code(self):
        self.QUESTION_CODE.click()
        self.NAME_FIELD_MODAL.press(Keys.CONTROL + "a").press(Keys.DELETE)
        self.NAME_FIELD_MODAL.set_value(self.random_value)
        self.SUBMIT_BUTTON.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.UPDATE_CODE_SUCCESS))
        self.MESSAGE.should(be.not_.visible)
        assert self.random_value == self.QUESTION_CODE.get(query.text), "Code not matched"

    @allure.step("Set invalid question value")
    def set_invalid_question_value(self, invalid_question_value):
        self.add_question_weight(invalid_question_value)
        self.QUESTION_MESSAGE.should(have.exact_text(QuestionActions.INVALID_QUESTION_VALUE))
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Set invalid answer score with closed answers dropdown")
    def set_invalid_answer_score_closed_dropdown(self, invalid_answer_score):
        self.add_answers_weight(invalid_answer_score)
        self.QUESTION_OPTIONS.click()
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Set invalid answer score")
    def set_invalid_answer_score(self, invalid_answer_score):
        self.QUESTION_OPTIONS.click()
        s(self.ANSWER_WEIGHT_FIELD).set_value(invalid_answer_score)
        self.QUESTION_MESSAGE.should(have.exact_text(QuestionActions.INVALID_ANSWER_SCORE))
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Set already exist question code")
    def set_already_exist_question_code(self):
        self.QUESTION_CODE.click()
        self.NAME_FIELD_MODAL.press(Keys.CONTROL + "a").press(Keys.DELETE)
        self.NAME_FIELD_MODAL.set_value("test")
        self.QUESTION_CODE_MESSAGE.should(have.exact_text("test"))
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Set invalid question code")
    def set_invalid_question_code(self, invalid_question_code):
        self.QUESTION_CODE.click()
        self.NAME_FIELD_MODAL.press(Keys.CONTROL + "a").press(Keys.DELETE)
        self.NAME_FIELD_MODAL.set_value(invalid_question_code)
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Reset weights")
    def reset_question_weight(self):
        self.RESET_WEIGHTS_BUTTON.click()
        self.CONFIRM_BUTTON.click()
        browser.driver.refresh()
