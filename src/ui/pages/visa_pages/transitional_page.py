import datetime
import os

import allure
from dateutil.relativedelta import relativedelta
from selene.api import be, browser, have, not_, query, s, ss

from data.visa.constants import (
    INCREASE_ABSHER_MODAL_TITLE,
    INCREASE_ALLOWED_QUOTA,
    IS_SEASONAL_VISA_AVAILABLE,
    ISSUE_VISA_TEXT,
    PERM_WORK_VISA_DESCRIPTION,
    PERM_WORK_VISA_ELIGIBILITY_ERRORS,
    PERM_WORK_VISA_TITLE,
    SEASONAL_WORK_VISA_BLOCKED_TEXT,
    SEASONAL_WORK_VISA_DESCRIPTION,
    SEASONAL_WORK_VISA_TITLE,
    SERVICE_PAGE_BUTTON_TEXT,
    TEMP_WORK_VISA_DESCRIPTION,
    TEMPORARY_WORK_VISA_TITLE,
    TIER,
    TRANSITIONAL_CARDS_TITLE_TEXT,
    WORK_VISA_CARD_WARNING,
    DateFormats,
    Numbers,
)
from utils.assertion.selene_conditions import have_any_number, have_in_text_number
from utils.assertion.soft_assertions import soft_assert_list, soft_assert_text
from utils.helpers import get_session_variable


