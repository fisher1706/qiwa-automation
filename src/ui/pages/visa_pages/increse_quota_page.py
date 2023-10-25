from time import sleep

import allure
from selene.api import be, command, query, s, ss

from data.visa.constants import Numbers
from src.ui.components.raw.table import Table
from src.ui.pages.visa_pages.base_page import BasePage
from utils.assertion.selene_conditions import have_any_number


class IncreaseQuotaPage(BasePage):
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

    def get_to_tier(self, visa_db, tier, num_visas=0):
        s(self.TIER_CHECK_BOX.format(tier)).click()
        if tier == Numbers.FOUR:
            self.tier_4_input_field.type(num_visas)
            self.agree_checkbox.click()
        self.next_step_button_tier_select.click()
        command.js.scroll_into_view(self.program_agreement_section)
        self.agree_agreement_checkbox.click()
        self.next_step_button_agreement.click()
        self.select_location()
        self.goto_payment_button.click()
        self.pay_successfully(visa_db)
        self.verify_created_request()
        self.back_to_perm_work_visa_button.click()
        self.history_tier_upgrades_table.row(1).should(be.visible)
        return self.history_tier_upgrades_table.cell(row=1, column="Request number").get(
            query.text
        )

    def create_balance_request(self, visa_db, visas_amount):
        sleep(3)  # TODO: remove when bug is fixed
        self.visas_amount_input_field.type(visas_amount)
        self.next_step_visas_amount_button.click()
        self.agree_agreement_checkbox.click()
        self.next_step_button_agreement.click()
        self.select_location()
        self.terms_agree_checkbox.click()
        self.goto_payment_button.click()
        self.pay_successfully(visa_db)
        self.payment_request_sent.should(have_any_number())
        self.back_to_perm_work_visa_button.click()
        ref_number = self.balanse_request_table.cell(row=Numbers.ONE, column="Request number").get(
            query.text
        )
        return ref_number

    def select_location(self, index=1):
        self.location_dropdown.click()
        self.location_dropdown_options.element(index).click()
        self.next_step_button_location.click()

    @allure.step("Verify request is created/sent")
    def verify_created_request(self):
        if self.payment_request_sent.with_(timeout=12).wait_until(be.visible):
            self.payment_request_sent.should(have_any_number())
        else:
            self.payment_request_approved.should(have_any_number())
