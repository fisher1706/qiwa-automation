from selene import browser, query
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.dataportal.constants import Links, Variables


class ContactUsPage:
    TITLE = s('//div[@class="contact-us-title"]//h1')
    FIELD_TITLES = ss('//label[@class="label-01"]')
    NAME_FIELD = s("#name")
    EMAIL_FIELD = s('//input[@name="Email"]')
    COMPANY_FIELD = s('//input[@name="CompanyName"]')
    REASON_FIELD = s("#reason")
    SEND_BUTTON = s('//div[@class="d-flex submit-wrapper"]//button')
    ALERT = ss('//p["error-msg"]')
    BACK_TO_HOME = s('//a[@class="button button-large button-secondary"]')
    TITLE_SUCCESS = s('//div[@class="message-title"]//h1')
    DESCR_SUCCESS = s('//div[@class="message-title"]//h2')

    """Contact us block"""
    TITLE_BLOCK = s('//div[@class="heading-03 md-heading-02 request-block_title"]')
    DESCRIPTION_BLOCK = s(
        '//div[@class="body-01-paragraph md-body-large-paragraph request-block_subtitle"]'
    )
    BUTTON = s('//section[@class="request-block "]//a')

    def __init__(self):
        self.validation_alerts = []

    def complete_request_form(self, name, email, text, company=None):
        self.NAME_FIELD.set_value(name)
        self.EMAIL_FIELD.set_value(email)
        self.REASON_FIELD.set_value(text)
        if company:
            self.COMPANY_FIELD.set_value(company)

    def check_disable_state_send_button(self):
        self.SEND_BUTTON.should(be.disabled)

    def check_validation_alerts(self, target_alerts):
        alerts = self.ALERT
        for alert in alerts:
            self.validation_alerts.append(alert.get(query.text))
        assert target_alerts == self.validation_alerts, (
            f"Validation alerts didn't match\nExpected: {target_alerts}\n"
            f"Actual: {self.validation_alerts}"
        )

    def check_element_on_the_page(self, element, element_text, perform_request=False):
        if perform_request:
            self.perform_request(
                Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(30)
            )
        element.should(have.text(element_text))

    @staticmethod
    def check_elements_on_the_page(elements, list_text):
        elements_list = []
        for element in elements:
            elements_list.append(element.get(query.text))
        assert elements_list == list_text, f"{elements_list}\n{list_text}"

    def perform_request(self, name, email, text, company=None):
        self.complete_request_form(name, email, text, company)
        self.SEND_BUTTON.click()
        self.TITLE_SUCCESS.should(be.visible)

    def perform_request_negative(self, name, email, text):
        self.complete_request_form(name, email, text)
        self.check_disable_state_send_button()

    def check_navigation_to_home_page_after_request(self):
        self.perform_request(Variables.AUTOTEST, Variables.EMAIL, Variables.generate_string(30))
        self.BACK_TO_HOME.click()
        assert browser.driver.current_url == Links.HOME_PAGE
