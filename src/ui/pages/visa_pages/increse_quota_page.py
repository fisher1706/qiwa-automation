import datetime
from time import sleep

import allure
from dateutil.relativedelta import relativedelta
from selene.api import be, command, have, not_, query, s, ss

from data.visa.constants import Numbers
from src.ui.components.raw.table import Table
from src.ui.pages.visa_pages.payment_gateway_page import PaymentGateWay
from utils.assertion.selene_conditions import have_any_number


class IncreaseQuotaPage:
    loader = s('//*[@data-testid="skeleton"]')
    TIER_CHECK_BOX = '//*[@id="tier-{}"]//following-sibling::span'
    tier_4_input_field = s('//*[@data-testid="TierNumberFieldValue"]')
    next_step_button_tier_select = s('//*[@data-testid="TierButtonNextStep"]')
    next_step_button_agreement = s('//button//p[contains(text(), "Next step")]')
    next_step_button_location = s('//*[@data-testid="estabAddressSectionButtonNextStep"]')
    goto_payment_button = s('//button/p[contains(text(), "Go to payment")]')
    agree_checkbox = s('//*[@data-testid="TierCheckboxValue"]//following-sibling::span/span')
    terms_agree_checkbox = s(
        '//*[@data-testid="qiwaPlatformTermsAndConditionsCheckbox"]//following-sibling::span/span'
    )
    agree_agreement_checkbox = s(
        '//*[@data-testid="programAgreement"]//following-sibling::span/span'
    )
    location_dropdown = s('//*[@data-testid="estabAddressSectionlocationSelect"]')
    location_dropdown_options = ss('//li[@role="option"]')
    back_to_perm_work_visa_button = s('//*[@data-testid="backToWorkVisas"]')
    program_agreement_section = s('//p[contains(text(), "Program agreement")]')
    payment_request_sent = s('//*[@data-testid="yourRequestHasBeenSent"]')
    payment_request_approved = s(
        '//*[@data-testid="yourRequestForPaymentIncreaseRecruitmentQuotaApproved"]'
    )
    history_tier_upgrades = s('//*[@data-testid="TierHistoryTable"]')
    balanse_request = s('//*[@data-testid="ExceptionalRequestsTable"]')
    history_tier_upgrades_table = Table(history_tier_upgrades)
    balanse_request_table = Table(balanse_request)
    visas_amount_input_field = s('//*[@data-testid="numberOfRequestedExceptionalVisasField"]')
    next_step_visas_amount_button = s(
        '//*[@data-testid="numberOfExceptionalVisasActiveNextStepBtn"]'
    )
    visit_date_input = s('//*[@data-testid="estabAddressSectionVisitDate"]')
    visit_date_calendar = s('//*[@data-testid="estabAddressSectionVisitDate"]')
    floating_popup = s('//*[@class="tippy-box"]')
    calendar_days = floating_popup.ss('//td[@role="gridcell"]/div[@role="button"]')
    selectable_days_not = calendar_days.by(have.attribute("aria-disabled"))
    selectable_days = calendar_days.by(not_(have.attribute("aria-disabled")))
    visit_time_input = s('//*[@data-testid="estabAddressSectionVisitTimeSelect"]')
    visit_time_options_box = floating_popup
    visit_time_options = visit_time_options_box.ss(".//ul/li")
    last_name = s("#person-name")
    payment = PaymentGateWay()

    def get_to_tier(self, visa_db, tier, num_visas=0):
        self.sign_agreement(tier, num_visas)
        self.select_location()
        self.select_inspection()
        self.next_step_button_location.click()
        self.goto_payment_button.click()
        self.payment.pay_successfully(visa_db)
        self.verify_created_request()
        self.back_to_perm_work_visa_button.click()
        self.history_tier_upgrades_table.row(1).should(be.visible)
        return self.history_tier_upgrades_table.cell(row=1, column="Request number").get(
            query.text
        )

    def create_balance_request(self, visa_db, visas_amount):
        sleep(4)  # TODO: remove when bug is fixed
        self.visas_amount_input_field.type(visas_amount)
        self.next_step_visas_amount_button.click()
        self.agree_agreement_checkbox.click()
        self.next_step_button_agreement.click()
        self.select_location()
        self.select_inspection()
        self.next_step_button_location.click()
        self.terms_agree_checkbox.click()
        self.goto_payment_button.click()
        self.payment.pay_successfully(visa_db)
        self.payment_request_sent.should(have_any_number())
        self.back_to_perm_work_visa_button.click()
        ref_number = self.balanse_request_table.cell(row=Numbers.ONE, column="Request number").get(
            query.text
        )
        return ref_number

    def select_location(self, index=1):
        self.location_dropdown.click()
        self.location_dropdown_options.element(index - 1).click()

    @allure.step("Verify request is created/sent")
    def verify_created_request(self):
        if self.payment_request_sent.with_(timeout=12).wait_until(be.visible):
            self.payment_request_sent.should(have_any_number())
        else:
            self.payment_request_approved.should(have_any_number())

    def select_inspection(self, days=Numbers.ONE, option=Numbers.ONE):
        self.select_visit_date(days=days)
        self.select_visit_time(option=option)

    def select_visit_date(self, days):
        command.js.scroll_into_view(self.last_name)
        self.visit_date_input.click()
        self.floating_popup.should(be.visible)
        select_date = datetime.date.today() + relativedelta(days=+days)
        self.selectable_days.element_by(have.exact_text(select_date.strftime("%-d"))).click()

    def select_visit_time(self, option):
        self.visit_time_input.click()
        self.visit_time_options_box.should(be.visible)
        self.visit_time_options.element(option - 1).click()

    def sign_agreement(self, tier, num_visas=0):
        s(self.TIER_CHECK_BOX.format(tier)).click()
        if tier == Numbers.FOUR:
            self.tier_4_input_field.type(num_visas)
            self.agree_checkbox.click()
        self.next_step_button_tier_select.click()
        command.js.scroll_into_view(self.program_agreement_section)
        self.agree_agreement_checkbox.click()
        self.next_step_button_agreement.click()
