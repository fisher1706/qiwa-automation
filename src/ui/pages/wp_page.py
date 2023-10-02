from __future__ import annotations

import time
from datetime import datetime, timedelta

from selene import be, browser, have, query
from selene.support.shared.jquery_style import s

import config
from src.ui.components.raw.table import Table


class LoWorkPermitPage:
    search_border_or_iqama = s("//input[@placeholder='Search employees by Border / Iqama number']")
    search_btn = s("//button[normalize-space()='Search']")
    check_available_periods_btn = s("//div[@class='c-work-permit-button__action-label']")
    wp_period_3 = s("//button[normalize-space()='3']")
    wp_period_6 = s("//button[normalize-space()='6']")
    wp_period_9 = s("//button[normalize-space()='9']")
    wp_period_12 = s("//button[normalize-space()='12']")
    wp_period_group = s("//div[@class='o-button-group']")
    error_msg = s(
        "//div[@class='c-work-permit-button__action-label c-work-permit-button__action-label--error']"
    )
    continue_with_wp_request = s("//button[normalize-space()='Continue with work permit request']")
    show_all_employees = s("//button[normalize-space()='Show all employees']")
    show_selected_employees = s(
        "div[class='o-button-group o-button-group--text'] button[class='btn-selected']"
    )
    show_not_selected_employees_btn = s("button[class='o-button--disabled']")
    iqama_number = s("//td[@data-label='Iqama number']")
    total_amount_general = s("//td[@data-label='Total amount']")
    work_permit_fees = s("//td[@data-label='Work permit fees']")
    work_permit_extra_fees = s("//td[@data-label='Extra fees']")
    late_years_no_extra = s("//td[@data-label='Late Years (No Extra Fees)']")
    late_years_extra_fees_exceeding = s("//td[@data-label='Late Years (Extra Fees - Exceeding*)']")
    late_years_extra_fees_equivalent = s(
        "//td[@data-label='Late Years (Extra Fees - Exceeding*)']"
    )
    extra_fees_for_late_year_exceeding = s(
        "//td[@data-label='Extra Fees for Late Years (Exceeding*)']"
    )
    extra_fees_for_late_year_equivalent = s(
        "//td[@data-label='Extra Fees for Late Years (Equivalent**)']"
    )
    view_wp_request = s("//div[normalize-space()='View work permit requests']")
    view_wp_debts = s("//div[normalize-space()='View work permit debts']")
    back_to_wp = s("//span[@class='c-requests__back-to-work-permits-action']")
    back_to_wp_from_debts = s("//div[contains(text(),'Back to Work Permits')]")
    wp_title = s("//span[@class='c-permits-header__title']")
    total_results = s(".c-pagination__total")
    unprocess_btn = s("//button[normalize-space()='Unprocess']")
    generate_sadad = s("//button[@class='o-button o-button--primary o-button--fit']")
    wp_debts_filter = s("//button[@class='c-filter-button__btn']")
    only_paid_radio = s("//label[normalize-space()='Show only paid']")
    not_paid_radio = s("//label[normalize-space()='Show only not paid']")
    show_all_radio = s("//label[normalize-space()='Show all']")
    show_me_results_btn = s("//button[normalize-space()='Show me results']")
    paid = s('//div[@class="o-badge o-badge--positive"]')
    not_paid = s('//div[@class="o-badge o-badge--negative"]')
    prev_btn = s("//button[normalize-space()='< Prev']")
    next_btn = s("//button[normalize-space()='Next >']")
    route = "/work-permits/overview"
    confirm_and_finish_btn = s(".c-overview__button.o-button.o-button--primary")
    confirm_and_send_email_to_client_btn = s(
        "//button[contains(text(),'Confirm and send email to the client')]"
    )
    bill_number = s("h2.c-summary__info-bill > span:last-child")
    back_to_establishment_page = s(".back-link")
    go_to_establishment_page = s("//button[normalize-space()='Go to Establishment page']")
    table_body = Table(s(".c-requests__table"))
    # TODO INVESTIGATE WITH FE OTP LOCATOR
    otp = s("(//input[@type='tel'])[37]")
    cancel_sadad_number_btn = s(".o-button.o-button--primary.c-requests__cancel-button")
    proceed_btn = s("button[class='o-button o-button--full-width o-button--primary']")
    total_amount = s(".c-fees-amounts__value.c-fees-amounts__value--primary")
    final_total_amount = s("h3[class='c-summary__info-total'] span:nth-child(2)")
    sadad_number = s("//td[@data-label='SADAD number']")
    clear_btn = s("//button[normalize-space()='Clear']")
    new_wp_expiration_date = s("td[data-label='New work permit expiration date']")
    wp_expiration_date = s("td[data-label='New work permit expiration date']")
    iqama_summary_page = s("td[data-label='Iqama number']")
    last_page = browser.all(".content__page")[-1]
    view_details = s("//span[@class='c-requests__table-view']")
    wp_period_requested = s("td[data-label='Work permit period requested']")
    sadad = "//td[@data-label='SADAD number']"
    status = "td[data-label='Status']"

    def verify_search_by_border_or_iqama(self, iqama) -> LoWorkPermitPage:
        self.search_border_or_iqama.type(iqama)
        self.search_btn.click()
        return self

    def check_available_periods(self) -> LoWorkPermitPage:
        self.check_available_periods_btn.click()
        self.wp_period_12.should(be.enabled)
        return self

    def verify_unfit_job_error(self) -> LoWorkPermitPage:
        self.check_available_periods_btn.click()
        self.error_msg.should(be.visible)
        return self

    def choose_wp_period_6(self) -> LoWorkPermitPage:
        self.wp_period_6.click()
        return self

    def choose_wp_period_12(self) -> LoWorkPermitPage:
        self.wp_period_12.click()
        return self

    def verify_continue_with_wp_request_btn_active(self) -> LoWorkPermitPage:
        self.continue_with_wp_request.should(be.enabled).click()
        return self

    def verify_redirect_to_overview(self) -> LoWorkPermitPage:
        url2 = config.qiwa_urls.lo_work_permit + self.route
        url = str(browser.driver.current_url)
        assert url == url2
        return self

    def click_on_show_only_selected_employees_btn(self) -> LoWorkPermitPage:
        self.show_selected_employees.click()
        return self

    def verify_selected_employees(self, personal_number) -> LoWorkPermitPage:
        self.iqama_number.should(have.exact_text(personal_number))
        return self

    def verify_selected_employees_on_calculation_page(self, personal_number) -> LoWorkPermitPage:
        self.iqama_number.should(have.exact_text(personal_number))
        return self

    def verify_wp_fees_is_displayed(self) -> LoWorkPermitPage:
        self.work_permit_fees.should(be.visible)
        return self

    def verify_extra_fees_is_displayed(self) -> LoWorkPermitPage:
        self.work_permit_extra_fees.should(be.visible)
        return self

    def verify_late_years_extra_fees(self) -> LoWorkPermitPage:
        self.late_years_no_extra.should(be.visible)
        self.late_years_extra_fees_exceeding.should(be.visible)
        self.late_years_extra_fees_equivalent.should(be.visible)
        return self

    def verify_wp_requests_service(self) -> LoWorkPermitPage:
        self.view_wp_request.should(be.visible).click()
        return self

    def verify_wp_debts_service(self) -> LoWorkPermitPage:
        self.view_wp_debts.should(be.visible).click()
        return self

    def click_on_back_to_wp(self) -> LoWorkPermitPage:
        self.back_to_wp.click()
        return self

    def verify_wp_dashboard_title(self, wp_title) -> LoWorkPermitPage:
        self.wp_title.should(have.exact_text(wp_title))
        return self

    def verify_show_employee_btns(self) -> LoWorkPermitPage:
        self.show_all_employees.should(be.visible).should(be.clickable)
        self.show_not_selected_employees_btn.should(be.disabled)
        return self

    def verify_total_results(self) -> LoWorkPermitPage:
        self.total_results.should(be.visible)
        return self

    def click_on_unprocess_btn(self) -> LoWorkPermitPage:
        self.unprocess_btn.click()
        return self

    def click_on_filter(self) -> LoWorkPermitPage:
        self.wp_debts_filter.click()
        return self

    def verify_paid_debts(self) -> LoWorkPermitPage:
        self.click_on_filter()
        self.only_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.paid.should(have.exact_text("Paid"))
        return self

    def verify_unpaid_debts(self) -> LoWorkPermitPage:
        self.click_on_filter()
        self.not_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.not_paid.should(have.exact_text("Not Paid"))
        return self

    def generate_sadad_number(self) -> LoWorkPermitPage:
        self.generate_sadad.click()
        return self

    def back_to_work_permits_from_debts(self) -> LoWorkPermitPage:
        self.back_to_wp_from_debts.click()
        return self

    def verify_page_pagination(self) -> LoWorkPermitPage:
        self.prev_btn.should(be.present)
        self.next_btn.should(be.clickable).click()
        self.prev_btn.should(be.clickable).click()
        return self

    def click_on_confirm_and_finish_btn(self) -> LoWorkPermitPage:
        self.confirm_and_finish_btn.click()
        return self

    def click_on_confirm_and_send_email_btn(self) -> LoWorkPermitPage:
        self.confirm_and_send_email_to_client_btn.click()
        return self

    def get_bill_number(self) -> str:
        bill = self.bill_number.should(be.visible).get(query.text).strip()
        return bill

    def get_sadad_number(self) -> str:
        sadad = self.sadad_number.should(be.visible).get(query.text).strip()
        return sadad

    def click_back_to_establishment_page(self) -> LoWorkPermitPage:
        self.back_to_establishment_page.click()
        self.go_to_establishment_page.click()
        return self

    def check_pending_status(self, bill_number, status) -> LoWorkPermitPage:
        self.table_body.row(2).s(self.sadad).should(have.exact_text(bill_number))
        self.table_body.row(2).s(self.status).should(have.exact_text(status))
        return self

    def check_canceled_status(self, bill_number, status) -> LoWorkPermitPage:
        self.table_body.row(0).s(self.sadad).should(have.exact_text(bill_number))
        self.table_body.row(0).s(self.status).should(have.exact_text(status))
        return self

    def click_on_cancel_sadad_number_btn(self) -> LoWorkPermitPage:
        self.cancel_sadad_number_btn.click()
        return self

    def enter_otp(self) -> LoWorkPermitPage:
        self.otp.set_value("0000")
        return self

    def click_on_proceed_btn(self) -> LoWorkPermitPage:
        self.proceed_btn.should(be.visible).click()
        time.sleep(20)
        return self

    def get_total_amount(self) -> str:
        amount = self.total_amount.get(query.text)
        return amount

    def compare_total_amounts(self, amount) -> LoWorkPermitPage:
        self.final_total_amount.should(have.exact_text(amount))
        return self

    def navigate_to_last_page(self) -> LoWorkPermitPage:
        self.last_page.click()
        return self

    def click_on_clear_btn(self) -> LoWorkPermitPage:
        self.clear_btn.click()
        return self

    def get_wp_expiration_date(self):
        date = str(self.wp_expiration_date.should(be.visible).get(query.text))
        date2 = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=365)
        return date2.strftime("%Y-%m-%d")

    def compare_expiration_dates(self, date):
        self.new_wp_expiration_date.should(have.exact_text(date))
        return self

    def click_on_view_details(self) -> LoWorkPermitPage:
        self.view_details.click()
        return self

    def verify_requested_period(self, period) -> LoWorkPermitPage:
        self.wp_period_requested.should(have.exact_text(period))
        return self

    def verify_total_amount_is_displayed(self) -> LoWorkPermitPage:
        self.total_amount_general.should(be.visible)
        return self

    def verify_iqama_is_displayed(self) -> LoWorkPermitPage:
        self.iqama_number.should(be.visible)
        return self
