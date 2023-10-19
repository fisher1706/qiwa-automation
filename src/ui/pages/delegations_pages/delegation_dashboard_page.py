from __future__ import annotations

import allure
from selene import Element, be, browser, have, query
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import general_data
from src.ui.components.raw.breadcrumb_navigation import BreadcrumbNavigation
from src.ui.components.raw.table import Table


class DelegationDashboardPage:
    localization_button = ss('[data-component="MenuTrigger"] button').element(1)
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization = s('div[data-component="Menu"] a:nth-child(1)')
    delegation_table = Table(s('[data-testid="SectionSharedComponent"] table'))
    active_breadcrumb = BreadcrumbNavigation().breadcrumb(1)
    active_breadcrumb_link = BreadcrumbNavigation().breadcrumb(1).s("#BreadcrumbsItemServices")
    location_breadcrumb = BreadcrumbNavigation().breadcrumb(2)
    page_title = s("#DashboardTitle")
    add_delegation_btn = s("#DashboardCreateDelegationBtn")
    government_tab = s('[data-testid="LineTabGovernment"]')
    title_on_delegations_table = s("#DashboardTableTitle")
    search_on_delegations_table = s('div[role="search"]')
    sort_on_delegations_table = s('#BaseSortWrapper > [data-component="Select"]')
    filter_on_delegations_table = s("#BaseFiltersButtonOpen")
    number_of_items = s('[data-component="Pagination"] > p')
    pagination = s('nav[role="navigation"]')
    rows_per_page = s("#PaginationBoxSelectLabel")
    rows_per_page_input = s('#PaginationBoxSelectLabel div[data-component="Select"]')
    rows_per_page_options = ss('li[role="option"]')
    status_filter = 'label[for="{0}"]'
    apply_filters_button = s("button#BaseFiltersButtonApply")
    status_of_filtered_delegation = delegation_table.row(1).s('[role="status"]')
    actions_buttons = ss('[data-component="ActionsMenu"] > button')
    id_on_delegation_table = delegation_table.cell(row=1, column=1)
    delegate_name_on_delegation_table = delegation_table.cell(row=1, column=2)
    external_entity_on_delegation_table = delegation_table.cell(row=1, column=3)
    permissions_on_delegation_table = delegation_table.cell(row=1, column=4)
    start_date_on_delegation_table = delegation_table.cell(row=1, column=5)
    expiry_date_on_delegation_table = delegation_table.cell(row=1, column=6)
    # pylint: disable=R0801
    # TODO move locators to components
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
    def wait_delegation_dashboard_page_to_load(self) -> DelegationDashboardPage:
        self.delegation_table.body.should(be.visible)
        return self

    @allure.step
    def select_english_localization_on_delegation_dashboard(self) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
        self.localization_button.click()
        self.english_localization.click()
        self.localization_state.wait_until(have.exact_text(general_data.ENGLISH_LOCAL))
        return self

    @allure.step
    def check_redirect_to_delegation_dashboard(self):
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/"))
        return self

    @allure.step
    def should_active_breadcrumb_is_displayed_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.active_breadcrumb.should(have.exact_text("Services"))
        self.active_breadcrumb_link.should(
            have.attribute(name="href", value=config.qiwa_urls.spa + "/company/e-services")
        )
        return self

    @allure.step
    def should_location_breadcrumb_is_displayed_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.location_breadcrumb.should(have.exact_text("Delegation to external entities"))
        return self

    @allure.step
    def should_page_title_has_correct_text_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.page_title.should(have.exact_text("Delegation to external entities"))
        return self

    @allure.step
    def should_add_delegation_button_has_correct_text(self) -> DelegationDashboardPage:
        self.add_delegation_btn.should(have.exact_text("Add delegation"))
        return self

    @allure.step
    def click_add_delegation_button(self) -> DelegationDashboardPage:
        self.add_delegation_btn.click()
        return self

    @allure.step
    def should_government_tab_has_correct_text(self) -> DelegationDashboardPage:
        self.government_tab.should(have.exact_text("Government"))
        return self

    @allure.step
    def should_delegations_table_has_correct_title(self) -> DelegationDashboardPage:
        self.title_on_delegations_table.should(have.exact_text("Government delegations"))
        return self

    @allure.step
    def should_search_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.search_on_delegations_table.should(be.visible)
        return self

    @allure.step
    def should_sort_by_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.sort_on_delegations_table.should(be.visible)
        return self

    @allure.step
    def should_filter_button_has_correct_text(self) -> DelegationDashboardPage:
        self.filter_on_delegations_table.should(have.exact_text("Filters"))
        return self

    @allure.step
    def should_delegations_table_is_displayed(self) -> DelegationDashboardPage:
        self.delegation_table.header.should(be.visible)
        self.delegation_table.body.should(be.visible)
        self.delegation_table.rows.should(have.size(10))
        return self

    @allure.step
    def should_delegation_table_headers_have_correct_titles(self) -> DelegationDashboardPage:
        self.delegation_table.headers.should(
            have.exact_texts(
                "Delegation ID",
                "Delegate name",
                "External entity",
                "Permissions",
                "Start date",
                "Expiration date",
                "Status",
                "Actions",
            )
        )
        return self

    @allure.step
    def should_rows_per_page_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.rows_per_page.should(be.visible)
        return self

    def select_rows_per_page(self, rows: str) -> DelegationDashboardPage:
        self.rows_per_page_input.click()
        self.rows_per_page_options.element_by(have.exact_text(rows)).click()
        return self

    @allure.step
    def should_pagination_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.pagination.should(be.visible)
        self.number_of_items.should(have.text("1-10 of"))
        return self

    @allure.step
    def filter_delegation_list_by_status(self, status: str) -> DelegationDashboardPage:
        self.filter_on_delegations_table.click()
        s(self.status_filter.format(status.upper())).click()
        self.apply_filters_button.click()
        return self

    @allure.step
    def should_status_text_of_filtered_delegation_be_correct(
        self, status: str
    ) -> DelegationDashboardPage:
        self.status_of_filtered_delegation.should(have.exact_text(status))
        return self

    @allure.step
    def should_background_color_of_filtered_delegation_be_correct(
        self, color: str
    ) -> DelegationDashboardPage:
        self.status_of_filtered_delegation.should(
            have.css_property(name="background-color", value=color)
        )
        return self

    @allure.step
    def click_more_button_on_delegation_dashboard(
        self, row_number: int = 1
    ) -> DelegationDashboardPage:
        self.delegation_table.cell(row=row_number, column="Actions").click()
        return self

    def get_id_on_delegation_table(self) -> str:
        delegation_id_on_dashboard = self.id_on_delegation_table.get(query.text)
        return delegation_id_on_dashboard

    @allure.step
    def should_correct_actions_be_displayed_on_delegation_dashboard(
        self, action_titles: list | str
    ) -> DelegationDashboardPage:
        self.actions_buttons.should(have.exact_texts(action_titles))
        return self

    @allure.step
    def should_number_of_delegations_be_correct(
        self, number_of_delegations: int | str
    ) -> DelegationDashboardPage:
        self.number_of_items.should(have.text(str(number_of_delegations)))
        return self

    @allure.step
    def should_delegation_id_be_correct(self, delegation_id: int | str) -> DelegationDashboardPage:
        self.id_on_delegation_table.should(have.text(str(delegation_id)))
        return self

    @allure.step
    def should_employee_name_be_correct(self, employee_name: str) -> DelegationDashboardPage:
        self.delegate_name_on_delegation_table.should(have.text(employee_name))
        return self

    @allure.step
    def should_entity_name_be_correct(self, entity_name: str) -> DelegationDashboardPage:
        self.external_entity_on_delegation_table.should(have.text(entity_name))
        return self

    @allure.step
    def should_delegation_permission_be_correct(self, permission: str) -> DelegationDashboardPage:
        self.permissions_on_delegation_table.should(have.text(permission))
        return self

    @allure.step
    def should_delegation_status_be_correct(
        self, status: str, row_number: int = 1
    ) -> DelegationDashboardPage:
        self.delegation_table.cell(row=row_number, column="Status").should(
            have.text(status.capitalize())
        )
        return self

    @allure.step
    def should_delegation_dates_be_correct_on_dashboard(
        self, status: str, date: str, locator: Element
    ) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
        if status in [general_data.ACTIVE, general_data.EXPIRED, general_data.REVOKED]:
            locator.should(have.text(date))
        else:
            locator.should(have.text("-"))
        return self

    @allure.step
    def select_action_on_delegation_dashboard(self, action: str) -> DelegationDashboardPage:
        self.actions_buttons.element_by(have.text(action)).click()
        return self

    def get_delegation_row(self, delegation_id: str | int):
        rows = self.delegation_table.rows()
        for row_number in range(1, len(rows) + 1):
            cell = self.delegation_table.cell(row=row_number, column=1)
            if str(delegation_id) == cell.get(query.text):
                return row_number

        raise AssertionError(f"No delegations found with {delegation_id} delegation id")

    @allure.step
    def should_resend_confirmation_modal_be_displayed_on_dashboard(
        self,
    ) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
        self.resend_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.RESEND_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.RESEND_MODAL_DESCRIPTION))
        self.message_on_resend_modal.should(have.exact_text(general_data.RESEND_MODAL_MESSAGE))
        self.resend_button_on_modal.should(have.exact_text(general_data.RESEND_BUTTON))
        self.cancel_button_on_resend_modal.should(have.exact_text(general_data.CANCEL_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_resend_request_button_on_dashboard(self) -> DelegationDashboardPage:
        self.resend_button_on_modal.click()
        self.loader_on_action_button.should(be.visible)
        return self

    @allure.step
    def click_cancel_button_on_resend_modal(self) -> DelegationDashboardPage:
        self.cancel_button_on_resend_modal.click()
        return self

    @allure.step
    def should_resend_confirmation_modal_be_hidden(self) -> DelegationDashboardPage:
        self.resend_modal.should(be.not_.visible)
        return self

    @allure.step
    def should_successful_message_be_displayed_on_dashboard(
        self, message: str
    ) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
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
    def should_revoke_confirmation_modal_be_displayed_on_dashboard(
        self,
    ) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
        self.revoke_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_DESCRIPTION))
        self.revoke_button_on_modal.should(have.exact_text(general_data.REVOKE_BUTTON))
        self.go_back_button_on_revoke_modal.should(have.exact_text(general_data.GO_BACK_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_revoke_delegation_button_on_dashboard(self) -> DelegationDashboardPage:
        # pylint: disable=R0801
        # TODO move method to components
        self.revoke_button_on_modal.click()
        self.loader_on_action_button.should(be.visible)
        return self
