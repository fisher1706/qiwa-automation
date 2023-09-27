from __future__ import annotations

import allure
from selene import Element, be, have, query
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation.constants import DelegationStatus
from src.ui.components.raw.breadcrumb_navigation import BreadcrumbNavigation
from src.ui.components.raw.table import Table
from utils.helpers import convert_timestamp_into_dates


class DelegationDashboardPage:
    localization_button = ss('[data-component="MenuTrigger"] button')[1]
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization_button = s('div[data-component="Menu"] a:first-child')
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
    status_filter = 'label[for="{0}"]'
    apply_filters_button = s("button#BaseFiltersButtonApply")
    status_of_filtered_delegation = delegation_table.row(1).s('[role="status"]')
    more_button = ss('button[aria-label="aria label"]').element(0)
    actions_buttons = ss('[data-component="ActionsMenu"] > button')
    id_on_delegation_table = delegation_table.cell(row=1, column=1)
    start_date_on_delegation_table = delegation_table.cell(row=1, column=5)
    expiry_date_on_delegation_table = delegation_table.cell(row=1, column=6)

    @allure.step
    def wait_delegation_dashboard_page_to_load(self) -> DelegationDashboardPage:
        self.delegation_table.body.should(be.visible)
        return self

    @allure.step
    def select_english_localization_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.localization_button.click()
        self.english_localization_button.click()
        self.localization_state.wait_until(have.exact_text("EN"))
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
    def click_more_button_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.more_button.click()
        return self

    def get_id_on_delegation_table(self) -> str:
        delegation_id_on_dashboard = self.id_on_delegation_table.get(query.text)
        return delegation_id_on_dashboard

    @allure.step
    def should_correct_actions_of_filtered_delegation_be_displayed(
        self, action_titles: list
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
        self.delegation_table.cell(row=1, column=1).should(have.text(str(delegation_id)))
        return self

    @allure.step
    def should_employee_name_be_correct(self, employee_name: str) -> DelegationDashboardPage:
        self.delegation_table.cell(row=1, column=2).should(have.text(employee_name))
        return self

    @allure.step
    def should_entity_name_be_correct(self, entity_name: str) -> DelegationDashboardPage:
        self.delegation_table.cell(row=1, column=3).should(have.text(entity_name))
        return self

    @allure.step
    def should_delegation_permission_be_correct(self, permission: str) -> DelegationDashboardPage:
        self.delegation_table.cell(row=1, column=4).should(have.text(permission))
        return self

    @allure.step
    def should_delegation_status_be_correct(self, status: str) -> DelegationDashboardPage:
        self.delegation_table.cell(row=1, column=7).should(have.text(status.capitalize()))
        return self

    @allure.step
    def should_delegation_dates_be_correct_on_dashboard(
        self, status: str, timestamp: float, locator: Element
    ) -> DelegationDashboardPage:
        if status in [DelegationStatus.ACTIVE, DelegationStatus.EXPIRED, DelegationStatus.REVOKED]:
            date = convert_timestamp_into_dates(timestamp)
            locator.should(have.text(date))
        else:
            locator.should(have.text("-"))
        return self

    @allure.step
    def select_action_on_delegation_dashboard(self, action: str) -> DelegationDashboardPage:
        self.actions_buttons.element_by(have.text(action)).click()
        return self
