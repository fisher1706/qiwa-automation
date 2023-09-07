from __future__ import annotations

import platform
import time

from selene import be, command, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class AdminSpacesPage:
    add_space_button = s('//*[@href="/spaces/create"]')
    clear_filters_button = s('//*[@class="q-btn q-btn--link q-btn--small"]')
    edit_button = s('//*[@title="Edit space"]')
    delete_button = s('//*[@title="Delete space"]')
    english_title_filter = s('//*[@id="titleEn"]')

    """SPACES PAGE"""
    spaces_table = s('//*[@class="table"]')
    arabic_spaces_title_filter = s('//*[@name="name.ar"]')
    english_spaces_title_filter = s('//*[@name="name.en"]')
    type_filter = s('//*[@name="type"]')
    arabic_link_filter = s('//*[@name="defaultUrl.ar"]')
    english_link_filter = s('//*[@name="defaultUrl.en"]')
    status_filter = s('//*[@name="enabled"]')
    status_active = s('//*[@value="true"]')
    pop_up_message = s('//*[@class="toast success is-top"]')

    """"CREATE SPACE PAGE"""
    create_spaces_page_title = s('//*[@class="q-page-box__title"]')
    fields_table = s('//*[@class="space-section"]')
    english_name_field = s('//*[@name="titleEn"]')
    arabic_name_field = s('//*[@name="titleAr"]')
    default_url_english_field = s('//*[@name="urlEn"]')
    default_url_arabic_field = s('//*[@name="urlAr"]')
    redirect_key_name_field = s('//*[@name="redirectKeyName"]')
    type_field = s('//*[@name="type"]')
    space_active_radio_button = s('//*[@class="check is-elastic"]')
    reset_changes_button = s('//*[@class="btn btn--border-red mr-5"]')
    create_space_button = s('//*[@type="submit"]')
    back_to_the_spaces_page_button = s('//*[@class="back-link"]')
    invalid_field_format_message = s('//*[@class="help is-danger"]')
    field_error = s("p.is-danger")
    title_english_field = s('//*[@name="name.en"]')
    filter_status = s('//*[@name="enabled"]')
    active_status = s('//*[@value="true"]')
    english_title_columns = ss('//*[@data-label="Spaces title (English) "]')

    def wait_admin_spaces_page_to_load(self) -> AdminSpacesPage:
        self.spaces_table.wait_until(be.visible)
        return self

    def go_to_add_space_page(self) -> AdminSpacesPage:
        self.add_space_button.click()
        self.fields_table.wait_until(be.visible)
        return self

    def go_to_edit_space_page(self) -> AdminSpacesPage:
        self.edit_button.click()
        self.fields_table.wait_until(be.visible)
        return self

    def check_elements_on_create_space_page(self) -> AdminSpacesPage:
        self.create_spaces_page_title.should(have.text("CREATE SPACE"))
        self.back_to_the_spaces_page_button.should(be.visible)
        self.reset_changes_button.should(be.visible)
        self.create_space_button.should(be.disabled)
        return self

    def fill_in_the_fields_for_new_space(self) -> AdminSpacesPage:
        self.english_name_field.type("English")
        self.arabic_name_field.type("إنجليزي")
        self.default_url_english_field.type("https://arabic-link.com")
        self.default_url_arabic_field.type("https://english-link.com")
        self.redirect_key_name_field.type("redirect_key_name")
        self.type_field.type("super-user")
        return self

    def click_create_space_button(self) -> AdminSpacesPage:
        self.create_space_button.perform(command.js.scroll_into_view).click()
        return self

    def filter_space_by_en_title(self, title: str) -> AdminSpacesPage:
        self.english_spaces_title_filter.should(be.visible).clear().type(title)
        time.sleep(3)
        return self

    def delete_space(self):
        time.sleep(3)
        self.delete_button.should(be.visible).click()
        if browser.wait.until(EC.alert_is_present()):
            browser.switch_to.alert.accept()
        else:
            print("Alert isn't displayed")

    def check_message(self, expected_message: str) -> AdminSpacesPage:
        message = self.pop_up_message
        message.should(have.text(expected_message))
        return self

    def enter_data_to_eng_name_field(self, new_title: str) -> AdminSpacesPage:
        english_title_field = self.english_name_field
        english_title_field.should(be.enabled).perform(command.js.set_value("")).type(new_title)

        return self

    def click_reset_space_changes_button(self) -> AdminSpacesPage:
        self.reset_changes_button.should(be.visible).click()
        time.sleep(3)
        return self

    def should_space_english_title_have_text(self, english_name) -> AdminSpacesPage:
        self.english_name_field.should(have.exact_text(english_name))
        return self

    def check_invalid_format_message(self, message: str) -> None:
        self.invalid_field_format_message.should(be.visible)
        self.invalid_field_format_message.should(have.text(message))

    def empty_fields_should_have_proper_error_message(self):
        field_names = {
            "The Name English field is required": self.english_name_field,
            "The Name Arabic field is required": self.arabic_name_field,
            "The Default url English field is not a valid URL": self.default_url_english_field,
            "The Default url Arabic field is not a valid URL": self.default_url_arabic_field,
            "The Redirect Key Name field is required": self.redirect_key_name_field,
            "The Type field is required": self.type_field,
        }
        for message, locator in field_names.items():
            element = locator
            element.wait_until(be.clickable)
            # pylint: disable=expression-not-assigned
            element.press(Keys.COMMAND, "a") if platform.system() == "Darwin" else element.press(
                Keys.CONTROL, "a"
            )
            element.press(Keys.DELETE)
            self.create_space_button.matching(be.disabled)
            self.field_error.matching(have.exact_text(message))
            browser.driver.refresh()
            return self

    def filtration_should_have_results(self, english_title: str) -> AdminSpacesPage:
        self.title_english_field.should(be.visible).clear().type(english_title)
        self.filter_status.click()
        self.active_status.click()
        time.sleep(3)
        self.english_title_columns.should(have.size(1)).first.should(
            have.exact_text(english_title)
        )
        return self

    def clear_space_filters(self) -> None:
        self.clear_filters_button.click()
        time.sleep(3)
        self.english_title_columns.should(have.size_greater_than(1))
