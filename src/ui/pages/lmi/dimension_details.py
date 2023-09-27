import allure
from selene import be, have, query
from selene.support.shared.jquery_style import s, ss

from data.lmi.constants import DimensionsInfo


class DimensionDetailsPage:
    MESSAGE = s('//div[@role="alert"]//div[@class="text"]')
    ADD_QUESTION_BUTTON = s('//button[@data-testid="add"]')
    ADD_ATTACHED_QUESTION_SS_BUTTON = s('//div[text()="Dropdown"]/../..//button')
    ADD_ATTACHED_QUESTION_QP_BUTTON = s('//div[text()="Multiple Choice Select one"]/../..//button')
    ADD_QUESTION_MODAL_BUTTON = s(
        '//button[@class="q-btn q-btn--small"][contains (text(), "Add")]'
    )
    QUESTIONS_NAME_COLUMN = '//div[@data-testid="question-name"]'
    ATTACHED_QUESTION_SS = s('//div[text()="Dropdown"]')
    ATTACHED_QUESTION_QP = s('//div[text()="Multiple Choice Select one"]')
    QUESTIONS_NAME_DIMENSION = '//p[@data-testid="dimension-name"][@class="mr-5 mb-1 mt-1"]'
    REMOVE_QUESTION_BUTTON = s('//button[@class="q-btn q-btn--small"]/span')
    EDIT_BUTTON = '//*[contains(text(), "{0}")]/..//following-sibling::div/button[1]'
    CONFIRMATION_MODAL = s('//div[@class="animation-content modal-content"]')
    DELETE_BUTTON_MODAL = s('//*[@data-testid][contains (text(),"Delete")]')
    CANCEL_BUTTON_MODAL = s('//*[contains (text(),"Cancel")]')
    CLOSE_CONFIRMATION_MODAL = s('//button[@class="modal-close is-large"]')
    SPINNER = s('//span[@class="q-spinner-inner"]')

    def __init__(self):
        self.question_name = None

    def check_attached_question(self):
        questions_dimension_name = []
        dimension_questions = ss(self.QUESTIONS_NAME_DIMENSION)
        for question_dimension_name in dimension_questions:
            questions_dimension_name.append(question_dimension_name.get(query.text))
        assert self.question_name in questions_dimension_name, "Question wasn't attached"

    @allure.step("Attach question")
    def attach_question_to_dimension(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        question_name = s(self.QUESTIONS_NAME_COLUMN).get(query.text)
        self.ADD_QUESTION_BUTTON.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.ADD_QUESTION_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        s(self.QUESTIONS_NAME_DIMENSION).should(have.exact_text(question_name))

    @allure.step("Attach questions")
    def attach_questions_to_dimension(self, message):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.question_name = s(self.QUESTIONS_NAME_COLUMN).get(query.text)
        for _ in range(7):
            self.ADD_QUESTION_BUTTON.click()
            self.MESSAGE.should(have.exact_text(message))
            self.check_attached_question()

    @allure.step("Detach question")
    def detach_question_from_dimension(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        question_name = s(self.QUESTIONS_NAME_DIMENSION).get(query.text)
        self.REMOVE_QUESTION_BUTTON.click()
        self.CONFIRMATION_MODAL.hover()
        self.DELETE_BUTTON_MODAL.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.DETACH_QUESTION_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        s(self.QUESTIONS_NAME_DIMENSION).should(have.no.exact_text(question_name))

    @allure.step("Attach already attached question")
    def attach_already_attached_question(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT_EDIT)).click()
        self.SPINNER.should(be.visible)
        self.SPINNER.should(be.not_.visible)
        if self.ATTACHED_QUESTION_QP.matching(be.visible):
            question_name = self.ATTACHED_QUESTION_QP.get(query.text)
            self.ADD_ATTACHED_QUESTION_QP_BUTTON.click()
        else:
            question_name = self.ATTACHED_QUESTION_SS.get(query.text)
            self.ADD_ATTACHED_QUESTION_SS_BUTTON.click()
        self.CONFIRMATION_MODAL.hover()
        self.ADD_QUESTION_MODAL_BUTTON.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.ADD_QUESTION_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        s(self.QUESTIONS_NAME_DIMENSION).should(have.exact_text(question_name))

    @allure.step("Cancellation attach already attached question")
    def cancel_attach_already_attached_question(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT_EDIT)).click()
        self.SPINNER.should(be.visible)
        self.SPINNER.should(be.not_.visible)
        if self.ATTACHED_QUESTION_QP.matching(be.visible):
            question_name = self.ATTACHED_QUESTION_QP.get(query.text)
            self.ADD_ATTACHED_QUESTION_QP_BUTTON.click()
        else:
            question_name = self.ATTACHED_QUESTION_SS.get(query.text)
            self.ADD_ATTACHED_QUESTION_SS_BUTTON.click()
        self.CONFIRMATION_MODAL.hover()
        self.CLOSE_CONFIRMATION_MODAL.click()
        s(self.QUESTIONS_NAME_DIMENSION).should(have.no.exact_text(question_name))

    @allure.step("Cancel Detach question")
    def cancel_detach_question_from_dimension(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        question_name = s(self.QUESTIONS_NAME_DIMENSION).get(query.text)
        self.REMOVE_QUESTION_BUTTON.click()
        self.CONFIRMATION_MODAL.hover()
        self.CANCEL_BUTTON_MODAL.click()
        s(self.QUESTIONS_NAME_DIMENSION).should(have.exact_text(question_name))
