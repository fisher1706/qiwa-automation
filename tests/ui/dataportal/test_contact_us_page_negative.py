import allure
import pytest

from data.dataportal.constants import ContactUs, Localization, Variables
from data.dataportal.dataset import ContactUsDataSet
from src.ui.pages.data_portal_pages.contact_us_page import ContactUsPage
from src.ui.qiwa import data_portal


@allure.title('Perform Contact us request negative')
@pytest.mark.parametrize('values', ContactUsDataSet.negative_data,
                         ids=['Empty all required fields', 'Request without Name', 'Request without Email',
                              'Request with email without at', 'Request with email without dot',
                              'With email without prefix', 'With email without domain', 'Without Reason',
                              'With Reason less than 30 characters', 'With Reason more than 2500 characters'])
def test_perform_request_negative(values):
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.perform_request_negative(*values)


@allure.title('Check English Validation Alerts')
def test_en_validation_alerts():
    data_portal.open_contact_us_page()
    data_portal.contact_us_page.complete_request_form(Variables.EMPTY, Variables.EMPTY,
                                                      Variables.EMPTY, Variables.AUTOTEST)
    data_portal.contact_us_page.check_elements_on_the_page(ContactUsPage.ALERT, ContactUs.VALIDATION_ALERTS_EN)


@allure.title('Check Arabic Validation Alerts')
def test_ar_validation_alerts():
    data_portal.open_contact_us_page()
    data_portal.header.setup_localization(Localization.AR_LOCAL)
    data_portal.contact_us_page.complete_request_form(Variables.EMPTY, Variables.EMPTY,
                                                      Variables.EMPTY, Variables.AUTOTEST)
    data_portal.contact_us_page.check_elements_on_the_page(ContactUsPage.ALERT, ContactUs.VALIDATION_ALERTS_AR)
