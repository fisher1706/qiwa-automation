import allure
import pytest

from data.data_portal.constants import Footer, Localization
from data.data_portal.dataset import FooterData
from src.ui.dataportal import data_portal
from src.ui.pages.data_portal_pages.base_methods import base_methods
from src.ui.pages.data_portal_pages.footer_block import FooterBlock
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check redirection to Qiwa Sa service')
@case_id(5653)
def test_redirection_to_qiwa_sa():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_qiwa_sa()


@allure.title('Check redirection to Twitter')
@case_id(5652, 5660)
def test_redirection_to_twitter():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_twitter()


@allure.title('Check redirection to Linkedin')
@case_id(5652, 5660)
def test_redirection_to_linkedin():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_linkedin()


@allure.title('Check redirection to Youtube')
@case_id(5652, 5660)
def test_redirection_to_youtube():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_youtube()


@allure.title('Check redirection to Term of user')
@case_id(5658, 5662)
def test_redirection_to_term_of_user():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_term_of_user()


@allure.title('Check redirection to Takamol')
@case_id(5652)
def test_redirection_to_takamol():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_takamol()


@allure.title('Check redirection to Human resources')
@case_id(5652)
def test_redirection_to_human_resources():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_human_resources()


@allure.title('Check navigation to All sectors page')
@case_id(5654)
def test_navigation_to_all_sectors_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_all_sectors_page()


@allure.title('Check navigation to Market overview page')
@case_id(5655)
def test_navigation_to_market_overview_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_market_overview_page()


@allure.title('Check navigation to Privacy Policy page')
@case_id(5659)
def test_navigation_to_privacy_policy_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_privacy_policy_page()


@allure.title('Check navigation to About us page')
@case_id(5656)
def test_navigation_about_us_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_about_us_page()


@allure.title('Check navigation to Contact us page')
@case_id(5657)
def test_navigation_contact_us_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_contact_us_page()


@allure.title('Check English translation of element on the page')
@case_id(5641, 5642, 5644, 5645, 5646, 5647, 5648, 5651, )
@pytest.mark.parametrize('element, translation', FooterData.en_element_data,
                         ids=['Sectors title en', 'Company title en', 'About us hyperlink en',
                              'Contact us hyperlink en', 'View all sectors hyperlink en',
                              'Market overview hyperlink en', 'Term of use hyperlink en',
                              'Privacy policy hyperlink en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    base_methods.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.parametrize('element, translation', FooterData.ar_element_data,
                         ids=['Sectors title ar', 'Company title ar', 'About us hyperlink ar',
                              'Contact us hyperlink ar', 'View all sectors hyperlink ar',
                              'Market overview hyperlink ar', 'Term of use hyperlink ar',
                              'Privacy policy hyperlink ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    base_methods.check_element_on_the_page(element, translation)


@allure.title('Check element translation on the page')
@case_id(5643)
def test_en_translation_elements_on_the_page():
    data_portal.open_home_page()
    data_portal.footer.wait_sectors()
    base_methods.check_elements_on_the_page(FooterBlock.SECTORS_ITEM, Footer.SECTORS_ITEM_EN)


@allure.title('Check element translation on the page')
@case_id(5424)
def test_ar_translation_elements_on_the_page():
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.footer.wait_sectors()
    base_methods.check_elements_on_the_page(FooterBlock.SECTORS_ITEM, Footer.SECTORS_ITEM_AR)
