import allure
import pytest

from data.data_portal.constants import Localization
from data.data_portal.dataset import ReportDataSet
from src.ui.dataportal import data_portal
from src.ui.pages.data_portal_pages.base_methods import base_methods
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check English translation for element on the page')
def test_title_en_translation_on_the_page():
    data_portal.open_reports_page()
    base_methods.check_en_element_on_the_page()


@allure.title('Check English translation for element on the page')
def test_title_ar_translation_on_the_page():
    data_portal.open_reports_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    base_methods.check_ar_element_on_the_page()


@allure.title('Check English translation of element on the page')
@pytest.mark.skip('Skipped due to absents translations from PO')
@pytest.mark.parametrize('elements, translation', ReportDataSet.en_elements_data,
                         ids=['Topic Titles en', 'Topic Descriptions en'])
def test_en_translation_elements_on_the_page(elements, translation):
    data_portal.open_all_sectors_page()
    base_methods.check_elements_on_the_page(elements, translation)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.skip('Skipped due to absents translations from PO')
@pytest.mark.parametrize('elements, translation', ReportDataSet.ar_elements_data,
                         ids=['Topic Titles ar', 'Topic Descriptions ar'])
def test_ar_translation_elements_on_the_page(elements, translation):
    data_portal.open_all_sectors_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    base_methods.check_elements_on_the_page(elements, translation)

