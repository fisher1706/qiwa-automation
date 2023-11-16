from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import add_delegation_data, general_data


class VerifyDelegationLetterPage:
    page_title = s("[data-testid='VerificationTitle']")
    page_description = s("[data-testid='VerificationSubTitle']")
    upload_file_input = s("input#file")
    delegation_letter_details_modal = s("div[data-testid='LetterDetailsModal']")
    back_to_verification = s("button[data-testid='LetterDetailsModalAction']")
    close_button = s("[aria-label='Close modal']")
    title_on_delegation_details_modal = s("p[data-testid='LetterDetailsModalTitle']")
    names_on_delegation_details_modal = ss("p.iPZhcW")
    values_on_delegation_details_modal = ss(".jBwkPH")
    status_on_delegation_details_modal = s("div[role='status']")
    title_on_error_modal = s("p[data-testid='LetterDetailsModalErrorTitle']")
    description_on_error_modal = s("p[data-testid='LetterDetailsModalErrorDescription']")

    @allure.step
    def should_verify_letter_page_be_displayed(self) -> VerifyDelegationLetterPage:
        self.page_title.should(have.text(general_data.VERIFY_LETTER_TITLE))
        self.page_description.should(have.text(general_data.VERIFY_LETTER_DESCRIPTION))
        return self

    @allure.step
    def upload_delegation_letter(self, file_path: str) -> VerifyDelegationLetterPage:
        self.upload_file_input.send_keys(file_path)
        return self

    @allure.step
    def should_delegation_letter_modal_be_displayed(self) -> VerifyDelegationLetterPage:
        self.delegation_letter_details_modal.should(be.visible)
        self.title_on_delegation_details_modal.should(
            have.text(general_data.DELEGATION_DETAILS_MODAL)
        )
        self.names_on_delegation_details_modal.should(
            have.texts(
                "Status",
                "Delegation ID",
                "Delegate name",
                "Delegate NID",
                "Permissions",
                "Establishment",
                "External entity name",
                "Expiration date",
            )
        )
        self.close_button.should(be.visible)
        return self

    @allure.step
    def should_values_on_delegation_letter_modal_be_correct(
        self,
        status: str,
        delegation_id: str,
        delegate_name: str,
        delegate_nid: str,
        establishment: str,
        expiry_date: str,
    ) -> VerifyDelegationLetterPage:
        self.status_on_delegation_details_modal.should(have.exact_text(status.capitalize()))
        self.values_on_delegation_details_modal.should(
            have.exact_texts(
                delegation_id,
                delegate_name,
                delegate_nid,
                add_delegation_data.PERMISSION,
                establishment,
                add_delegation_data.ENTITY_NAME,
                expiry_date,
            )
        )
        return self

    @allure.step
    def click_back_to_verification_button(self) -> VerifyDelegationLetterPage:
        self.back_to_verification.click()
        return self

    @allure.step
    def should_verify_delegation_letter_modal_be_closed(self) -> VerifyDelegationLetterPage:
        self.delegation_letter_details_modal.should(be.not_.visible)
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/verify"))
        return self

    @allure.step
    def should_modal_with_error_be_displayed(self) -> VerifyDelegationLetterPage:
        self.delegation_letter_details_modal.should(be.visible)
        self.title_on_error_modal.should(have.text(general_data.ERROR_MODAL_TITLE))
        self.description_on_error_modal.should(have.text(general_data.ERROR_MODAL_DESCRIPTION))
        return self
