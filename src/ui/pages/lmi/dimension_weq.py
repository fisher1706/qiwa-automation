import allure
from selene import be, have
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys

from data.lmi.constants import DimensionsInfo


class DimensionWeqPage:
    CREATE_DIMENSION = s('//*[contains (text(),"Create new dimension")]')
    DELETE_DIMENSION = '//*[contains(text(), "{0}")]/..//following-sibling::div/button[2]'
    NAME_AR = s('//*[@data-testid="name"][@placeholder="أدخل اسم البعد"]')
    NAME_EN = s('//*[@data-testid="name"][@placeholder="Enter dimension name"][@class="input"]')
    EDIT_BUTTON = '//*[contains(text(), "{0}")]/..//following-sibling::div/button[1]'
    DELETE_BUTTON_MODAL = s('//*[@data-testid][contains (text(),"Delete")]')
    CANCEL_BUTTON_MODAL = s('//*[contains (text(),"Cancel")]')
    DIMENSION_TITLE = s('//*[@class="q-page-box__title"]')
    MESSAGE = s('//div[@role="alert"]//div[@class="text"]')
    SAVE_BUTTON = s('//*[@data-testid="save"]')
    BACK_HYPERLINK = s('//*[@class="back-link"]')
    DIMENSION_MESSAGE = s('//span[@class="error-message"]')

    def enter_dimension_name_en(self, name_en):
        dimension_name_en = self.NAME_EN
        dimension_name_en.wait_until(be.visible)
        dimension_name_en.press(Keys.CONTROL + "a")
        dimension_name_en.press(Keys.DELETE)
        dimension_name_en.set_value(name_en)

    def enter_dimension_name_ar(self, name_ar):
        dimension_name_ar = self.NAME_AR
        dimension_name_ar.wait_until(be.visible)
        dimension_name_ar.press(Keys.CONTROL + "a")
        dimension_name_ar.press(Keys.DELETE)
        dimension_name_ar.set_value(name_ar)

    def fill_dimension_names_fields(self, name_en, name_ar):
        self.enter_dimension_name_ar(name_ar)
        self.enter_dimension_name_en(name_en)
        self.SAVE_BUTTON.click()

    @allure.step("Create dimension")
    def create_new_dimension(self):
        self.CREATE_DIMENSION.click()
        self.fill_dimension_names_fields(DimensionsInfo.NAME_EN_TEXT, DimensionsInfo.NAME_AR_TEXT)
        self.MESSAGE.should(have.exact_text(DimensionsInfo.CREATE_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        self.DIMENSION_TITLE.should(have.exact_text(DimensionsInfo.NAME_EN_TEXT))

    @allure.step("Cancel editing dimension")
    def cancel_edit_dimension(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.enter_dimension_name_ar(DimensionsInfo.NAME_AR_TEXT_EDIT)
        self.enter_dimension_name_en(DimensionsInfo.NAME_EN_TEXT_EDIT)
        self.BACK_HYPERLINK.click()
        self.DIMENSION_TITLE.should(have.exact_text(DimensionsInfo.NAME_EN_TEXT))

    @allure.step("Edit dimension")
    def edit_dimension(self):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.fill_dimension_names_fields(
            DimensionsInfo.NAME_EN_TEXT_EDIT, DimensionsInfo.NAME_AR_TEXT_EDIT
        )
        self.MESSAGE.should(have.exact_text(DimensionsInfo.EDIT_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        self.BACK_HYPERLINK.click()
        self.DIMENSION_TITLE.should(have.exact_text(DimensionsInfo.NAME_EN_TEXT_EDIT))

    @allure.step("Cancel deleting dimension")
    def cancel_delete_dimension(self):
        s(self.DELETE_DIMENSION.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.CANCEL_BUTTON_MODAL.click()
        self.DIMENSION_TITLE.should(have.exact_text(DimensionsInfo.NAME_EN_TEXT))

    @allure.step("Delete dimension")
    def delete_dimension(self):
        s(self.DELETE_DIMENSION.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.DELETE_BUTTON_MODAL.click()
        self.MESSAGE.should(have.exact_text(DimensionsInfo.DELETE_SUCCESS_MESSAGE))
        self.MESSAGE.should(be.not_.visible)
        self.DIMENSION_TITLE.should(be.not_.visible)

    @allure.step("Create already created dimension")
    def create_already_created_dimension(self, dimension_name_en, dimension_name_ar, message):
        self.CREATE_DIMENSION.click()
        self.enter_dimension_name_ar(dimension_name_ar)
        self.enter_dimension_name_en(dimension_name_en)
        self.SAVE_BUTTON.click()
        self.DIMENSION_MESSAGE.should(have.exact_text(message))
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Create dimension with invalid values")
    def create_dimension_with_invalid_values(self, dimension_name_en, dimension_name_ar):
        self.CREATE_DIMENSION.click()
        self.enter_dimension_name_ar(dimension_name_ar)
        self.enter_dimension_name_en(dimension_name_en)
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Edit already created dimension")
    def edit_already_created_dimension(self, dimension_name_en, dimension_name_ar, message):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.enter_dimension_name_ar(dimension_name_ar)
        self.enter_dimension_name_en(dimension_name_en)
        self.SAVE_BUTTON.click()
        self.DIMENSION_MESSAGE.should(have.exact_text(message))
        self.SAVE_BUTTON.should(have.attribute("disabled"))

    @allure.step("Edit dimension with invalid values")
    def edit_dimension_with_invalid_values(self, dimension_name_en, dimension_name_ar):
        s(self.EDIT_BUTTON.format(DimensionsInfo.NAME_EN_TEXT)).click()
        self.enter_dimension_name_ar(dimension_name_ar)
        self.enter_dimension_name_en(dimension_name_en)
        self.SAVE_BUTTON.should(have.attribute("disabled"))
