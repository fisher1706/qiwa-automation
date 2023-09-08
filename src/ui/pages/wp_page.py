from __future__ import annotations

from datetime import time
import time
import allure
from selene import be, browser, command, have
from selene.support.shared.jquery_style import s

import config


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
    iqama_number = s("td[data-label='Iqama number'] span[class='column-wraper']")
    late_years_no_extra = s("")
    late_years_extra_fees_exceeding = s("")
    late_years_extra_fees_equivalent = s("")
    view_wp_request = s("//div[normalize-space()='View work permit requests']")
    view_wp_debts = s("//div[normalize-space()='View work permit debts']")
    back_to_wp = s("//div[contains(text(),'Back to Work Permits')]")
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

    otp_code_first_cell = s("(//input[@type='tel'])[1]")
    otp_code_second_cell = s("(//input[@type='tel'])[2]")
    otp_code_third_cell = s("(//input[@type='tel'])[3]")
    otp_code_fourth_cell = s("(//input[@type='tel'])[4]")
    confirm_button = s("//button[normalize-space()='Confirm']")

    def verify_search_by_border_or_iqama(self, iqama):
        self.search_border_or_iqama.type(iqama)
        self.search_btn.click()
        time.sleep(5)

    def check_available_periods(self):
        self.check_available_periods_btn.click()
        self.wp_period_12.should(be.enabled)

    def verify_unfit_job_error(self):
        self.check_available_periods_btn.click()
        self.error_msg.should(be.visible)

    def check_all_wp_periods_available(self):
        self.wp_period_group = browser.element("//div[@class='o-button-group']")
        periods = self.wp_period_group.all(".//button")
        for button in periods:
            if button.has_class("btn-disabled"):
                print(f"Button '{button.text}' is disabled.")
            else:
                print(f"Button '{button.text}' is active.")

    def choose_wp_period_6(self):
        self.wp_period_6.click()

    def choose_wp_period_12(self):
        self.wp_period_12.click()

    def verify_continue_with_wp_request_btn_active(self):
        self.continue_with_wp_request.should(be.enabled).click()

    def verify_redirect_to_overview(self):
        url2 = 'https://lo-work-permits.qiwa.info/work-permits/overview'
        url = browser.location()
        assert url == url2
        return self

    def click_on_show_only_selected_employees_btn(self):
        self.show_selected_employees.click()

    def verify_selected_employees(self, personal_number):
        self.iqama_number.should(have.exact_text(personal_number))

    def verify_selected_employees_on_calculation_page(self, personal_number):
        self.iqama_number.should(have.exact_text(personal_number))

    def verify_late_years_extra_fees(self):
        browser.element(self.late_years_no_extra).should(have.size_greater_than(0))
        browser.element(self.late_years_extra_fees_exceeding).should(have.size_greater_than(0))
        browser.element(self.late_years_extra_fees_equivalent).should(have.size_greater_than(0))

    def verify_wp_requests_service(self):
        self.view_wp_request.should(be.visible).click()

    def verify_wp_debts_service(self):
        self.view_wp_debts.should(be.visible).click()

    def click_on_back_to_wp(self):
        time.sleep(5)
        self.back_to_wp.click()

    def verify_wp_dashboard_title(self, wp_title):
        self.wp_title.should(have.exact_text(wp_title))

    def verify_show_employee_btns(self):
        self.show_all_employees.should(be.visible).should(be.selected)
        self.show_selected_employees.should(be.disabled)

    def verify_total_results(self):
        self.total_results.should(be.visible)

    def switch_to_en(self):
        time.sleep(5)
        self.switch_to_en.click()

    def click_on_unprocess_btn(self):
        self.unprocess_btn.click()

    def click_on_filter(self):
        self.wp_debts_filter.click()

    def verify_paid_debts(self):
        self.click_on_filter()
        self.only_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.paid.should(have.exact_text('Paid'))

    def verify_unpaid_debts(self):
        time.sleep(5)
        self.click_on_filter()
        self.not_paid_radio.click()
        self.show_me_results_btn.click()
        self.click_on_filter()
        self.not_paid.should(have.exact_text('Not Paid'))

    def generate_sadad_number(self):
        self.generate_sadad.click()
        self.proceed_otp_code('0000')

    def proceed_otp_code(self, number: str):
        self.otp_code_first_cell.type(number)
        self.otp_code_second_cell.type(number)
        self.otp_code_third_cell.type(number)
        self.otp_code_fourth_cell.type(number)
        self.confirm_button.click()
        return self

