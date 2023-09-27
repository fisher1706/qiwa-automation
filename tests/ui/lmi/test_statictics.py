import allure
import pytest

from src.ui.lmi import lmi


@pytest.mark.skip("Hided again in the framework https://employeesgate.atlassian.net/browse/LR-1000")
@allure.title('Check unhidden Labor Market Statistics Block')
def test_unhidden_labor_block():
    lmi.open_landing_page()
    lmi.lmi_landing.check_labor_market_statistics_block()


@pytest.mark.skip("Hided again in the framework https://employeesgate.atlassian.net/browse/LR-1000")
@allure.title('Check unhidden All Retail Establishments results Block')
def test_unhidden_company_list():
    lmi.open_landing_page()
    lmi.lmi_landing.check_company_list()


@pytest.mark.skip("Hided again in the framework https://employeesgate.atlassian.net/browse/LR-1000")
@allure.title('Check unhidden Labor Market Top companies Block')
def test_top_companies_block():
    lmi.open_landing_page()
    lmi.lmi_landing.check_top_companies_block()


@pytest.mark.skip("Hided again in the framework https://employeesgate.atlassian.net/browse/LR-1000")
@allure.title('Check unhidden Ranking for company')
def test_ranking_block():
    lmi.open_landing_page()
    lmi.lmi_landing.check_ranking_block()

