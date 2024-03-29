import datetime
from time import sleep
from typing import Union

import allure
from dateutil.relativedelta import relativedelta
from selene.api import Element, be, command, have, query, s, ss
from selene.support.shared import browser

from data.visa.constants import (
    ALLOWANCE_PERIOD_END_DATE,
    ALLOWANCE_PERIOD_START_DATE,
    BR_ACCEPTED,
    BR_REFUNDED,
    BR_SUCCESS,
    CAN_BE_REFUNDED,
    ESTABLISHING,
    ESTABLISHMENT_FUND,
    ESTABLISHMENT_PHASE,
    ESTIMATED_RECRUITMENT_QUOTA,
    EXPANSION,
    FILTERS,
    HOW_TO_INCREASE_ESTABLISHMENT_FUNDS,
    INCREASE_ABSHER_MODAL_TITLE,
    ISSUE_VISA_MODAL_CONTENT_ESTABLISHING_TEXT,
    ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT,
    ISSUE_VISA_MODAL_CONTENT_HIGHEST_TIER_TEXT,
    ISSUE_VISA_MODAL_TITLE_TEXT,
    KNOWLEDGE_CENTER_URL,
    OTHER_VISAS_NO_RESULTS,
    OTHER_VISAS_TITLE,
    PERM_VISA_EXP_WORK_PERMIT_ERROR,
    PERM_VISA_EXP_WORK_PERMIT_ERROR_LINK,
    PERMANENT_VISAS_NO_RESULTS,
    PERMANENT_VISAS_TITLE,
    RECRUITMENT_QUOTA,
    RECRUITMENT_QUOTA_TIER,
    REFUND_ERROR_MODAL_MESSAGE,
    REFUND_SUCCESS_MODAL_CONTENT,
    REFUND_SUCCESS_MODAL_TITLE,
    TIER,
    USER_CANNOT_SIGN_AGREEMENT_CONTENT_EST,
    USER_CANNOT_SIGN_AGREEMENT_CONTENT_EXP,
    USER_CANNOT_SIGN_AGREEMENT_TITLE_EST,
    USER_CANNOT_SIGN_AGREEMENT_TITLE_EXP,
    WORK_PERMIT_URL,
    WORK_VISA_PAGE_TITLE_TEXT,
    BalanceRequestStatus,
    BRRefundMessages,
    ColName,
    DateFormats,
    ExceptionalBalanceRequestStatus,
    Numbers,
    VisaType,
)
from src.ui.components.raw.table import Table
from utils.assertion.selene_conditions import have_any_number, have_in_text_number
from utils.assertion.soft_assertions import soft_assert, soft_assert_text
from utils.helpers import verify_new_tab_url_contains
from utils.pdf_parser import (
    file_is_valid_pdf,
    get_downloaded_filename,
    verify_text_in_pdf,
)
from utils.selene import scroll_into_view_if_needed


