from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.user_management import user_management_data
from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class ConfirmationPage(BaseEstablishmentPayment):
    page_title = s("[data-testid='layout-with-instruction'] > p")
    btn_proceed_subscription = ss("//button//p[contains(text(), 'Proceed with subscription')]")
    content_sections = ss("div.Bntha")
    back_btn = s("[data-testid='breadcrumps'] a")
    establishment_name = "[data-testid='named-row'] p.hCLJZp"
    establishment_number = "[role='status']"
    establishment_data = "[data-testid='named-row'] p.gtnWDv"
    error_message = "[data-component='Message']"
    links = "[data-component='Link']"
    add_address_info_btn = s("[data-testid='button-edit-address']")
    vat_error_description = "p.gggtgX"
    vat_error_buttons = "[type='button']"
    edit_button = "[data-testid='edit-btn']"
    register_without_vat_btn = s("[data-testid='button-edit-vat']")

    @allure.step
    def click_btn_proceed_subscription(self, number: int = None) -> ConfirmationPage:
        self.btn_proceed_subscription[number].should(
            be.visible
        ).click() if number else self.btn_proceed_subscription[0].should(be.visible).click()
        return self

    def check_confirmation_page_is_displayed(self) -> ConfirmationPage:
        self.page_title.should(have.text(user_management_data.CONFIRMATION_PAGE_TITLE))
        browser.should(have.url_containing(f"{config.qiwa_urls.ui_user_management}/confirmation/"))
        content_sections_titles = [
            user_management_data.ESTABLISHMENT_NAME_SECTION,
            user_management_data.CONTACT_INFO_SECTION,
            user_management_data.ESTABLISHMENT_ADDRESS_SECTION,
            user_management_data.ZAKAT_TAX_SECTION,
        ]
        for title in content_sections_titles:
            self.content_sections.element_by(have.text(title)).should(be.visible)
        return self

    def click_back_btn_on_owner_subscription_flow(self) -> ConfirmationPage:
        self.back_btn.click()
        return self

    def check_content_on_establishment_section(
        self, establishment_name: str, establishment_number: str
    ) -> ConfirmationPage:
        establishment_section = self.content_sections.element_by(
            have.text(user_management_data.ESTABLISHMENT_NAME_SECTION)
        )
        establishment_section.s(self.establishment_name).should(have.text(establishment_name))
        establishment_section.s(self.establishment_number).should(have.text(establishment_number))
        return self

    def check_sections_content_on_confirmation_page(
        self, section_title: str, content_data: list
    ) -> ConfirmationPage:
        establishment_section = self.content_sections.element_by(have.text(section_title))
        establishment_section.ss(self.establishment_data).should(have.texts(content_data))
        return self

    def check_texts_for_main_error_block(self, title: str, links: list) -> ConfirmationPage:
        main_error_block = ss(self.error_message).element_by(have.text(title)).should(be.visible)
        main_error_block.ss(self.links).should(have.texts(links))
        return self

    def check_texts_for_address_error_block(
        self, title: str, missing_address_data: list, btn_text: str
    ) -> ConfirmationPage:
        address_error_block = (
            ss(self.error_message).element_by(have.text(title)).should(be.visible)
        )
        address_error_block.ss("li").should(have.texts(missing_address_data))
        self.add_address_info_btn.should(have.text(btn_text))
        return self

    def check_texts_for_vat_error_block(
        self, title: str, vat_error_description: str, btn_texts: list
    ) -> ConfirmationPage:
        vat_error_block = ss(self.error_message).element_by(have.text(title)).should(be.visible)
        vat_error_block.s(self.vat_error_description).should(have.text(vat_error_description))
        vat_error_block.ss(self.vat_error_buttons).should(have.texts(btn_texts))
        return self

    def click_edit_btn_for_section(self, section_title: str) -> ConfirmationPage:
        section = self.content_sections.element_by(have.text(section_title))
        section.s(self.edit_button).click()
        return self

    def click_add_address_info_btn_on_confirmation_page(self) -> ConfirmationPage:
        self.add_address_info_btn.click()
        return self

    def check_error_message_is_not_displayed(self) -> ConfirmationPage:
        s(self.error_message).should(be.not_.visible)
        return self

    def click_register_without_vat_btn(self) -> ConfirmationPage:
        self.register_without_vat_btn.click()
        return self
