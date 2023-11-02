from time import sleep

import allure
from selene.api import Element, be, command, have, query, s, ss

from data.visa.constants import (
    ESTABLISHMENT_FUND,
    FILTERS,
    OTHER_VISAS_NO_RESULTS,
    OTHER_VISAS_TITLE,
    PERMANENT_VISAS_NO_RESULTS,
    PERMANENT_VISAS_TITLE,
    WORK_VISA_PAGE_TITLE_TEXT,
    BalanceRequestStatus,
    ColName,
    Numbers,
    VisaType,
)
from src.ui.components.raw.table import Table
from src.ui.pages.visa_pages.base_page import BasePage
from utils.assertion.selene_conditions import have_any_number, have_in_text_number
from utils.assertion.soft_assertions import soft_assert, soft_assert_text
from utils.pdf_parser import (
    file_is_valid_pdf,
    get_downloaded_filename,
    verify_text_in_pdf,
)


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
    print_action = s('//button/p[contains(text(), "Print")]')
    view_action = s('//button/p[contains(text(), "View details")]')
    establishment_fund_section = s('//*[@data-testid="absherFundsSection"]')
    establishment_fund_section_title = establishment_fund_section.ss("./div").first
    establishment_fund_table = Table(establishment_fund_section.s(".//table"))
    establishment_fund_left_cell = establishment_fund_table.cell(row=1, column=1)
    establishment_fund_right_cell = establishment_fund_table.cell(row=1, column=2)
    increase_quota_establishment_button = s('//*[@data-testid="establishmentPhase"]//button')
    increase_quota_expansion_button = s('//*[@data-testid="increaseRecruitmentQuotaBtn"]')
    nav_link_to_transitional_page = ss("//nav//li").second
    allowed_quota_section = s('//*[@id="allowedQuotaSection"]')
    exceptional_requests_table = s('//*[@data-testid="ExceptionalRequestsTable"]')
    tier_upgrades_requests_table = s('//*[@data-testid="TierHistoryTable"]')
    establishment_fund_tab = s('//*[@data-testid="nav-Establishment fund"]')
    learn_more_tab = s('//*[@data-testid="nav-Learn more"]')
    learn_more_section = s('//*[@id="knowledgeSection"]//p')
    recruitment_quota_section = s("#allowedQuotaSection")
    recruitment_quota_tab = s('//*[@data-testid="nav-Recruitment quota"]')
    increase_fund_modal = s('//*[@data-testid="absherFundsModal"]')
    increase_fund_modal_x_button = increase_fund_modal.ss(".//button").first
    increase_fund_modal_close_button = increase_fund_modal.ss(".//button").second
    increase_fund_modal_link = increase_fund_modal.s(".//a")
    navigation_list = s("#navigationList")

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
    def verify_perm_work_visa_request_pdf(self, request, visa_type=VisaType.ESTABLISHMENT):
        self.open_action_menu_on_first_visa_request(visa_type, request)
        self.print_action.click()
        filename = get_downloaded_filename(timeout=20)
        if visa_type == VisaType.ESTABLISHMENT:
            verify_text_in_pdf(filename, request)
        else:
            file_is_valid_pdf(filename)

    @allure.step("Return to transitional page")
    def return_to_transitional_page(self):
        self.nav_link_to_transitional_page.click()

    def open_action_menu_on_first_visa_request(self, visa_type, request):
        if visa_type == VisaType.ESTABLISHMENT:
            self.permanent_visas_tab.click()
            command.js.scroll_into_view(self.establishment_fund_section)
            self.permanent_visas_table.ss(self.table_rows).by(have.text(request)).first.s(
                self.request_action_button
            ).click()
        else:
            command.js.scroll_into_view(self.allowed_quota_section)
            self.exceptional_requests_table.ss(self.table_rows).by(have.text(request)).first.s(
                self.request_action_button
            ).click()

    @allure.step("Verify tier upgrade status of tier upgrade request")
    def verify_tier_upgrade_status(self, ref_number: str, status: BalanceRequestStatus) -> None:
        self.verify_request_status(ref_number, status, self.tier_upgrades_requests_table)

    @allure.step("Verify balance request status")
    def verify_balance_request_status(self, ref_number: str, status: BalanceRequestStatus) -> None:
        self.verify_request_status(ref_number, status, self.exceptional_requests_table)

    def verify_request_status(
        self, ref_number: str, status: BalanceRequestStatus, element: Element
    ) -> None:
        table = Table(element)
        status_cell = table.cell(row=have.text(ref_number), column=ColName.REQUEST_STATUS)
        command.js.scroll_into_view(element)
        soft_assert_text(
            element=status_cell, text=status.label, element_name="Balance request status"
        )

    @allure.step("Verify top navigation tabs (links) scrolling work")
    def verify_top_navigation_tabs_work(self):
        self.verify_section_visible(self.allowed_quota_section)
        self.establishment_fund_tab.click()
        self.verify_section_visible(self.establishment_fund_section)
        self.permanent_visas_tab.click()
        self.verify_section_visible(self.permanent_visas_section)
        self.other_visas_tab.click()
        self.verify_section_visible(self.other_visas_section)
        self.learn_more_tab.click()
        self.verify_section_visible(self.learn_more_section)
        self.recruitment_quota_tab.click()
        self.verify_section_visible(self.allowed_quota_section)

    def verify_section_visible(self, element: Element) -> None:
        sleep(2)  # wait until scrolling is complete
        top_y = (
            self.navigation_list.get(query.location)["y"]
            + self.navigation_list.get(query.size)["height"]
        )
        element_y = element.get(query.location)["y"]
        soft_assert(
            top_y <= element_y < top_y + 100,
            error_message=f"Element {element} is not scrolled properly",
        )

    @allure.step("Verify establishment section")
    def verify_absher_balance_section(self) -> None:
        self.establishment_fund_tab.click()
        soft_assert_text(
            self.establishment_fund_section_title,
            ESTABLISHMENT_FUND,
            element_name="Establishment title section",
        )
        self.establishment_fund_left_cell.should(have_any_number())
        self.establishment_fund_left_cell.s("./a").should(be.visible)
        self.establishment_fund_right_cell.should(have_in_text_number(Numbers.TEN_THOUSAND))
        self.open_increase_fund_modal()
        self.verify_increase_fund_modal()
        self.increase_fund_modal_x_button.click()
        self.increase_fund_modal.should(be.hidden)
        self.establishment_fund_left_cell.s("./a").click()
        self.verify_increase_fund_modal()
        self.increase_fund_modal_close_button.click()
        self.increase_fund_modal.should(be.hidden)

    def verify_increase_fund_modal(self) -> None:
        self.increase_fund_modal.should(be.visible)
        self.increase_fund_modal_x_button.should(be.visible).should(be.clickable)
        self.increase_fund_modal_close_button.should(be.visible).should(be.clickable)
        self.increase_fund_modal_link.should(be.visible)

    def open_increase_fund_modal(self) -> None:
        self.establishment_fund_left_cell.s("./a").click()
