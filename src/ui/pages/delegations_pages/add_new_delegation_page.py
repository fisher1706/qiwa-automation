from __future__ import annotations

import allure
from selene import be, browser, command, have, query
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import add_delegation_data, general_data
from src.ui.components.raw.table import Table


class AddDelegationPage:
    step = 'div[data-testid="{0}"]'
    step_title = 'div[data-testid="{0}"] > div:nth-child(1) > div'
    step_number = 'div[data-testid="{0}"] span[data-component="StepIndex"]'
    successful_step_img = 'div[data-testid="{0}"] span[data-component="StepIndex"] svg'
    localization_button = ss('[data-component="MenuTrigger"] button').element(1)
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization = s('div[data-component="Menu"] a:nth-child(1)')
    entity_types_radio_buttons = s('[data-testid="ExternalEntityRadioTileGroup"]')
    government_entity_type = s("#GOVERNMENT")
    government_entity_type_text = s("#GOVERNMENT-label")
    financial_entity_type = s("#FINANCIAL")
    financial_entity_type_text = s("#FINANCIAL-label")
    telecom_entity_type = s("#TELECOM")
    telecom_entity_type_text = s("#TELECOM-label")
    entity_name_input = s("#ExternalEntitySelect")
    input_option = s('li[role="option"]')
    entity_message = s(
        'div[data-testid="StepsWrapperExternalEntityStep"] [data-component="Message"]'
    )
    next_button = s("#StepsWrapperNextButton")
    permission_input = s("#PermissionsSelect")
    selected_option = s('div[data-component="InputChip"]')
    remove_permission_button = s('button[aria-label="Remove permission"]')
    duration_input = s("#DurationSelect")
    duration_months_list = ss('ul[role="listbox"] li[role="option"]')
    duration_message = s('div[data-testid="StepsWrapperDurationStep"] [data-component="Message"]')
    entity_data_on_completed_step = ss(
        '[data-testid="StepsWrapperExternalEntityStep"] p[data-testid="CompletedViewValue"]'
    )
    permission_on_completed_step = s(
        '[data-testid="StepsWrapperPermissionsStep"] p[data-testid="CompletedViewValue"]'
    )
    duration_on_completed_step = s(
        '[data-testid="StepsWrapperDurationStep"] p[data-testid="CompletedViewValue"]'
    )
    number_of_employees = s('div[data-component="Pagination"] > p')
    employees_input = s("#SearchBoxSearchField")
    employees_table = Table("#DelegateTableWrapper table")
    search_result = employees_table.cells(row=1).from_(1)
    remove_selected_employee_button = s('button[aria-label="remove"]')
    employee_table_on_completed_step = Table(
        '[data-testid="StepsWrapperDelegateDetailsStep"] table'
    )
    selected_employee_data = employee_table_on_completed_step.cells(row=1)
    partner_step_description = s('div[data-component="Divider"] + p')
    confirmation_modal = s('div[data-testid="ConfirmCreateDelegationModal"]')
    title_on_confirmation_modal = s('p[data-testid="ConfirmCreateDelegationModalTitle"]')
    confirm_button_on_modal = s('button[data-testid="ConfirmCreateDelegationModalAction"]')
    cancel_button_on_modal = s('button[data-testid="ConfirmCreateDelegationModalClose"]')
    close_button_on_modal = s('button[aria-label="Close modal"]')
    successful_modal = s('div[data-testid="CreateDelegationResult"]')
    title_on_successful_modal = s('p[role="heading"]')
    text_on_successful_modal = s('[data-testid="CreateDelegationResultDescription"]')
    button_on_successful_modal = successful_modal.s("button")
    partners_message = s(
        'div[data-testid="StepsWrapperSummaryStep"] div[data-component="Message"]'
    )
    partners_table = Table('div[data-testid="StepsWrapperSummaryStep"] table')
    table_description = s('p[data-testid="SummaryTableTitle"]')

    @allure.step
    def wait_add_new_delegation_page_to_load(self) -> AddDelegationPage:
        self.entity_name_input.should(be.visible)
        return self

    @allure.step
    def should_step_be_opened(self, step_id: str, step_number: str) -> AddDelegationPage:
        s(self.step_number.format(step_id)).should(have.exact_text(step_number))
        s(self.step_number.format(step_id)).should(
            have.css_property(
                name=add_delegation_data.BACKGROUND_COLOR_NAME,
                value=add_delegation_data.OPENED_STEP_COLOR,
            )
        )
        return self

    @allure.step
    def should_step_be_closed(self, step_id: str) -> AddDelegationPage:
        s(self.step_number.format(step_id)).should(
            have.css_property(
                name=add_delegation_data.BACKGROUND_COLOR_NAME,
                value=add_delegation_data.CLOSED_STEP_COLOR,
            )
        )
        return self

    @allure.step
    def should_url_for_add_delegation_page_be_correct(self) -> AddDelegationPage:
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/create-delegation"))
        return self

    @allure.step
    def select_english_localization_on_add_delegation_page(self) -> AddDelegationPage:
        # pylint: disable=R0801
        self.localization_button.click()
        self.english_localization.click()
        self.localization_state.wait_until(have.exact_text(general_data.ENGLISH_LOCAL))
        return self

    @allure.step
    def select_entity_name_on_add_delegation_page(self, entity_name: str) -> AddDelegationPage:
        self.entity_name_input.click()
        self.input_option.should(have.exact_text(entity_name))
        self.input_option.click()
        return self

    @allure.step
    def should_entity_name_be_selected(self, entity_name: str) -> AddDelegationPage:
        self.entity_name_input.should(have.value(entity_name))
        self.entity_message.should(have.exact_text(add_delegation_data.MESSAGE_ON_FIRST_STEP))
        return self

    @allure.step
    def click_next_button_on_add_delegation_page(self) -> AddDelegationPage:
        self.next_button.click()
        return self

    @allure.step
    def should_government_entity_type_be_selected(
        self, government_entity: str
    ) -> AddDelegationPage:
        self.government_entity_type.should(be.selected)
        self.government_entity_type_text.should(have.exact_text(government_entity))
        return self

    @allure.step
    def should_financial_entity_type_be_disabled(self, financial_entity: str) -> AddDelegationPage:
        self.financial_entity_type.should(be.disabled)
        self.financial_entity_type_text.should(have.exact_text(financial_entity))
        return self

    @allure.step
    def should_telecom_entity_type_be_disabled(self, telecom_entity: str) -> AddDelegationPage:
        self.telecom_entity_type.should(be.disabled)
        self.telecom_entity_type_text.should(have.exact_text(telecom_entity))
        return self

    @allure.step
    def select_permission_on_add_delegation_page(self, permission: str) -> AddDelegationPage:
        self.permission_input.click()
        self.input_option.should(have.exact_text(permission))
        self.input_option.click()
        return self

    @allure.step
    def should_permission_be_selected(self, permission: str) -> AddDelegationPage:
        self.selected_option.should(have.exact_text(permission))
        return self

    @allure.step
    def click_remove_button_for_selected_permission(self) -> AddDelegationPage:
        self.remove_permission_button.click()
        return self

    @allure.step
    def should_option_be_removed(self) -> AddDelegationPage:
        self.selected_option.should(be.not_.visible)
        return self

    @allure.step
    def should_months_be_displayed_on_duration_list(self, months_list: list) -> AddDelegationPage:
        self.duration_input.click()
        self.duration_months_list.should(have.exact_texts(months_list))
        self.duration_input.click()
        return self

    @allure.step
    def select_duration_month(self, month_number: str) -> AddDelegationPage:
        self.duration_input.click()
        self.duration_months_list.element_by(have.text(month_number)).click()
        return self

    @allure.step
    def should_duration_month_be_selected(self, month_number: str) -> AddDelegationPage:
        self.duration_input.should(have.value(month_number))
        self.duration_message.should(have.exact_text(add_delegation_data.MESSAGE_ON_THIRD_STEP))
        return self

    @allure.step
    def should_step_be_completed(self, step_id: str) -> AddDelegationPage:
        s(self.step_number.format(step_id)).should(
            have.css_property(
                name=add_delegation_data.BACKGROUND_COLOR_NAME,
                value=add_delegation_data.COMPLETED_STEP_COLOR,
            )
        )
        s(self.successful_step_img.format(step_id)).should(be.visible)
        return self

    @allure.step
    def should_entity_data_be_displayed_on_completed_step(
        self, entity_data: list
    ) -> AddDelegationPage:
        self.entity_data_on_completed_step.should(have.exact_texts(entity_data))
        self.entity_message.should(be.visible)
        return self

    @allure.step
    def should_permission_be_displayed_on_completed_step(
        self, permission: str
    ) -> AddDelegationPage:
        self.permission_on_completed_step.should(have.exact_text(permission))
        return self

    @allure.step
    def should_duration_be_displayed_on_completed_step(self, duration: str) -> AddDelegationPage:
        self.duration_on_completed_step.should(have.exact_text(duration))
        self.duration_message.should(be.not_.visible)
        return self

    @allure.step
    def should_employee_data_be_displayed_on_completed_step(
        self, employee_data: dict
    ) -> AddDelegationPage:
        self.selected_employee_data.should(
            have.exact_texts(
                employee_data["name"],
                employee_data["nid"],
                employee_data["nationalityEn"],
                employee_data["jobName"],
            )
        )
        return self

    @allure.step
    def should_number_of_employees_be_correct(
        self, number_of_delegates: int | str
    ) -> AddDelegationPage:
        self.number_of_employees.should(have.text(str(number_of_delegates)))
        return self

    @allure.step
    def search_employee_list_by_nid(self, employee_nid: str) -> AddDelegationPage:
        self.employees_input.type(employee_nid)
        return self

    @allure.step
    def should_employee_data_be_correct(self, employee_data: dict) -> AddDelegationPage:
        self.search_result.should(
            have.exact_texts(
                employee_data["name"],
                employee_data["nid"],
                employee_data["nationalityEn"],
                employee_data["jobName"],
            )
        )
        return self

    @allure.step
    def select_employee_on_add_delegation_page(self, employee_number: int) -> AddDelegationPage:
        self.employees_table.cell(row=employee_number, column=1).click()
        self.employees_table.cell(row=employee_number, column=1).s("input").should(be.selected)
        return self

    def get_selected_employee_name_on_add_delegation_page(self, employee_number: int) -> str:
        employee_name = self.employees_table.cell(row=employee_number, column=2).get(query.text)
        return employee_name

    @allure.step
    def should_employee_be_selected(self, employee_name) -> AddDelegationPage:
        self.selected_option.should(have.exact_text(employee_name))
        self.remove_selected_employee_button.should(be.visible)
        return self

    @allure.step
    def click_remove_button_for_selected_employee(self) -> AddDelegationPage:
        self.remove_selected_employee_button.click()
        return self

    @allure.step
    def should_content_be_displayed_for_establishment_without_partner(self) -> AddDelegationPage:
        self.partner_step_description.should(
            have.exact_text(add_delegation_data.STEP_DESCRIPTION_WITH_NO_PARTNERS)
        )
        self.partners_table.web_element.should(be.not_.visible)
        self.next_button.should(
            have.exact_text(add_delegation_data.CONFIRM_BUTTON_WITH_NO_PARTNERS)
        )
        return self

    @allure.step
    def should_content_be_displayed_for_establishment_with_partners(self) -> AddDelegationPage:
        self.partner_step_description.should(
            have.exact_text(add_delegation_data.STEP_DESCRIPTION_WITH_PARTNERS)
        )
        self.partners_message.should(have.exact_text(add_delegation_data.MESSAGE_ON_FIFTH_STEP))
        self.table_description.should(have.exact_text(add_delegation_data.TABLE_DESCRIPTION))
        self.partners_table.web_element.should(be.visible)
        self.next_button.should(have.exact_text(add_delegation_data.CONFIRM_BUTTON_WITH_PARTNERS))
        return self

    @allure.step
    def should_confirmation_modal_be_opened(self) -> AddDelegationPage:
        self.confirmation_modal.should(be.visible)
        self.title_on_confirmation_modal.should(
            have.exact_text(add_delegation_data.CONFIRM_MODAL_TITLE)
        )
        self.confirm_button_on_modal.should(have.exact_text(add_delegation_data.CONFIRM_BUTTON))
        self.cancel_button_on_modal.should(have.exact_text(add_delegation_data.CANCEL_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_close_button_on_confirmation_modal(self) -> AddDelegationPage:
        self.close_button_on_modal.click()
        return self

    @allure.step
    def should_confirmation_modal_be_closed(self) -> AddDelegationPage:
        self.confirmation_modal.should(be.not_.visible)
        return self

    @allure.step
    def click_confirm_request_button_on_confirmation_modal(self) -> AddDelegationPage:
        self.confirm_button_on_modal.click()
        return self

    @allure.step
    def should_successful_modal_be_opened(
        self, establishment_with_partners: bool
    ) -> AddDelegationPage:
        self.successful_modal.should(be.visible)
        self.title_on_successful_modal.should(
            have.exact_text(add_delegation_data.SUCCESSFUL_MODAL_TITLE)
        )
        if establishment_with_partners:
            self.text_on_successful_modal.should(
                have.exact_text(add_delegation_data.SUCCESSFUL_MODAL_TEXT_WITH_PARTNERS)
            )
        else:
            self.text_on_successful_modal.should(
                have.exact_text(add_delegation_data.SUCCESSFUL_MODAL_TEXT_WITH_NO_PARTNERS)
            )
        self.button_on_successful_modal.should(
            have.exact_text(add_delegation_data.SUCCESSFUL_MODAL_BUTTON)
        )
        return self

    @allure.step
    def click_go_back_to_delegations_button_on_modal(self) -> AddDelegationPage:
        self.button_on_successful_modal.click()
        return self

    @allure.step
    def should_number_of_partners_be_correct(self, partner_number: int) -> AddDelegationPage:
        self.partners_table.rows.should(have.size(partner_number))
        return self

    @allure.step
    def should_partners_data_be_correct(
        self, partner_number: int, partners_data: list
    ) -> AddDelegationPage:
        self.partners_table.cells(row=partner_number).from_(1).should(
            have.exact_texts(partners_data)
        )
        return self

    def scroll_to_the_fifth_step(self) -> AddDelegationPage:
        self.partners_table.web_element.perform(command.js.scroll_into_view)
        return self
