import allure
import pytest

from data.dataportal.constants import Localization
from data.dataportal.dataset import AboutUsData
from src.ui.qiwa import data_portal


@allure.title('Check redirection to Qiwa Sa service from title')
def test_redirection_to_qiwa_sa_service_from_title():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_qiwa_sa_service_from_title()


@allure.title('Check redirection to Qiwa Sa service')
def test_redirection_to_qiwa_sa():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_qiwa_sa()


@allure.title('Check redirection to Linkedin')
def test_redirection_to_linkedin():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_linkedin()


@allure.title('Check redirection to Twitter')
def test_redirection_to_twitter():
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_redirection_to_twitter()


@allure.title('Check English translation of element on the page')
@pytest.mark.parametrize('element, translation', AboutUsData.en_element_data,
                         ids=['Hero Title en', 'Hero Description en', 'Mission Title en', 'Benefits Title en',
                              'Believe Title en', 'QiwaSa Title en', 'Visit Title en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.parametrize('element, translation', AboutUsData.ar_element_data,
                         ids=['Hero Title ar', 'Hero Description ar', 'Mission Title ar', 'Benefits Title ar',
                              'Believe Title ar', 'QiwaSa Title ar', 'Visit Title ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_about_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.about_us_page.check_element_on_the_page(element, translation)


@allure.title('Check element translation on the page')
@pytest.mark.parametrize('elements, translation', AboutUsData.en_elements_data,
                         ids=['Mission Card Title en', 'Mission Card Description en', 'Benefits Card Title en',
                              'Benefits Card Description en', 'Believe Card Title en', 'Believe Card Description en',
                              'QiwaSa Description en', 'Visit Qiwa Title en'])
def test_en_translation_elements_on_the_page(elements, translation):
    data_portal.open_about_us_page()
    data_portal.about_us_page.check_elements_on_the_page(elements, translation)


@allure.title('Check element translation on the page')
@pytest.mark.parametrize('elements, translation', AboutUsData.ar_elements_data,
                         ids=['Mission Card Title ar', 'Mission Card Description ar', 'Benefits Card Title ar',
                              'Benefits Card Description ar', 'Believe Card Title ar', 'Believe Card Description ar',
                              'QiwaSa Description ar', 'Visit Qiwa Title ar'])
def test_ar_translation_elements_on_the_page(elements, translation):
    data_portal.open_about_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.about_us_page.check_elements_on_the_page(elements, translation)
