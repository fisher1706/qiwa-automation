from pathlib import Path

from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from data.data_portal.constants import Admin, Variables
from src.ui.pages.data_portal_pages.base_methods import base_methods

attachment = (
    Path(__file__)
    .parent.parent.parent.parent.parent.joinpath("data/files")
    .joinpath("{0}")
    .as_posix()
)


class DataPortalAdmin:
    USER_NAME = s("#edit-name")
    PASSWORD = s("#edit-pass")
    LOGIN_BUTTON = s("#edit-submit")
    PAGE_TITLE = s(".page-title")
    VALIDATION_MESSAGE = s(".form-item--error-message")
    MESSAGE = s("#block-stark-page-title")
    DURATION_READ_FIELD = s("#edit-field-duration-read-0-value")
    PUBLISH_CHECKBOX = "#edit-status-value"
    PUBLISH_NAME_CHECKBOX = s('//*[@for="edit-status-value"]')
    SAVE = s("#edit-submit")
    ATTACH_IMAGE = s('//input[@accept="image/*"]')
    IMAGE_PREVIEW = s(".image-preview__img-wrapper")
    SUCCESS_MESSAGE = s("#message-status-title")
    SUCCESS_MESSAGE_CHART = s("#message-status-title")
    CHANGE_CATEGORY_SUCCESS_MESSAGE = s('//li[@class="messages__item"]')
    ADD_BUTTON = s(".local-actions__item")
    NAME_FIELD = s("#edit-title-0-value")
    NAME_TERM_FIELD = s("#edit-name-0-value")
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
    CATEGORY_FILTER = '//select[@id="edit-category"]/option[text()="{0}"]'
    FILTER_BUTTON = s("#edit-submit-content")
    REPORT_NAME = s("//table/tbody/tr/td[2]")
    SORT_BY_TITLE = s('//a[@title="sort by Title"]')
    SORT_BY_STATUS = s('//a[@title="sort by Status"]')
    SORT_BY_UPDATED = s('//a[@title="sort by Updated"]')
    REPORT_LIST = ss("//table[1]/tbody/tr/td[2]")
    SELECT_ALL_CHECKBOX = (
        "th.views-field.views-field-views-bulk-operations-bulk-form > input:nth-child(1)"
    )
    SELECT_REPORT_CHECKBOX = "#edit-views-bulk-operations-bulk-form-0"
    ACTION_FORM = s("#vbo-action-form-wrapper")
    ACTION_DROPDOWN = s("#edit-action")
    CHANGE_CATEGORY_OPTION = s("#edit-action>option:nth-child(2)")
    APPLY_BUTTON = s("#edit-submit")
    TITLE_MODAL = s("#ui-id-1")
    VALIDATION_ERROR = s(".form-item__error-message")
    TAKEAWAY_SECTION_OPTION = s("#block-claro-content>dl>div:nth-child(5)>dt>a")
    ADD_TRANSLATION_OPTION = (
        '//*[contains(text(),"{0}")]/../..//td//'
        'li[@class="translate dropbutton__item dropbutton-action secondary-action"]'
    )
    ADD_TRANSLATION_BUTTON = s('//li[@class="add dropbutton__item dropbutton-action"]')
    DELETE_TRANSLATION_BUTTON = s("#edit-delete-translation")
    CREATE_REPORT_TITLE = s("#block-claro-page-title>h1")
    REQUIRED_FIELD = ss('//*[@class="form-item__label js-form-required form-required"]')
    BLOCKS_DROPDOWN = s('[id^="edit-field-blocks-actions-bundle"]')
    BLOCKS_OPTION = '[id^="edit-field-blocks-actions-bundle"]>option[value="{0}"]'
    ADD_NEW_BLOCK_BUTTON = s('[id^="edit-field-blocks-actions-ief-add"]')
    AUTHOR = s("#edit-meta-author>label")
    ERROR_REPORT_MESSAGE = s("#message-error-title")
    ALTERNATIVE_TEXT = s('[id^="edit-field-hero-image-0-alt"]')
    IMAGE_TITLE = s('[id^="edit-field-hero-image-0-title"]')
    IMAGE_VALIDATION = s('//*[@class="messages messages--error file-upload-js-error"]')
    IMAGE_RESOLUTION_VALIDATION = s('//*[@class="form-item__error-message"]')
    BLOCK_TITLE_INPUT = s('[id^="edit-field-blocks-form"][id*="field-block-title-0-value"]')
    TAB_TITLE_INPUT = s('[id*="edit-field-blocks-form"][id*="subform-field-title-0-value"]')
    TAB_TITLE_INPUT_2 = s(
        '[id*="edit-field-blocks-form-0-field-tabs-1"][id*="subform-field-title-0-value"]'
    )
    TAB_DESCRIPTION_INPUT = s('[id*="edit-field-blocks-form"][id*="field-description-0-value"]')
    TAB_SOURCE_INPUT = s('[id^="edit-field-blocks-form"][id*="subform-field-source-0-value"]')
    CREATE_CONTENT_BLOCK_BUTTON = s('[id^="edit-field-blocks-form"][id*="add-save"]')
    ADD_LINE_CHART_BUTTON = s('[id*="field-blocks-form"][id*="chart-line-chart-add-more"]')
    ADD_LINE_CHART_BUTTON_2 = s(
        '[id*="field-blocks-form-0-field-tabs-1"][id*="chart-line-chart-add-more"]'
    )
    ADD_CHART_TAB_BUTTON = s('[id*="field-blocks-form"][id*="chart-tab-add-more"]')
    CHART_LABEL_INPUT = s(
        '[id*="edit-field-blocks-form"][id*="subform-field-chart-label-0-value"]'
    )
    FORMAT_DROPDOWN = s('select[id*="edit-field-blocks-form"][id*="subform-field-format"]')
    FORMAT_DROPDOWN_2 = s(
        'select[id*="edit-field-blocks-form-0-field-tabs-1"][id*="subform-field-format"]'
    )
    FORMAT_OPTION = 'option[value="{0}"]'
    FORMAT_OPTION_2 = '(//option[@value="{0}"])[2]'
    ADD_ROW = s('[id^="button-add-table_json_editor"]')
    ADD_ROW_2 = s('(//*[starts-with(@id, "button-add-table_json_editor")])[2]')
    TABLE_CELL = 'td[class^="tui-grid-cell tui-grid-cell-has-input tui-grid-cell-e"]>div'
    COLOR_DROPDOWN = s('div[class="sp-preview-inner"]')
    ALL_ROW_CHECKBOX = s('td>div>input[type="checkbox"]')
    ALL_ROW_CHECKBOX_2 = s('(//td/div/input[@type="checkbox"])[2]')
    DELETE_ROW = s('[id^="button-remove-table_json_editor"]')
    DELETE_ROW_2 = s('(//*[starts-with(@id, "button-remove-table_json_editor")])[2]')
    SHOW_LEGEND_CHECKBOX = s('[id*="show-legend-value"]')
    SHOW_VALUES_CHECKBOX = s('[id*="show-values-value"]')
    COLOR_ALTERNATIVE = '[data-color="rgb{0}"]'
    EDIT_BLOCK = s('[id*="entity-edit"]')
    REMOVE_TAB = s("[id*=field-tabs-0-remove]")
    PARAGRAPH_DROPDOWN = s('(//button[@class="paragraphs-dropdown-toggle"])[2]')
    UPDATE_CONTENT_BLOCK = s('[id*="form-actions-ief-edit-save"]')
    SPINNER = s('[class*="ajax-progress__throbber"]')
    IMAGE_BLOCK_ATTACHMENT = s('//*[@class="fieldset__wrapper"]//input[@accept="image/*"]')
    IMAGE_CAPTURE_INPUT = '[class^="ck ck-editor__main"]>div>p'
    IMAGE_CHART_DROPDOWN = s('select[id^="edit-field-blocks-form-0-field-type"]')
    IMAGE_OPTION = '[id^="edit-field-blocks-form-0-field-type"]>option[value="{0}"]'
    TEXT_FORMAT = '[data-cke-tooltip-text="{0}"]'
    ALIGNMENT_FORMAT_DROPDOWN = s('[data-cke-tooltip-text="Text alignment"]')
    SPECIAL_CHARACTERS_DROPDOWN = s('[data-cke-tooltip-text="Special characters"]')
    EURO_SIGN = s('[title="Euro sign"]')
    HYPER_LINK_FIELD = '[class^="ck ck-input ck-input_focused"]'

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

    def fill_mandatory_fields_for_report(self, report_name=Admin.AUTOMATION):
        self.NAME_FIELD.set_value(report_name)
        self.DURATION_READ_FIELD.set_value(1)
        self.ATTACH_IMAGE.send_keys(attachment.format(Admin.PNG))
        self.IMAGE_PREVIEW.wait_until(be.visible)

    def click_on_add_report_button(self):
        self.ADD_BUTTON.click()

    def create_report(
        self,
        report_name=Admin.AUTOMATION,
        new_category=False,
        exist_category=False,
        unpublished=False,
    ):
        self.ADD_BUTTON.click()
        self.fill_mandatory_fields_for_report(report_name)
        if unpublished:
            self.unchecked_publish_checkbox()
        else:
            self.checked_publish_checkbox()
        if new_category:
            self.add_new_category_to_report()
        if exist_category:
            self.add_existing_category_to_report()
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def edit_report(self):
        s(self.EDIT_REPORT_BUTTON.format(Admin.AUTOMATION)).click()
        self.NAME_FIELD.set_value(Admin.AUTOMATION_EDIT)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def delete_report(self):
        s(self.DROPDOWN.format(Admin.AUTOMATION)).click()
        s(self.DELETE_REPORT_BUTTON.format(Admin.AUTOMATION)).click()
        self.TITLE_MODAL.should(have.text(Admin.MODAL_WARNING.format(Admin.AUTOMATION)))
        self.DELETE_BUTTON_MODAL.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_terms(self, name=Admin.AUTOMATION):
        self.ADD_BUTTON.click()
        self.NAME_TERM_FIELD.set_value(name)
        self.SAVE_AND_GO_TO_LIST.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def edit_terms(self):
        s(self.EDIT_CATEGORY_BUTTON.format(Admin.AUTOMATION)).click()
        self.NAME_TERM_FIELD.set_value(Admin.AUTOMATION_EDIT)
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
            if item:
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
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.SELECT_REPORT_CHECKBOX}").checked;'
        )
        if checkbox_status is False:
            s(self.SELECT_REPORT_CHECKBOX).click()

    def deselect_report(self):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.SELECT_REPORT_CHECKBOX}").checked;'
        )
        if checkbox_status:
            s(self.SELECT_REPORT_CHECKBOX).click()

    def select_all_reports(self):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.SELECT_ALL_CHECKBOX}").checked;'
        )
        if checkbox_status is False:
            s(self.SELECT_ALL_CHECKBOX).click()

    def deselect_all_reports(self):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.SELECT_ALL_CHECKBOX}").checked;'
        )
        if checkbox_status:
            s(self.SELECT_ALL_CHECKBOX).click()

    def checked_publish_checkbox(self):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.PUBLISH_CHECKBOX}").checked;'
        )
        if checkbox_status is False:
            s(self.PUBLISH_CHECKBOX).click()

    def unchecked_publish_checkbox(self):
        checkbox_status = browser.driver.execute_script(
            f'return document.querySelector("{self.PUBLISH_CHECKBOX}").checked;'
        )
        if checkbox_status:
            s(self.PUBLISH_CHECKBOX).click()

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
        self.SAVE.click()

    def check_change_category(self):
        self.CHANGE_CATEGORY_SUCCESS_MESSAGE.should(
            have.text(
                Admin.CHANGE_CATEGORY_SUCCESS_MESSAGE.format(
                    Admin.AUTOMATION, Admin.AUTOMATION_EDIT
                )
            )
        )

    def check_title_validation(self):
        self.ADD_BUTTON.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION_UPPER_CASE)
        self.SAVE.click()
        self.VALIDATION_ERROR.should(have.text(Admin.VALIDATION_TITLE))

    def check_content_validation(self):
        self.ADD_BUTTON.click()
        self.TITLE_NAME.set_value(Admin.AUTOMATION)
        self.CONTENT_FIELD.set_value(Variables.generate_string(2001))
        self.SAVE.click()
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
        self.APPLY_BUTTON.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def check_display_of_elements_on_report_editor_page(self):
        base_methods.check_element_on_the_page(self.CREATE_REPORT_TITLE, Admin.CREATE_REPORT_TITLE)
        base_methods.check_elements_on_the_page(
            self.REQUIRED_FIELD, Admin.CREATE_REPORT_REQUIRED_FIELDS
        )
        base_methods.check_element_attributes_value(self.ADD_NEW_TERM_BUTTON, Admin.ADD_NEW_TERM)
        base_methods.check_element_attributes_value(
            self.ADD_EXISTING_TERM_BUTTON, Admin.ADD_EXISTING_TERM
        )
        base_methods.check_element_on_the_page(self.BLOCKS_DROPDOWN, Admin.BLOCKS_DROPDOWN_TITLE)
        base_methods.check_element_attributes_value(self.ADD_NEW_BLOCK_BUTTON, Admin.ADD_NEW_BLOCK)
        base_methods.check_element_on_the_page(self.PUBLISH_NAME_CHECKBOX, Admin.PUBLISHED_NAME)

    def create_report_without_values(self):
        self.SAVE.click()
        validation_message_text = browser.execute_script(
            'return document.querySelector("input:invalid").validationMessage'
        )
        assert validation_message_text == Admin.BROWSER_VALIDATION
        self.SUCCESS_MESSAGE.should(be.not_.visible)

    def create_report_without_duration(self):
        self.NAME_FIELD.set_value(Admin.AUTOMATION)
        self.ATTACH_IMAGE.send_keys(attachment.format(Admin.PNG))
        self.IMAGE_PREVIEW.wait_until(be.visible)
        self.DURATION_READ_FIELD.clear()
        self.SAVE.click()
        validation_message_text = browser.execute_script(
            'return document.querySelector("input:invalid").validationMessage'
        )
        assert validation_message_text == Admin.BROWSER_VALIDATION
        self.SUCCESS_MESSAGE.should(be.not_.visible)

    def create_report_without_file(self):
        self.NAME_FIELD.set_value(Admin.AUTOMATION)
        self.DURATION_READ_FIELD.set_value(1)
        self.SAVE.click()
        self.ERROR_REPORT_MESSAGE.should(have.text(Admin.ERROR_MESSAGE))

    def create_report_without_name(self):
        self.DURATION_READ_FIELD.set_value(1)
        self.ATTACH_IMAGE.send_keys(attachment.format(Admin.PNG))
        self.IMAGE_PREVIEW.wait_until(be.visible)
        self.SAVE.click()
        validation_message_text = browser.execute_script(
            'return document.querySelector("input:invalid").validationMessage'
        )
        assert validation_message_text == Admin.BROWSER_VALIDATION
        self.SUCCESS_MESSAGE.should(be.not_.visible)

    def create_report_with_invalid_duration(self, value):
        self.NAME_FIELD.set_value(Admin.AUTOMATION)
        self.ATTACH_IMAGE.send_keys(attachment.format(Admin.PNG))
        self.IMAGE_PREVIEW.wait_until(be.visible)
        self.DURATION_READ_FIELD.set_value(value)
        self.SAVE.click()
        validation_message_text = browser.execute_script(
            'return document.querySelector("input:invalid").validationMessage'
        )
        assert validation_message_text == Admin.BROWSER_VALIDATION_DURATION
        self.SUCCESS_MESSAGE.should(be.not_.visible)

    def create_report_with_alternative_text_and_title(self):
        self.ALTERNATIVE_TEXT.set_value(Admin.AUTOMATION)
        self.IMAGE_TITLE.set_value(Admin.AUTOMATION)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def check_ability_add_allowed_types_of_image(self, file_format):
        self.NAME_FIELD.set_value(Admin.AUTOMATION)
        self.DURATION_READ_FIELD.set_value(1)
        self.ATTACH_IMAGE.send_keys(attachment.format(file_format))
        self.IMAGE_PREVIEW.wait_until(be.visible)
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def check_inability_add_other_types_of_image(self, file_format):
        self.ATTACH_IMAGE.send_keys(attachment.format(file_format))
        self.IMAGE_VALIDATION.should(have.text(Admin.IMAGE_VALIDATION_ERROR.format(file_format)))

    def check_limitation_size_of_image(self, file_format):
        self.ATTACH_IMAGE.send_keys(attachment.format(file_format))
        self.IMAGE_RESOLUTION_VALIDATION.should(
            have.text(Admin.IMAGE_RESOLUTION_ERROR.format(file_format))
        )

    def select_content_block_type(self, block_type=Admin.CHART):
        self.BLOCKS_DROPDOWN.click()
        s(self.BLOCKS_OPTION.format(block_type)).click()
        self.ADD_NEW_BLOCK_BUTTON.click()

    def add_chart_block(self):
        self.BLOCK_TITLE_INPUT.set_value(Admin.AUTOMATION)
        self.TAB_TITLE_INPUT.set_value(Admin.AUTOMATION)
        self.TAB_DESCRIPTION_INPUT.set_value(Admin.AUTOMATION)
        self.TAB_SOURCE_INPUT.set_value(Admin.AUTOMATION)

    def delete_all_row(self):
        self.ALL_ROW_CHECKBOX.click()
        self.DELETE_ROW.click()

    def fill_chart_format_table(self, chart_format):
        self.FORMAT_DROPDOWN.click()
        s(self.FORMAT_OPTION.format(chart_format)).click()
        self.delete_all_row()
        self.ADD_ROW.click()
        for cell in ss(self.TABLE_CELL):
            cell.double_click()
            ActionChains(browser.driver).send_keys(Admin.AUTOMATION).perform()
        ActionChains(browser.driver).send_keys(Keys.ENTER).perform()

    def fill_mandatory_fields_for_line_chart(
        self, title=Admin.AUTOMATION, chart_format=Admin.NUMBER
    ):
        self.TAB_TITLE_INPUT.set_value(title)
        self.ADD_LINE_CHART_BUTTON.click()
        self.fill_chart_format_table(chart_format)
        self.COLOR_DROPDOWN.should(be.visible)

    def save_report_with_content(self):
        self.save_chart()
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def save_chart(self):
        self.CREATE_CONTENT_BLOCK_BUTTON.click()
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)

    def add_line_chart_with_comparison_chart(self):
        for _ in range(2):
            self.select_content_block_type()
            self.TAB_TITLE_INPUT.set_value(Admin.AUTOMATION)
            self.ADD_LINE_CHART_BUTTON.click()
            self.fill_chart_format_table(Admin.NUMBER)
            self.COLOR_DROPDOWN.should(be.visible)
            self.save_chart()
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def add_report_with_disabled_show_checkboxes(self):
        self.TAB_TITLE_INPUT.set_value(Admin.AUTOMATION)
        self.ADD_LINE_CHART_BUTTON.click()
        self.fill_chart_format_table(Admin.NUMBER)
        self.SHOW_LEGEND_CHECKBOX.click()
        self.SHOW_VALUES_CHECKBOX.click()

    def add_chart_block_with_changed_color(self):
        self.TAB_TITLE_INPUT.set_value(Admin.AUTOMATION)
        self.ADD_LINE_CHART_BUTTON.click()
        self.fill_chart_format_table(Admin.NUMBER)
        self.COLOR_DROPDOWN.click()
        s(self.COLOR_ALTERNATIVE.format(Admin.YELLOW)).click()

    def create_chart_with_more_than_1_tab(self):
        self.fill_mandatory_fields_for_line_chart(chart_format=Admin.NUMBER)
        self.ADD_CHART_TAB_BUTTON.click()
        self.ADD_LINE_CHART_BUTTON_2.click()
        self.TAB_TITLE_INPUT_2.set_value(Admin.AUTOMATION)
        self.FORMAT_DROPDOWN_2.click()
        s(self.FORMAT_OPTION_2.format(Admin.NUMBER)).click()
        self.ALL_ROW_CHECKBOX_2.click()
        self.DELETE_ROW_2.click()
        self.ADD_ROW_2.click()
        for cell in ss(self.TABLE_CELL):
            cell.double_click()
            ActionChains(browser.driver).send_keys(Admin.AUTOMATION).perform()
        ActionChains(browser.driver).send_keys(Keys.ENTER).perform()

    def delete_chart_tab(self):
        self.EDIT_BLOCK.click()
        browser.driver.execute_script("window.scrollTo(0, 0);")
        self.PARAGRAPH_DROPDOWN.click()
        self.REMOVE_TAB.click()
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)
        self.UPDATE_CONTENT_BLOCK.click()

    def edit_chart_tab(self):
        self.EDIT_BLOCK.click()
        self.TAB_TITLE_INPUT.set_value(Admin.AUTOMATION_EDIT)
        self.fill_chart_format_table(Admin.PERCENTAGE)
        self.UPDATE_CONTENT_BLOCK.click()
        self.SAVE.click()
        self.SUCCESS_MESSAGE.should(be.visible)

    def fill_required_fields_for_image_block(self, file_format=Admin.PNG):
        s(self.IMAGE_CAPTURE_INPUT).set_value(Admin.AUTOMATION)
        self.IMAGE_BLOCK_ATTACHMENT.send_keys(attachment.format(file_format))
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)

    def check_image_limitation_size_for_image_chart(self, file_format):
        self.IMAGE_BLOCK_ATTACHMENT.send_keys(attachment.format(file_format))
        self.IMAGE_RESOLUTION_VALIDATION.should(
            have.text(Admin.IMAGE_RESOLUTION_ERROR.format(file_format))
        )

    def select_image_type_option(self, block_type):
        self.IMAGE_CHART_DROPDOWN.click()
        s(self.IMAGE_OPTION.format(block_type)).click()

    def fill_required_fields_for_image_paragraph(self, file_format=Admin.PNG):
        for field in ss(self.IMAGE_CAPTURE_INPUT):
            field.set_value(Admin.AUTOMATION)
        self.IMAGE_BLOCK_ATTACHMENT.send_keys(attachment.format(file_format))
        self.SPINNER.wait_until(be.visible)
        self.SPINNER.wait_until(be.not_.visible)

    def set_format_text(self, text_format=None):
        s(self.IMAGE_CAPTURE_INPUT).send_keys(Keys.CONTROL + "A")
        s(self.TEXT_FORMAT.format(text_format)).click()

    def set_special_character(self):
        s(self.IMAGE_CAPTURE_INPUT).send_keys(Keys.CONTROL + "A")
        self.SPECIAL_CHARACTERS_DROPDOWN.click()
        self.EURO_SIGN.click()

    def set_hyperlink(self):
        s(self.IMAGE_CAPTURE_INPUT).send_keys(Keys.CONTROL + "A")
        s(self.TEXT_FORMAT.format(Admin.HYPER_LINK)).click()
        s(self.HYPER_LINK_FIELD).set_value(Admin.GOOGLE_LINK)
        s(self.TEXT_FORMAT.format("Save")).click()

    def set_alignment(self, align):
        s(self.IMAGE_CAPTURE_INPUT).send_keys(Keys.CONTROL + "A")
        self.ALIGNMENT_FORMAT_DROPDOWN.click()
        s(self.TEXT_FORMAT.format(align)).click()
