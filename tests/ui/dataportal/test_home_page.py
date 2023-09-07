import allure
import pytest

from data.dataportal.constants import Localization, SubscribeBlock
from data.dataportal.dataset import HomePageDataSet
from src.ui.qiwa import data_portal


@allure.title('Check navigation to Market overview from Hero')
def test_navigation_to_market_overview_from_hero():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_hero()


@allure.title('Check navigation to Market overview from Growth')
def test_navigation_to_market_overview_from_growth_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_growth_block()


@allure.title('Check navigation to Market overview from Employee')
def test_navigation_to_market_overview_from_empl_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_empl_block()


@allure.title('Check navigation to Market overview from Establish')
def test_navigation_to_market_overview_from_estab_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_estab_block()


@allure.title('Check navigation to to Market overview from Trending')
def test_navigation_to_market_overview_from_trending_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_trending_block()


@allure.title('Check navigation to Finance sector')
def test_navigation_to_finance_sector():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_finance_sector()


@allure.title('Check navigation to All sectors page')
def test_navigation_to_all_sectors_page():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_all_sectors_page()


@allure.title('Check navigation to Market overview from Insight')
def test_navigation_to_market_overview_from_insight():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_insight()


@allure.title('Check navigation to Contact us page')
def test_navigation_to_contact_us_page():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_contact_us_page()


@allure.title('Check English translation of element on the page')
@pytest.mark.parametrize('element, translation', HomePageDataSet.en_element_data,
                         ids=['Hero description en', 'Hero Market overview button en', 'Hero Growth description en',
                              'Hero Employee description en',  'Hero Establish description en', 'Trending title en',
                              'Trending Stats title en', 'Trending Card title en',  'Finance chart title en',
                              'Finance chart description en', 'Finance chart header title en',
                              'Finance chart Explore button en', 'Explore by sector title en', 'View all sectors en',
                              'Insights title en', 'Insights description en', 'Insights Explore button en',
                              'Solution title en',  'Solution description en', 'Trust title en', 'Trust description en',
                              'ContactUs title en',  'ContactUs description en', 'ContactUs button en',
                              'Subscribe title en', 'Subscribe description en', 'Subscribe button en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.home_page.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.parametrize('element, translation', HomePageDataSet.ar_element_data,
                         ids=['Hero description ar', 'Hero Market overview button ar', 'Hero Growth description ar',
                              'Hero Employee description ar', 'Hero Establish description ar', 'Trending title ar',
                              'Trending Stats title ar', 'Trending Card title ar',  'Finance chart title ar',
                              'Finance chart description ar', 'Finance chart header title ar',
                              'Finance chart Explore button ar', 'Explore by sector title ar', 'View all sectors ar',
                              'Insights title ar', 'Insights description ar', 'Insights Explore button ar',
                              'Solution title ar', 'Solution description ar', 'Trust title ar', 'Trust description ar',
                              'ContactUs title ar',  'ContactUs description ar', 'ContactUs button ar',
                              'Subscribe title ar', 'Subscribe description ar',  'Subscribe button ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.home_page.check_element_on_the_page(element, translation)


@allure.title('Check English translation of element on the page')
@pytest.mark.parametrize('values', HomePageDataSet.en_elements_data,
                         ids=['Home hero titles en', 'Trending descriptions en', 'Sectors titles en',
                              'Insight slide descriptions en',  'Solution titles en', 'Solution descriptions en',
                              'Trust provide titles en', 'Trust info title en'])
def test_en_translation_elements_on_the_page(values):
    data_portal.open_home_page()
    data_portal.home_page.check_elements_on_the_page(*values)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.parametrize('values', HomePageDataSet.ar_elements_data,
                         ids=['Home hero titles ar', 'Trending descriptions ar', 'Sectors title ar',
                              'Insight slide descriptions ar', 'Solution titles ar', 'Solution descriptions ar',
                              'Trust provide titles ar',  'Trust info title ar'])
def test_ar_translation_elements_on_the_page(values):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.home_page.check_elements_on_the_page(*values)


@allure.title('Check elements on the page')
def test_insights_block_navigation():
    data_portal.open_home_page()
    data_portal.home_page.check_insight_block_navigation()


@allure.title('Check Chart dropdown')
@pytest.mark.skip('Skipped due to no data from IBM')
@pytest.mark.parametrize('arg', HomePageDataSet.chart_dropdown_option)
def test_chart_dropdown(arg):
    data_portal.open_home_page()
    data_portal.home_page.check_picked_chart_option(*arg)


@allure.title('Create Subscribe request with English loc')
def test_en_subscribe_request():
    data_portal.open_home_page()
    data_portal.home_page.check_subscribe_request(SubscribeBlock.SUCCESS_MESSAGE_EN)


@allure.title('Create Subscribe request with Arabic loc')
def test_ar_subscribe_request():
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.home_page.check_subscribe_request(SubscribeBlock.SUCCESS_MESSAGE_AR)
