import allure
import pytest

from data.data_portal.constants import Localization
from data.data_portal.dataset import AboutUsData
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check redirection to Qiwa Sa service from title')
@case_id(5436)
def test_redirection_to_qiwa_sa_service_from_title():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_qiwa_sa_service_from_title()


@allure.title('Check redirection to Qiwa Sa service')
@case_id(5439)
def test_redirection_to_qiwa_sa():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_qiwa_sa()


@allure.title('Check redirection to Linkedin')
@case_id(5440)
def test_redirection_to_linkedin():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_linkedin()


@allure.title('Check redirection to Twitter')
@case_id(5441)
def test_redirection_to_twitter():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_twitter()


@allure.title('Check English translation of element on the page')
@case_id(5424, 5425, 5429, 5438)
@pytest.mark.parametrize('element, translation', AboutUsData.en_element_data,
                         ids=['Hero Title en', 'Hero Description en', 'Mission Title en', 'Benefits Title en',
                              'Believe Title en', 'QiwaSa Title en', 'Visit Title en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation of element on the page')
@case_id(5442)
@pytest.mark.parametrize('element, translation', AboutUsData.ar_element_data,
                         ids=['Hero Title ar', 'Hero Description ar', 'Mission Title ar', 'Benefits Title ar',
                              'Believe Title ar', 'QiwaSa Title ar', 'Visit Title ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_about_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.about_us_page.check_element_on_the_page(element, translation)


@allure.title('Check English translation of elements on the page')
@case_id(5427, 5429, 5430, 5432, 5433, 5435, 5437)
@pytest.mark.parametrize('elements, translation', AboutUsData.en_elements_data,
                         ids=['Mission Card Title en', 'Mission Card Description en', 'Benefits Card Title en',
                              'Benefits Card Description en', 'Believe Card Title en', 'Believe Card Description en',
                              'QiwaSa Description en', 'Visit Qiwa Title en'])
def test_en_translation_elements_on_the_page(elements, translation):
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_elements_on_the_page(elements, translation)


@allure.title('Check Arabic translation of elements on the page')
@case_id(5442)
@pytest.mark.parametrize('elements, translation', AboutUsData.ar_elements_data,
                         ids=['Mission Card Title ar', 'Mission Card Description ar', 'Benefits Card Title ar',
                              'Benefits Card Description ar', 'Believe Card Title ar', 'Believe Card Description ar',
                              'QiwaSa Description ar', 'Visit Qiwa Title ar'])
def test_ar_translation_elements_on_the_page(elements, translation):
    data_portal.open_about_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.about_us_page.check_elements_on_the_page(elements, translation)
