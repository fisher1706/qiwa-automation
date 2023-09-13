import allure
import pytest

from data.data_portal.dataset import SectorData
from src.api.dataportal.workforcestatistics_api import workforce_api
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check the displaying of data from the backend to the interface')
@case_id(5907)
@pytest.mark.skip('Need to adjust endpoint ids ')
@pytest.mark.parametrize('sector_id', SectorData.economic_sector_ids_data)
@pytest.mark.parametrize('locator, endpoint_id, filtered_data, response_filter, action', SectorData.sector_data,
                         ids=['Employees amount', 'Establishments amount', 'Employees amount chart', 'Total male',
                              'Total female', 'Establishments amount chart', 'Unified amount chart',
                              'Entities amount chart'])
def test_incoming_data_for_economic_sectors(sector_id, locator, endpoint_id, filtered_data, response_filter, action):
    data_portal.open_economic_activity_sector_page(sector_id)
    filtered_data[0]["gt"] = workforce_api.last_quarter
    filtered_data[1]["lt"] = workforce_api.max_date
    filtered_data[2]["eq"] = str(sector_id)
    workforce_api.post_workforcestatistics(endpoint_id, filtered_data, response_filter)
    data_portal.sector_page.check_incoming_data(locator, workforce_api.converted_value, action)

