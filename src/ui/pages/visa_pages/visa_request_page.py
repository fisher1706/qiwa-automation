from selene.api import be, have, query, s, ss
from selene.api.shared import browser

from data.visa.constants import VISA_REQUEST_PAGE_TITLE_TEXT, VisaUser
from src.ui.components.raw.table import Table
from src.ui.pages.visa_pages.base_page import BasePage
from utils.assertion.soft_assertions import soft_assert_text
from utils.pdf_parser import get_downloaded_filename, verify_text_in_pdf


class VisaRequestPage(BasePage):
    loader = s('//*[@data-testid="viewVisaRequestSkeleton"]')
    visa_request_details = s('//*[@data-testid="visaRequestDetailsBox"]')
    visa_request_number = s('//*[@data-testid="visaRequestDetailsTableRowrequestNumberValue"]')
    visa_request_id = ss('//*[@data-testid="visaRequestDetailsTableRowvisaId"]//p').second
    visa_request_table = Table(s('//*[@data-testid="borderNumbersTable"]//table'))
    visa_request_statuses = ".//p[1]"
    visa_request_print_button = s('//*[@data-testid="printBtn"]')

    def verify_visa_request_page_open(self):
        self.loader.wait_until(be.visible)
        self.loader.wait_until(be.hidden)
        self.page_navigation_chain.should(be.visible)
        self.page_navigation_chain.should(have.text(VISA_REQUEST_PAGE_TITLE_TEXT))
        self.page_title.should(be.visible)
        self.page_title.should(have.text(VISA_REQUEST_PAGE_TITLE_TEXT))

    def verify_details_in_pdf(self, request):
        check_data = [request]
        self.visa_request_number.should(be.visible)
        soft_assert_text(
            self.visa_request_number, text=request, element_name="Visa request number"
        )
        check_data.append(self.visa_request_id.get(query.text))
        check_data.append(VisaUser.ESTABLISHMENT_ID)
        check_data.append(
            self.visa_request_table.cell(row=1, column=7)
            .s(self.visa_request_statuses)
            .get(query.text)
        )
        browser.driver.execute_script("window.scrollTo(0, 0);")
        self.visa_request_print_button.click()
        filename = get_downloaded_filename(timeout=20)
        verify_text_in_pdf(filename, check_data)