class TransitionalPage:
    cards_loading = s('//*[@data-testid="cardSkeleton"]')
    absher_loading = s('//*[@data-testid="abshereFundsSkeleton"]')
    absher_value = s('//*[@data-testid="absherFundsAmount"]')
    increase_absher_link = s('//*[@data-testid="absherFundsLink"]')
    perm_work_visa_card_title = s('//*[@data-testid="workVisaEligibilityCardTitle"]')
    temp_work_visa_card_title = s('//*[@data-testid="visitVisaEligibilityCardTitle"]')
    seasonal_work_visa_card_title = s('//*[@data-testid="seasonalVisaEligibilityCardTitle"]')
    card_titles = [
        perm_work_visa_card_title,
        temp_work_visa_card_title,
        seasonal_work_visa_card_title,
    ]
    perm_work_visa_description = s('//*[@data-testid="workVisaEligibilityCardDescription"]')
    perm_work_recruitment_quota = s('//*[@data-testid="workVisaEligibilityAllowedQuotaValue"]')
    perm_work_available_visas = s(
        '//*[@data-testid="workVisaEligibilityAvailableUnusedVisasValue"]'
    )
    perm_work_recruitment_quota_tier = s(
        '//*[@data-testid="workVisaEligibilityAllowedQuotaTierValue"]'
    )
    perm_work_visa_service_page_button = s(
        '//*[@data-testid="workVisaEligibilityGoToServicePageButton"]'
    )
    perm_work_visa_increase_quota_visa_button = s(
        '//*[@data-testid="workVisaEligibilityIncreaseAllowedQuotaButton"]'
    )
    perm_work_visa_issue_visa = s('//*[@data-testid="workVisaEligibilityIssueVisaButton"]')
    temp_work_visa_description = s('//*[@data-testid="visitVisaEligibilityCardDescription"]')
    temp_work_recruitment_quota = s('//*[@data-testid="visitVisaEligibilityAllowedQuotaValue"]')
    temp_work_available_visas = s(
        '//*[@data-testid="visitVisaEligibilityAvailableUnusedVisasValue"]'
    )
    temp_work_expire_date = s('//*[@data-testid="visitVisaEligibilityPackageExpirationDateValue"]')
    temp_work_visa_service_page_button = s(
        '//*[@data-testid="visitVisaEligibilityGoToServicePageButton"]'
    )
    temp_work_visa_issue_visa = s('//*[@data-testid="visitVisaEligibilityIssueVisaButton"]')
    seasonal_work_visa_description = s(
        '//*[@data-testid="seasonalVisaEligibilityCardDescription"]'
    )
    seasonal_work_visa_block_text = s('//*[@data-testid="seasonalVisaEligibilityCardDisabled"]')
    seasonal_work_recruitment_quota = s(
        '//*[@data-testid="seasonalVisaEligibilityAllowedQuotaValue"]'
    )
    seasonal_work_available_visas = s(
        '//*[@data-testid="seasonalVisaEligibilityAvailableUnusedVisasValue"]'
    )
    seasonal_work_visa_service_page_button = s(
        '//*[@data-testid="seasonalVisaEligibilityGoToServicePageButton"]'
    )
    seasonal_work_visa_issue_visa = s('//*[@data-testid="seasonalVisaEligibilityIssueVisaButton"]')
    allowance_period_banner = s(
        '//*[@data-testid="workVisaEligibilityAllowancePeriodEndingBadge"]'
    )
    global_warning_banner = s('//*[@data-testid="commonEligibilityWarningMessageCard"]')
    global_error_banner = s('//*[@data-testid="commonEligibilityErrorMessageCard"]')
    global_warning_banner_link = s('//*[@data-testid="commonEligibilityWarningMessageLink"]')
    global_error_banner_link = s('//*[@data-testid="commonEligibilityErrorMessageLink"]')
    modal_popup_window = s('//div[contains(@class, "Modal__ModalWrapper")]')
    modal_popup_window_error_list = ss('//div[contains(@class, "Modal__ModalWrapper")]//li')
    modal_popup_window_close_button = s('//div[contains(@class, "Modal__ModalWrapper")]//button')
    modal_popup_window_x_button = s('//div[contains(@class, "Modal__ModalWrapper")]//span')
    perm_work_visa_error_banner = s('//*[@data-testid="workVisaEligibilityErrorMessageCard"]')
    perm_work_visa_error_link = s('//*[@data-testid="workVisaEligibilityErrorMessageLink"]')
    temp_work_visa_error_banner = s('//*[@data-testid="visitVisaEligibilityErrorMessageCard"]')
    temp_work_visa_error_banner_link = s(
        '//*[@data-testid="visitVisaEligibilityErrorMessageLink"]'
    )
    banner_icon = './/*[name()="svg"]'
    account_number = s('//*[@data-testid="absherFundsDescription"]')
    perm_work_visa_warning_banner = s('//*[@data-testid="workVisaEligibilityWarningMessageCard"]')
    perm_work_visa_warning_banner_icon = s(
        '//*[@data-testid="workVisaEligibilityWarningMessageCard"]//*[name()="svg"]'
    )
    increase_absher_modal = s('//*[@data-testid="absherFundsModal"]')
    increase_absher_modal_title = increase_absher_modal.s(".//p")
    increase_absher_modal_x_button = increase_absher_modal.s(
        './/button[@aria-label="Close modal"]'
    )
    increase_absher_modal_close_button = increase_absher_modal.s('.//button[@aria-live="polite"]')
    perm_work_visa_card = s('//*[@data-testid="work-visa"]')
    temp_work_visa_card = s('//*[@data-testid="visit-visa"]')
    seasonal_work_visa_card = s('//*[@data-testid="seasonal-visa"]')
    perm_work_visa_card_exp_date = s('//*[@data-testid="workVisaEligibilityExpirationDateValue"]')
    # errors:
    error_message = s('//*[@data-testid="customErrorMessage"]')
    error_message_link = s('//*[@data-testid="customErrorMessageLink"]')
    error_message_modal = s('//*[@data-testid="dataLoadErrorModal"]')
    error_button = s('//button[text() = "Retry"]')
    error_messages = [error_message, error_message_link, error_message_modal, error_button]

    def page_is_loaded(self):
        for _ in range(3):
            self.cards_loading.should(be.hidden)
            self.absher_loading.should(be.hidden)
            if not self.any_errors_on_page():
                break
            browser.driver.refresh()

    @allure.step("Verifies transitional cards are loaded")
    def verify_cards_loaded(self):
        for _ in range(3):
            self.absher_loading.should(be.hidden)
            self.verify_cards_title_text(TRANSITIONAL_CARDS_TITLE_TEXT)
            if not self.any_errors_on_page():
                break
            browser.driver.refresh()

    @allure.step("Verifies absher balance part is loaded")
    def verify_absher_balance_loaded(self, expected_value):
        self.absher_value.should(have_in_text_number(expected_value))
        self.account_number.should(have_any_number())
        self.increase_absher_link.should(be.visible)

    @allure.step("Verify increase absher modal window is shown")
    def verify_increase_establishment_fund_modal(self):
        self.increase_absher_link.click()
        self.verify_increase_modal_elements()
        self.increase_absher_modal_x_button.click()
        self.increase_absher_modal.should(be.hidden)
        self.increase_absher_link.click()
        self.verify_increase_modal_elements()
        self.increase_absher_modal_close_button.click()
        self.increase_absher_modal.should(be.hidden)

    def verify_increase_modal_elements(self):
        self.increase_absher_modal.should(be.visible)
        soft_assert_text(self.increase_absher_modal_title, INCREASE_ABSHER_MODAL_TITLE)
        self.increase_absher_modal_x_button.should(be.visible).should(be.clickable)
        self.increase_absher_modal_close_button.should(be.visible).should(be.clickable)

    def verify_cards_title_text(self, cards_title_text):
        soft_assert_list(self.card_titles, cards_title_text)

    @allure.step("Verifies work visa card")
    def verify_work_visa_card_loaded(self, allowed_quota, available):
        soft_assert_text(self.perm_work_visa_description, PERM_WORK_VISA_DESCRIPTION)
        self.perm_work_recruitment_quota.should(have_in_text_number(allowed_quota))
        self.perm_work_available_visas.should(have_in_text_number(available))
        self.perm_work_visa_service_page_button.should(be.visible).should(be.clickable)
        self.perm_work_visa_issue_visa.should(be.visible).should(be.clickable)

    @allure.step("Verifies temporary work visa card")
    def verify_temporary_work_visa_card_loaded(self, allowed_quota, available, expire_date):
        self.temp_work_visa_description.should(have.text(TEMP_WORK_VISA_DESCRIPTION))
        self.temp_work_recruitment_quota.should(have_in_text_number(allowed_quota))
        self.temp_work_available_visas.should(have_in_text_number(available))
        self.temp_work_expire_date.should(have.text(expire_date))
        self.temp_work_visa_service_page_button.should(be.visible).should(be.clickable)
        self.temp_work_visa_issue_visa.should(be.visible).should(be.clickable)

    @allure.step("Verifies seasonal work visa card")
    def verify_seasonal_work_visa_card_loaded(self):
        self.seasonal_work_visa_description.should(have.text(SEASONAL_WORK_VISA_DESCRIPTION))
        if not get_session_variable(IS_SEASONAL_VISA_AVAILABLE):
            self.verify_seasonal_work_visa_card_seasonal_visa_not_available_case()
        else:
            self.verify_seasonal_work_visa_card_seasonal_visa_available_case()

    def verify_seasonal_work_visa_card_seasonal_visa_available_case(self):
        self.seasonal_work_visa_block_text.should(not_(have.text(SEASONAL_WORK_VISA_BLOCKED_TEXT)))
        self.seasonal_work_visa_service_page_button.should(be.visible)
        self.seasonal_work_visa_issue_visa.should(be.visible)
        self.seasonal_work_recruitment_quota.should(have.exact_text(str(Numbers.TEN)))
        self.seasonal_work_available_visas.should(have.exact_text(str(Numbers.NINE)))

    def verify_seasonal_work_visa_card_seasonal_visa_not_available_case(self):
        self.seasonal_work_visa_block_text.should(have.text(SEASONAL_WORK_VISA_BLOCKED_TEXT))
        self.seasonal_work_visa_service_page_button.should(be.hidden)
        self.seasonal_work_visa_issue_visa.should(be.hidden)
        self.seasonal_work_recruitment_quota.should(be.hidden)
        self.seasonal_work_available_visas.should(be.hidden)

    @allure.step("Verifies temporary work visa page open")
    def verify_temporary_work_visa_page_open(self):
        browser.should(not_(have.url_containing(os.getenv("WEB_URL"))))

    @allure.step("Verifies work visa allowance banner appears")
    def verify_work_visa_allowance_banner_appears(self, date):
        soft_assert_text(
            element=self.allowance_period_banner,
            element_name="Allowance period banner",
            text=date,
            timeout=3,
        )

    @allure.step("Verifies work visa allowance banner does not appear")
    def verify_work_visa_allowance_banner_not_appear(self):
        soft_assert_text(
            element=self.allowance_period_banner,
            element_name="Allowance period banner",
            expected=False,
        )

    @allure.step("Verifies global warning banner appears if expected")
    def verify_grace_period_ends_in_days_warning_banner_shown(self, days, expected=True):
        self.global_warning_banner_link.should(be.visible if expected else be.hidden)
        soft_assert_text(
            element=self.global_warning_banner,
            text=str(days),
            element_name="Global warning banner",
            expected=expected,
            timeout=3,
        )

    @allure.step(
        "Verifies global error banner appears with two errors and modal popup contains the same"
    )
    def verify_two_generic_errors_are_shown(self):
        self.global_error_banner.should(be.visible)
        self.global_error_banner.s(self.banner_icon).should(be.visible)
        self.global_error_banner_link.should(be.visible)
        soft_assert_text(self.global_error_banner, text=Numbers.TWO)
        self.global_error_banner_link.click()
        self.verify_modal_popup_window(error_list_size=Numbers.TWO)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.global_error_banner_link.click()
        self.verify_modal_popup_window(error_list_size=Numbers.TWO)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)
        self.global_error_banner_link.click()
        self.verify_modal_popup_window(error_list_size=Numbers.TWO)

    @allure.step("Verifies global error banner is not shown")
    def verify_no_generic_errors_are_shown(self):
        self.global_error_banner.should(be.hidden)
        self.global_error_banner_link.should(be.hidden)
        self.global_error_banner.s(self.banner_icon).should(be.hidden)

    @allure.step("Verify modal popup window")
    def verify_modal_popup_window(self, error_list_size):
        self.modal_popup_window.should(be.visible)
        self.modal_popup_window_close_button.should(be.visible)
        self.modal_popup_window_x_button.should(be.visible)
        self.modal_popup_window_error_list.should(have.size(error_list_size))

    @allure.step("Verify work visa error banner has text and amount of errors")
    def verify_work_visa_error_shown(self, text):
        self.perm_work_visa_error_banner.should(be.visible)
        self.perm_work_visa_error_banner.s(self.banner_icon).should(be.visible)
        soft_assert_text(self.perm_work_visa_error_banner, text=text)

    @allure.step("Verifies work visa card no errors banner is shown")
    def verify_no_visa_card_errors_are_shown(self):
        self.perm_work_visa_error_banner.should(be.hidden)
        self.perm_work_visa_error_banner.s(self.banner_icon).should(be.hidden)

    @allure.step("Verify temporary work visa error banner has text and amount of errors")
    def verify_temp_work_visa_error_shown(self, text, error_quantity):
        self.temp_work_visa_error_banner.should(be.visible)
        self.temp_work_visa_error_banner.s(self.banner_icon).should(be.visible)
        self.temp_work_visa_error_banner_link.should(be.visible)
        self.temp_work_visa_error_banner_link.should(be.clickable)
        soft_assert_text(self.temp_work_visa_error_banner, text=text)
        self.temp_work_visa_error_banner_link.click()
        self.verify_modal_popup_window(error_quantity)

    @allure.step("Verifies temporary work visa card no errors banner is shown")
    def verify_temp_work_visa_no_error_shown(self):
        self.temp_work_visa_error_banner.should(be.hidden)
        self.temp_work_visa_error_banner.s(self.banner_icon).should(be.hidden)
        self.temp_work_visa_error_banner_link.should(be.hidden)

    @allure.step("Verifies account number is shown")
    def verify_account_number_on_page(self):
        self.account_number.should(have_any_number())

    @allure.step("Verifies work visa warning is shown")
    def verify_perm_work_visa_warning(self):
        self.perm_work_visa_warning_banner.should(be.visible)
        self.perm_work_visa_warning_banner.s(self.banner_icon).should(be.visible)
        soft_assert_text(
            self.perm_work_visa_increase_quota_visa_button,
            INCREASE_ALLOWED_QUOTA,
            element_name="Issue visa button",
        )
        self.perm_work_visa_warning_banner.should(have.text(WORK_VISA_CARD_WARNING))
        self.perm_work_visa_increase_quota_visa_button.should(be.visible).should(be.clickable)
        self.perm_work_visa_increase_quota_visa_button.s(self.banner_icon).should(be.hidden)

    @allure.step("Verifies generic error is shown")
    def verify_generic_error_shown(self):
        self.global_error_banner.should(be.visible)
        self.global_error_banner.s(self.banner_icon).should(be.visible)
        error_text = self.global_error_banner.get(query.text)
        self.perm_work_visa_issue_visa.element(self.banner_icon).should(be.visible).should(
            be.clickable
        )
        self.perm_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.ONE)
        self.modal_popup_window_error_list.first.should(have.text(error_text))
        self.modal_popup_window_close_button.click()
        self.temp_work_visa_issue_visa.element(self.banner_icon).should(be.visible).should(
            be.clickable
        )
        self.temp_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.ONE)
        self.modal_popup_window_error_list.first.should(have.text(error_text))

    @allure.step("Verifies generic error permanent work visa error are shown")
    def verify_generic_error_and_perm_visa_error_shown(self):
        self.global_error_banner.should(be.visible)
        self.global_error_banner_link.should(be.hidden)
        self.global_error_banner.s(self.banner_icon).should(be.visible)
        error_text = self.global_error_banner.get(query.text)
        self.perm_work_visa_error_banner.should(be.visible)
        self.perm_work_visa_error_banner.should(
            have.text(PERM_WORK_VISA_ELIGIBILITY_ERRORS.format(Numbers.TWO))
        )
        self.perm_work_visa_issue_visa.element(self.banner_icon).should(be.visible).should(
            be.clickable
        )
        self.perm_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_error_list.first.should(have.text(error_text))
        self.modal_popup_window_error_list.second.should(have.text(error_text))
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)
        self.temp_work_visa_issue_visa.element(self.banner_icon).should(be.visible).should(
            be.clickable
        )
        self.temp_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.ONE)
        self.modal_popup_window_error_list.first.should(have.text(error_text))

    @allure.step("Verifies two generic errors and two permanent work visa errors are shown")
    def verify_two_generic_error_and_two_perm_visa_errors_shown(self):
        self.global_error_banner.should(be.visible)
        self.global_error_banner_link.should(be.visible)
        self.global_error_banner.s(self.banner_icon).should(be.visible)
        self.global_error_banner_link.click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.global_error_banner_link.click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_x_button.click()
        self.perm_work_visa_error_banner.should(be.visible)
        self.perm_work_visa_error_banner.s(self.banner_icon).should(be.visible)
        self.perm_work_visa_error_link.click()
        self.verify_modal_popup_window(Numbers.FOUR)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_error_link.click()
        self.verify_modal_popup_window(Numbers.FOUR)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_issue_visa.element(self.banner_icon).should(be.visible).should(
            be.clickable
        )
        self.perm_work_visa_error_link.click()
        self.verify_modal_popup_window(Numbers.FOUR)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_error_link.click()
        self.verify_modal_popup_window(Numbers.FOUR)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_error_link.should(be.visible).should(be.clickable)
        self.temp_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.temp_work_visa_issue_visa.element(self.banner_icon).click()
        self.verify_modal_popup_window(Numbers.TWO)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)

    @allure.step("Verify permanent work visa card")
    def verify_perm_work_visa_card(
        self, tier=TIER.ONE, recruitment_quota=Numbers.FOUR, available=Numbers.THREE
    ):
        self.perm_work_visa_card.should(be.visible)
        soft_assert_text(
            self.perm_work_visa_card_title,
            PERM_WORK_VISA_TITLE,
            element_name="Perm work visa card title",
        )
        soft_assert_text(
            self.perm_work_visa_description,
            PERM_WORK_VISA_DESCRIPTION,
            element_name="Perm work visa card description",
        )
        soft_assert_text(
            self.perm_work_recruitment_quota,
            recruitment_quota,
            element_name="Perm recruitment quota",
        )
        soft_assert_text(
            self.perm_work_available_visas, available, element_name="Perm available visas"
        )
        soft_assert_text(self.perm_work_recruitment_quota_tier, tier, element_name="Current tier")
        soft_assert_text(
            self.perm_work_visa_service_page_button,
            SERVICE_PAGE_BUTTON_TEXT,
            "Service page in perm work visa card ",
        )
        soft_assert_text(
            self.perm_work_visa_issue_visa,
            ISSUE_VISA_TEXT,
            "Issue visa button perm work visa card",
        )
        self.perm_work_visa_issue_visa.should(be.visible).should(be.clickable)
        self.perm_work_visa_service_page_button.should(be.visible).should(be.clickable)

    @allure.step("Verify temporary work visa card")
    def verify_temp_work_visa_card(self):
        end_date = datetime.date.today() + relativedelta(months=+6)
        self.temp_work_visa_card.should(be.visible)
        soft_assert_text(
            self.temp_work_visa_card_title,
            TEMPORARY_WORK_VISA_TITLE,
            element_name="Temp work visa card title",
        )
        soft_assert_text(
            self.temp_work_visa_description,
            TEMP_WORK_VISA_DESCRIPTION,
            element_name="Temp work visa card description",
        )
        soft_assert_text(
            self.temp_work_recruitment_quota,
            Numbers.ONE_HUNDRED,
            element_name="Temp recruitment quota",
        )
        soft_assert_text(
            self.temp_work_available_visas,
            Numbers.NINETY_NINE,
            element_name="Temp available visas",
        )
        soft_assert_text(
            self.temp_work_expire_date,
            end_date.strftime(DateFormats.DD_MM_YYYY),
            element_name="Temp visas expiration date",
        )
        soft_assert_text(
            self.temp_work_visa_service_page_button,
            SERVICE_PAGE_BUTTON_TEXT,
            "Service page in temp work visa card",
        )
        soft_assert_text(
            self.temp_work_visa_issue_visa,
            ISSUE_VISA_TEXT,
            "Issue visa button in temp work visa card",
        )
        self.temp_work_visa_service_page_button.should(be.visible).should(be.clickable)
        self.temp_work_visa_issue_visa.should(be.visible).should(be.clickable)

    @allure.step("Verify seasonal work visa card")
    def verify_seasonal_work_visa_card(self):
        self.seasonal_work_visa_card.should(be.visible)
        soft_assert_text(
            self.seasonal_work_visa_card_title,
            SEASONAL_WORK_VISA_TITLE,
            element_name="Temp work visa card title",
        )
        soft_assert_text(
            self.seasonal_work_visa_description,
            SEASONAL_WORK_VISA_DESCRIPTION,
            element_name="Temp work visa card descrition",
        )
        soft_assert_text(
            self.seasonal_work_recruitment_quota,
            Numbers.TEN,
            element_name="Temp recruitment quota",
        )
        soft_assert_text(
            self.seasonal_work_available_visas, Numbers.NINE, element_name="Temp available visas"
        )
        self.seasonal_work_visa_service_page_button.should(be.visible).should(be.clickable)
        self.seasonal_work_visa_issue_visa.should(be.visible).should(be.clickable)

    @allure.step("Verify allowed quota tier is shown")
    def verify_allowed_quota_tier_shown(self):
        self.perm_work_recruitment_quota_tier.should(have.text(TIER.ONE))

    @allure.step("Verify increase allowed quota button")
    def verify_perm_work_visa_increase_allowed_quota_button(self):
        self.perm_work_visa_increase_quota_visa_button.should(have.text(INCREASE_ALLOWED_QUOTA))

    @allure.step("Verify permanent work visa error banner is shown")
    def verify_perm_work_visa_error_shown(self):
        self.perm_work_visa_error_banner.should(be.visible)
        self.perm_work_visa_error_banner.s(self.banner_icon).should(be.visible)
        self.perm_work_visa_issue_visa.element(self.banner_icon).should(be.visible)
        self.perm_work_visa_issue_visa.click()
        self.verify_modal_popup_window(Numbers.ONE)
        self.modal_popup_window_close_button.click()
        self.modal_popup_window.should(be.hidden)
        self.perm_work_visa_issue_visa.click()
        self.verify_modal_popup_window(Numbers.ONE)
        self.modal_popup_window_x_button.click()
        self.modal_popup_window.should(be.hidden)

    def verify_no_balance_expiration_date_perm_visa_card(self):
        self.perm_work_visa_card_exp_date.should(be.hidden)

    def verify_balance_expiration_date_perm_visa_card(self):
        exp_date = datetime.date.today() + relativedelta(years=+1)
        self.perm_work_visa_card_exp_date.should(be.visible)
        self.perm_work_visa_card_exp_date.should(
            have.exact_text(exp_date.strftime(DateFormats.DD_MM_YYYY))
        )

    def any_errors_on_page(self):
        return any(message.matching(be.visible) for message in self.error_messages)
