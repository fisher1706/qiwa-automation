import allure
from selene.support.shared.jquery_style import s, ss
from selene import be, query
from data.establishment_violations.constants import ViolationDetailsPageText
from .violations_page import ViolationsPage


class ViolationDetails:
    DETAILS_PRINT_BUTTON = s("[data-testid='print']")
    CANNOT_OBJECT_TO_THIS_VIOLATION_PARAGRAPHS = ss("#hideObjection p")
    DYNAMIC_VIEW_DETAILS_GENERAL_INFO_SECTION = "//tbody//td//span[text()='{}']//parent::div//p"
    DYNAMIC_VIEW_DETAILS_OBJECTION_SECTION = "//tbody//td//span[text()='{}']//following-sibling::p"
    VIOLATION_ID_HEADER = s("//*[text()='Violation ID']")

    @allure.step
    def check_cannot_object_message(self):
        self.VIOLATION_ID_HEADER.wait_until(be.visible)
        assert (
            self.CANNOT_OBJECT_TO_THIS_VIOLATION_PARAGRAPHS[0].get(query.text)
            == ViolationDetailsPageText.CANNOT_OBJECT_VIOLATION_HEADER
        )
        assert (
            self.CANNOT_OBJECT_TO_THIS_VIOLATION_PARAGRAPHS[1].get(query.text)
            == ViolationDetailsPageText.CANNOT_OBJECT_VIOLATION_BODY
        )

        return self

    @allure.step
    def validate_view_details_elements(self, column_name, pattern):
        data = (
            s(self.DYNAMIC_VIEW_DETAILS_GENERAL_INFO_SECTION.format(column_name))
            .should(be.visible)
            .get(query.text)
        )
        assert ViolationsPage.validate_format(data, pattern) or data == "-"

    @allure.step
    def click_on_print_button(self):
        self.VIOLATION_ID_HEADER.wait_until(be.visible)
        self.DETAILS_PRINT_BUTTON.should(be.clickable).click()
        # alert = Alert(browser.driver())
        # alert.accept()
        return self

    @allure.step
    def validate_print_btn_is_clickable(self):
        self.VIOLATION_ID_HEADER.wait_until(be.visible)
        self.DETAILS_PRINT_BUTTON.should(be.clickable)
        return self
