from __future__ import annotations

from selene import be, browser, have
from selene.support.shared.jquery_style import s


class WorkPermitPage:
    search_border_or_iqama = s("//input[@placeholder='Search employees by Border / Iqama number']")
    search_btn = s("//button[normalize-space()='Search']")
    check_available_periods_btn = s("//div[@class='c-work-permit-button__action-label']")
    wp_period_3 = s("//button[normalize-space()='3']")
    wp_period_6 = s("//button[normalize-space()='6']")
    wp_period_9 = s("//button[normalize-space()='9']")
    wp_period_12 = s("//button[normalize-space()='12']")
    wp_period_group = s("//div[@class='o-button-group']")
    error_msg = s("//div[@class='c-work-permit-button__action-label c-work-permit-button__action-label--error']")
    continue_with_wp_request = s("//button[normalize-space()='Continue with work permit request']")
    show_all_employees = s("//button[normalize-space()='Show all employees']")
    show_selected_employees = s("div[class='o-button-group o-button-group--text'] button[class='btn-selected']")
    show_not_selected_employees_btn = s("button[class='o-button--disabled']")
    iqama_number = s("td[data-label='Iqama number'] span[class='column-wraper']")
    late_years_no_extra = s("")
    late_years_extra_fees_exceeding = s("")
    late_years_extra_fees_equivalent = s("")
    view_wp_request = s("//div[normalize-space()='View work permit requests']")
    view_wp_debts = s("//div[normalize-space()='View work permit debts']")
    back_to_wp = s("//span[@class='c-requests__back-to-work-permits-action']")
    back_to_wp_from_debts = s("//div[contains(text(),'Back to Work Permits')]")
    wp_title = s("//span[@class='c-permits-header__title']")
    switch_to_en = s("//button[normalize-space()='English']")
    pagination_text = s("")
    total_results = s("//p[@class='c-pagination__total']")
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

    otp_code_first_cell = s("(//input[@type='tel'])[1]")
    otp_code_second_cell = s("(//input[@type='tel'])[2]")
    otp_code_third_cell = s("(//input[@type='tel'])[3]")
    otp_code_fourth_cell = s("(//input[@type='tel'])[4]")
    confirm_button = s("//button[normalize-space()='Confirm']")

    def verify_search_by_border_or_iqama(self, iqama) -> WorkPermitPage:
        self.search_border_or_iqama.type(iqama)
        self.search_btn.click()
        return self

    def check_available_periods(self) -> WorkPermitPage:
        self.check_available_periods_btn.click()
        self.wp_period_12.should(be.enabled)
        return self

    def verify_unfit_job_error(self) -> WorkPermitPage:
        self.check_available_periods_btn.click()
        self.error_msg.should(be.visible)
        return self

    def check_all_wp_periods_available(self) -> WorkPermitPage:
        self.wp_period_group = browser.element("//div[@class='o-button-group']")
        periods = self.wp_period_group.all(".//button")
        for button in periods:
            if button.has_class("btn-disabled"):
                print(f"Button '{button.text}' is disabled.")
            else:
                print(f"Button '{button.text}' is active.")
        return self

    def choose_wp_period_6(self) -> WorkPermitPage:
        self.wp_period_6.click()
        return self

    def choose_wp_period_12(self) -> WorkPermitPage:
        self.wp_period_12.click()
        return self

    def verify_continue_with_wp_request_btn_active(self) -> WorkPermitPage:
        self.continue_with_wp_request.should(be.enabled).click()
        return self

    def verify_redirect_to_overview(self) -> WorkPermitPage:
        url2 = 'https://lo-work-permits.qiwa.info/work-permits/overview'
        url = browser.driver.current_url()
        assert url == url2
        return self

    def click_on_show_only_selected_employees_btn(self) -> WorkPermitPage:
        self.show_selected_employees.click()
        return self

    def verify_selected_employees(self, personal_number) -> WorkPermitPage:
        self.iqama_number.should(have.exact_text(personal_number))
        return self

    def verify_selected_employees_on_calculation_page(self, personal_number) -> WorkPermitPage:
        self.iqama_number.should(have.exact_text(personal_number))
        return self

    def verify_late_years_extra_fees(self) -> WorkPermitPage:
        browser.element(self.late_years_no_extra).should(have.size_greater_than(0))
        browser.element(self.late_years_extra_fees_exceeding).should(have.size_greater_than(0))
        browser.element(self.late_years_extra_fees_equivalent).should(have.size_greater_than(0))
        return self

    def verify_wp_requests_service(self) -> WorkPermitPage:
        self.view_wp_request.should(be.visible).click()
        return self

    def verify_wp_debts_service(self) -> WorkPermitPage:
        self.view_wp_debts.should(be.visible).click()
        return self

    def click_on_back_to_wp(self) -> WorkPermitPage:
        self.back_to_wp.click()
        return self

    def verify_wp_dashboard_title(self, wp_title) -> WorkPermitPage:
        self.wp_title.should(have.exact_text(wp_title))
        return self

    def verify_show_employee_btns(self) -> WorkPermitPage:
        self.show_all_employees.should(be.visible).should(be.clickable)
        self.show_not_selected_employees_btn.should(be.disabled)
        return self

    def verify_total_results(self) -> WorkPermitPage:
        self.total_results.should(be.visible)
        return self

    def click_on_unprocess_btn(self) -> WorkPermitPage:
        self.unprocess_btn.click()
        return self

    def click_on_filter(self) -> WorkPermitPage:
        self.wp_debts_filter.click()
        return self

    def verify_paid_debts(self) -> WorkPermitPage:
        self.click_on_filter()
        self.only_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.paid.should(have.exact_text('Paid'))
        return self

    def verify_unpaid_debts(self) -> WorkPermitPage:
        self.click_on_filter()
        self.not_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.not_paid.should(have.exact_text('Not Paid'))
        return self

    def generate_sadad_number(self) -> WorkPermitPage:
        self.generate_sadad.click()
        self.proceed_otp_code('0000')
        return self

    def proceed_otp_code(self, number: str) -> WorkPermitPage:
        self.otp_code_first_cell.type(number)
        self.otp_code_second_cell.type(number)
        self.otp_code_third_cell.type(number)
        self.otp_code_fourth_cell.type(number)
        self.confirm_button.click()
        return self

    def back_to_work_permits_from_debts(self) -> WorkPermitPage:
        self.back_to_wp_from_debts.click()
        return self

    def verify_pagination(self) -> WorkPermitPage:
        self.prev_btn.should(be.disabled)
        self.next_btn.should(be.clickable).click()
        self.prev_btn.should(be.clickable).click()
        return self
