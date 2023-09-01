from __future__ import annotations

from selene import be, have
from selene.support.shared.jquery_style import s

import config
from src.ui.components.raw.breadcrumb_navigation import BreadcrumbNavigation
from src.ui.components.raw.table import Table


class DelegationDashboardPage:
    localization_button = s("div.cwZIaz div.OcnFf:nth-child(2) button")
    localization_state = s("div.cwZIaz div:nth-child(2) p.eHeBbx")
    english_localization_button = s("div.fzbjKl a:first-child")
    delegation_table = Table(s('[data-testid="SectionSharedComponent"] table'))
    active_breadcrumb = BreadcrumbNavigation().breadcrumb(1)
    active_breadcrumb_text = BreadcrumbNavigation().breadcrumb(1).s("span.cLJfIR")
    active_breadcrumb_link = BreadcrumbNavigation().breadcrumb(1).s("a.bUNLWM")
    location_breadcrumb = BreadcrumbNavigation().breadcrumb(2)
    location_breadcrumb_text = BreadcrumbNavigation().breadcrumb(2).s('p[aria-current="page"]')
    page_title = s(".hAVbwT")
    add_delegation_btn = s("div.iNfHrh p.bPryTV")
    government_tab = s("div.fsqetJ")
    title_on_delegations_table = s("p.kidPyR")
    search_on_delegations_table = s('div[role="search"]')
    sort_on_delegations_table = s("div.gUKAZH")
    filter_on_delegations_table = s("#BaseFiltersButtonOpen div.duHkYx")
    rows_per_page = s("div.fultmG")
    pagination = s('nav[role="navigation"]')
    number_of_items_text = s("div.cUpZhX p.kRtCwb")

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
        self.number_of_items_text.should(have.text("1-10 of"))
        return self
