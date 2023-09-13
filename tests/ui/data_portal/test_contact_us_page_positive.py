import allure
import pytest

from data.data_portal.constants import ContactUs, Localization
from data.data_portal.dataset import ContactUsDataSet
from src.ui.dataportal import data_portal
from src.ui.pages.data_portal_pages.contact_us_page import ContactUsPage
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check English translation for element on the page')
@case_id(5546, 5548)
@pytest.mark.parametrize('element, translation, perform_request', ContactUsDataSet.en_element_data,
                         ids=['Page title en', 'Send button en', 'Back button en', 'Success Title en',
                              'Success Description en'])
def test_en_translation_element_on_the_page(element, translation, perform_request):
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.check_element_on_the_page(element, translation, perform_request)


@allure.title('Check Arabic translation for element on the page')
@case_id(5547, 5549)
@pytest.mark.parametrize('element, translation, perform_request', ContactUsDataSet.ar_element_data,
                         ids=['Page title ar', 'Send button ar',  'Back button ar', 'Success Title ar',
                              'Success Description ar'])
def test_ar_translation_element_on_the_page(element, translation, perform_request):
    data_portal.open_contact_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.contact_us_page.check_element_on_the_page(element, translation, perform_request)


@allure.title('Check English translations for Titles on the page')
@case_id(5546)
def test_en_translation_titles_element_on_the_page():
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.check_elements_on_the_page(ContactUsPage.FIELD_TITLES, ContactUs.FIELD_NAMES_EN)


@allure.title('Check Arabic translations for Titles on the page')
@case_id(5547)
def test_ar_translation_titles_on_the_page():
    data_portal.open_contact_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.contact_us_page.check_elements_on_the_page(ContactUsPage.FIELD_TITLES, ContactUs.FIELD_NAMES_AR)


@allure.title('Check navigation to Home page after request')
def test_navigation_to_home_page_after_request():
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.check_navigation_to_home_page_after_request()


@allure.title('Create Contact us request')
@case_id(5537, 5541)
@pytest.mark.parametrize('values', ContactUsDataSet.setup_data, ids=['request with Company, reason=30char',
                                                                     'request with Company, reason=2500char',
                                                                     'request without Company, reason=30char',
                                                                     'request without Company, reason=2500char'])
def test_complete_the_form(values):
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.perform_request(*values)
