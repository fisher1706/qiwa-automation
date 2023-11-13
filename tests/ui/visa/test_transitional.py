import datetime

import allure
import pytest
from dateutil.relativedelta import relativedelta
from selene.support.shared import browser

from data.visa.constants import (
    BR_ACCEPTED,
    BR_EXPIRED,
    BR_INACTIVE,
    BR_NEW,
    BR_REFUNDED,
    BR_REJECTED,
    BR_TERMINATED,
    BR_WAITING,
    ERROR_CODE,
    ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT,
    WORK_VISA_CARD_ZERO_QUOTA_ERROR,
    DateFormats,
    Numbers,
    VisaType,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.helpers import join_codes

case_id = project(TestmoProject.VISAS)

@case_id(21267)
@allure.title('Test verifies transitional page opens absher balance part')
def test_verify_transitional_page_absher_balance(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, absher_balance=Numbers.TEN_THOUSAND)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_absher_balance_loaded(Numbers.TEN_THOUSAND)
    qiwa.transitional.verify_increase_establishment_fund_modal()


@case_id(22101)
@allure.title('Test verifies balances on the transitional page')
def test_verify_balances_on_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_card()
    qiwa.transitional.verify_temp_work_visa_card()
    qiwa.transitional.verify_seasonal_work_visa_card()


@case_id(22170)
@allure.title('Test verifies transitional page opens')
def test_verify_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, absher_balance=Numbers.TEN_THOUSAND)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_cards_loaded()
    qiwa.transitional.verify_absher_balance_loaded(Numbers.TEN_THOUSAND)


@case_id(22101)
@allure.title('Test verifies work visa card is loaded')
def test_verify_work_visa_card(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, immediate_balance=Numbers.ONE_HUNDRED)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_card_loaded(allowed_quota=Numbers.ONE_HUNDRED,
                                                   available=Numbers.NINETY_NINE)


@case_id(22101)
@allure.title('Test verifies temporary work visa card is loaded')
def test_verify_temporary_work_visa_card(visa_mock):
    end_date = datetime.date.today() + relativedelta(months=+11)
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            visit_visa_balance=Numbers.ONE_HUNDRED,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_temporary_work_visa_card_loaded(allowed_quota=Numbers.ONE_HUNDRED,
                                                             available=Numbers.NINETY_NINE,
                                                             expire_date=end_date.strftime(DateFormats.DD_MM_YYYY))


