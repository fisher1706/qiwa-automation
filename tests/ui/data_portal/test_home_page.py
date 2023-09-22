import allure
import pytest

from data.data_portal.constants import Localization, SubscribeBlock
from data.data_portal.dataset import HomePageDataSet
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check navigation to Market overview from Hero')
@case_id(5702)
def test_navigation_to_market_overview_from_hero():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_hero()


@allure.title('Check navigation to Market overview from Growth')
@case_id(5705)
def test_navigation_to_market_overview_from_growth_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_growth_block()


@allure.title('Check navigation to Market overview from Employee')
@case_id(5705)
def test_navigation_to_market_overview_from_empl_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_empl_block()


@allure.title('Check navigation to Market overview from Establish')
@case_id(5705)
def test_navigation_to_market_overview_from_estab_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_estab_block()


@allure.title('Check navigation to to Market overview from Trending')
@case_id(12375)
def test_navigation_to_market_overview_from_trending_block():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_trending_block()


@allure.title('Check navigation to Finance sector')
@case_id(5738)
def test_navigation_to_finance_sector():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_finance_sector()


@allure.title('Check navigation to All sectors page')
@case_id(5734)
def test_navigation_to_all_sectors_page():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_all_sectors_page()


@allure.title('Check navigation to Market overview from Insight')
@case_id(5722)
def test_navigation_to_market_overview_from_insight():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_market_overview_from_insight()


@allure.title('Check navigation to Contact us page')
@case_id(17458)
def test_navigation_to_contact_us_page():
    data_portal.open_home_page()
    data_portal.home_page.check_navigation_to_contact_us_page()


@allure.title('Check English translation of element on the page')
@case_id(5700, 5701, 5703, 5706, 5709, 5719, 5720, 5721, 5735, 5736, 5737, 5741, 5768, 5769, 5779, 17455, 17457)
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
@case_id(12382, 12383, 12384)
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
@case_id(5699, 5700, 5770, 5771, 5772, 5773, 5774, 5777, 5778)
@pytest.mark.parametrize('values', HomePageDataSet.en_elements_data,
                         ids=['Home hero titles en', 'Trending descriptions en', 'Sectors titles en',
                              'Insight slide descriptions en',  'Solution titles en', 'Solution descriptions en',
                              'Trust provide titles en', 'Trust info title en'])
def test_en_translation_elements_on_the_page(values):
    data_portal.open_home_page()
    data_portal.home_page.check_elements_on_the_page(*values)


@allure.title('Check Arabic translation of element on the page')
@case_id(12382, 12383, 12384)
@pytest.mark.parametrize('values', HomePageDataSet.ar_elements_data,
                         ids=['Home hero titles ar', 'Trending descriptions ar', 'Sectors title ar',
                              'Insight slide descriptions ar', 'Solution titles ar', 'Solution descriptions ar',
                              'Trust provide titles ar',  'Trust info title ar'])
def test_ar_translation_elements_on_the_page(values):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.home_page.check_elements_on_the_page(*values)


@allure.title('Check elements on the page')
@case_id(5723)
def test_insights_block_navigation():
    data_portal.open_home_page()
    data_portal.home_page.check_insight_block_navigation()


@allure.title('Check Chart dropdown')
@case_id(5740, 5742, 5743, 5746, 5795)
@pytest.mark.skip('Skipped due to no data from IBM')
@pytest.mark.parametrize('arg', HomePageDataSet.chart_dropdown_option)
def test_chart_dropdown(arg):
    data_portal.open_home_page()
    data_portal.home_page.check_picked_chart_option(*arg)


@allure.title('Create Subscribe request with English loc')
@case_id(5960, 5962)
def test_en_subscribe_request():
    data_portal.open_home_page()
    data_portal.home_page.check_subscribe_request(SubscribeBlock.SUCCESS_MESSAGE_EN)


@allure.title('Create Subscribe request with Arabic loc')
@case_id(5961, 5962)
def test_ar_subscribe_request():
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.home_page.check_subscribe_request(SubscribeBlock.SUCCESS_MESSAGE_AR)
