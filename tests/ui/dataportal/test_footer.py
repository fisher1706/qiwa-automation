import allure
import pytest

from data.dataportal.constants import Footer, Localization
from data.dataportal.dataset import FooterData
from src.ui.pages.data_portal_pages.footer_block import FooterBlock
from src.ui.qiwa import data_portal


@allure.title('Check redirection to Qiwa Sa service')
def test_redirection_to_qiwa_sa():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_qiwa_sa()


@allure.title('Check redirection to Twitter')
def test_redirection_to_twitter():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_twitter()


@allure.title('Check redirection to Linkedin')
def test_redirection_to_linkedin():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_linkedin()


@allure.title('Check redirection to Youtube')
def test_redirection_to_youtube():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_youtube()


@allure.title('Check redirection to Term of user')
def test_redirection_to_term_of_user():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_term_of_user()


@allure.title('Check redirection to Takamol')
def test_redirection_to_takamol():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_takamol()


@allure.title('Check redirection to Human resources')
def test_redirection_to_human_resources():
    data_portal.open_home_page()
    data_portal.footer.check_redirection_to_human_resources()


@allure.title('Check navigation to All sectors page')
def test_navigation_to_all_sectors_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_all_sectors_page()


@allure.title('Check navigation to Market overview page')
def test_navigation_to_market_overview_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_market_overview_page()


@allure.title('Check navigation to Privacy Policy page')
def test_navigation_to_privacy_policy_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_privacy_policy_page()


@allure.title('Check navigation to About us page')
def test_navigation_about_us_page():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_about_us_page()


@allure.title('Check navigation to Contact us page')
def test_navigation_to_twitter():
    data_portal.open_home_page()
    data_portal.footer.check_navigation_to_contact_us_page()


@allure.title('Check English translation of element on the page')
@pytest.mark.parametrize('element, translation', FooterData.en_element_data,
                         ids=['Sectors title en', 'Company title en', 'About us hyperlink en',
                              'Contact us hyperlink en', 'View all sectors hyperlink en',
                              'Market overview hyperlink en', 'Term of use hyperlink en',
                              'Privacy policy hyperlink en'])
def test_en_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.footer.check_element_on_the_page(element, translation)


@allure.title('Check Arabic translation of element on the page')
@pytest.mark.parametrize('element, translation', FooterData.ar_element_data,
                         ids=['Sectors title ar', 'Company title ar', 'About us hyperlink ar',
                              'Contact us hyperlink ar', 'View all sectors hyperlink ar',
                              'Market overview hyperlink ar', 'Term of use hyperlink ar',
                              'Privacy policy hyperlink ar'])
def test_ar_translation_element_on_the_page(element, translation):
    data_portal.open_home_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.footer.check_element_on_the_page(element, translation)


@allure.title('Check element translation on the page')
@pytest.mark.skip('Skipped due to absence translations')
def test_en_translation_elements_on_the_page():
    data_portal.open_about_us_page()
    data_portal.footer.check_elements_on_the_page(FooterBlock.SECTORS_ITEM, Footer.SECTORS_ITEM_EN)


@allure.title('Check element translation on the page')
@pytest.mark.skip('Skipped due to absence translations')
def test_ar_translation_elements_on_the_page():
    data_portal.open_about_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.footer.check_elements_on_the_page(FooterBlock.SECTORS_ITEM, Footer.SECTORS_ITEM_AR)
