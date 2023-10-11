import allure
from selene.api import be, s

from src.ui.pages.visa_pages.base_page import BasePage
from utils.pdf_parser import file_is_valid_pdf, get_downloaded_filename


class BalanceRequest(BasePage):
    request_details_section = s('//*[@data-testid="balanceDetailsPageContent"]')
    print_button = s('//button//p[contains(text(), "Print")]')

    def verify_page_is_open(self):
        self.request_details_section.should(be.visible)

    @allure.step("Verify PDF file is downloaded and valid")
    def verify_pdf_is_downloaded(self):
        self.print_button.click()
        filename = get_downloaded_filename(timeout=20)
        file_is_valid_pdf(filename)
