import datetime

import allure
import pytest
from dateutil.relativedelta import relativedelta

from data.visa.constants import (
    ERROR_CODE,
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
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_absher_balance_loaded(Numbers.TEN_THOUSAND)
    qiwa.transitional.verify_increase_establishment_fund_modal()

@case_id(22101)
@allure.title('Test verifies balances on the transitional page')
def test_verify_balances_on_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_card()
    qiwa.transitional.verify_temp_work_visa_card()
    qiwa.transitional.verify_seasonal_work_visa_card()

@case_id(22170)
@allure.title('Test verifies transitional page opens')
def test_verify_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, absher_balance=Numbers.TEN_THOUSAND)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_cards_loaded()
    qiwa.transitional.verify_absher_balance_loaded(Numbers.TEN_THOUSAND)


@allure.title('Test verifies work visa card is loaded')
def test_verify_work_visa_card(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, immediate_balance=Numbers.ONE_HUNDRED)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_card_loaded(allowed_quota=Numbers.ONE_HUNDRED,
                                                   available=Numbers.NINTY_NINE)


@allure.title('Test verifies temporary work visa card is loaded')
def test_verify_temporary_work_visa_card(visa_mock):
    end_date = datetime.date.today() + relativedelta(months=+11)
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            visit_visa_balance=Numbers.ONE_HUNDRED,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_temporary_work_visa_card_loaded(allowed_quota=Numbers.ONE_HUNDRED,
                                                             available=Numbers.NINTY_NINE,
                                                             expire_date=end_date.strftime(DateFormats.DD_MM_YYYY))


@allure.title('Test verifies seasonal work visa card is loaded')
def test_verify_seasonal_work_visa_card(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_seasonal_work_visa_card_loaded()

@case_id(22102)
@allure.title('Test verifies work visa page is opened')
def test_verify_work_visa_page_open(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()


@allure.title('Test verifies temporary work visa page is opened')
def test_verify_temporary_work_visa_page_open(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.temp_work_visa_service_page_button.click()
    qiwa.transitional.verify_temporary_work_visa_page_open()


@allure.title('Test verifies work visa card contains allowance period banner')
def test_verify_work_visa_allowance_period_banner_appears(visa_mock):
    end_date = datetime.date.today() + relativedelta(months=+6)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_appears(date=end_date.strftime(DateFormats.DD_MM_YYYY))


@allure.title('Test verifies work visa card does not contain allowance period banner, when company in expansion')
def test_verify_work_visa_allowance_period_banner_not_appear_in_expansion(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_not_appear()


@allure.title('Test verifies work visa card does not contain allowance period banner, when company not started GP')
def test_verify_work_visa_allowance_period_banner_not_appear_not_in_grace_period(visa_mock):
    start_date = datetime.date.today() + relativedelta(days=+1)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_start_date=start_date.strftime(DateFormats.YYYYMMDD))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_allowance_banner_not_appear()

@case_id(25575)
@pytest.mark.parametrize("days", [1, 14, 15])
@allure.title('Test verifies global warning is shown if 1, 14 days to the end of GP and not shown if >=15')
def test_verify_global_warning_shown_depending_on_gp_days_left(visa_mock, days):
    end_date = datetime.date.today() + relativedelta(days=+days)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_grace_period_ends_in_days_warning_banner_shown(days=days, expected=days < 15)


@allure.title('Test verifies global two errors are shown')
def test_verify_two_generic_errors_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_two_generic_errors_are_shown()


@allure.title('Test verifies global no errors are shown')
def test_verify_no_generic_errors_shown(visa_mock):
    visa_mock.setup_company()
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_generic_errors_are_shown()

@case_id(25575)
@allure.title('Test verifies global no warning are shown, when there are generic errors')
def test_verify_no_generic_warning_shown_if_generic_errors(visa_mock):
    end_date = datetime.date.today() + relativedelta(days=+14)
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            allowance_end_date=end_date.strftime(DateFormats.YYYYMMDD))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_grace_period_ends_in_days_warning_banner_shown(days=14, expected=False)
    qiwa.transitional.verify_two_generic_errors_are_shown()


@allure.title('Test verifies one error in work visa card')
def test_verify_work_visa_one_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION,
                            expan_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            immediate_balance=Numbers.ZERO)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.ZERO, Numbers.ONE)


@allure.title('Test verifies no errors in work visa card')
def test_verify_work_visa_no_errors(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_visa_card_errors_are_shown()


@allure.title('Test verifies two errors in work visa card')
def test_verify_work_visa_two_errors(visa_mock):
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO, Numbers.TWO)


@allure.title('Test verifies two errors in work visa card in case when immediate balance is zero')
def test_verify_work_visa_two_errors_balance_zero(visa_mock):
    visa_mock.setup_company(immediate_balance=Numbers.ZERO,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO, Numbers.TWO)


@allure.title('Test verifies one error in temporary work visa card')
def test_verify_temp_work_visa_one_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            visit_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_error_shown(Numbers.TWO, Numbers.TWO)


@allure.title('Test verifies no errors in temporary work visa card')
def test_verify_temp_work_visa_no_error(visa_mock):
    visa_mock.setup_company()
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_no_error_shown()


@allure.title('Test verifies errors in temporary work visa card concatenates with generic errors')
def test_verify_temp_work_visa_error_and_generic_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            visit_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_temp_work_visa_error_shown(Numbers.FOUR, Numbers.FOUR)

