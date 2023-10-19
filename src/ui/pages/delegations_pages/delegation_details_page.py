from __future__ import annotations

import allure
from selene import Element, be, browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import general_data
from src.ui.components.raw.table import Table


class DelegationDetailsPage:
    localization_button = ss('[data-component="MenuTrigger"] button').element(1)
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization = s('div[data-component="Menu"] a:nth-child(1)')
    action_buttons_block = s('div[data-component="ButtonGroup"]')
    action_buttons = action_buttons_block.ss("button")
    general_information_block = s("#DelegationDetailsSection1")
    general_information_table = Table(general_information_block.element("table"))
    delegation_status = general_information_table.row(1).s('[role="status"]')
    delegation_id = general_information_table.row(2).s('[data-testid="tableCellValue"]')
    entity_name = general_information_table.row(3).s('[data-testid="tableCellValue"]')
    permissions = general_information_table.row(4).s('[data-testid="tableCellValue"]')
    start_date_on_delegation_details = general_information_table.row(5).s(
        '[data-testid="tableCellValue"]'
    )
    expiry_date_on_delegation_details = general_information_table.row(6).s(
        '[data-testid="tableCellValue"]'
    )
    partners_approval_block = s("#DelegationDetailsSection2")
    partner_approval_table = Table(partners_approval_block.element("table"))
    partner_names = partner_approval_table.rows.all('[data-testid="partnerName"]')
    partner_phone_numbers = partner_approval_table.rows.all('[data-testid="partnerPhoneNumber"]')
    partner_request_status = partner_approval_table.rows.all('[role="status"]')
    delegate_block = s("#DelegationDetailsSection3")
    delegate_table = Table(delegate_block.element("table"))
    delegate_name = delegate_table.row(1).s('[data-testid="tableCellValue"]')
    delegate_nid = delegate_table.row(2).s('[data-testid="tableCellValue"]')
    delegate_nationality = delegate_table.row(3).s('[data-testid="tableCellValue"]')
    delegate_occupation = delegate_table.row(4).s('[data-testid="tableCellValue"]')
    resend_modal = s('div[data-testid="ResendModal"]')
    title_on_modal = s('[id="modalBodyWrapper"] p.dIVImG')
    description_on_modal = s('[id="modalBodyWrapper"] p.gggtgX')
    message_on_resend_modal = s('div[data-component="Message"]')
    resend_button_on_modal = s('button[data-testid="ResendModalAction"]')
    loader_on_action_button = s('span[data-component="Loader"]')
    cancel_button_on_resend_modal = s('button[data-testid="ResendModalClose"]')
    toast_after_action = s('div[data-component="Toast"]')
    icon_on_toast = s('div[data-component="Toast"] > span[data-component="Icon"] > svg')
    revoke_modal = s('div[data-testid="RevokeModal"]')
    revoke_button_on_modal = s('button[data-testid="RevokeModalAction"]')
    go_back_button_on_revoke_modal = s('button[data-testid="RevokeModalClose"]')
    close_button_on_modal = s('button[aria-label="Close modal"]')

    @allure.step
    def select_english_localization_on_delegation_details(self) -> DelegationDetailsPage:
        self.localization_button.click()
        self.english_localization.click()
        self.localization_state.wait_until(have.exact_text(general_data.ENGLISH_LOCAL))
        return self

    @allure.step
    def wait_delegation_details_page_to_load(self) -> DelegationDetailsPage:
        self.general_information_block.should(be.visible)
        return self

    @allure.step
    def should_action_buttons_be_correct(self, actions: list | str) -> DelegationDetailsPage:
        self.action_buttons.should(have.exact_texts(actions))
        return self

    @allure.step
    def should_action_buttons_be_hidden(self) -> DelegationDetailsPage:
        self.action_buttons_block.should(be.not_.visible)
        return self

    @allure.step
    def check_actions_for_rejected_delegation(
        self, available_for_resending: bool
    ) -> DelegationDetailsPage:
        if available_for_resending:
            self.should_action_buttons_be_correct([general_data.RESEND_ACTION])
        else:
            self.should_action_buttons_be_hidden()
        return self

    @allure.step
    def select_action_on_delegation_details(self, action: str) -> DelegationDetailsPage:
        self.action_buttons.element_by(have.text(action)).click()
        return self

    @allure.step
    def check_redirect_to_delegation_details(self, delegation_id: str):
        browser.should(
            have.url(f"{config.qiwa_urls.delegation_service}/delegation-details/{delegation_id}")
        )
        return self

    @allure.step
    def should_general_information_block_be_displayed(self) -> DelegationDetailsPage:
        self.general_information_block.should(be.visible)
        return self

    @allure.step
    def should_delegation_status_be_correct_on_delegation_details(
        self, delegation_status: str
    ) -> DelegationDetailsPage:
        self.delegation_status.should(have.exact_text(delegation_status.capitalize()))
        return self

    @allure.step
    def should_delegation_id_be_correct_on_delegation_details(
        self, delegation_id: int | str
    ) -> DelegationDetailsPage:
        self.delegation_id.should(have.exact_text(str(delegation_id)))
        return self

    @allure.step
    def should_entity_name_be_correct_on_delegation_details(
        self, entity_name: str
    ) -> DelegationDetailsPage:
        self.entity_name.should(have.exact_text(entity_name))
        return self

    @allure.step
    def should_permission_be_correct_on_delegation_details(
        self, permission: str
    ) -> DelegationDetailsPage:
        self.permissions.should(have.exact_text(permission))
        return self

    @allure.step
    def should_dates_be_correct_on_delegation_details(
        self, status: str, date: str, locator: Element
    ) -> DelegationDetailsPage:
        if status in [general_data.ACTIVE, general_data.EXPIRED, general_data.REVOKED]:
            locator.should(have.text(date))
        else:
            locator.should(have.text("-"))
        return self

    @allure.step
    def should_partners_approval_block_be_displayed(self) -> DelegationDetailsPage:
        self.partners_approval_block.should(be.visible)
        return self

    @allure.step
    def should_partner_name_be_correct(self, partner_names: list) -> DelegationDetailsPage:
        self.partner_names.should(have.texts(partner_names))
        return self

    @allure.step
    def should_partner_phone_be_correct(self, partner_numbers: list) -> DelegationDetailsPage:
        self.partner_phone_numbers.should(have.texts(partner_numbers))
        return self

    @allure.step
    def should_partner_request_status_be_correct(
        self, partner_request_statuses: list | str
    ) -> DelegationDetailsPage:
        self.partner_request_status.should(have.texts(partner_request_statuses))
        return self

    @allure.step
    def should_partner_approval_block_be_hidden(self) -> DelegationDetailsPage:
        self.partners_approval_block.should(be.not_.visible)
        return self

    @allure.step
    def should_delegate_block_be_displayed(self) -> DelegationDetailsPage:
        self.delegate_block.should(be.visible)
        return self

    @allure.step
    def should_delegate_name_be_correct_on_delegation_details(
        self, delegate_name: str
    ) -> DelegationDetailsPage:
        self.delegate_name.should(have.exact_text(delegate_name))
        return self

    @allure.step
    def should_delegate_nid_be_correct_on_delegation_details(
        self, delegate_nid: str
    ) -> DelegationDetailsPage:
        self.delegate_nid.should(have.exact_text(delegate_nid))
        return self

    @allure.step
    def should_delegate_nationality_be_correct_on_delegation_details(
        self, delegate_nationality: str
    ) -> DelegationDetailsPage:
        self.delegate_nationality.should(have.exact_text(delegate_nationality))
        return self

    @allure.step
    def should_delegate_occupation_be_correct_on_delegation_details(
        self, delegate_occupation: str
    ) -> DelegationDetailsPage:
        self.delegate_occupation.should(have.exact_text(delegate_occupation))
        return self

    @allure.step
    def should_resend_confirmation_modal_be_displayed_on_delegation_details(
        self,
    ) -> DelegationDetailsPage:
        self.resend_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.RESEND_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.RESEND_MODAL_DESCRIPTION))
        self.message_on_resend_modal.should(have.exact_text(general_data.RESEND_MODAL_MESSAGE))
        self.resend_button_on_modal.should(have.exact_text(general_data.RESEND_BUTTON))
        self.cancel_button_on_resend_modal.should(have.exact_text(general_data.CANCEL_BUTTON))
        return self

    @allure.step
    def click_resend_request_button_on_delegation_details(self) -> DelegationDetailsPage:
        self.resend_button_on_modal.click()
        self.loader_on_action_button.should(be.visible)
        return self

    @allure.step
    def should_successful_message_be_displayed_on_delegation_details(
        self, message: str
    ) -> DelegationDetailsPage:
        self.toast_after_action.should(have.text(message))
        self.toast_after_action.should(
            have.css_property(
                name=general_data.BACKGROUND_COLOR_NAME,
                value=general_data.SUCCESSFUL_MESSAGE_COLOR,
            )
        )
        self.icon_on_toast.should(be.visible)
        return self

    @allure.step
    def should_revoke_confirmation_modal_be_displayed_on_delegation_details(
        self,
    ) -> DelegationDetailsPage:
        self.revoke_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_DESCRIPTION))
        self.revoke_button_on_modal.should(have.exact_text(general_data.REVOKE_BUTTON))
        self.go_back_button_on_revoke_modal.should(have.exact_text(general_data.GO_BACK_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_revoke_delegation_button_on_dashboard(self) -> DelegationDetailsPage:
        self.revoke_button_on_modal.click()
        self.loader_on_action_button.should(be.visible)
        return self
