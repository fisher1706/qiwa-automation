from pathlib import Path

from selene import be, browser, have
from selene.support.shared.jquery_style import s

from data.data_portal.constants import Admin


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

    def create_report_using_mandatory_fields(self):
        attachment = (
            Path(__file__)
            .parent.parent.parent.parent.parent.joinpath("data/files")
            .joinpath("admin_portal_test_attach.png")
            .as_posix()
        )
        self.ADD_BUTTON.click()
        self.REPORT_NAME_FIELD.set_value(Admin.AUTOMATION)
        self.DURATION_READ_FIELD.set_value(1)
        self.ATTACH_IMAGE.send_keys(attachment)
        self.IMAGE_PREVIEW.wait_until(be.visible)
        self.PUBLISH_CHECKBOX.click()
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
        self.DELETE_BUTTON_MODAL.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_terms(self):
        self.ADD_BUTTON.click()
        self.NAME_FIELD.set_value(Admin.AUTOMATION)
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

    def edit_takeaway_section(self):
        s(self.EDIT_TAKEAWAY_BUTTON.format(Admin.AUTOMATION)).click()
        self.CONTENT_FIELD.set_value(Admin.AUTOMATION_EDIT)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_takeaway_section(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.DELETE_TAKEAWAY_BUTTON.format(Admin.AUTOMATION)).click()
        self.DELETE_BUTTON_MODAL.click()
        self.SUCCESS_MESSAGE.should(be.visible)
