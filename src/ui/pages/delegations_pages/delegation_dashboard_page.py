from __future__ import annotations

from datetime import datetime

from selene import be, have
from selene.support.shared.jquery_style import s, ss

import config
from src.ui.components.raw.breadcrumb_navigation import BreadcrumbNavigation
from src.ui.components.raw.table import Table


class DelegationDashboardPage:
    localization_button = s("div.kiolZy div.OcnFf:nth-child(2) button")
    localization_state = s("div.kiolZy div:nth-child(2) p.eHeBbx")
    english_localization_button = s("div.fzbjKl a:first-child")
    delegation_table = Table(s('[data-testid="SectionSharedComponent"] table'))
    active_breadcrumb = BreadcrumbNavigation().breadcrumb(1)
    active_breadcrumb_text = BreadcrumbNavigation().breadcrumb(1).s("span.cLJfIR")
    active_breadcrumb_link = BreadcrumbNavigation().breadcrumb(1).s("a.bUNLWM")
    location_breadcrumb = BreadcrumbNavigation().breadcrumb(2)
    location_breadcrumb_text = BreadcrumbNavigation().breadcrumb(2).s('p[aria-current="page"]')
    page_title = s(".hAVbwT")
    add_delegation_btn = s("button.dkndXj")
    government_tab = s("div.kHrKEQ")
    title_on_delegations_table = s("p.kidPyR")
    search_on_delegations_table = s('div[role="search"]')
    sort_on_delegations_table = s("div.OVoQi")
    filter_on_delegations_table = s("#BaseFiltersButtonOpen")
    number_of_items = s('[data-component="Pagination"] > p')
    pagination = s('nav[role="navigation"]')
    rows_per_page = s("div.bkfJsL")
    status_filter = 'label[for="{0}"]'
    apply_filters_button = s("button#BaseFiltersButtonApply")
    status_of_filtered_delegation = delegation_table.row(1).web_element.s('[role="status"]')
    more_button = ss('button[aria-label="aria label"]').element(0)
    actions_buttons = ss("div.hFITww button")

    def wait_delegation_dashboard_page_to_load(self) -> DelegationDashboardPage:
        self.delegation_table.body.should(be.visible)
        return self

    def select_english_localization_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.localization_button.click()
        self.english_localization_button.click()
        self.localization_state.wait_until(have.exact_text("EN"))
        return self

    def should_active_breadcrumb_is_displayed_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.active_breadcrumb.should(be.visible)
        self.active_breadcrumb_text.should(have.exact_text("Services"))
        self.active_breadcrumb_link.should(
            have.attribute(name="href", value=config.qiwa_urls.spa + "/company/e-services")
        )
        return self

    def should_location_breadcrumb_is_displayed_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.location_breadcrumb.should(be.visible)
        self.location_breadcrumb_text.should(have.exact_text("Delegation to external entities"))
        return self

    def should_page_title_has_correct_text_on_delegation_dashboard(
        self,
    ) -> DelegationDashboardPage:
        self.page_title.should(have.exact_text("Delegation to external entities"))
        return self

    def should_add_delegation_button_has_correct_text(self) -> DelegationDashboardPage:
        self.add_delegation_btn.should(have.exact_text("Add delegation"))
        return self

    def should_government_tab_has_correct_text(self) -> DelegationDashboardPage:
        self.government_tab.should(have.exact_text("Government"))
        return self

    def should_delegations_table_has_correct_title(self) -> DelegationDashboardPage:
        self.title_on_delegations_table.should(have.exact_text("Government delegations"))
        return self

    def should_search_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.search_on_delegations_table.should(be.visible)
        return self

    def should_sort_by_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.sort_on_delegations_table.should(be.visible)
        return self

    def should_filter_button_has_correct_text(self) -> DelegationDashboardPage:
        self.filter_on_delegations_table.should(have.exact_text("Filters"))
        return self

    def should_delegations_table_is_displayed(self) -> DelegationDashboardPage:
        self.delegation_table.header.should(be.visible)
        self.delegation_table.body.should(be.visible)
        self.delegation_table.rows.should(have.size(10))
        return self

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

    def should_rows_per_page_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.rows_per_page.should(be.visible)
        return self

    def should_pagination_is_displayed_on_delegation_dashboard(self) -> DelegationDashboardPage:
        self.pagination.should(be.visible)
        self.number_of_items.should(have.text("1-10 of"))
        return self

    def filter_delegation_list_by_status(self, status) -> DelegationDashboardPage:
        self.filter_on_delegations_table.click()
        s(self.status_filter.format(status.upper())).click()
        self.apply_filters_button.click()
        return self

    def should_status_text_of_filtered_delegation_be_correct(
        self, status
    ) -> DelegationDashboardPage:
        self.status_of_filtered_delegation.should(have.exact_text(status))
        return self

    def should_background_color_of_filtered_delegation_be_correct(
        self, color
    ) -> DelegationDashboardPage:
        self.status_of_filtered_delegation.should(
            have.css_property(name="background-color", value=color)
        )
        return self

    def click_more_button_of_filtered_delegation(self) -> DelegationDashboardPage:
        self.more_button().click()
        return self

    def should_correct_actions_of_filtered_delegation_be_displayed(
        self, action_titles
    ) -> DelegationDashboardPage:
        self.actions_buttons.should(have.exact_texts(action_titles))
        return self

    def should_number_of_delegations_be_correct(
        self, number_of_delegations
    ) -> DelegationDashboardPage:
        self.number_of_items.should(have.text(number_of_delegations))
        return self

    def should_delegation_id_be_correct(self, delegation_id) -> DelegationDashboardPage:
        self.delegation_table.row(1).cells.element(1).should(have.text(str(delegation_id)))
        return self

    def should_employee_name_be_correct(self, employee_name) -> DelegationDashboardPage:
        self.delegation_table.row(1).cells.element(2).should(have.text(employee_name))
        return self

    def should_entity_name_be_correct(self, entity_name) -> DelegationDashboardPage:
        self.delegation_table.row(1).cells.element(3).should(have.text(entity_name))
        return self

    def should_delegation_permission_be_correct(self, permission) -> DelegationDashboardPage:
        self.delegation_table.row(1).cells.element(4).should(have.text(permission))
        return self

    def should_delegation_status_be_correct(self, status) -> DelegationDashboardPage:
        self.delegation_table.row(1).cells.element(7).should(have.text(status.capitalize()))
        return self

    def should_delegation_start_date_be_correct(
        self, first_delegation_data
    ) -> DelegationDashboardPage:
        start_date_timestamp = first_delegation_data["startDate"]
        start_date = datetime.fromtimestamp(start_date_timestamp)
        self.delegation_table.row(1).cells.element(5).should(
            have.text(start_date.strftime("%d/%m/%Y"))
        )
        return self

    def should_delegation_expiry_date_be_correct(
        self, first_delegation_data
    ) -> DelegationDashboardPage:
        expiry_date_timestamp = first_delegation_data["expireAt"]
        expiry_date = datetime.fromtimestamp(expiry_date_timestamp)
        self.delegation_table.row(1).cells.element(6).should(
            have.text(expiry_date.strftime("%d/%m/%Y"))
        )
        return self
