from __future__ import annotations

import allure
from selene import Element, be, have, query
from selene.support.shared.jquery_style import s, ss

from data.user_management import user_management_data
from src.ui.components.raw.table import Table


class UserDetailsPage:
    user_details_title = s("//div[contains(@data-testid, 'section-header')]/div/p")
    subscribed_user_info = s("//div[contains(@data-testid, 'about-user-block')]//p[2]")
    subscribed_user_field_names = ss("//div[contains(@data-testid, 'about-user-block')]//p[1]")
    subscribed_user_name = subscribed_user_info.s("//div[1]/div[1]/p[2]")
    subscription_expiry_date = subscribed_user_info.s("//div[2]/div[2]/p[2]")
    subscribed_personal_number = subscribed_user_info.s("//div[1]/div[2]/p[2]")
    subscription_period_year = subscribed_user_info.s("//div[2]/div[1]/p[2]")

    full_name = subscribed_user_field_names[0]
    national_id = subscribed_user_field_names[1]
    subscription_period = subscribed_user_field_names[2]
    subscription_expiry_field = subscribed_user_field_names[3]

    terminate_btn = s("[data-testid='remove-user-block'] span")
    terminate_text = s("[data-testid='remove-user-block'] p")

    establishment_table_title = s("//div[contains(@data-testid, 'section-table')]/div/p[1]")
    establishment_table_text = s("//div[contains(@data-testid, 'section-table')]/div/p[2]")
    search_title = s("[role='search'] label")
    table_access_tabs = ss("[role='tablist'] button")
    establishment_name_column = s("//thead/tr/th[2]")
    establishment_id_column = s("//thead/tr/th[3]")
    privileges_column = s("//thead/tr/th[4]")
    actions_column = s("//thead/tr/th[5]")
    details_page_breadcrumbs = s("[aria-label='Breadcrumb'] p")

    no_access_table = Table(s("[data-testid='tab-no-allow']"))
    allowed_access_table = Table(s("[data-testid='tab-allow']"))
    actions_buttons = ss("[data-component='Actions']")
    add_access_btn_on_table = "[data-testid='link-toggler-showAddPrivileges']"
    add_privileges_modal = s("[data-testid='modal-add-privileges']")
    edit_privilege_modal = s("[data-testid='modal-edit-privileges']")
    edit_user_privilege_button = s("[data-testid='modal-toggle-state-showEditPrivileges']")
    add_access_btn_on_modal = add_privileges_modal.s("[data-testid='add-access-button']")
    privilege_groups = ss("div[data-testid='group-block']")
    privilege_groups_titles = "p.dSyftF"
    privileges_items = "[data-component='Checkbox']"
    privileges_checkboxes = add_privileges_modal.all("input")
    selected_privilege_items = ss("[data-testid='group-privileges-item']")
    selected_privilege_checkboxes = "input[data-testid='group-privileges-checkbox']"
    unselected_privilege_checkboxes = "input[data-testid='toggle-show-checkbox']"
    all_privileges_item = s("[data-testid='body-modal'] label")
    all_privileges_checkbox = s("input#select-all-modal-body")
    show_more_privileges_buttons = "[data-testid='cb-toggler-link-on']"
    hide_privileges_buttons = "[data-testid='cb-toggler-link-off']"
    close_button = s("button[aria-label='Close modal']")
    success_message = s("[data-component='Toast']")

    def check_user_details_title(self, title) -> UserDetailsPage:
        self.user_details_title.should(have.text(title))
        return self

    def check_users_info_block(self) -> UserDetailsPage:
        self.subscribed_user_name.should(be.visible)
        self.subscription_expiry_date.should(be.visible)
        self.subscribed_personal_number.should(be.visible)
        self.subscription_period_year.should(be.visible)
        return self

    def check_companies_table_is_displayed(self) -> UserDetailsPage:
        self.subscribed_user_info.should(be.visible)
        return self

    def check_ar_localization(self, *texts) -> UserDetailsPage:
        elements = [
            self.full_name,
            self.national_id,
            self.subscription_period,
            self.subscription_expiry_field,
            self.terminate_btn,
            self.terminate_text,
            self.establishment_table_title,
            self.establishment_table_text,
            self.search_title,
            self.table_access_tabs.second,
            self.establishment_name_column,
            self.establishment_id_column,
            self.privileges_column,
            self.actions_column,
            self.details_page_breadcrumbs,
        ]

        for element, text in zip(elements, texts):
            element.should(have.text(text))

        return self

    def switch_to_tab(self, tab_name: str) -> UserDetailsPage:
        self.table_access_tabs.element_by(have.text(tab_name)).click()
        return self

    def click_add_access_button_for_workspace_without_access(
        self, establishment: str
    ) -> UserDetailsPage:
        establishment_without_access = self.no_access_table.rows.element_by(
            have.text(establishment)
        )
        establishment_without_access.s(self.add_access_btn_on_table).click()
        return self

    def check_add_privileges_modal_is_displayed(self) -> UserDetailsPage:
        self.add_privileges_modal.should(be.visible)
        return self

    def check_privileges_group_names(self, groups_data: list) -> UserDetailsPage:
        for i, group_data in enumerate(groups_data):
            privilege_group = self.privilege_groups.element(i)
            privilege_group.s(self.privilege_groups_titles).should(have.text(group_data["title"]))
            privileges_list = privilege_group.ss(self.privileges_items)
            privileges_list.should(have.texts(group_data["privileges"]))
        return self

    def wait_until_privilege_list_is_displayed(self) -> UserDetailsPage:
        ss(self.privileges_items).element_by(
            have.text(user_management_data.OCCUPATION_MANAGEMENT)
        ).should(be.visible)
        return self

    def check_all_privileges_are_selected(self) -> UserDetailsPage:
        for item in self.privileges_checkboxes:
            item.should(be.selected)
        return self

    @allure.step
    def check_privileges_are_selected(
        self, privilege_names: list, active_state: bool = True
    ) -> UserDetailsPage:
        for privilege in privilege_names:
            privilege = self.selected_privilege_items.element_by(have.text(privilege))
            privilege_checkbox = privilege.s(self.selected_privilege_checkboxes).should(
                be.selected
            )
            if active_state:
                privilege_checkbox.should(be.enabled)
            else:
                privilege_checkbox.should(be.disabled)
        return self

    @allure.step
    def check_privileges_are_unselected(
        self, privilege_names: list, active_state: bool = True
    ) -> UserDetailsPage:
        for privilege in privilege_names:
            privilege = ss(self.privileges_items).element_by(have.text(privilege))
            privilege_checkbox = privilege.s(self.unselected_privilege_checkboxes).should(
                have.attribute("aria-checked", "false")
            )
            if active_state:
                privilege_checkbox.should(be.enabled)
            else:
                privilege_checkbox.should(be.disabled)
        return self

    def check_non_default_privileges_are_unselected(self) -> UserDetailsPage:
        for item in ss(self.unselected_privilege_checkboxes):
            item.should(have.attribute("aria-checked", "false"))
        return self

    def click_all_privileges_checkbox(self) -> UserDetailsPage:
        self.all_privileges_item.click()
        return self

    def check_all_privileges_checkbox_is_unselected(self) -> UserDetailsPage:
        self.all_privileges_checkbox.should(have.attribute("aria-checked", "false"))
        return self

    def click_privilege_from_the_list(self, privilege_names: list) -> UserDetailsPage:
        for privilege in privilege_names:
            ss(self.privileges_items).element_by(have.text(privilege)).click()
        return self

    @allure.step
    def close_select_privileges_modal(self) -> UserDetailsPage:
        self.close_button.click()
        self.add_privileges_modal.should(be.not_.visible)
        return self

    def click_show_more_privileges_btn_for_all_groups(self) -> UserDetailsPage:
        for button in ss(self.show_more_privileges_buttons):
            button.click()
        return self

    def click_show_more_btn_for_group(self, group: Element) -> UserDetailsPage:
        group.s(self.show_more_privileges_buttons).click()
        return self

    def click_hide_btn_for_group(self, group: Element) -> UserDetailsPage:
        group.s(self.hide_privileges_buttons).click()
        return self

    def check_show_more_btn_is_displayed(
        self, group: Element, privileges_number: int
    ) -> UserDetailsPage:
        group.s(self.show_more_privileges_buttons).should(
            have.text(f"{user_management_data.SHOW_PRIVILEGES.format(privileges_number)}")
        )
        return self

    def check_hide_privileges_btn_is_displayed(self, group: Element) -> UserDetailsPage:
        group.s(self.hide_privileges_buttons).should(
            have.text(user_management_data.HIDE_PRIVILEGES)
        )
        return self

    def check_hide_privileges_btn_is_not_displayed(self, group: Element) -> UserDetailsPage:
        group.s(self.hide_privileges_buttons).should(be.not_.visible)
        return self

    def click_add_access_btn_on_add_privileges_modal(self) -> UserDetailsPage:
        self.add_access_btn_on_modal.click()
        return self

    def check_establishment_is_added_to_allowed_access(
        self, establishment: str
    ) -> UserDetailsPage:
        self.actions_buttons.element(1).should(be.visible)
        self.allowed_access_table.rows.element_by(have.text(establishment)).should(be.visible)
        return self

    def success_message_is_hidden(self) -> UserDetailsPage:
        self.success_message.should(be.not_.visible)
        return self

    def get_row_with_allowed_establishment(self, labor_office_id: str, sequence_number: str):
        establishment = f"{labor_office_id}-{sequence_number}"
        allowed_table = self.allowed_access_table
        rows = self.allowed_access_table.rows()
        for row_number in range(1, len(rows) + 1):
            cell = allowed_table.cell(row=row_number, column=3)
            if establishment == cell.get(query.text):
                return row_number
        raise AssertionError(f"No establishment found with {establishment}")

    def get_establishment_name(self, row: int) -> str:
        return self.allowed_access_table.cell(row=row, column="Establishment name").get(query.text)

    def check_success_message_is_displayed(self, establishment_name: str) -> UserDetailsPage:
        self.success_message.should(
            have.text(
                f"{user_management_data.SUCCESS_MESSAGE_AFTER_ADD_ACCESS.format(establishment_name)}"
            )
        )
        return self

    def open_edit_privilege_modal(self, row: int) -> UserDetailsPage:
        self.allowed_access_table.cell(row=row, column="Actions").click()
        self.edit_user_privilege_button.click()
        self.edit_privilege_modal.should(be.visible)
        return self
