from __future__ import annotations

import allure
from selene import Element, be, browser, have
from selene.support.shared.jquery_style import s, ss

from data.delegation.constants import DelegationDetailsData, DelegationStatus
from src.ui.components.raw.table import Table
from utils.helpers import convert_timestamp_into_dates


class DelegationDetailsPage:
    localization_button = ss('[data-component="MenuTrigger"] button')[1]
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization_button = s('div[data-component="Menu"] a:first-child')
    action_buttons_block = s('div[data-component="ButtonGroup"]')
    action_buttons = action_buttons_block.ss("button")
    delegation_details_block = ss('div[data-testid="SectionSharedComponent"]')
    general_information_block = delegation_details_block.element_by(
        have.text("General information")
    )
    general_information_table = Table(general_information_block.element("table"))
    delegation_status = general_information_table.row(1).web_element.s('[role="status"]')
    delegation_id = general_information_table.row(2).web_element.s(".hQzqOf")
    entity_name = general_information_table.row(3).web_element.s(".hQzqOf")
    permissions = general_information_table.row(4).web_element.s(".hQzqOf")
    start_date_on_delegation_details = general_information_table.row(5).web_element.s(".hQzqOf")
    expiry_date_on_delegation_details = general_information_table.row(6).web_element.s(".hQzqOf")
    partners_approval_block = delegation_details_block.element_by(have.text("Partners approval"))
    partner_approval_table = Table(partners_approval_block.element("table"))
    partner_names = partner_approval_table.rows.all(".yjILx")
    partner_phone_numbers = partner_approval_table.rows.all(".kFZsWB")
    partner_request_status = partner_approval_table.rows.all('[role="status"]')
    delegate_block = delegation_details_block.element_by(have.text("Delegate"))
    delegate_table = Table(delegate_block.element("table"))
    delegate_name = delegate_table.row(1).web_element.s(".hQzqOf")
    delegate_nid = delegate_table.row(2).web_element.s(".hQzqOf")
    delegate_nationality = delegate_table.row(3).web_element.s(".hQzqOf")
    delegate_occupation = delegate_table.row(4).web_element.s(".hQzqOf")

    @allure.step
    def select_english_localization_on_delegation_details(self) -> DelegationDetailsPage:
        self.localization_button.click()
        self.english_localization_button.click()
        self.localization_state.wait_until(have.exact_text("EN"))
        return self

    @allure.step
    def wait_delegation_details_page_to_load(self) -> DelegationDetailsPage:
        self.general_information_block.should(be.visible)
        return self

    @allure.step
    def should_action_buttons_be_correct(self, actions: list) -> DelegationDetailsPage:
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
            self.should_action_buttons_be_correct(DelegationDetailsData.RESEND_ACTION)
        else:
            self.should_action_buttons_be_hidden()
        return self

    @allure.step
    def check_redirect_to_delegation_details(self, delegation_id: str):
        browser.should(
            have.url("https://delegationservice.qiwa.info/delegation-details/" + delegation_id)
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
        self, status: str, timestamp: float, locator: Element
    ) -> DelegationDetailsPage:
        if status in [DelegationStatus.ACTIVE, DelegationStatus.EXPIRED, DelegationStatus.REVOKED]:
            date = convert_timestamp_into_dates(timestamp)
            locator.should(have.text(date))
        else:
            locator.should(have.text("-"))
        return self

    @allure.step
    def should_partners_approval_block_be_displayed(self) -> DelegationDetailsPage:
        self.partners_approval_block.should(be.visible)
        return self

    @allure.step
    def should_partner_name_be_correct(self, partner_list: list) -> DelegationDetailsPage:
        partner_names = []
        for partner in partner_list:
            partner_names.append(partner["partnerName"])
        self.partner_names.should(have.texts(partner_names))
        return self

    @allure.step
    def should_partner_phone_be_correct(self, partner_list: list) -> DelegationDetailsPage:
        partner_phones = []
        for partner in partner_list:
            partner_phones.append(partner["partnerPhoneNumber"])
        self.partner_phone_numbers.should(have.texts(partner_phones))
        return self

    @allure.step
    def should_partner_request_status_be_correct(
        self, partner_list: list
    ) -> DelegationDetailsPage:
        partner_request_statuses = []
        for partner in partner_list:
            if partner["status"] == DelegationStatus.PENDING:
                expected_status = DelegationDetailsData.PENDING_REQUEST
            else:
                expected_status = partner["status"].capitalize()
            partner_request_statuses.append(expected_status)
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
