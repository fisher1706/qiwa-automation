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

    @allure.step
    def click_btn_proceed_subscription(self, number: int = None) -> ConfirmationPage:
        self.btn_proceed_subscription[number].should(
            be.visible
        ).click() if number else self.btn_proceed_subscription[0].should(be.visible).click()
        return self

    def check_confirmation_page_is_opened(self) -> ConfirmationPage:
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

    def click_back_btn_on_confirmation_page(self) -> ConfirmationPage:
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
