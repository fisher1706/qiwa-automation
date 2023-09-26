import allure
from selene import be, browser, have, query
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys

from data.lmi.constants import DimensionsInfo


class ResultDetailsPage:
    RESULT_BUTTON = s('//button[@data-testid="result"]')
    SPINNER_RESULT_DOWNLOAD = s('//i[@class="fas fa-sync-alt fa-spin"]')
    CREATE_NEW_LINK_BUTTON = s(
        '//button[@class="q-btn btn-sync-s ml-3 mr-3"][contains (text(), "Create new link")]'
    )
    LINK_NAMES_COLUMN = '//td[@data-label="Name"]//span[@style]'
    LINK_EDIT_BUTTON = s('//button[contains (text(), "Edit")]')
    DELETE_BUTTON = s('//button[contains (text(), "Delete")]')
    SURVEY_LINK = s('//span[@class="link-holder has-tooltip"]')
    VIEWS_COLUMN = s('//td[@data-label="Views"]//span[@style]')
    SPINNER_LANDING = s('//div[@class="loading-icon"]')
    MESSAGE = s('//div[@role="alert"]//div[@class="text"]')
    CONFIRMATION_MODAL = s('//div[@class="animation-content modal-content"]')
    NAME_FIELD_MODAL = s('//input[@type="text"]')
    DELETE_BUTTON_MODAL = s('//*[@data-testid][contains (text(),"Delete")]')
    CANCEL_BUTTON_MODAL = s('//*[contains (text(),"Cancel")]')
    SUBMIT_BUTTON = s('//button[@type="submit"]')

    def fill_link_name_field(self, link_name):
        self.CONFIRMATION_MODAL.wait_until(be.visible)
        link_name_field = self.NAME_FIELD_MODAL
        link_name_field.press(Keys.CONTROL + "a")
        link_name_field.press(Keys.DELETE)
        link_name_field.set_value(link_name)

    def click_on_cancel_link_button_modal(self):
        self.CONFIRMATION_MODAL.wait_until(be.visible)
        self.CANCEL_BUTTON_MODAL.click()

    def check_created_link(self, link_name):
        link_names = []
        for name in ss(self.LINK_NAMES_COLUMN):
            link_names.append(name.get(query.text))
        assert link_name in link_names, "Link not created"

    def check_delete_link(self, link_name):
        link_names = []
        for name in ss(self.LINK_NAMES_COLUMN):
            link_names.append(name.get(query.text))
        assert link_name not in link_names, "Link not deleted"

    @allure.step("Download result xlsx")
    def download_result_xlsx(self):
        self.RESULT_BUTTON.click()
        self.SPINNER_RESULT_DOWNLOAD.wait_until(be.visible)
        self.SPINNER_RESULT_DOWNLOAD.wait_until(be.not_.visible)

    @allure.step("Create new link")
    def create_new_link(self):
        self.CREATE_NEW_LINK_BUTTON.click()
        self.fill_link_name_field(DimensionsInfo.NAME_EN_TEXT)
        self.SUBMIT_BUTTON.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.CREATE_LINK_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        self.check_created_link(DimensionsInfo.NAME_EN_TEXT)

    @allure.step("Delete link")
    def delete_link(self):
        self.DELETE_BUTTON.click()
        self.CONFIRMATION_MODAL.wait_until(be.visible)
        self.DELETE_BUTTON_MODAL.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.DELETE_LINK_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        self.check_delete_link(DimensionsInfo.NAME_EN_TEXT)

    @allure.step("Edit new link")
    def edit_link(self):
        self.LINK_EDIT_BUTTON.click()
        self.fill_link_name_field(DimensionsInfo.NAME_EN_TEXT_EDIT)
        self.SUBMIT_BUTTON.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.EDIT_LINK_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        s(self.LINK_NAMES_COLUMN).should(have.exact_text(DimensionsInfo.NAME_EN_TEXT_EDIT))

    @allure.step("Activation of counter")
    def check_counter(self):
        self.SURVEY_LINK.click()
        intended_value = int(self.VIEWS_COLUMN.get(query.text)) + 1
        self.MESSAGE.should(have.exact_text(DimensionsInfo.COPY_LINK_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        browser.execute_script(f"window.open('{self.SURVEY_LINK.get(query.text)}','_blank');")
        self.SPINNER_LANDING.wait_until(be.visible)
        self.SPINNER_LANDING.wait_until(be.not_.visible)
        browser.switch_to_tab(0)
        browser.driver.refresh()
        self.VIEWS_COLUMN.wait_until(be.visible)
        changed_value = int(self.VIEWS_COLUMN.get(query.text))
        assert intended_value == changed_value, (
            f"Incorrect views values: intended_value = {intended_value},"
            f" changed_value = {changed_value}"
        )
