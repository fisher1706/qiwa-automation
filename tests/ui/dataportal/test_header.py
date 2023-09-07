import allure
import pytest

from data.dataportal.constants import Header, Localization
from data.dataportal.dataset import HeaderData
from src.ui.pages.data_portal_pages.header_block import HeaderBlock
from src.ui.qiwa import data_portal


@allure.title('Check navigation to All sectors page')
def test_navigation_to_all_sectors_page():
    data_portal.open_home_page()
    data_portal.header.check_navigation_to_all_sectors_page()


@allure.title('Check navigation to Market overview page')
def test_navigation_to_market_overview_page():
    data_portal.open_home_page()
    data_portal.header.check_navigation_to_market_overview_page()


@allure.title('Check navigation to Reports page')
def test_navigation_to_reports_page():
    data_portal.open_home_page()
    data_portal.header.check_navigation_to_reports_page()


@allure.title('Check English translation for element on the page')
@pytest.mark.parametrize('element, translation', HeaderData.en_element_data,
                         ids=['Sectors title en', 'Market overview hyperlink en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation for element on the page')
@pytest.mark.parametrize('element, translation', HeaderData.ar_element_data,
                         ids=['Sectors title ar', 'Market overview hyperlink ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.header.check_element_on_the_page(element, translation)


@allure.title('Check English translations for Services on the page')
@pytest.mark.parametrize('element, translation', HeaderData.en_services_data,
                         ids=['View all sectors hyperlink en', 'Economic activities option en',
                              'Nitaqat activities option en'])
def test_en_translation_services_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.check_element_on_the_page(element, translation, True)


@allure.title('Check Arabic translations for Services on the page')
@pytest.mark.parametrize('element, translation', HeaderData.ar_services_data,
                         ids=['View all sectors hyperlink ar', 'Economic activities option ar',
                              'Nitaqat activities option ar'])
def test_ar_translation_services_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.header.check_element_on_the_page(element, translation, True)


@allure.title('Check English translation for elements on the page')
@pytest.mark.skip('Skipped due to absence translations')
def test_en_translation_elements_on_the_page():
    data_portal.open_home_page()
    data_portal.header.check_elements_on_the_page(HeaderBlock.SECTORS_ITEM, Header.SECTORS_ITEM_EN)


@allure.title('Check Arabic translation for elements on the page')
@pytest.mark.skip('Skipped due to absence translations')
def test_ar_translation_elements_on_the_page():
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.header.check_elements_on_the_page(HeaderBlock.SECTORS_ITEM, Header.SECTORS_ITEM_AR)
