from __future__ import annotations

from selene import be, browser, have, query
from selene.support.shared.jquery_style import s, ss

from src.ui.components.raw.table import Table


class UserManagementMainPage:
    add_new_user_btn = s("[data-testid='add-user-btn'] p")
    user_management_title = s("//div[contains(@data-testid, 'page-title')]/div/div/p")
    user_name = s("//tbody/tr[1]/td/div/p")

    users_role = s("[data-testid='owner-role']")
    subscription_valid_until_text = s(
        "//div[contains(@data-testid, 'your-subscription')]//tbody/tr[3]/td/div/p"
    )
    subscription_info_text = s("//*/table/tbody/tr[3]/td/div[2]/div[1]/p")
    how_to_renew_btn = s("//div[contains(@data-testid, 'your-subscription')]//td/div/a/span")

    count_of_users_in_selected_tab_users_table = s(
        "//button[contains(@aria-selected,'true')]/div/div/p"
    )
    unselected_tab_users_table_btn = s("//button[contains(@aria-selected,'false')]")

    users_in_table = s("//div[contains(@data-testid, 'user-table')]//tbody")
    title_in_users_in_company_tab = s("//div[contains(@role, 'tablist')]//button[1]/div/p")
    users_in_subscribed_table_tr = ss("[data-testid='user-table'] tbody tr")
    action_btn_table = ss("td button[data-testid='row-actions']")
    action_btn_for_owner = s("tr:nth-child(1) td button[data-testid='row-actions']")
    user_role_in_table = users_in_table.s("//tr[1]/td[4]")
    view_details_btn = s("button[data-testid='view-action'] p")
    view_detail_for_renew_btn = s("button[data-testid='renew-action'] p")
    renew_subscription_btn = s("button[data-testid='renew-action']")

    next_btn_pagination = s("//button/span[contains(text(), 'Next')]")
    previous_btn_pagination = s("//button/span[contains(text(), 'Previous')]")
    first_page_btn = s("//button[contains(@aria-label, 'Page 1')]")
    second_page_btn = s("//button[contains(@aria-label, 'Page 2')]")

    change_language_icon = s("//div[2]/div[contains(@data-component, 'MenuTrigger')]/button")
    arabic_language = s("//*[contains(text(), 'العربية')]")
    header_menu_btn = s("//div[contains(@data-testid, 'menu-trigger')]/div/button")

    global_error = s("//div[contains(@data-testid,'global-error')]/div/p[1]")
    change_workspace_btn = s("//div[contains(@class, 'tippy-content')]//div[3]//a")
    table = Table(s("[data-testid='user-table'] table"))

    def __init__(self):
        super().__init__()
        self.users_count = None

    def wait_until_page_is_loaded(self) -> UserManagementMainPage:
        self.users_in_table.wait_until(be.visible)
        return self

    def check_page_is_displayed(self) -> UserManagementMainPage:
        browser.driver.refresh()
        self.users_in_table.should(be.visible)
        return self

    def click_subscribe_btn(self) -> UserManagementMainPage:
        self.add_new_user_btn.click()
        return self

    def check_subscription_text_is_present(
        self, subscription_info_text: str
    ) -> UserManagementMainPage:
        self.subscription_info_text.wait_until(be.visible)
        self.subscription_info_text.should(have.text(subscription_info_text))
        return self

    def check_users_role_is_present(self) -> UserManagementMainPage:
        self.users_role.should(be.visible)
        return self

    def compare_user_name(self) -> UserManagementMainPage:
        self.user_name.should(be.visible)
        return self

    def select_users_in_establishment_tab(self) -> UserManagementMainPage:
        self.unselected_tab_users_table_btn.click()
        return self

    def get_title_in_user_company_table(self, title_test: str) -> UserManagementMainPage:
        title = self.title_in_users_in_company_tab
        title.wait_until(be.visible)
        title.should(have.text(title_test))
        return self

    def get_number_of_subscribed_user_in_company(self, selected: bool = True) -> str:
        if selected is False:
            self.select_users_in_establishment_tab()
        self.users_count = self.count_of_users_in_selected_tab_users_table.get(query.text)
        return self.users_count

    def compare_count_of_users_in_table(self) -> UserManagementMainPage:
        self.users_in_subscribed_table_tr.should(have.size(int(self.users_count)))
        return self

    def compare_count_of_users_in_company_table(self) -> UserManagementMainPage:
        self.select_users_in_establishment_tab()
        self.users_in_subscribed_table_tr.should(have.size(int(self.users_count)))
        return self

    def click_view_details_in_table(self) -> UserManagementMainPage:
        self.action_btn_table.first.should(be.visible).click()
        return self

    def navigate_to_view_details(self) -> UserManagementMainPage:
        self.view_details_btn.should(be.visible).click()
        return self

    def check_user_status(self) -> UserManagementMainPage:
        self.users_in_table.wait_until(be.visible)
        for row in enumerate(self.table.rows, start=1):
            if self.table.cell(row=row, column=5).matching(have.text("Active")):
                if self.table.cell(row=row, column=6).matching(be.in_dom):
                    self.table.cell(row=row, column=6).click()
                    self.view_details_btn.matching(have.text("View details"))
                    self.table.cell(row=row, column=6).click()
                else:
                    pass
            elif self.table.cell(row=row, column=5).matching(have.text("Terminated" or "Expired")):
                self.table.cell(row=row, column=6).click()
                self.view_detail_for_renew_btn.matching(have.text("Renew subscription"))
                self.table.cell(row=row, column=6).click()
        return self

    def check_pagination_btns(self) -> UserManagementMainPage:
        self.select_users_in_establishment_tab()
        self.second_page_btn.click()
        self.previous_btn_pagination.matching(be.visible)
        self.next_btn_pagination.matching(be.not_.visible)

        self.first_page_btn.click()
        self.previous_btn_pagination.matching(be.not_.visible)
        self.next_btn_pagination.matching(be.visible)
        return self

    def check_owner_role_in_table(self) -> UserManagementMainPage:
        self.user_role_in_table.should(have.text("Group Manager"))
        return self

    def change_language_to_arabic(self) -> UserManagementMainPage:
        self.change_language_icon.should(be.visible).click()
        self.arabic_language.should(be.visible).click()
        return self

    def check_translation(self, *texts) -> UserManagementMainPage:
        elements = [
            self.user_management_title,
            self.add_new_user_btn,
            self.users_role,
            self.subscription_valid_until_text,
            self.subscription_info_text,
            self.how_to_renew_btn,
        ]
        for element, text in zip(elements, texts):
            element.should(have.text(text))
        return self

    def confirm_that_action_btn_is_missed(self) -> UserManagementMainPage:
        self.action_btn_for_owner.should(be.absent)
        return self

    def check_error_message_for_um_page_without_permission(
        self, error_message
    ) -> UserManagementMainPage:
        self.global_error.should(have.text(error_message))
        return self

    def click_header_main_menu_btn(self) -> UserManagementMainPage:
        self.header_menu_btn.click()
        return self

    def click_change_workspace_btn(self) -> UserManagementMainPage:
        self.change_workspace_btn.click()
        return self
