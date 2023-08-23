import dataclasses
import platform
import time

from selene import be, command, have, query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


@dataclasses.dataclass
class SpacesPageLocators:
    """BUTTON AND ACTIONS"""

    ADD_SPACE_BUTTON = '//*[@href="/spaces/create"]'
    CLEAR_FILTERS_BUTTON = '//*[@class="q-btn q-btn--link q-btn--small"]'
    EDIT_BUTTON = '//*[@title="Edit space"]'
    DELETE_BUTTON = '//*[@title="Delete space"]'
    ENGLISH_TITLE_FILTER = '//*[@id="titleEn"]'

    """SPACES PAGE"""
    SPACES_TABLE = '//*[@class="table"]'
    ARABIC_SPACES_TITLE_FILTER = '//*[@name="name.ar"]'
    ENGLISH_SPACES_TITLE_FILTER = '//*[@name="name.en"]'
    TYPE_FILTER = '//*[@name="type"]'
    ARABIC_LINK_FILTER = '//*[@name="defaultUrl.ar"]'
    ENGLISH_LINK_FILTER = '//*[@name="defaultUrl.en"]'
    STATUS_FILTER = '//*[@name="enabled"]'
    STATUS_ACTIVE = '//*[@value="true"]'
    POP_UP_MESSAGE = '//*[@class="toast success is-top"]'

    """"CREATE SPACE PAGE"""
    CREATE_SPACES_PAGE_TITLE = '//*[@class="q-page-box__title"]'
    FIELDS_TABLE = '//*[@class="space-section"]'
    ENGLISH_NAME_FIELD = '//*[@name="titleEn"]'
    ARABIC_NAME_FIELD = '//*[@name="titleAr"]'
    DEFAULT_URL_ENGLISH_FIELD = '//*[@name="urlEn"]'
    DEFAULT_URL_ARABIC_FIELD = '//*[@name="urlAr"]'
    REDIRECT_KEY_NAME_FIELD = '//*[@name="redirectKeyName"]'
    TYPE_FIELD = '//*[@name="type"]'
    SPACE_ACTIVE_RADIO_BUTTON = '//*[@class="check is-elastic"]'
    RESET_CHANGES_BUTTON = '//*[@class="btn btn--border-red mr-5"]'
    CREATE_SPACE_BUTTON = '//*[@type="submit"]'
    BACK_TO_THE_SPACES_PAGE_BUTTON = '//*[@class="back-link"]'
    INVALID_FIELD_FORMAT_MESSAGE = '//*[@class="help is-danger"]'
    FIELD_ERROR = "p.is-danger"


class SpacesPage(SpacesPageLocators):
    title_english_field = s('//*[@name="name.en"]')
    filter_status = s('//*[@name="enabled"]')
    active_status = s('//*[@value="true"]')
    english_title_columns = ss('//*[@data-label="Spaces title (English) "]')

    def wait_page_to_load(self):
        element = s(self.SPACES_TABLE)
        element.wait_until(be.visible)

    def go_to_add_space_page(self):
        element = s(self.ADD_SPACE_BUTTON)
        element.click()
        s(self.FIELDS_TABLE).wait_until(be.visible)

    def go_to_edit_space_page(self):
        s(self.EDIT_BUTTON).should(be.clickable).click()
        s(self.FIELDS_TABLE).wait_until(be.visible)

    def check_create_space_page(self, title):
        s(self.CREATE_SPACES_PAGE_TITLE).should(have.text(title))
        s(self.BACK_TO_THE_SPACES_PAGE_BUTTON).should(be.visible)
        s(self.RESET_CHANGES_BUTTON).should(be.visible)
        s(self.CREATE_SPACE_BUTTON).should(be.disabled)

    def fill_in_the_fields_for_new_space(
        self, english_title, arabic_title, english_link, arabic_link, redirect_key_name, user_type
    ):
        s(self.ENGLISH_NAME_FIELD).type(english_title)
        s(self.ARABIC_NAME_FIELD).type(arabic_title)
        s(self.DEFAULT_URL_ENGLISH_FIELD).type(english_link)
        s(self.DEFAULT_URL_ARABIC_FIELD).type(arabic_link)
        s(self.REDIRECT_KEY_NAME_FIELD).type(redirect_key_name)
        s(self.TYPE_FIELD).type(user_type)

    def click_on_create_space_button(self):
        button = s(self.CREATE_SPACE_BUTTON)
        button.perform(command.js.scroll_into_view)
        button.should(be.clickable).click()

    def filter_space_by_en_title(self, title):
        s(self.ENGLISH_SPACES_TITLE_FILTER).should(be.visible).clear().type(title)
        time.sleep(3)

    def deleting(self):
        time.sleep(3)
        s(self.DELETE_BUTTON).should(be.visible).click()
        if browser.wait.until(EC.alert_is_present()):
            browser.switch_to.alert.accept()
        else:
            print("Alert isn't displayed")

    def check_message(self, expected_message):
        message = s(self.POP_UP_MESSAGE)
        message.should(have.text((expected_message["text"])))

    def enter_data_to_eng_name_field(self, new_title):
        english_title_field = s(self.ENGLISH_NAME_FIELD)
        english_title_field.wait_until(be.enabled)
        english_title_field.should(be.visible).perform(command.js.set_value(""))
        english_title_field.type(new_title)

    def click_reset_changes_button(self):
        s(self.RESET_CHANGES_BUTTON).should(be.visible).click()
        time.sleep(3)

    def comparison_text_from_title_english_field(self, english_name):
        get_title = s(self.ENGLISH_NAME_FIELD).get(query.attribute("value"))
        assert english_name == get_title, f"{english_name} is not equal to {get_title}"

    def check_invalid_format_message(self, message):
        s(self.INVALID_FIELD_FORMAT_MESSAGE).should(be.visible)
        message_text = s(self.INVALID_FIELD_FORMAT_MESSAGE).get(query.text)
        assert message_text == message["text"]

    def check_empty_fields(self):
        field_names = {
            "The Name English field is required": self.ENGLISH_NAME_FIELD,
            "The Name Arabic field is required": self.ARABIC_NAME_FIELD,
            "The Default url English field is not a valid URL": self.DEFAULT_URL_ENGLISH_FIELD,
            "The Default url Arabic field is not a valid URL": self.DEFAULT_URL_ARABIC_FIELD,
            "The Redirect Key Name field is required": self.REDIRECT_KEY_NAME_FIELD,
            "The Type field is required": self.TYPE_FIELD,
        }
        for message, locator in field_names.items():
            element = s(locator)
            element.wait_until(be.clickable)
            # pylint: disable=expression-not-assigned
            element.press(Keys.COMMAND, "a") if platform.system() == "Darwin" else element.press(
                Keys.CONTROL, "a"
            )
            element.press(Keys.DELETE)
            s(self.CREATE_SPACE_BUTTON).matching(be.disabled)
            s(self.FIELD_ERROR).matching(have.exact_text(message))
            browser.driver.refresh()

    def check_space_filters(self, english_title, clear_filter=False):
        self.title_english_field.should(be.visible).clear().type(english_title)

        self.filter_status.click()
        self.active_status.click()
        time.sleep(3)
        if clear_filter:
            s(self.CLEAR_FILTERS_BUTTON).click()
            time.sleep(3)
            self.english_title_columns.should(have.size_greater_than(1))
        else:
            self.english_title_columns.should(have.size(1)).first.should(
                have.exact_text(english_title)
            )
