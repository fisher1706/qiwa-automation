from pathlib import Path

from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss

from data.data_portal.constants import Admin, Variables
from src.ui.pages.data_portal_pages.base_methods import base_methods

attachment = (
    Path(__file__)
    .parent.parent.parent.parent.parent.joinpath("data/files")
    .joinpath("admin_portal_test_attach.png")
    .as_posix()
)


class DataPortalAdmin:
    USER_NAME = s("#edit-name")
    PASSWORD = s("#edit-pass")
    LOGIN_BUTTON = s("#edit-submit")
    PAGE_TITLE = s(".page-title")
    VALIDATION_MESSAGE = s(".form-item--error-message")
    MESSAGE = s("#block-stark-page-title")
    REPORT_NAME_FIELD = s("#edit-title-0-value")
    DURATION_READ_FIELD = s("#edit-field-duration-read-0-value")
    PUBLISH_CHECKBOX = s("#edit-status-value")
    SAVE = s("#edit-submit")
    ATTACH_IMAGE = s('//input[@accept="image/*"]')
    IMAGE_PREVIEW = s(".image-preview__img-wrapper")
    SUCCESS_MESSAGE = s("#message-status-title")
    ADD_BUTTON = s(".local-actions__item")
    NAME_FIELD = s("#edit-name-0-value")
    TITLE_NAME = s('//input[@name="title[0][value]"]')
    CONTENT_FIELD = s('//*[@role="textbox"]')
    SAVE_AND_GO_TO_LIST = s("#edit-overview:nth-child(2)")
    EDIT_REPORT_BUTTON = (
        '//*[contains(text(),"{0}")]/../../td//'
        'li[@class="edit dropbutton__item dropbutton-action"]'
    )
    EDIT_CATEGORY_BUTTON = (
        '//*[contains(text(),"{0}")]/../../../../td[2]//'
        'li[@class="edit dropbutton__item dropbutton-action"]'
    )
    EDIT_TAKEAWAY_BUTTON = '//*[contains(text(),"{0}")]/../..//td//li[@class="edit dropbutton__item dropbutton-action"]'
    DROPDOWN = '//*[contains(text(),"{0}")]/../../../..//button[@class="dropbutton__toggle"]'
    DELETE_REPORT_BUTTON = (
        '//*[contains(text(),"{0}")]/../../td//'
        'li[@class="delete dropbutton__item dropbutton-action secondary-action"]'
    )
    DELETE_CATEGORY_BUTTON = (
        '//*[contains(text(),"{0}")]/../../../../'
        'td[2]//li[@class="delete dropbutton__item dropbutton-action secondary-action"]'
    )
    DELETE_BUTTON_MODAL = s('//div[@class="ui-dialog-buttonset form-actions"]/button')
    DELETE_TAKEAWAY_BUTTON = (
        '//*[contains(text(),"{0}")]/../..//td//'
        'li[@class="delete dropbutton__item dropbutton-action secondary-action"]'
    )
    REPORT_TITLE = s("#block-claro-page-title")
    TAB = ss("#block-claro-primary-local-tasks > nav > ul > li > a")
    FILTER = ss('//div[@class="view-filters"]//label')
    CATEGORY_TITLE = s("//table")
    REPORT_CATEGORY_COLUMN = ss("//table[1]/thead/tr/th[@id]")
    ADD_EXISTING_TERM_BUTTON = s("#edit-field-category-actions-ief-add-existing")
    ADD_NEW_TERM_BUTTON = s("#edit-field-category-actions-ief-add")
    CATEGORY_DROPDOWN = s('//div[@class="fieldset__wrapper"][1]//select')
    OPTION = s("//option[@value]")
    ADD_CATEGORY_BUTTON = s('//input[@value="Add taxonomy term"]')
    CREATE_CATEGORY_BUTTON = s('//input[@value="Create taxonomy term"]')
    CATEGORY_NAME = s('[id*="edit-field-category-form-0-name-0-value"]')
    LANGUAGE = ss("//tr[@class]/td[1]")
    TRANSLATION_REPORT_BUTTON = (
        '//*[contains(text(),"{0}")]/../../td//'
        'li[@class="translate dropbutton__item dropbutton-action secondary-action"]'
    )
    TITLE_FILTER = s("input#edit-title")
    PUBLISHED_STATUS_DROPDOWN = s("#edit-status")
    PUBLISHED_STATUS = '//*[@id="edit-status"]//option[@value="{0}"]'
    LANGUAGE_DROPDOWN = s("#edit-langcode")
    LANGUAGE_FILTER = '//*[@id="edit-langcode"]//option[@value="{0}"]'
    CATEGORY_FILTER_DROPDOWN = s("#edit-category")
    CATEGORY_FILTER = '//*[@id="edit-category"]//option[@value="{0}"]'
    FILTER_BUTTON = s("#edit-submit-content")
    REPORT_NAME = s("//table/tbody/tr/td[2]")
    SORT_BY_TITLE = s('//a[@title="sort by Title"]')
    SORT_BY_STATUS = s('//a[@title="sort by Status"]')
    SORT_BY_UPDATED = s('//a[@title="sort by Updated"]')
    REPORT_LIST = ss("//table[1]/tbody/tr/td[2]")
    SELECT_ALL_CHECKBOX = s("//table[1]/thead/tr/th/input")
    SELECT_REPORT_CHECKBOX = "#edit-views-bulk-operations-bulk-form-0"
    ACTION_FORM = s("#vbo-action-form-wrapper")
    ACTION_DROPDOWN = s("#edit-action")
    CHANGE_CATEGORY_OPTION = s("#edit-action>option:nth-child(2)")
    APPLY_BUTTON = s("#edit-submit")
    TITLE_MODAL = s("")
    VALIDATION_ERROR = s(".form-item__error-message")
    TAKEAWAY_SECTION_OPTION = s("#block-claro-content>dl>div:nth-child(5)")
    ADD_TRANSLATION_OPTION = (
        '//*[contains(text(),"{0}")]/../..//td//'
        'li[@class="translate dropbutton__item dropbutton-action secondary-action"]'
    )
    ADD_TRANSLATION_BUTTON = s('//li[@class="add dropbutton__item dropbutton-action"]')
    DELETE_TRANSLATION_BUTTON = s("#edit-delete-translation")

    def input_creds(self, login, password):
        self.USER_NAME.set_value(login)
        self.PASSWORD.set_value(password)
        self.LOGIN_BUTTON.click()

    def login_to_data_portal_admin(self):
        self.input_creds(Admin.LOGIN, Admin.PASSWORD)
        self.PAGE_TITLE.wait_until(be.visible)

    def check_validation(self):
        self.VALIDATION_MESSAGE.should(have.text(Admin.VALIDATION_MESSAGE))

    def check_copy_past_link_into_another_browser(self):
        current_url = browser.driver.current_url
        browser.driver.delete_all_cookies()
        browser.open(current_url)
        self.MESSAGE.should(have.text(Admin.LOGIN_PAGE))

    def create_report(
        self,
        report_name=Admin.AUTOMATION,
        new_category=False,
        exist_category=False,
        unpublished=False,
    ):
        self.ADD_BUTTON.click()
        self.REPORT_NAME_FIELD.set_value(report_name)
        self.DURATION_READ_FIELD.set_value(1)
        self.ATTACH_IMAGE.send_keys(attachment)
        self.IMAGE_PREVIEW.wait_until(be.visible)
        if unpublished:
            self.PUBLISH_CHECKBOX.click()
        if new_category:
            self.add_new_category_to_report()
        if exist_category:
            self.add_existing_category_to_report()
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def edit_report(self):
        s(self.EDIT_REPORT_BUTTON.format(Admin.AUTOMATION)).click()
        self.REPORT_NAME_FIELD.set_value(Admin.AUTOMATION_EDIT)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_report(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.DELETE_REPORT_BUTTON.format(Admin.AUTOMATION)).click()
        self.TITLE_MODAL.should(have.text(Admin.MODAL_WARNING))
        self.DELETE_BUTTON_MODAL.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_terms(self, name=Admin.AUTOMATION):
        self.ADD_BUTTON.click()
        self.NAME_FIELD.set_value(name)
        self.SAVE_AND_GO_TO_LIST.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def edit_terms(self):
        s(self.EDIT_CATEGORY_BUTTON.format(Admin.AUTOMATION)).click()
        self.NAME_FIELD.set_value(Admin.AUTOMATION_EDIT)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_terms(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.DELETE_CATEGORY_BUTTON.format(Admin.AUTOMATION)).click()
        self.DELETE_BUTTON_MODAL.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_takeaway_section(self):
        self.ADD_BUTTON.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_takeaway_section_with_invalid_title(self):
        self.ADD_BUTTON.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION_UPPER_CASE)
        self.SAVE.click()

    def add_takeaway_section_with_invalid_content(self):
        self.ADD_BUTTON.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION)
        self.CONTENT_FIELD.set_value(Variables.generate_string(2001))
        self.SAVE.click()

    def edit_takeaway_section(self):
        s(self.EDIT_TAKEAWAY_BUTTON.format(Admin.AUTOMATION)).click()
        self.CONTENT_FIELD.set_value(Admin.AUTOMATION_EDIT)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_takeaway_section(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.DELETE_TAKEAWAY_BUTTON.format(Admin.AUTOMATION)).click()
        self.DELETE_BUTTON_MODAL.click()

    def add_existing_category_to_report(self):
        self.ADD_EXISTING_TERM_BUTTON.click()
        self.CATEGORY_DROPDOWN.click()
        self.OPTION.should(have.text(Admin.AUTOMATION)).click()
        self.ADD_CATEGORY_BUTTON.click()

    def add_new_category_to_report(self):
        self.ADD_NEW_TERM_BUTTON.click()
        self.CATEGORY_NAME.set_value(Admin.AUTOMATION)
        self.CREATE_CATEGORY_BUTTON.click()

    def check_report_tabs(self):
        base_methods.check_elements_on_the_page(self.TAB, Admin.TABS)

    def check_report_filters(self):
        base_methods.check_elements_on_the_page(self.FILTER, Admin.FILTERS)

    def check_report_categories(self):
        base_methods.check_elements_on_the_page(
            self.REPORT_CATEGORY_COLUMN, Admin.REPORT_CATEGORY_COLUMNS
        )

    def check_translation_page(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.TRANSLATION_REPORT_BUTTON.format(Admin.AUTOMATION)).click()
        base_methods.check_elements_on_the_page(self.LANGUAGE, Admin.LANGUAGES)

    def check_deleted_report(self):
        s(self.EDIT_REPORT_BUTTON.format(Admin.AUTOMATION)).should(be.not_.visible)

    def define_title(self, title):
        self.TITLE_FILTER.set_value(title)

    def define_published_status(self, status):
        self.PUBLISHED_STATUS_DROPDOWN.click()
        s(self.PUBLISHED_STATUS.format(status)).click()

    def define_language(self, language):
        self.LANGUAGE_DROPDOWN.click()
        s(self.LANGUAGE_FILTER.format(language)).click()

    def define_category(self, category):
        self.CATEGORY_FILTER_DROPDOWN.click()
        s(self.CATEGORY_FILTER.format(category)).click()

    def perform_filtration(self, title, published_status, language, category):
        criteria = (title, published_status, language, category)
        actions = {
            title: self.define_title,
            published_status: self.define_published_status,
            language: self.define_language,
            category: self.define_category,
        }
        for item in criteria:
            if (item in actions) is not None:
                actions[item](item)
            self.FILTER_BUTTON.click()

    def check_filtration(self):
        base_methods.check_element_on_the_page(self.CATEGORY_TITLE, Admin.AUTOMATION)
        base_methods.check_element_on_the_page(self.REPORT_NAME, Admin.AUTOMATION)

    def sort_by_title(self):
        self.SORT_BY_TITLE.click()

    def sort_by_status(self):
        self.SORT_BY_STATUS.click()

    def sort_by_updated(self):
        self.SORT_BY_UPDATED.click()

    def check_sorting(self):
        base_methods.check_elements_on_the_page(
            self.REPORT_LIST, [Admin.AUTOMATION_EDIT, Admin.AUTOMATION]
        )

    def select_report(self):
        s(self.SELECT_REPORT_CHECKBOX).click()

    def select_all_reports(self):
        self.SELECT_ALL_CHECKBOX.click()

    def check_checkbox_status(self, checked=None, unchecked=None):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.SELECT_REPORT_CHECKBOX}").checked;'
        )
        if checked:
            assert checkbox_status is True
        if unchecked:
            assert checkbox_status is False

    def check_action_form(self, visible=None, invisible=None):
        if visible:
            self.ACTION_FORM.should(be.visible)
        if invisible:
            self.ACTION_FORM.should(be.not_.visible)

    def change_category_by_action_form(self):
        self.ACTION_DROPDOWN.click()
        self.CHANGE_CATEGORY_OPTION.click()
        self.APPLY_BUTTON.click()
        self.CATEGORY_FILTER_DROPDOWN.click()
        s(self.CATEGORY_FILTER.format(Admin.AUTOMATION_EDIT)).click()
        self.APPLY_BUTTON.click()

    def check_change_category(self):
        self.SUCCESS_MESSAGE.should(have.text(Admin.SUCCESS_MESSAGE))

    def check_title_validation(self):
        self.VALIDATION_ERROR.should(have.text(Admin.VALIDATION_TITLE))

    def check_content_validation(self):
        self.VALIDATION_ERROR.should(have.text(Admin.VALIDATION_CONTENT))

    def add_content_as_takeaway_section(self):
        self.ADD_BUTTON.click()
        self.TAKEAWAY_SECTION_OPTION.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_translation(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.ADD_TRANSLATION_OPTION.format(Admin.AUTOMATION)).click()
        self.ADD_TRANSLATION_BUTTON.click()
        self.CONTENT_FIELD.set_value(Admin.AUTOMATION_AR)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_translation(self):
        self.DELETE_TRANSLATION_BUTTON.click()
        self.SUCCESS_MESSAGE.should(be.visible)