@case_id(25569)
@allure.title('Test verifies warning in work visa card is shown')
def test_verify_work_visa_warning_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT, immediate_balance=Numbers.ZERO)
    visa_mock.change_visa_quantity(Numbers.ONE, Numbers.ZERO)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_warning()
    qiwa.transitional.verify_perm_work_visa_increase_allowed_quota_button()


@allure.title('Test verifies zero quota error in work visa card')
def test_verify_work_visa_one_error_balance_zero(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION, immediate_balance=Numbers.ZERO)
    visa_mock.change_visa_quantity(Numbers.ONE, Numbers.ZERO)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(WORK_VISA_CARD_ZERO_QUOTA_ERROR, Numbers.ONE)


@allure.title('Test verifies there is no other visas on work visa page')
def test_verify_no_other_visas_requests(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.other_visas_tab.click()
    qiwa.work_visa.verify_other_visas_table_empty()


@allure.title('Test verifies there is no permanent visas on work visa page')
def test_verify_no_permanent_visas_requests(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.permanent_visas_tab.click()
    qiwa.work_visa.verify_permanent_visas_table_empty()


@allure.title('Test verifies generic one error is shown')
def test_verify_one_generic_error_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_generic_error_shown()


@allure.title('Test verifies one generic and permanent work visa errors are shown')
def test_verify_generic_and_perm_work_visa_error_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE)
                            )
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_generic_error_and_perm_visa_error_shown()


@allure.title('Test verifies errors in permanent work visa card concatenates with generic errors')
def test_verify_perm_work_visa_error_and_generic_error(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.refresh_page()
    qiwa.transitional.page_is_loaded()
    qiwa.transitional.verify_two_generic_error_and_two_perm_visa_errors_shown()


@case_id(25563)
@allure.title('Test verifies allowed quota tier is shown in case when company is in establishment phase')
def test_verify_allowed_quota_tier_in_establishment_shown(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_allowed_quota_tier_shown()


@case_id(25571)
@allure.title('Test verifies general eligibility errors on the transitional page')
def test_verify_general_eligibility_errors_on_transitional_page(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_generic_error_shown()
    visa_mock.setup_company(visa_type=VisaType.UNKNOWN,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_two_generic_errors_are_shown()
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_perm_work_visa_error_shown()
    visa_mock.setup_company(estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_work_visa_error_shown(Numbers.TWO, Numbers.TWO)
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE),
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.ONE)
                            )
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_generic_error_and_perm_visa_error_shown()
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT,
                            estab_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO),
                            common_eligibility_errors=join_codes(code=ERROR_CODE, times=Numbers.TWO))
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_two_generic_error_and_two_perm_visa_errors_shown()


@pytest.mark.parametrize("visa_type", [VisaType.EXPANSION, VisaType.ESTABLISHMENT])
@allure.title('Test verifies there is visa request (expansion, establishment) in permanent work visa page')
def test_verify_perm_work_visa_request(visa_mock, visa_type):
    visa_mock.setup_company(visa_type=visa_type)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_issue_visa.click()
    qiwa.issue_visa.verify_issue_visa_page_open()
    ref_number = qiwa.issue_visa.create_perm_visa_request()
    qiwa.work_visa.verify_perm_work_visa_request(ref_number)


@allure.title('Test verifies permanent work visa request (pdf) in establishing phase')
def test_verify_perm_work_visa_request_establishment_pdf(visa_mock):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_issue_visa.click()
    qiwa.issue_visa.verify_issue_visa_page_open()
    ref_number = qiwa.issue_visa.create_perm_visa_request()
    qiwa.work_visa.verify_perm_work_visa_request_pdf(ref_number)
    qiwa.work_visa.view_action.click()
    qiwa.visa_request.verify_visa_request_page_open()
    qiwa.visa_request.verify_details_in_pdf(ref_number)


@case_id(25571)
@allure.title("Test verifies permanent work visa work visa card's errors appearance (internal error) [establishment]")
def test_verify_perm_work_visa_card_internal_error(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
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
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.verify_work_visa_page_open()
    qiwa.work_visa.increase_quota_expansion_button.click()
    ref_num = qiwa.increase_quota.create_balance_request(visa_db, Numbers.ONE_THOUSAND)
    qiwa.work_visa.return_to_transitional_page()
    qiwa.transitional.verify_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.ESTABLISHMENT)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.TWO, Numbers.TWO)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.THREE, Numbers.THREE)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()
    visa_mock.change_balance_request(ref_num, Numbers.FOUR, Numbers.FOUR)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.verify_no_balance_expiration_date_perm_visa_card()


@allure.title('Test verifies permanent work visa request (pdf) in expansion phase')
def test_verify_perm_work_visa_request_expansion_pdf(visa_mock, visa_db):
    visa_mock.setup_company(visa_type=VisaType.EXPANSION)
    qiwa.transitional.refresh_page().page_is_loaded()
    qiwa.transitional.perm_work_visa_service_page_button.click()
    qiwa.work_visa.increase_quota_expansion_button.click()
    ref_num = qiwa.increase_quota.create_balance_request(visa_db, Numbers.ONE_THOUSAND)
    qiwa.work_visa.verify_perm_work_visa_request_pdf(ref_num, VisaType.EXPANSION)
    qiwa.work_visa.view_action.click()
    qiwa.balnce_request.verify_page_is_open()
    qiwa.balnce_request.verify_pdf_is_downloaded()