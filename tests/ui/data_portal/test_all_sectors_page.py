import allure
import pytest

from data.data_portal.constants import Localization
from data.data_portal.dataset import AllSectorsData
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check English translation for element on the page')
@case_id(5500)
@pytest.mark.parametrize('element, translation', AllSectorsData.en_element_data,
                         ids=['Hero Title en', 'Economic Act tab Title en', 'Nitaqat Act tab Title en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_all_sectors_page()
    data_portal.all_sectors_page.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation for element on the page')
@case_id(5518, 5519)
@pytest.mark.parametrize('element, translation', AllSectorsData.ar_element_data,
                         ids=['Hero Title ar', 'Economic Act tab Title ar', 'Nitaqat Act tab Title ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_all_sectors_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.all_sectors_page.check_element_on_the_page(element, translation)


@allure.title('Check English translation of element on the page')
@case_id(5500)
@pytest.mark.skip('Skipped due to absents translations from PO')
@pytest.mark.parametrize('elements, translation, activities_type', AllSectorsData.en_elements_data,
                         ids=['Economic Sector Title en', 'Nitaqat Sector Title en'])
def test_en_translation_elements_on_the_page(elements, translation, activities_type):
    data_portal.open_all_sectors_page()
    data_portal.all_sectors_page.check_elements_on_the_page(elements, translation, activities_type)


@allure.title('Check Arabic translation of element on the page')
@case_id(5518, 5519)
@pytest.mark.skip('Skipped due to absents translations from PO')
@pytest.mark.parametrize('elements, translation, activities_type', AllSectorsData.ar_elements_data,
                         ids=['Economic Sector Title ar', 'Nitaqat Sector Title ar'])
def test_ar_translation_elements_on_the_page(elements, translation, activities_type):
    data_portal.open_all_sectors_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.all_sectors_page.check_elements_on_the_page(elements, translation, activities_type)


@allure.title('Check Search Sectors with English criteria')
@case_id(5501, 5503, 5504, 5511, 5512)
@pytest.mark.parametrize('search_criteria, target_items', AllSectorsData.en_search_data,
                         ids=['Search request en', 'No results en'])
def test_search_sectors_en_criteria(search_criteria, target_items):
    data_portal.open_all_sectors_page()
    data_portal.all_sectors_page.perform_searching(search_criteria, target_items)


@allure.title('Check Search Sectors with Arabic criteria')
@case_id(5518, 5519)
@pytest.mark.parametrize('search_criteria, target_items', AllSectorsData.ar_search_data,
                         ids=['Search request ar', 'No results ar'])
def test_search_sectors_ar_criteria(search_criteria, target_items):
    data_portal.open_all_sectors_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.all_sectors_page.perform_searching(search_criteria, target_items)