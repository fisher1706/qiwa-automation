import allure
import pytest

from data.dataportal.dataset import MarketOverviewData
from src.api.dataportal.schemas.response_mapping import WorkForceStatistics
from src.api.dataportal.workforcestatistics_api import workforce_api
from src.ui.pages.data_portal_pages.market_overview_page import MarketOverViewPage
from src.ui.qiwa import data_portal


@allure.title('Open Close Customize Modal')
def test_open_close_customize_modal():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.open_close_customize_modal()


@allure.title('Check Clear Customize Searching Field')
def test_customize_clear_searching():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_clear_searching_field()


@allure.title('Check Customize Searching Options')
def test_customize_options_searching():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_options_searching()


@allure.title('Check Customize No Result Searching')
def test_customize_no_result_searching():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_no_result_searching()


@allure.title('Check Customize Show All Sectors')
def test_show_all_sectors():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_show_all_sectors()


@allure.title('Check Customize Selected Options')
def test_customize_selected_options():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_selected_options()


@allure.title('Check Customize Select All Options')
def test_customize_selected_all_options():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_selected_all_options()


@allure.title('Check Customize Clear Selected Options')
def test_customize_clear_selected_options():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_clear_each_selected_options()


@allure.title('Check Customize Clear All Selected Options')
def test_customize_clear_all_selected_options():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.check_clear_all_selected_options()


@allure.title('Check Customize Apply Options')
def test_customize_apply_option():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.apply_option()


@allure.title('Add Customize Another Options')
def test_customize_add_another_option():
    data_portal.open_market_overview_page()
    data_portal.market_overview_page.add_another_option()


@allure.title('Check the displaying employee and establishment data from the backend to the interface')
@pytest.mark.parametrize('locator, endpoint_id, filtered_data, response_filter, action',
                         MarketOverviewData.employee_establish_data,
                         ids=['Employees amount', 'Establishments amount', 'Employees amount chart',
                              'Male employee amount chart', 'Female employee amount chart',
                              'Establishments chart amount', 'Unified chart amount', 'Entities chart amount'])
def test_employee_establish_chart_data(locator, endpoint_id, filtered_data, response_filter, action):
    data_portal.open_market_overview_page()
    filtered_data[0]["gt"] = workforce_api.last_quarter
    filtered_data[1]["lt"] = workforce_api.max_date
    workforce_api.post_workforcestatistics(endpoint_id, filtered_data, response_filter)
    data_portal.market_overview_page.check_incoming_data(locator, workforce_api.converted_value, action)


@allure.title('Check the displaying data Employees for last 5 years')
def test_employee_calculation():
    data_portal.open_market_overview_page()
    workforce_api.post_workforcestatistics(1, [{"name": "StartDate", "gt": workforce_api.min_date},
                                               {"name": "EndDate", "lt": workforce_api.max_date}],
                                           WorkForceStatistics.NOOFEMPLOYEES)
    data_portal.market_overview_page.employee_calculation(workforce_api.first_value, workforce_api.last_value)
    data_portal.market_overview_page.check_incoming_data(MarketOverViewPage.EMPLOYEE_5_YEARS,
                                                         data_portal.market_overview_page.calculation, None)


@allure.title('Check the displaying workforce chart data from the backend to the interface')
@pytest.mark.parametrize('locator, endpoint_id, filtered_data, response_filter, action',
                         MarketOverviewData.workforce_by_sector_data,
                         ids=['Top largest sector', 'All sectors'])
def test_workforce_chart_data(locator, endpoint_id, filtered_data, response_filter, action):
    data_portal.open_market_overview_page()
    filtered_data[0]["gt"] = workforce_api.max_date
    filtered_data[1]["lt"] = workforce_api.as_of_today
    workforce_api.post_workforcestatistics(endpoint_id, filtered_data, response_filter)
    values = []
    for value in workforce_api.all_values[:7]:
        if not action:
            workforce_api.convert_value(value)
        values.append(str(value) if action else workforce_api.converted_value)
    data_portal.market_overview_page.check_incoming_multiple_data(locator, values, action)
