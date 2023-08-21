from __future__ import annotations

import time
from enum import Enum
from pathlib import Path

from selene import be, browser, by, command, have, query
from selene.support.shared.jquery_style import s, ss
from selenium.common.exceptions import StaleElementReferenceException

from utils.assertion import assert_that
from src.ui.components.raw.table import Table


class FilterLocators(Enum):
    TITLE_ENGLISH_FIELD = '//*[@id="titleEn"]'
    STATUS_FILTER = '//*[@id="state"]'
    STATUS_ACTIVE = '//*[@value="active"]'
    ENGLISH_TITLE_COLUMN = '//*[@data-label="E-services title (English) "]'


class AdminPage:
    # e-service page
    e_services_button_block = s(".button-block")
    e_services_table = Table(s(".table"))
    E_SERVICES = by.xpath('//*[@class="icon-writing"]')
    SPACES = by.xpath('//*[@href="/spaces"]')
    ADD_E_SERVICE = by.xpath('//*[@href="/e-services/create"]')
    ENGLISH_TITLE_FILTER = by.xpath('//*[@id="titleEn"]')
    ARABIC_TITLE_FILTER = by.xpath('//*[@id="titleAr"]')
    ENGLISH_TITLE_COLUMN = by.xpath('//*[@data-label="E-services title (English) "]')
    ARABIC_TITLE_COLUMN = by.xpath('//*[@data-label="E-services title (Arabic) "]')
    E_SERVICES_STATUS_FILTER = by.xpath('//*[@id="state"]')
    STATUS_ACTIVE = by.xpath('//*[@value="active"]')
    CLEAR_FILTERS_BUTTON = by.xpath('//*[@class="q-btn q-btn--link q-btn--small"]')
    CATEGORY_LIST_BUTTON = by.xpath('//*[@href="/e-services/tags"]')

    # new and edit e-service fields
    E_SERVICES_STATUS_FIELD = by.xpath('//*[@class="control"]')
    ACTIVE_STATUS = by.xpath('//*[@value="active"]')
    TITLE_ENGLISH_FIELD = by.xpath('//*[@data-vv-as="Name English"]')
    TITLE_ARABIC_FIELD = by.xpath('//*[@name="titleAr"]')
    SERVICE_CODE_FIELD = by.xpath('//*[@name="code"]')
    ENGLISH_LINK_NAME_FIELD = by.xpath('//*[@name="linkEn-0"]')
    ARABIC_LINK_NAME_FIELD = by.xpath('//*[@name="linkAr-0"]')
    CREATE_E_SERVICE_BUTTON = by.xpath('//*[@type="submit"]')
    RESET_CHANGES_BUTTON = by.xpath('//*[@class="btn btn--border-red mr-5"]')
    BACK_LINK = by.xpath('//*[@class="back-link"]')
    PRIVILEGE_CHECKBOX = s("div:nth-child(2) > .checkbox__label")
    SHARABLE_SERVICE_CHECKBOX = "div:nth-child(3) > .checkbox__label"
    ADD_ICON = by.xpath('//*[@type="file"]')
    ICON = by.xpath('//*[@alt="icon logo"]')
    DELETE_ICON = by.xpath('//*[@title="Delete icon"]')

    E_SERVICES_SUCCESSFUL_MESSAGE = by.css(".toast.success.is-top div")

    # E-SERVICE CATEGORIES LIST
    E_SERVICE_CATEGORY_HEADER = by.xpath('//*[@class="q-page-box__header-l"]')
    E_SERVICES_CATEGORY_TABLE = by.xpath('//*[@class="q-page-box__content"]')
    ADD_E_SERVICE_CATEGORY = by.xpath('//*[@id="btn-add"]')
    NEW_CATEGORY_AR_NAME_FIELD = by.xpath('//*[@id="new-nameAr"]')
    NEW_CATEGORY_EN_NAME_FIELD = by.xpath('//*[@id="new-nameEn"]')
    NEW_CODE_FIELD = by.xpath('//*[@id="new-code"]')
    SAVE_CATEGORY_BUTTON = by.xpath(
        '//*[@class="action-button m-1 btn btn--primary btn--small with-preloader"]'
    )
    SUCCESSFUL_CREATED_NEW_CATEGORY = by.xpath('//*[@class="toast success is-top"]/div')
    CATEGORY_ENGLISH_NAME_FILTER = by.xpath('//*[@id="nameEn"]')
    DELETE_CATEGORY_BUTTON = by.xpath('//*[@title="Delete category"]')
    EDIT_CATEGORY_BUTTON = by.xpath('//*[@title="Edit category"]')
    EDIT_ENGLISH_NAME_FIELD = by.xpath(
        '//*[@data-label="E-services Category English name"]/span/input'
    )
    CANCEL_BUTTON = by.xpath('//*[@class="action-button m-1 btn btn--small"]')
    CLEAR_CATEGORY_FILTER_BUTTON = by.xpath('//*[@class="q-page-box__header-r"]')

    CATEGORY_ENGLISH_NAME_COLUMN = by.xpath('//*[@data-label="E-services Category English name"]')

    # E-SERVICE ACTION
    EDIT_BUTTON = by.xpath('//*[@title="Edit e-service"]')
    DELETE_BUTTON = by.css(".column-wraper button")
    E_SERVICE_DETAIL_BUTTON = by.xpath('//*[@class="mdi mdi-chevron-right mdi-24px"]')
    E_SERVICES_LINKS_ON_DETAIL = by.xpath('//*[@class="eservice__el-title text--medium"]')
    E_SERVICES_ARABIC_LINK_TITLE = by.xpath('//*[@class="links-list"]/li/span[1]')
    E_SERVICES_ENGLISH_LINK_TITLE = by.xpath('//*[@class="links-list"]/li/span[2]')
    E_SERVICES_DETAIL_LINK = by.xpath('//*[@class="links-list"]/li/a')

    def wait_page_to_load(self) -> AdminPage:
        element = s(self.E_SERVICES)
        element.wait_until(be.visible)
        return self

    def check_button_block_is_displayed(self) -> AdminPage:
        self.e_services_button_block.should(be.visible)
        return self

    def check_e_services_table_is_displayed(self) -> AdminPage:
        self.e_services_table.headers.should(be.not_.blank)
        self.e_services_table.body.should(be.not_.blank)
        return self

    def go_to_e_services_tab(self) -> AdminPage:
        element = s(self.E_SERVICES)
        element.should(be.visible).click()
        return self

    def open_e_services_page(self) -> AdminPage:
        browser.open("https://super.qiwa.tech/en/e-services/")
        return self

    def go_to_spaces_tab(self):
        element = s(self.SPACES)
        element.should(be.visible).click()

    def add_e_service(self) -> AdminPage:
        element = s(self.ADD_E_SERVICE)
        element.should(be.visible).click()
        return self

    def fill_in_the_fields_for_new_e_service(
        self, english_title, arabic_title, service_code, english_link, arabic_link
    ) -> AdminPage:
        s(self.E_SERVICES_STATUS_FIELD).click()
        s(self.ACTIVE_STATUS).click()
        s(self.TITLE_ENGLISH_FIELD).type(english_title)
        s(self.TITLE_ARABIC_FIELD).type(arabic_title)
        s(self.SERVICE_CODE_FIELD).type(service_code)
        s(self.ENGLISH_LINK_NAME_FIELD).type(english_link)
        s(self.ARABIC_LINK_NAME_FIELD).type(arabic_link)
        return self

    def click_on_save_e_service_button(self) -> AdminPage:
        button = s(self.CREATE_E_SERVICE_BUTTON)
        button.perform(command.js.scroll_into_view)
        button.should(be.clickable).click()
        return self

    def check_successful_action(self, expected_message) -> AdminPage:
        message = s(self.E_SERVICES_SUCCESSFUL_MESSAGE)
        message.wait_until(be.visible)
        message.should(have.text((expected_message["text"])))
        return self

    def filter_by_english_title(self, title):
        filter_field = s(self.ENGLISH_TITLE_FILTER)
        filter_field.should(be.visible).clear().type(title)
        return self

    def click_edit_button(self) -> AdminPage:
        s(self.EDIT_BUTTON).should(be.clickable).click()
        s(self.TITLE_ENGLISH_FIELD).wait_until(be.visible)
        return self

    def edit_english_title_field(self, new_title) -> AdminPage:
        english_title_field = s(self.TITLE_ENGLISH_FIELD)
        english_title_field.wait_until(be.enabled)
        english_title_field.should(be.visible).perform(command.js.set_value(""))
        english_title_field.type(new_title)
        return self

    def click_reset_changes_button(self):
        button = s(self.RESET_CHANGES_BUTTON)
        button.should(be.clickable).click()
        button.wait_until(be.clickable)
        time.sleep(1)

    def comparison_text_from_title_english_field(self, english_title):
        get_title = s(self.TITLE_ENGLISH_FIELD).get(query.attribute("value"))
        assert english_title == get_title, f"{english_title} is not equal to {get_title}"

    def select_privilege_checkbox(self, attempts=3) -> AdminPage:
        for _ in range(attempts):
            try:
                check_box = self.PRIVILEGE_CHECKBOX
                check_box.hover()
                check_box.click()
                check_box.matching(be.selected)
                return self
            except StaleElementReferenceException:
                continue
        return self

    def check_privilege_checkbox_is_not_checked(self):
        check_box = self.PRIVILEGE_CHECKBOX
        check_box.matching(be.blank)

    def check_e_service_detail(self):
        s(self.E_SERVICE_DETAIL_BUTTON).click()
        s(self.E_SERVICES_LINKS_ON_DETAIL).should(be.visible)
        s(self.E_SERVICES_ARABIC_LINK_TITLE).should(be.visible)
        s(self.E_SERVICES_ENGLISH_LINK_TITLE).should(be.visible)
        s(self.E_SERVICES_DETAIL_LINK).should(be.visible)

    def filter_e_services(self, english_title) -> AdminPage:
        locators = FilterLocators
        english_filter = s(locators.TITLE_ENGLISH_FIELD.value)
        english_filter.wait_until(be.visible)
        english_filter.perform(command.js.set_value("")).type(english_title)
        return self

    def clear_e_services_filter(self) -> AdminPage:
        locators = FilterLocators
        s(locators.STATUS_FILTER.value).click()
        time.sleep(3)
        s(self.CLEAR_FILTERS_BUTTON).click()
        time.sleep(3)
        ss(locators.ENGLISH_TITLE_COLUMN.value).should(have.size_greater_than(1))
        return self

    def add_icon(self) -> AdminPage:
        upload_file = s(self.ADD_ICON)
        upload_file.perform(command.js.scroll_into_view)
        upload_file.type(
            str(
                Path(__file__).parent.parent.parent.parent.joinpath(
                    "data/test_files/attachment_file.png"
                )
            )
        )
        return self

    def check_icon(self) -> AdminPage:
        s(self.ICON).should(be.visible)
        return self

    def delete_icon(self):
        delete_icon = s(self.DELETE_ICON)
        delete_icon.perform(command.js.scroll_into_view).should(be.clickable).click()

    def go_to_e_services_categories_list_page(self):
        s(self.CATEGORY_LIST_BUTTON).should(be.visible).click()

    def check_e_services_category_page(self):
        s(self.E_SERVICE_CATEGORY_HEADER).should(be.visible)
        s(self.E_SERVICES_CATEGORY_TABLE).should(be.visible)
        s(self.ADD_E_SERVICE_CATEGORY).should(be.visible)

    def click_add_category_button(self):
        s(self.ADD_E_SERVICE_CATEGORY).should(be.clickable).click()

    def create_new_category_field(self, arabic_name, english_name, code, is_cancel=False):
        arabic_name_field = s(self.NEW_CATEGORY_AR_NAME_FIELD)
        arabic_name_field.wait_until(be.visible)
        arabic_name_field.clear().type(arabic_name)
        s(self.NEW_CATEGORY_EN_NAME_FIELD).should(be.visible).clear().type(english_name)
        s(self.NEW_CODE_FIELD).should(be.visible).clear().type(code)
        if not is_cancel:
            s(self.SAVE_CATEGORY_BUTTON).should(be.enabled).click()
        else:
            s(self.CANCEL_BUTTON).should(be.enabled).click()

    def filter_category_by_english_name(self, english_name):
        s(self.CATEGORY_ENGLISH_NAME_FILTER).should(be.visible).clear().type(english_name)
        time.sleep(3)

    def delete_category(self):
        s(self.DELETE_CATEGORY_BUTTON).should(be.clickable).click()
        alert = browser.switch_to.alert
        assert_that(alert.text).as_("Alert message").equals_to(
            "Are you sure you want to delete this category?"
        )
        alert.accept()

    def edit_category(self, new_en_name, is_cancel=False):
        s(self.EDIT_CATEGORY_BUTTON).should(be.visible).click()
        s(self.EDIT_ENGLISH_NAME_FIELD).clear().type(new_en_name)
        if not is_cancel:
            s(self.SAVE_CATEGORY_BUTTON).should(be.enabled).click()
        else:
            s(self.CANCEL_BUTTON).should(be.enabled).click()

    def check_cancel_action(self):
        s(self.NEW_CATEGORY_AR_NAME_FIELD).should(be.not_.visible)
        s(self.NEW_CATEGORY_EN_NAME_FIELD).should(be.not_.visible)
        s(self.NEW_CODE_FIELD).should(be.not_.visible)

    def check_filtration_on_category_page(self, en_name: str) -> None:
        s(self.CATEGORY_ENGLISH_NAME_COLUMN).should(have.text(en_name))

    def clear_filters_on_category_page(self):
        s(self.CLEAR_CATEGORY_FILTER_BUTTON).should(be.clickable).click()
        time.sleep(3)
        assert len(ss(self.CATEGORY_ENGLISH_NAME_COLUMN)) > 1
