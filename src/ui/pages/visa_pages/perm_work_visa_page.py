import allure
from selene.api import be, command, have, s, ss

from data.visa.constants import (
    FILTERS,
    OTHER_VISAS_NO_RESULTS,
    OTHER_VISAS_TITLE,
    PERMANENT_VISAS_NO_RESULTS,
    PERMANENT_VISAS_TITLE,
    WORK_VISA_PAGE_TITLE_TEXT,
)
from src.ui.pages.visa_pages.base_page import BasePage
from utils.assertion.soft_assertions import soft_assert_text
from utils.pdf_parser import get_downloaded_filename, verify_text_in_pdf


class PermWorkVisaPage(BasePage):
    other_visas_tab = s('//*[@data-testid="nav-Other visas"]')
    permanent_visas_tab = s('//*[@data-testid="nav-Permanent work visas requests"]')
    other_visas_section = s("#otherVisaRequestsSection")
    other_visas_section_title = other_visas_section.s(".//div/p")
    permanent_visas_section = s("#visaRequestsSection")
    permanent_visas_section_title = permanent_visas_section.s(".//div/p")
    other_visas_table = other_visas_section.s('//*[@data-testid="otherVisaRequestsTable"]')
    permanent_visas_table = permanent_visas_section.element(
        './/*[@data-testid="visaRequestsTable"]'
    )
    button = ".//button"
    no_results = './/*[@data-testid="tableNoResults"]'
    no_results_icon = './/*[name()="svg"]'
    table = ".//table"
    page_loader = s('//*[@data-testid="workVisaSkeleton"]')
    absher_funds_loader = s('//*[@data-testid="absherFundsSkeleton"]')
    allowed_quota_loader = s('//*[@data-testid="allowedQuotaSkeleton"]')
    table_loader = s('//*[@data-testid="tableLoader"]')
    all_loaders = ss(
        '//*[contains(@data-testid, "workVisaSkeleton") or '
        'contains(@data-testid, "absherFundsSkeleton") or '
        'contains(@data-testid, "allowedQuotaSkeleton") or '
        'contains(@data-testid, "tableLoader")]'
    )
    table_rows = './/*[@data-testid="tableContent"]'
    request_action_button = './/*[@data-testid="baseTableActions"]'
    print_action = s('//button/p[contains(text(), "Print request details")]')
    view_action = s('//button/p[contains(text(), "View details")]')
    establishment_fund_section = s('//*[@data-testid="absherFundsSection"]')

    @allure.step("Verify work visa page is opened")
    def verify_work_visa_page_open(self):
        self.all_loaders.wait_until(have.size_greater_than(0))
        self.all_loaders.wait_until(have.size(0))
        self.page_navigation_chain.should(be.visible)
        self.page_navigation_chain.should(have.text(WORK_VISA_PAGE_TITLE_TEXT))
        self.page_title.should(be.visible)
        self.page_title.should(have.text(WORK_VISA_PAGE_TITLE_TEXT))

    @allure.step("Verify other visas table on work visa page is empty")
    def verify_other_visas_table_empty(self):
        self.other_visas_section.should(be.visible)
        soft_assert_text(
            element=self.other_visas_section_title,
            text=OTHER_VISAS_TITLE,
            element_name="Other visas title",
        )
        self.other_visas_table.should(be.visible)
        self.other_visas_table.s(self.button).should(be.visible)
        self.other_visas_table.s(self.button).should(be.clickable)
        soft_assert_text(
            self.other_visas_table.s(self.button),
            text=FILTERS,
            element_name="Other visas filters button",
        )
        self.other_visas_table.s(self.no_results).should(be.visible)
        self.other_visas_table.s(self.no_results).s(self.no_results_icon).should(be.visible)
        self.other_visas_table.s(self.no_results).should(have.text(OTHER_VISAS_NO_RESULTS))
        self.other_visas_table.s(self.table).should(be.hidden)

    @allure.step("Verify permanent visas table on work visa page is empty")
    def verify_permanent_visas_table_empty(self):
        self.permanent_visas_section.should(be.visible)
        soft_assert_text(
            element=self.permanent_visas_section_title,
            text=PERMANENT_VISAS_TITLE,
            element_name="Permanent visas title",
        )
        self.permanent_visas_table.should(be.visible)
        self.permanent_visas_table.s(self.button).should(be.visible)
        self.permanent_visas_table.s(self.button).should(be.clickable)
        soft_assert_text(
            self.permanent_visas_table.s(self.button),
            text=FILTERS,
            element_name="Other visas filters button",
        )
        self.permanent_visas_table.s(self.no_results).should(be.visible)
        self.permanent_visas_table.s(self.no_results).s(self.no_results_icon).should(be.visible)
        self.permanent_visas_table.s(self.no_results).should(have.text(PERMANENT_VISAS_NO_RESULTS))
        self.permanent_visas_table.s(self.table).should(be.hidden)

    @allure.step("Verify visa request exists on permanent work visa page")
    def verify_perm_work_visa_request(self, request):
        self.permanent_visas_tab.click()
        self.permanent_visas_table.should(be.visible)
        self.permanent_visas_table.ss(self.table_rows).by(have.text(request)).should(
            have.size_greater_than(0)
        )
        self.other_visas_table.should(be.visible)
        self.other_visas_table.ss(self.table_rows).by(have.text(request)).should(have.size(1))

    @allure.step("Verify visa request (pdf) permanent work visa page")
    def verify_perm_work_visa_request_pdf(self, request):
        self.permanent_visas_tab.click()
        command.js.scroll_into_view(self.establishment_fund_section)
        self.permanent_visas_table.ss(self.table_rows).by(have.text(request)).first.s(
            self.request_action_button
        ).click()
        self.print_action.click()
        filename = get_downloaded_filename(timeout=20)
        verify_text_in_pdf(filename, request)
