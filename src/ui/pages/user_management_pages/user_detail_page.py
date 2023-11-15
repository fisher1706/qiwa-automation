from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s, ss


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
    allowed_access_btn = s("//button[1]/div/p")
    no_access_btn = s("//button[2]/div/p")
    establishment_name_column = s("//thead/tr/th[2]")
    establishment_id_column = s("//thead/tr/th[3]")
    privileges_column = s("//thead/tr/th[4]")
    actions_column = s("//thead/tr/th[5]")
    details_page_breadcrumbs = s("[aria-label='Breadcrumb'] p")

    add_access_btn = s("[data-testid='link-toggler-showAddPrivileges']")
    select_privileges_modal = s("[data-testid='modal-add-privileges']")
    privilege_groups = ss("div[data-testid='group-block']")
    privilege_groups_titles = "p.dSyftF"
    privileges_items = "[data-component='Checkbox']"
    privileges_checkboxes = select_privileges_modal.all("input")
    default_privilege_items = ss("[data-testid='group-privileges-item']")
    default_privilege_checkboxes = "input[data-testid='group-privileges-checkbox']"
    ineligible_privilege_checkboxes = "input[data-testid='toggle-show-checkbox']"
    non_default_privileges_checkboxes = ss("input[data-testid='toggle-show-checkbox']")
    all_privileges_item = s("[data-testid='body-modal'] label")
    all_privileges_checkbox = s("input#select-all-modal-body")
    show_more_privileges_buttons = ss("[data-testid='cb-toggler-link-on']")

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
            self.no_access_btn,
            self.establishment_name_column,
            self.establishment_id_column,
            self.privileges_column,
            self.actions_column,
            self.details_page_breadcrumbs,
        ]

        for element, text in zip(elements, texts):
            element.should(have.text(text))

        return self

    def select_no_access_tab(self) -> UserDetailsPage:
        self.no_access_btn.click()
        return self

    def click_add_access_button(self) -> UserDetailsPage:
        self.add_access_btn.click()
        return self

    def check_select_privileges_modal_is_displayed(self) -> UserDetailsPage:
        self.select_privileges_modal.should(be.visible)
        return self

    def click_show_more_privileges_btn_for_groups(self) -> UserDetailsPage:
        for button in self.show_more_privileges_buttons:
            button.click()
        return self

    def check_privileges_group_names(self, groups_data: list) -> UserDetailsPage:
        for i, group_data in enumerate(groups_data):
            privilege_group = self.privilege_groups.element(i)
            privilege_group.s(self.privilege_groups_titles).should(have.text(group_data["title"]))
            privileges_list = privilege_group.ss(self.privileges_items)
            privileges_list.should(have.texts(group_data["privileges"]))
        return self

    @allure.step
    def check_default_privileges_are_selected(self, default_privileges: list) -> UserDetailsPage:
        for default_privilege in default_privileges:
            default_item = self.default_privilege_items.element_by(have.text(default_privilege))
            default_item.s(self.default_privilege_checkboxes).should(be.disabled).should(
                be.selected
            )
        return self

    @allure.step
    def check_ineligible_privileges_cannot_be_selected(
        self, ineligible_privileges: list
    ) -> UserDetailsPage:
        for ineligible_privilege in ineligible_privileges:
            ineligible_item = ss(self.privileges_items).element_by(have.text(ineligible_privilege))
            ineligible_item.s(self.ineligible_privilege_checkboxes).should(be.disabled).should(
                have.attribute("aria-checked", "false")
            )
        return self

    def wait_until_privilege_list_is_displayed(self) -> UserDetailsPage:
        self.non_default_privileges_checkboxes.element(1).wait_until(be.visible)
        return self

    def click_all_privileges_checkbox(self) -> UserDetailsPage:
        self.all_privileges_item.click()
        return self

    def check_privileges_are_selected(self) -> UserDetailsPage:
        for item in self.privileges_checkboxes:
            item.should(be.selected)
        return self

    def click_privilege_from_the_list(self, privilege_name: str) -> UserDetailsPage:
        ss(self.privileges_items).element_by(have.text(privilege_name)).click()
        return self

    def check_all_privileges_checkbox_is_unselected(self) -> UserDetailsPage:
        self.all_privileges_checkbox.should(have.attribute("aria-checked", "false"))
        return self

    def check_non_default_privileges_are_unselected(self) -> UserDetailsPage:
        for item in self.non_default_privileges_checkboxes:
            item.should(have.attribute("aria-checked", "false"))
        return self