class PermWorkVisaPage:
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
    BUTTON = ".//button"
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
    refund_action_button = s('//button/p[contains(text(), "Return and refund")]')
    establishment_fund_section = s('//*[@data-testid="absherFundsSection"]')
    establishment_fund_section_title = establishment_fund_section.ss("./div").first
    establishment_fund_table = Table(establishment_fund_section.s(".//table"))
    establishment_fund_left_cell = establishment_fund_table.cell(row=1, column=1)
    establishment_fund_right_cell = establishment_fund_table.cell(row=1, column=2)
    increase_quota_establishment_button = s('//*[@data-testid="establishmentPhase"]//button')
    increase_quota_button = s('//*[@data-testid="increaseRecruitmentQuotaBtn"]')
    nav_link_to_transitional_page = ss("//nav//li").second
    allowed_quota_section = s('//*[@id="allowedQuotaSection"]')
    exceptional_requests_table = s('//*[@data-testid="ExceptionalLOBalanceTable"]')
    tier_upgrades_requests_table = s('//*[@data-testid="TierHistoryTable"]')
    establishment_fund_tab = s('//*[@data-testid="nav-Establishment fund"]')
    learn_more_tab = s('//*[@data-testid="nav-Learn more"]')
    learn_more_section = s('//*[@id="knowledgeSection"]//p')
    recruitment_quota_section = s("#allowedQuotaSection")
    recruitment_quota_tab = s('//*[@data-testid="nav-Recruitment quota"]')
    increase_fund_modal = s('//*[@data-testid="absherFundsModal"]')
    increase_fund_modal_x_button = increase_fund_modal.ss(".//button").first
    increase_fund_modal_close_button = increase_fund_modal.ss(".//button").second
    LINK = ".//a"
    ICON = './/*[name()="svg"]'
    increase_fund_modal_link = increase_fund_modal.s(LINK)
    navigation_list = s("#navigationList")
    recruitment_quota_table_expansion = Table('//*[@data-testid="expansionPhase"]')
    recruitment_quota_table_establishment = Table('//*[@data-testid="establishmentPhase"]')
    issue_visa_button = s('//*[@data-testid="issueVisaBtn"]')
    modal_window = s('//*[@id="modalBodyWrapper"]//parent::div')
    modal_window_x_button = modal_window.ss(".//button").first
    modal_window_close_button = modal_window.s('.//button/*[text()="Close"]')
    modal_window_title = modal_window.ss(".//p").first
    modal_error_window_content = modal_window.s(".//ol/li")
    modal_warning_window_content = modal_window.ss(".//p").second
    modal_success_window_content = modal_warning_window_content
    modal_cancel_button = modal_window.s('.//button/*[text()="Cancel request"]')
    modal_return_button = modal_window.s('.//button/*[text()="Back to Permanent work visas"]')
    page_navigation_chain = s("//nav")
    page_title = ss('//div[@data-component="Layout"]/div[@data-component="Box"]//p').first
    internal_validation_banner = s('//*[@data-testid="internalValidationErrorMessageCard"]')
    work_permit_banner = s('//*[@data-testid="workPermitErrorMessageCard"]')
    modal_error_message = modal_window.s('.//*[@data-component="ErrorMessage"]')
    modal_retry_button = modal_window.s('.//button/*[text()="Retry"]')
    action_menu = s('//*[@data-component="ActionsMenu"]')
    increase_fund_modal_title = increase_fund_modal.s(".//p")

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
        self.other_visas_table.s(self.BUTTON).should(be.visible)
        self.other_visas_table.s(self.BUTTON).should(be.clickable)
        soft_assert_text(
            self.other_visas_table.s(self.BUTTON),
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
        self.permanent_visas_table.s(self.BUTTON).should(be.visible)
        self.permanent_visas_table.s(self.BUTTON).should(be.clickable)
        soft_assert_text(
            self.permanent_visas_table.s(self.BUTTON),
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
        self.open_action_menu_on_visa_request(visa_type, request)
        self.print_action.click()
        filename = get_downloaded_filename(timeout=20)
        if visa_type == VisaType.ESTABLISHMENT:
            verify_text_in_pdf(filename, request)
        else:
            file_is_valid_pdf(filename)

    @allure.step("Return to transitional page")
    def return_to_transitional_page(self):
        self.nav_link_to_transitional_page.click()

    def open_action_menu_on_visa_request(self, visa_type, request):
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
        table = Table(self.tier_upgrades_requests_table)
        self.verify_request_status(ref_number, status, table)

    @allure.step("Verify balance request status")
    def verify_balance_request_status(self, ref_number: str, status: BalanceRequestStatus) -> None:
        table = Table(self.exceptional_requests_table)
        self.verify_request_status(ref_number, status, table)

    def verify_request_status(
        self,
        ref_number: str,
        status: Union[BalanceRequestStatus | ExceptionalBalanceRequestStatus],
        table: Table,
    ) -> None:
        status_cell = table.cell(row=have.text(ref_number), column=ColName.REQUEST_STATUS)
        command.js.scroll_into_view(table.web_element)
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
        soft_assert_text(
            self.increase_fund_modal_title,
            text=INCREASE_ABSHER_MODAL_TITLE,
            element_name="Increase establishment modal title",
        )
        self.verify_go_to_knowledge_center_open_page(self.increase_fund_modal.s(self.LINK))
        self.increase_fund_modal_x_button.should(be.visible).should(be.clickable)
        self.increase_fund_modal_close_button.should(be.visible).should(be.clickable)
        self.increase_fund_modal_link.should(be.visible)

    def open_increase_fund_modal(self) -> None:
        self.establishment_fund_left_cell.s("./a").click()

    @allure.step("Verify allowed quota section (expansion)")
    def verify_allowed_quota_section_expansion(self) -> None:
        self.recruitment_quota_table_expansion.body.should(be.visible)
        self.recruitment_quota_table_expansion.rows.should(have.size(Numbers.TWO))
        soft_assert_text(
            self.recruitment_quota_table_expansion.cell(row=1, column=1),
            text=RECRUITMENT_QUOTA,
            element_name="Recruitment quota cell (header)",
        )
        self.recruitment_quota_table_expansion.cell(row=1, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_expansion.cell(row=1, column=2).should(
            have_in_text_number(Numbers.NINE_HUNDRED_NINETY_NINE)
        )
        soft_assert_text(
            self.recruitment_quota_table_expansion.cell(row=2, column=1),
            text=ESTABLISHMENT_PHASE,
            element_name="Establishment phase cell (header)",
        )
        self.recruitment_quota_table_expansion.cell(row=2, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        soft_assert_text(
            self.recruitment_quota_table_expansion.cell(row=2, column=2),
            text=EXPANSION,
            element_name="Establishment phase cell (value)",
        )

    @allure.step("Verify allowed quota section (establishment)")
    def verify_allowed_quota_section_establishment(self) -> None:
        self.recruitment_quota_table_establishment.body.should(be.visible)
        self.recruitment_quota_table_establishment.rows.should(have.size(Numbers.SIX))
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=1, column=1),
            text=RECRUITMENT_QUOTA,
            element_name="Recruitment quota cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=2, column=1),
            text=ESTABLISHMENT_PHASE,
            element_name="Establishment phase cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=3, column=1),
            text=RECRUITMENT_QUOTA_TIER,
            element_name="Recruitment quota tier cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=4, column=1),
            text=ALLOWANCE_PERIOD_START_DATE,
            element_name="Allowance period start date cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=5, column=1),
            text=ALLOWANCE_PERIOD_END_DATE,
            element_name="Allowance period end date cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=6, column=1),
            text=ESTIMATED_RECRUITMENT_QUOTA,
            element_name="Estimated recruitment quota after allowance period ends cell (header)",
        )
        self.recruitment_quota_table_establishment.cell(row=1, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=2, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=3, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=4, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=5, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=6, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=1, column=2).should(
            have_in_text_number(Numbers.FOUR)
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=2, column=2),
            text=ESTABLISHING,
            element_name="Establishing cell (value)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=3, column=2),
            text=TIER.ONE,
            element_name="Tier cell (value)",
        )
        today = datetime.date.today()
        start_date = today + relativedelta(months=-6)
        end_date = today + relativedelta(months=+6)
        left = end_date - today
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=4, column=2),
            text=start_date.strftime(DateFormats.DD_MM_YYYY),
            element_name="Start date cell (value)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=5, column=2),
            text=end_date.strftime(DateFormats.DD_MM_YYYY),
            element_name="End date cell (date value)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=5, column=2),
            text=f"{left.days} days left",
            element_name="End date cell (days left value)",
        )
        self.recruitment_quota_table_establishment.cell(row=5, column=2).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=6, column=2).should(
            have_in_text_number(Numbers.NINE_HUNDRED_NINETY_NINE)
        )

    @allure.step(
        "Verify if buttons 'Issue visa' and 'Increase recruitment quota' are enable/disabled in expansion flow"
    )
    def verify_buttons_expansion(self, issue_enabled: bool, increase_enabled: bool) -> None:
        if issue_enabled:
            self.verify_issue_visa_button_enabled()
        else:
            self.verify_issue_visa_button_disabled()
        if increase_enabled:
            self.verify_increase_recruitment_quota_button_enabled(self.increase_quota_button)
        else:
            self.verify_increase_recruitment_quota_button_disabled(self.increase_quota_button)

    def verify_issue_visa_button_enabled(self) -> None:
        self.issue_visa_button.should(be.visible).should(be.clickable)
        self.issue_visa_button.s(self.ICON).should(be.hidden)
        curr_url = browser.driver.current_url
        self.issue_visa_button.click()
        soft_assert(
            curr_url != browser.driver.current_url,
            "Issue visa button not redirected to another page",
        )
        browser.driver.back()

    def verify_issue_visa_button_disabled(
        self, modal_title: str = None, modal_content: str = None
    ) -> None:
        self.issue_visa_button.should(be.visible).should(be.clickable)
        self.issue_visa_button.s(self.ICON).should(be.visible)
        self.issue_visa_button.click()
        self.verify_modal_window(modal_title, modal_content)
        self.modal_window_x_button.click()
        self.modal_window.should(be.hidden)
        self.issue_visa_button.click()
        self.verify_modal_window(modal_title, modal_content)
        self.modal_window_close_button.click()
        self.modal_window.should(be.hidden)

    def verify_increase_recruitment_quota_button_enabled(self, button: Element) -> None:
        scroll_into_view_if_needed(button)
        button.should(be.visible).should(be.clickable)
        button.s(self.ICON).should(be.hidden)
        curr_url = browser.driver.current_url
        button.click()
        soft_assert(
            curr_url != browser.driver.current_url,
            f"{str(button)} not redirected to another page",
        )
        browser.driver.back()

    def verify_increase_recruitment_quota_button_disabled(
        self, button: Element, title: str = None, content: str = None
    ) -> None:
        scroll_into_view_if_needed(button)
        button.should(be.visible).should(be.clickable)
        button.s(self.ICON).should(be.visible)
        button.click()
        self.verify_modal_window(title, content)
        self.modal_window_x_button.click()
        self.modal_window.should(be.hidden)
        button.click()
        self.verify_modal_window()
        self.modal_window_close_button.click()
        self.modal_window.should(be.hidden)

    def verify_modal_window(
        self,
        title: str = None,
        content: str = None,
        content_element: Element = None,
        close_button: bool = True,
    ) -> None:
        self.modal_window.should(be.visible)
        self.modal_window_x_button.should(be.visible).should(be.clickable)
        condition = be.visible if close_button else be.hidden
        self.modal_window_close_button.should(condition)
        if title:
            soft_assert_text(
                self.modal_window_title, text=title, element_name="modal window title"
            )
        if content:
            soft_assert_text(content_element, text=content, element_name="modal window content")

    @allure.step(
        "Verify if buttons 'Issue visa' and 'Increase recruitment quota' are enable/disabled in establishment flow"
    )
    def verify_buttons_establishment(self, issue_enabled: bool, increase_enabled: bool) -> None:
        if issue_enabled:
            self.verify_issue_visa_button_enabled()
        else:
            self.verify_issue_visa_button_disabled()
        if increase_enabled:
            self.verify_increase_recruitment_quota_button_enabled(self.increase_quota_button)
            self.verify_increase_recruitment_quota_button_enabled(
                self.increase_quota_establishment_button
            )
        else:
            self.verify_increase_recruitment_quota_button_disabled(self.increase_quota_button)
            self.verify_increase_recruitment_quota_button_disabled(
                self.increase_quota_establishment_button
            )

    @allure.step("Verify allowance period")
    def verify_allowance_period_block_perm_work_visa_request(self, allowance_started):
        if allowance_started:
            self.verify_allowed_quota_section_establishment()
        else:
            self.verify_allowance_period_hidden_block_perm_work_visa_request()

    def verify_allowance_period_hidden_block_perm_work_visa_request(self):
        self.recruitment_quota_table_establishment.body.should(be.visible)
        self.recruitment_quota_table_establishment.rows.should(have.size(Numbers.FOUR))
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=1, column=1),
            text=RECRUITMENT_QUOTA,
            element_name="Recruitment quota cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=2, column=1),
            text=ESTABLISHMENT_PHASE,
            element_name="Establishment phase cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=3, column=1),
            text=RECRUITMENT_QUOTA_TIER,
            element_name="Recruitment quota tier cell (header)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=4, column=1),
            text=ESTIMATED_RECRUITMENT_QUOTA,
            element_name="Estimated recruitment quota after allowance period ends cell (header)",
        )
        self.recruitment_quota_table_establishment.cell(row=1, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=2, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=3, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=4, column=1).s(self.LINK).should(
            be.visible
        ).should(be.clickable)
        self.recruitment_quota_table_establishment.cell(row=1, column=2).should(
            have_in_text_number(Numbers.FOUR)
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=2, column=2),
            text=ESTABLISHING,
            element_name="Establishing cell (value)",
        )
        soft_assert_text(
            self.recruitment_quota_table_establishment.cell(row=3, column=2),
            text=TIER.ONE,
            element_name="Tier cell (value)",
        )
        self.recruitment_quota_table_establishment.cell(row=4, column=2).should(
            have_in_text_number(Numbers.NINE_HUNDRED_NINETY_NINE)
        )

    @allure.step("Check the error text above Recruitment quota title on the work visa dashboard.")
    def verify_error_banner(self):
        soft_assert_text(
            self.internal_validation_banner,
            text=ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT,
            element_name="Error banner",
        )

    @allure.step("Check buttons in the top block on the Instant work visa page [expansion]")
    def verify_expansion_balance_zero_buttons_behavior(self):
        self.verify_issue_visa_button_disabled(
            ISSUE_VISA_MODAL_TITLE_TEXT, ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT
        )
        self.verify_increase_recruitment_quota_button_enabled(self.increase_quota_button)

    @allure.step("Verify tier one, balance zero case validations")
    def verify_issue_perm_work_visa_blocked(self):
        self.verify_error_modal_window(content=ISSUE_VISA_MODAL_CONTENT_ESTABLISHING_TEXT)
        self.verify_issue_visa_button_disabled(
            ISSUE_VISA_MODAL_TITLE_TEXT, ISSUE_VISA_MODAL_CONTENT_ESTABLISHING_TEXT
        )
        self.verify_increase_recruitment_quota_button_enabled(self.increase_quota_button)

    @allure.step("Verify tier four, balance more than zero case validations")
    def verify_increase_perm_work_visa_quota_blocked(self):
        self.internal_validation_banner.should(be.hidden)
        self.verify_issue_visa_button_enabled()
        self.verify_increase_recruitment_quota_button_disabled(self.increase_quota_button)

    @allure.step("Verify tier four, balance zero case validations")
    def verify_increase_perm_work_visa_quota_and_issue_blocked(self):
        self.internal_validation_banner.should(be.hidden)
        self.verify_issue_visa_button_disabled(
            ISSUE_VISA_MODAL_TITLE_TEXT, ISSUE_VISA_MODAL_CONTENT_HIGHEST_TIER_TEXT
        )
        self.verify_increase_recruitment_quota_button_disabled(self.increase_quota_button)

    @allure.step("Verify knowledge center links")
    def verify_knowledge_center_links(self):
        soft_assert_text(
            self.establishment_fund_section.s(self.LINK),
            text=HOW_TO_INCREASE_ESTABLISHMENT_FUNDS,
            element_name="Link to modal window",
        )
        self.establishment_fund_section.s(self.LINK).click()
        self.verify_increase_fund_modal()
        self.increase_fund_modal_close_button.click()
        command.js.scroll_into_view(self.other_visas_section)
        self.verify_go_to_knowledge_center_open_page(self.learn_more_section.s(self.BUTTON))

    @allure.step("Verify knowledge center page open")
    def verify_go_to_knowledge_center_open_page(self, link):
        link.click()
        verify_new_tab_url_contains(KNOWLEDGE_CENTER_URL)

    @allure.step("Verify visa request status")
    def verify_perm_status_work_visa_request(self, ref_number: str) -> None:
        status_cell_perm_work_visas_request = self.table_status_cell(
            self.permanent_visas_table, ref_number
        )
        status_cell_others_visa_request = self.table_status_cell(
            self.other_visas_table, ref_number
        )
        soft_assert_text(
            element=status_cell_perm_work_visas_request,
            text=BR_ACCEPTED.label,
            element_name=f"Perm work visas request status ref_num={ref_number}",
        )
        soft_assert_text(
            element=status_cell_others_visa_request,
            text=BR_ACCEPTED.label,
            element_name=f"Other visas status ref_num={ref_number}",
        )

    @allure.step("Open visa request view")
    def open_visa_request_view(self, ref_number: str) -> None:
        self.open_action_menu_on_visa_request(visa_type=VisaType.ESTABLISHMENT, request=ref_number)
        self.view_action.click()

    def table_status_cell(self, table_element: Element, ref_number: str) -> Element:
        table = Table(table_element)
        return table.cell(row=have.text(ref_number), column=ColName.VISA_STATUS)

    def verify_perm_work_visa_refund_status(
        self, ref_number: str, br_status: BRRefundMessages
    ) -> None:
        self.open_action_menu_on_tier_upgrade_request(ref_number)
        self.refund_action_button.click()
        self.verify_warning_modal_window(title=br_status.title, content=br_status.content)
        self.modal_window_close_button.click()
        self.open_action_menu_on_tier_upgrade_request(ref_number)
        self.refund_action_button.click()
        self.verify_warning_modal_window(title=br_status.title, content=br_status.content)
        self.modal_window_x_button.click()
        if br_status.id in CAN_BE_REFUNDED:
            self.refund_tier_upgrade_request(ref_number, br_status.success)

    @allure.step("Verify successful refund modal window")
    def verify_successful_refund_modal(self):
        self.verify_success_modal_window(
            title=REFUND_SUCCESS_MODAL_TITLE, content=REFUND_SUCCESS_MODAL_CONTENT
        )
        self.modal_return_button.should(be.visible)
        self.modal_return_button.click()

    @allure.step("Verify erroneous refund modal window")
    def verify_error_refund_modal(self):
        self.verify_modal_window(
            title=BRRefundMessages.title,
            content=BRRefundMessages.content,
            content_element=self.modal_error_window_content,
        )
        soft_assert_text(
            self.modal_error_message,
            REFUND_ERROR_MODAL_MESSAGE,
            element_name="Refund modal error message",
        )
        self.modal_retry_button.should(be.visible)
        self.modal_retry_button.click()
        self.modal_error_message.should(be.hidden)
        self.modal_cancel_button.should(be.visible)
        self.verify_modal_window(
            title=BRRefundMessages.title,
            content=BRRefundMessages.content,
            content_element=self.modal_error_window_content,
        )
        soft_assert_text(
            self.modal_error_message,
            REFUND_ERROR_MODAL_MESSAGE,
            element_name="Refund modal error message",
        )
        self.modal_retry_button.should(be.visible)
        self.modal_window_close_button.click()

    def open_action_menu_on_tier_upgrade_request(self, request):
        if self.action_menu.matching(be.hidden):
            self.recruitment_quota_table_establishment.rows.should(have.size(Numbers.SIX))
            command.js.scroll_into_view(
                self.recruitment_quota_table_establishment.cell(
                    row=Numbers.SIX, column=Numbers.ONE
                )
            )
            self.tier_upgrades_requests_table.ss(self.table_rows).by(have.text(request)).first.s(
                self.request_action_button
            ).click()

    def refund_tier_upgrade_request(self, ref_number, expected):
        self.open_action_menu_on_tier_upgrade_request(ref_number)
        self.refund_action_button.click()
        self.modal_cancel_button.should(be.visible)
        self.modal_cancel_button.click()
        self.verify_refund_modal(expected)
        self.modal_window.should(be.hidden)

    def verify_error_modal_window(self, title: str = None, content: str = None) -> None:
        self.verify_modal_window(title, content, content_element=self.modal_error_window_content)

    def verify_warning_modal_window(self, title: str, content: str, error: bool = False) -> None:
        self.verify_modal_window(title, content, content_element=self.modal_warning_window_content)
        if error:
            soft_assert_text(
                self.modal_error_message,
                text=REFUND_ERROR_MODAL_MESSAGE,
                element_name="Refund modal error message",
            )

    def verify_success_modal_window(self, title: str, content: str) -> None:
        self.verify_modal_window(
            title, content, content_element=self.modal_success_window_content, close_button=False
        )

    def verify_refund_modal(self, expected: bool) -> None:
        if expected:
            self.verify_success_modal_window(
                title=REFUND_SUCCESS_MODAL_TITLE, content=REFUND_SUCCESS_MODAL_CONTENT
            )
            self.modal_return_button.should(be.visible)
            self.modal_return_button.click()
        else:
            self.verify_warning_modal_window(
                title=BR_SUCCESS.title, content=BR_SUCCESS.content, error=True
            )
            self.modal_window_close_button.click()

    def verify_perm_work_visa_refund_available(
        self, ref_number: str, status: BalanceRequestStatus
    ) -> None:
        self.open_action_menu_on_tier_upgrade_request(ref_number)
        condition = be.visible if status.refundable else be.hidden
        self.refund_action_button.should(condition)
        if status.refundable:
            self.refund_tier_upgrade_request(ref_number, expected=True)
            self.open_action_menu_on_tier_upgrade_request(ref_number)
            self.refund_action_button.should(be.hidden)
            table = Table(self.tier_upgrades_requests_table)
            self.verify_request_status(ref_number, BR_REFUNDED, table)

    def verify_exceptional_balance_request_status(
        self, ref_number: str, status: ExceptionalBalanceRequestStatus
    ) -> None:
        table = Table(self.exceptional_requests_table)
        self.verify_request_status(ref_number, status, table)

    @allure.step("Verify the option to sign agreement is not available [establishing]")
    def verify_user_cannot_sign_agreement_establishing(self):
        self.verify_issue_visa_button_enabled()
        self.verify_increase_recruitment_quota_button_disabled(
            self.increase_quota_button,
            title=USER_CANNOT_SIGN_AGREEMENT_TITLE_EST,
            content=USER_CANNOT_SIGN_AGREEMENT_CONTENT_EST,
        )

    @allure.step("Verify the option to sign agreement is not available [expansion]")
    def verify_user_cannot_sign_agreement_expansion(self):
        self.verify_issue_visa_button_enabled()
        self.verify_increase_recruitment_quota_button_disabled(
            self.increase_quota_button,
            title=USER_CANNOT_SIGN_AGREEMENT_TITLE_EXP,
            content=USER_CANNOT_SIGN_AGREEMENT_CONTENT_EXP,
        )

    @allure.step("Verify the option to sign agreement is available, and this step is skipped")
    def verify_user_can_sign_agreement(self):
        self.verify_issue_visa_button_enabled()
        self.verify_increase_recruitment_quota_button_enabled(self.increase_quota_button)

    @allure.step("Verify expired work permit error banner")
    def verify_exp_work_permit_error_shown(self):
        self.work_permit_banner.should(be.visible)
        soft_assert_text(
            element=self.work_permit_banner,
            text=PERM_VISA_EXP_WORK_PERMIT_ERROR,
            element_name="Work permit error banner",
        )
        soft_assert_text(
            element=self.work_permit_banner.s(self.LINK),
            text=PERM_VISA_EXP_WORK_PERMIT_ERROR_LINK,
            element_name="Work permit error banner link",
        )
        self.work_permit_banner.s(self.LINK).click()
        verify_new_tab_url_contains(WORK_PERMIT_URL)
