from __future__ import annotations

import allure
from selene import Element, be, have
from selene.core.entity import Collection
from selene.support.shared.jquery_style import s, ss

from data.user_management import user_management_data
from data.user_management.user_management_datasets import ArabicTranslations
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
    allowed_establishments_checkboxes = allowed_access_table.web_element.all("input")
    establishments_inputs = "input[data-testid='handle-selected']"
    actions_buttons = "[data-component='Actions']"
    remove_access_btn_below_establishments_table = s("[data-testid='toggle-modal-state']")
    cancel_btn_below_establishments_table = s("[data-testid='clear-all']")
    selected_establishments_text_below_table = ss("div.fvDbgF > div.iPxNsA").first
    link_below_establishments_table = s("[data-testid='toggle-select-all']")
    add_access_btn_on_table = "[data-testid='link-toggler-showAddPrivileges']"
    add_privileges_modal = s("[data-testid='modal-add-privileges']")
    texts_on_select_privileges_modal = ss("#modalBodyWrapper p")
    edit_privilege_modal = s("[data-testid='modal-edit-privileges']")
    save_btn_on_edit_privilege_modal = edit_privilege_modal.s(
        "[data-testid='save-edit-privileges']"
    )
    remove_access_btn_on_edit_privilege_modal = edit_privilege_modal.s(
        "[data-testid='modal-state-toggler']"
    )
    remove_access_modal = s("[data-testid='modal-remove-access-block']")
    texts_on_remove_access_modal = ss("#modalBodyWrapper p")
    cancel_btn_on_modal = s("[data-testid='close-button']")
    remove_btn_on_remove_access_modal = remove_access_modal.s(
        "[data-testid='store-delete-button']"
    )
    edit_user_privilege_btn_on_table = s("[data-testid='modal-toggle-state-showEditPrivileges']")
    remove_access_btn_on_table = s("[data-testid='modal-toggle-state-showRemoveAccess']")
    add_access_btn_on_modal = add_privileges_modal.s("[data-testid='add-access-button']")
    terminate_modal = s("[data-testid='modal-remove-user-block']")
    delete_user_btn_on_terminate_modal = terminate_modal.s("[data-testid='button-delete']")
    paired_privileges_descriptions = ss("[data-testid='is-dependence']")
    privilege_groups = ss("div[data-testid='group-block']")
    privilege_groups_titles = "p.dSyftF"
    checkbox_items = "[data-component='Checkbox']"
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
            self.table_access_tabs.first,
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

    def check_ar_localization_for_add_access_btn(self) -> UserDetailsPage:
        s(self.add_access_btn_on_table).should(have.text(ArabicTranslations.add_access_btn))
        return self

    def check_ar_localization_for_content_on_select_privileges_modal(
        self, *texts
    ) -> UserDetailsPage:
        elements = [
            self.texts_on_select_privileges_modal.second,
            self.all_privileges_item,
            s(self.hide_privileges_buttons),
            ss(self.show_more_privileges_buttons).first,
            self.paired_privileges_descriptions.element(0),
            self.paired_privileges_descriptions.element(1),
            self.paired_privileges_descriptions.element(2),
        ]

        for element, text in zip(elements, texts):
            element.should(have.text(text))
        return self

    def check_ar_localization_for_select_privileges_modal(
        self, elements: list, texts: list
    ) -> UserDetailsPage:
        for element, text in zip(elements, texts):
            element.should(have.text(text))
        return self

    def check_actions_ar_texts_on_allowed_access_table(self) -> UserDetailsPage:
        s(self.actions_buttons).click()
        self.edit_user_privilege_btn_on_table.should(
            have.text(ArabicTranslations.edit_user_privileges_btn)
        )
        self.remove_access_btn_on_table.should(have.text(ArabicTranslations.remove_access_btn))
        return self

    def switch_to_tab_on_user_details(self, tab_name: str) -> UserDetailsPage:
        tab = self.table_access_tabs.element_by(have.text(tab_name)).click()
        tab.should(have.attribute("aria-selected", "true"))
        return self

    def click_add_access_button_for_workspace_without_access(
        self, establishment_without_access: Element
    ) -> UserDetailsPage:
        establishment_without_access.s(self.add_access_btn_on_table).click()
        return self

    def check_add_privileges_modal_is_displayed(self) -> UserDetailsPage:
        self.add_privileges_modal.should(be.visible)
        return self

    def check_privileges_group_names(self, groups_data: list) -> UserDetailsPage:
        for i, group_data in enumerate(groups_data):
            privilege_group = self.privilege_groups.element(i)
            privilege_group.s(self.privilege_groups_titles).should(have.text(group_data["title"]))
            privileges_list = privilege_group.ss(self.checkbox_items)
            privileges_list.should(have.texts(group_data["privileges"]))
        return self

    def wait_until_privilege_list_is_displayed(self) -> UserDetailsPage:
        ss(self.checkbox_items).element_by(
            have.text(user_management_data.OCCUPATION_MANAGEMENT)
        ).should(be.visible)
        return self

    def check_all_checkboxes_are_selected_on_user_details(
        self, checkboxes_list: Collection
    ) -> UserDetailsPage:
        for item in checkboxes_list:
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
            privilege = ss(self.checkbox_items).element_by(have.text(privilege))
            privilege_checkbox = privilege.s(self.unselected_privilege_checkboxes).should(
                have.attribute("aria-checked", "false")
            )
            if active_state:
                privilege_checkbox.should(be.enabled)
            else:
                privilege_checkbox.should(be.disabled)
        return self

    def check_all_checkboxes_are_unselected_on_user_details(
        self, checkboxes_list: Collection
    ) -> UserDetailsPage:
        for item in checkboxes_list:
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
            ss(self.checkbox_items).element_by(have.text(privilege)).click()
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

    def check_establishment_is_displayed_on_table(
        self, establishment_row: Element
    ) -> UserDetailsPage:
        establishment_row.should(be.visible)
        return self

    def success_message_is_hidden(self) -> UserDetailsPage:
        self.success_message.should(be.not_.visible)
        return self

    def check_success_message_is_displayed(self, establishment_name: str) -> UserDetailsPage:
        self.success_message.should(
            have.text(
                f"{user_management_data.SUCCESS_MESSAGE_AFTER_ADD_ACCESS.format(establishment_name)}"
            )
        )
        return self

    def open_edit_privilege_modal(self, establishment_row: Element) -> UserDetailsPage:
        establishment_row.s(self.actions_buttons).click()
        self.select_edit_privileges_action()
        return self

    def select_edit_privileges_action(self) -> UserDetailsPage:
        self.edit_user_privilege_btn_on_table.click()
        return self

    def get_establishment_row_on_allowed_access_table(self, establishment: str) -> Element:
        return self.allowed_access_table.rows.element_by(have.text(establishment))

    def get_establishment_row_on_no_access_table(self, establishment: str) -> Element:
        return self.no_access_table.rows.element_by(have.text(establishment))

    def check_edit_privileges_modal_is_displayed(self) -> UserDetailsPage:
        self.edit_privilege_modal.should(be.visible)
        return self

    def click_remove_access_btn_on_edit_privileges_modal(self) -> UserDetailsPage:
        self.remove_access_btn_on_edit_privilege_modal.click()
        return self

    def check_remove_access_modal_is_displayed(
        self, establishment_name: str, user_name: str
    ) -> UserDetailsPage:
        self.remove_access_modal.should(be.visible)
        self.texts_on_remove_access_modal.element(1).should(
            have.text(
                f"{user_management_data.TEXT_ON_REMOVE_ACCESS_MODAL.format(establishment_name)}"
            )
        )
        self.texts_on_remove_access_modal.element(2).should(
            have.text(f"{user_management_data.QUESTION_ON_REMOVE_ACCESS_MODAL.format(user_name)}")
        )
        return self

    def check_remove_access_modal_is_closed(self) -> UserDetailsPage:
        self.remove_access_modal.should(be.not_.visible)
        return self

    def close_remove_access_modal(self) -> UserDetailsPage:
        self.cancel_btn_on_modal.click()
        return self

    def click_remove_btn_on_remove_access_modal(self) -> UserDetailsPage:
        self.remove_btn_on_remove_access_modal.click()
        return self

    def check_success_message_is_displayed_after_remove_access(
        self, number_of_establishments: str, user_name: str
    ) -> UserDetailsPage:
        self.success_message.should(
            have.text(
                f"{user_management_data.SUCCESS_MESSAGE_AFTER_REMOVE_ACCESS.format(number_of_establishments, user_name)}"
            )
        )
        return self

    def check_establishment_is_removed_from_the_table(
        self, establishment_row: Element
    ) -> UserDetailsPage:
        establishment_row.should(be.not_.visible)
        return self

    def check_establishment_is_removed_from_the_table_with_success_message(
        self, establishment_row: Element
    ) -> UserDetailsPage:
        self.success_message.wait_until(be.not_.visible)
        establishment_row.should(be.not_.visible)
        return self

    def click_all_allowed_access_establishments_checkbox(self) -> UserDetailsPage:
        self.allowed_access_table.header.s(self.checkbox_items).click()
        return self

    def click_allowed_access_establishment_checkbox(self, row_number: int) -> UserDetailsPage:
        self.allowed_access_table.row(row_number).s(self.checkbox_items).click()
        return self

    def check_allowed_access_establishment_checkbox_is_selected(
        self, row_number: int
    ) -> UserDetailsPage:
        self.allowed_access_table.row(row_number).s(self.establishments_inputs).should(be.selected)
        return self

    def check_buttons_below_establishments_table_are_displayed(self) -> UserDetailsPage:
        self.remove_access_btn_below_establishments_table.should(be.visible)
        self.cancel_btn_below_establishments_table.should(be.visible)
        return self

    def check_elements_with_all_establishments_are_displayed(
        self, all_establishments: str
    ) -> UserDetailsPage:
        self.selected_establishments_text_below_table.should(
            have.text(
                f"{user_management_data.SELECTED_ESTABLISHMENTS_TEXT.format(all_establishments, all_establishments)}"
            )
        )
        self.link_below_establishments_table.should(have.text(user_management_data.CLEAR_ALL_LINK))
        return self

    def check_elements_with_selected_establishment_are_displayed(
        self, selected_establishments: str, all_establishments: str
    ) -> UserDetailsPage:
        self.selected_establishments_text_below_table.should(
            have.text(
                f"{user_management_data.SELECTED_ESTABLISHMENTS_TEXT.format(selected_establishments, all_establishments)}"
            )
        )
        self.link_below_establishments_table.should(
            have.text(
                f"{user_management_data.SELECT_ALL_ESTABLISHMENTS_LINK.format(all_establishments)}"
            )
        )
        return self

    def check_elements_below_establishments_table_are_hidden(self) -> UserDetailsPage:
        self.remove_access_btn_below_establishments_table.should(be.not_.visible)
        self.cancel_btn_below_establishments_table.should(be.not_.visible)
        self.selected_establishments_text_below_table.should(be.not_.visible)
        self.link_below_establishments_table.should(be.not_.visible)
        return self

    def click_remove_access_btn(self) -> UserDetailsPage:
        self.remove_access_btn_below_establishments_table.click()
        return self

    def check_terminate_access_modal_is_displayed(self, user_name: str) -> UserDetailsPage:
        self.terminate_modal.should(be.visible)
        self.texts_on_remove_access_modal.should(
            have.texts(
                user_management_data.TITLE_ON_TERMINATE_MODAL,
                user_management_data.TEXT_ON_TERMINATE_MODAL,
                user_management_data.TEXT2_ON_TERMINATE_MODAL,
                f"{user_management_data.QUESTION_ON_TERMINATE_MODAL.format(user_name)}",
            )
        )
        self.delete_user_btn_on_terminate_modal.should(be.visible)
        self.cancel_btn_on_modal.should(be.visible)
        return self

    def confirm_terminating_user(self) -> UserDetailsPage:
        self.delete_user_btn_on_terminate_modal.click()
        return self