@case_id(22101)
@allure.title('Test verifies seasonal work visa card is loaded')
def test_verify_seasonal_work_visa_card(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_seasonal_work_visa_card_loaded()


@case_id(22102)
@allure.title('Test verifies work visa page is opened')
def test_verify_work_visa_page_open(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()


@allure.title('Test verifies temporary work visa page is opened')
def test_verify_temporary_work_visa_page_open(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.temp_work_visa_service_page_button.click()
    qiwa.transitional.verify_temporary_work_visa_page_open()


@case_id(25575)
@allure.title('Test verifies work visa card contains allowance period banner')
def test_verify_work_visa_allowance_period_banner_appears(visa_mock):
    end_date = datetime.date.today() + relativedelta(months=+6)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_appears(date=end_date.strftime(DateFormats.DD_MM_YYYY))


@allure.title('Test verifies work visa card does not contain allowance period banner, when company in expansion')
def test_verify_work_visa_allowance_period_banner_not_appear_in_expansion(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_not_appear()


@case_id(41423)
@allure.title('Test verifies work visa card does not contain allowance period banner, when company not started GP')
def test_verify_work_visa_allowance_period_banner_not_appear_not_in_grace_period(visa_mock):
    start_date = datetime.date.today() + relativedelta(days=+1)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_start_date=start_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_not_appear()


@case_id(25575)
@pytest.mark.parametrize("days", [1, 14, 15])
@allure.title('Test verifies global warning is shown if 1, 14 days to the end of GP and not shown if >=15')
def test_verify_global_warning_shown_depending_on_gp_days_left(visa_mock, days):
    end_date = datetime.date.today() + relativedelta(days=+days)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_grace_period_ends_in_days_warning_banner_shown(days=days, expected=days < 15)


@case_id(25571)
@allure.title('Test verifies global two errors are shown')
def test_verify_two_generic_errors_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_two_generic_errors_are_shown()


@allure.title('Test verifies global no errors are shown')
def test_verify_no_generic_errors_shown(visa_mock):
    visa_mock.setup_company()
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_generic_errors_are_shown()


@case_id(25575)
@allure.title('Test verifies global no warning are shown, when there are generic errors')
def test_verify_no_generic_warning_shown_if_generic_errors(visa_mock):
    end_date = datetime.date.today() + relativedelta(days=+14)
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_grace_period_ends_in_days_warning_banner_shown(days=14, expected=False)
    qiwa.transitional.verify_two_generic_errors_are_shown()


@case_id(25571)
@allure.title('Test verifies one error in work visa card')
def test_verify_work_visa_one_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            expan_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            immediate_balance=Numbers.ZERO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.ZERO)


@allure.title('Test verifies no errors in work visa card')
def test_verify_work_visa_no_errors(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_visa_card_errors_are_shown()


@case_id(25571)
@allure.title('Test verifies two errors in work visa card')
def test_verify_work_visa_two_errors(visa_mock):
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO)


@allure.title('Test verifies two errors in work visa card in case when immediate balance is zero')
def test_verify_work_visa_two_errors_balance_zero(visa_mock):
    visa_mock.setup_company(immediate_balance=Numbers.ZERO,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO)


@allure.title('Test verifies one error in temporary work visa card')
def test_verify_temp_work_visa_one_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            visit_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_error_shown(Numbers.TWO, Numbers.TWO)


@allure.title('Test verifies no errors in temporary work visa card')
def test_verify_temp_work_visa_no_error(visa_mock):
    visa_mock.setup_company()
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_no_error_shown()


@case_id(25571)
@allure.title('Test verifies errors in temporary work visa card concatenates with generic errors')
def test_verify_temp_work_visa_error_and_generic_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            visit_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_error_shown(Numbers.FOUR, Numbers.FOUR)


@case_id(25569)
@allure.title('Test verifies warning in work visa card is shown')
def test_verify_work_visa_warning_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT, immediate_balance=Numbers.ZERO)
    visa_mock.change_visa_quantity(Numbers.ONE, Numbers.ZERO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_warning()
    qiwa.transitional.verify_perm_work_visa_increase_allowed_quota_button()


@case_id(25577)
@allure.title('Test verifies zero quota error in work visa card')
def test_verify_work_visa_one_error_balance_zero(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, immediate_balance=Numbers.ZERO)
    visa_mock.change_visa_quantity(Numbers.ONE, Numbers.ZERO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(WORK_VISA_CARD_ZERO_QUOTA_ERROR)


@allure.title('Test verifies there is no other visas on work visa page')
def test_verify_no_other_visas_requests(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.other_visas_tab.click()
    qiwa.work_visa.verify_other_visas_table_empty()


@allure.title('Test verifies there is no permanent visas on work visa page')
def test_verify_no_permanent_visas_requests(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.permanent_visas_tab.click()
    qiwa.work_visa.verify_permanent_visas_table_empty()


@case_id(25571)
@allure.title('Test verifies generic one error is shown')
def test_verify_one_generic_error_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_generic_error_shown()


@case_id(25571)
@allure.title('Test verifies one generic and permanent work visa errors are shown')
def test_verify_generic_and_perm_work_visa_error_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE)
                            )
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_generic_error_and_perm_visa_error_shown()


@case_id(25571)
@allure.title('Test verifies errors in permanent work visa card concatenates with generic errors')
def test_verify_perm_work_visa_error_and_generic_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_two_generic_error_and_two_perm_visa_errors_shown()


@case_id(25563)
@allure.title('Test verifies allowed quota tier is shown in case when company is in establishment phase')
def test_verify_allowed_quota_tier_in_establishment_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_allowed_quota_tier_shown()


@case_id(25571)
@allure.title('Test verifies general eligibility errors on the transitional page')
def test_verify_general_eligibility_errors_on_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_generic_error_shown()
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_two_generic_errors_are_shown()
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_error_shown()
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE)
                            )
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_generic_error_and_perm_visa_error_shown()
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_two_generic_error_and_two_perm_visa_errors_shown()


@pytest.mark.parametrize("visa_type", [VisaType.EXPANSION, VisaType.ESTABLISHMENT])
@allure.title('Test verifies there is visa request (expansion, establishment) in permanent work visa page')
def test_verify_perm_work_visa_request(visa_mock, visa_type):
    visa_mock.setup_company(visa_type=visa_type)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_issue_visa.click()
    qiwa.issue_visa.verify_issue_visa_page_open()
    ref_number = qiwa.issue_visa.create_perm_visa_request()
    qiwa.work_visa.verify_perm_work_visa_request(ref_number)


@case_id(6347)
@allure.title('Test verifies permanent work visa request (pdf) in establishing phase')
def test_verify_perm_work_visa_request_establishment_pdf(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_issue_visa.click()
    qiwa.issue_visa.verify_issue_visa_page_open()
    ref_number = qiwa.issue_visa.create_perm_visa_request()
    qiwa.work_visa.verify_perm_work_visa_request_pdf(ref_number)
    qiwa.work_visa.view_action.click()
    qiwa.visa_request.verify_visa_request_page_open()
    qiwa.visa_request.verify_details_in_pdf(ref_number)


@case_id(25564)
@allure.title("Test verifies permanent work visa work visa card's errors appearance (internal error) [establishment]")
def test_verify_perm_work_visa_card_internal_error(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.increase_quota_establishment_button.click()
    ref_number = qiwa.increase_quota.get_to_tier(visa_db, Numbers.FOUR, Numbers.ONE_HUNDRED)
    visa_mock.change_balance_request(ref_number, Numbers.ONE, Numbers.ONE)
    visa_mock.change_visa_quantity(Numbers.FOUR, Numbers.ZERO)
    qiwa.work_visa.return_to_transitional_page()
    qiwa.transitional.verify_perm_work_visa_error_shown()


@case_id(25576)
@allure.title("Test verifies expiration of exceptional balance on perm work visa transitional page")
def test_verify_perm_work_visa_card_expiration_balance(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.increase_quota_button.click()
    ref_num = qiwa.increase_quota.create_balance_request(visa_db, Numbers.ONE_THOUSAND)
    qiwa.work_visa.return_to_transitional_page()
    qiwa.transitional.verify_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.TWO, Numbers.TWO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.THREE, Numbers.THREE)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.FOUR, Numbers.FOUR)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()


@allure.title('Test verifies permanent work visa request (pdf) in expansion phase')
def test_verify_perm_work_visa_request_expansion_pdf(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.increase_quota_button.click()
    ref_num = qiwa.increase_quota.create_balance_request(visa_db, Numbers.ONE_THOUSAND)
    qiwa.work_visa.verify_perm_work_visa_request_pdf(ref_num, VisaType.EXPANSION)
    qiwa.work_visa.view_action.click()
    qiwa.balnce_request.verify_page_is_open()
    qiwa.balnce_request.verify_pdf_is_downloaded()


@case_id(25470)
@allure.title('Test verifies statuses of tier upgrades table for establishment flow')
def test_verify_statuses_tier_upgrades_table_establishment_flow(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.increase_quota_establishment_button.click()
    ref_number = qiwa.increase_quota.get_to_tier(visa_db, Numbers.FOUR, Numbers.ONE_HUNDRED)
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_WAITING)

    visa_mock.change_balance_request(ref_number, status_id=BR_ACCEPTED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_ACCEPTED)

    visa_mock.change_balance_request(ref_number, status_id=BR_INACTIVE.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_INACTIVE)

    visa_mock.change_balance_request(ref_number, status_id=BR_REJECTED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_REJECTED)

    visa_mock.change_balance_request(ref_number, status_id=BR_REFUNDED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_REFUNDED)

    visa_mock.change_balance_request(ref_number, status_id=BR_EXPIRED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_EXPIRED)

    visa_mock.change_balance_request(ref_number, status_id=BR_TERMINATED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_TERMINATED)

    visa_mock.change_balance_request(ref_number, status_id=BR_NEW.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_tier_upgrade_status(ref_number, BR_NEW)


@case_id(25465)
@allure.title('Test verifies statuses of tier upgrades table for establishment flow')
def test_verify_statuses_exceptional_balance_requests_table_expansion_flow(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.increase_quota_button.click()
    ref_number = qiwa.increase_quota.create_balance_request(visa_db, Numbers.ONE_THOUSAND)
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_ACCEPTED)

    visa_mock.change_balance_request(ref_number, status_id=BR_INACTIVE.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_INACTIVE)

    visa_mock.change_balance_request(ref_number, status_id=BR_INACTIVE.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_INACTIVE)

    visa_mock.change_balance_request(ref_number, status_id=BR_WAITING.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_WAITING)

    visa_mock.change_balance_request(ref_number, status_id=BR_REJECTED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_REJECTED)

    visa_mock.change_balance_request(ref_number, status_id=BR_REFUNDED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_REFUNDED)

    visa_mock.change_balance_request(ref_number, status_id=BR_EXPIRED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_EXPIRED)

    visa_mock.change_balance_request(ref_number, status_id=BR_TERMINATED.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_TERMINATED)

    visa_mock.change_balance_request(ref_number, status_id=BR_NEW.id)
    browser.driver.refresh()
    qiwa.work_visa.verify_balance_request_status(ref_number, BR_NEW)


@case_id(25572)
@allure.title('Test verifies top navigation tabs/links scrolling work')
def test_verify_top_navigation_block_perm_work_visa_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.return_to_transitional_page()
    qiwa.transitional.verify_cards_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_top_navigation_tabs_work()


@case_id(25573)
@allure.title('Test verifies absher balance section on permanent work visa page')
def test_verify_absher_balance_perm_work_visa_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_absher_balance_section()


@case_id(25574)
@allure.title('Test verifies allowed quota section on permanent work visa page')
def test_verify_allowed_quota_perm_work_visa_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_allowed_quota_section_expansion()
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.work_visa.verify_allowed_quota_section_establishment()


@case_id(25565)
@allure.title('Test verifies buttons on permanent work visa page (expansion)')
def test_validation_issue_visa_increase_allowed_quota_buttons_expansion(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_buttons_expansion(issue_enabled=False, increase_enabled=False)
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    browser.driver.refresh()
    qiwa.work_visa.verify_buttons_expansion(issue_enabled=True, increase_enabled=True)
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            expansion_balance_validation_code = join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.work_visa.verify_buttons_expansion(issue_enabled=True, increase_enabled=False)


@case_id(41431)
@allure.title('Test verifies buttons on permanent work visa page (establishing)')
def test_validation_issue_visa_increase_allowed_quota_buttons_establishing(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_buttons_establishment(issue_enabled=False, increase_enabled=False)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.work_visa.verify_buttons_establishment(issue_enabled=True, increase_enabled=True)


@case_id(46648)
@allure.title('Test verifies allowance period block permanent work visa request')
def test_verify_allowance_period_block_perm_work_visa_request(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.verify_allowance_period_block_perm_work_visa_request(allowance_started=True)
    start_date = datetime.date.today() + relativedelta(days=+1)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_start_date=start_date.strftime(DateFormats.YYYYMMDD))
    browser.driver.refresh()
    qiwa.work_visa.verify_allowance_period_block_perm_work_visa_request(allowance_started=False)


@case_id(46947)
@allure.title("Test verifies errors appearance (internal error) on permanent work visa page [expansion]")
def test_verify_internal_errors_perm_work_visa_page_expansion(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, immediate_balance=Numbers.ZERO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_error_banner(ISSUE_VISA_MODAL_CONTENT_EXPANSION_TEXT)
    qiwa.work_visa.verify_expansion_balance_zero_buttons_behavior()

@case_id(46945)
@allure.title("Test verifies errors appearance (internal error) on permanent work visa page [establishing]")
def test_verify_internal_tier_balance_validations_perm_work_visa_page(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    visa_mock.change_visa_quantity(Numbers.ONE, Numbers.ZERO)
    browser.driver.refresh()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_issue_perm_work_visa_blocked()
    qiwa.work_visa.increase_quota_establishment_button.click()
    ref_number = qiwa.increase_quota.get_to_tier(visa_db, Numbers.FOUR, Numbers.ONE_HUNDRED)
    visa_mock.change_balance_request(ref_number, Numbers.ONE, Numbers.ONE)
    browser.driver.refresh()
    qiwa.work_visa.verify_increase_perm_work_visa_quota_blocked()
    visa_mock.change_visa_quantity(Numbers.FOUR, Numbers.ZERO)
    browser.driver.refresh()
    qiwa.work_visa.verify_increase_perm_work_visa_quota_and_issue_blocked()
