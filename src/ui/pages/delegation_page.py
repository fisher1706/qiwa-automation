from __future__ import annotations

from selene import be, have
from selene.support.shared.jquery_style import s, ss

from data.delegation.delegation_dashboard import DelegationMain
from src.ui.components.raw.table import Table


class DelegationPage:
    localization_button = s("div.cwZIaz div.OcnFf:nth-child(2) button")
    localization_state = s("div.cwZIaz div:nth-child(2) p.eHeBbx")
    english_localization_button = s("div.fzbjKl a:first-child")
    delegation_table = Table(s('[data-testid="SectionSharedComponent"] table'))
    breadcrumbs = ss('[aria-label="Breadcrumb"] li.eHUTqN')
    active_breadcrumb_text = s('[aria-label="Breadcrumb"] li span.cLJfIR')
    active_breadcrumb_link = s('[aria-label="Breadcrumb"] li > a.bUNLWM')
    location_breadcrumb_text = s('[aria-label="Breadcrumb"] li > p[aria-current="page"]')
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

    def __init__(self):
        self.delegation_main = DelegationMain()

    def wait_page_to_load(self) -> DelegationPage:
        self.delegation_table.body.should(be.visible)
        return self

    def select_english_localization(self) -> DelegationPage:
        self.localization_button.click()
        self.english_localization_button.click()
        self.localization_state.wait_until(have.exact_text("EN"))
        return self

    def check_active_breadcrumb(self, index: int, title: str, url: str) -> DelegationPage:
        self.breadcrumbs.element(index).should(be.visible)
        self.active_breadcrumb_text.should(have.exact_text(title))
        self.active_breadcrumb_link.should(have.attribute(name="href", value=url))
        return self

    def check_location_breadcrumb(self, index: int, title: str) -> DelegationPage:
        self.breadcrumbs.element(index).should(be.visible)
        self.location_breadcrumb_text.should(have.exact_text(title))
        return self

    def check_page_title(self) -> DelegationPage:
        self.page_title.should(have.exact_text(self.delegation_main.main_page_title))
        return self

    def verify_add_delegation_button(self) -> DelegationPage:
        self.add_delegation_btn.should(have.exact_text(self.delegation_main.add_delegation_button))
        return self

    def check_government_tab(self) -> DelegationPage:
        self.government_tab.should(have.exact_text(self.delegation_main.government_tab))
        return self

    def verify_delegation_table_title(self) -> DelegationPage:
        self.title_on_delegations_table.should(have.exact_text(self.delegation_main.table_title))
        return self

    def check_search_is_displayed(self) -> DelegationPage:
        self.search_on_delegations_table.should(be.visible)
        return self

    def verify_sort_by_is_displayed(self) -> DelegationPage:
        self.sort_on_delegations_table.should(be.visible)
        return self

    def check_filter_button(self) -> DelegationPage:
        self.filter_on_delegations_table.should(
            have.exact_text(self.delegation_main.filter_button)
        )
        return self

    def verify_delegations_table_is_displayed(self) -> DelegationPage:
        self.delegation_table.header.should(be.visible)
        self.delegation_table.body.should(be.visible)
        self.delegation_table.rows.should(have.size(10))
        return self

    def check_delegation_table_headers_titles(self) -> DelegationPage:
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

    def check_rows_per_page_is_displayed(self) -> DelegationPage:
        self.rows_per_page.should(be.visible)
        return self

    def verify_pagination_is_displayed(self) -> DelegationPage:
        self.pagination.should(be.visible)
        self.number_of_items_text.should(have.text("1-10 of"))
        return self
