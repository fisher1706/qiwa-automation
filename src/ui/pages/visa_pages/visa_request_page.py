import datetime

import allure
from dateutil.relativedelta import relativedelta
from selene.api import Condition, Element, be, have, query, s, ss

from data.visa.constants import (
    CANCEL_VISA,
    VISA_REQUEST_PAGE_TITLE_TEXT,
    VR_CANCELABLE,
    WORK_VISA_PAGE_TITLE_TEXT,
    YOUR_REQUEST_HAS_BEEN_SENT,
    ColName,
    DateFormats,
    Numbers,
    VisaRequestStatus,
    VisaUser,
)
from src.ui.components.feedback_pop_up import FeedbackPopup
from src.ui.components.raw.table import Table
from utils.assertion.soft_assertions import soft_assert_text
from utils.helpers import scroll_to_top
from utils.pdf_parser import get_downloaded_filename, verify_text_in_pdf


class VisaRequestPage:
    loader = s('//*[@data-testid="viewVisaRequestSkeleton"]')
    visa_request_details = s('//*[@data-testid="visaRequestDetailsBox"]')
    visa_request_number = s('//*[@data-testid="visaRequestDetailsTableRowrequestNumberValue"]')
    visa_request_id = ss('//*[@data-testid="visaRequestDetailsTableRowvisaId"]//p').second
    visa_request_table = Table(s('//*[@data-testid="borderNumbersTable"]//table'))
    visa_request_statuses = ".//p[1]"
    visa_request_print_button = s('//*[@data-testid="printBtn"]')
    page_navigation_chain = s("//nav")
    page_title = ss('//div[@data-component="Layout"]/div[@data-component="Box"]//p').first
    back_to_visa_requests_button = page_navigation_chain.s(
        f'.//*[text()="{WORK_VISA_PAGE_TITLE_TEXT}"]'
    )
    visas = Table('//*[@data-testid="borderNumbersTable"]//table')
    cancel_modal = s('//*[@data-testid="visaRequestsModal"]')
    cancel_modal_title = cancel_modal.ss(".//p").first
    cancel_modal_content = cancel_modal.ss(".//p").second
    cancel_modal_cancel_visa_button = cancel_modal.s('.//button/p[text() = "Cancel visa"]')
    cancel_modal_go_back_button = cancel_modal.s('.//button/p[text() = "Go back"]')
    confirm_modal = s('//*[@data-testid="successModal"]')
    confirm_modal_title = confirm_modal.ss(".//p").first
    confirm_modal_content = confirm_modal.ss(".//p").second
    confirm_modal_back_button = confirm_modal.s(".//button")
    popup = FeedbackPopup('//*[@data-component="Modal"]')
    VISA_CANCEL_BUTTON = './/*[@data-testid="borderNumbersTableCancelBtn"]'

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
        scroll_to_top()
        self.visa_request_print_button.click()
        filename = get_downloaded_filename(timeout=20)
        verify_text_in_pdf(filename, check_data)

    @allure.step("Verify visa status in particular row has expected status")
    def verify_visa_status(
        self, expected_status: VisaRequestStatus, row: int | Condition[Element] = Numbers.ONE
    ) -> None:
        status_cell = self.visas.cell(row=row, column=ColName.VISA_STATUS)
        border_number = self.visas.cell(row=row, column=ColName.VISA_BORDER_NUMBER).get(query.text)
        soft_assert_text(
            status_cell,
            text=expected_status.label,
            element_name=f"Visa status with BN={border_number}",
        )
        if expected_status.expire:
            end_date = datetime.date.today() + relativedelta(years=+2)
            soft_assert_text(
                status_cell,
                text=end_date.strftime(DateFormats.DD_MM_YYYY),
                element_name=f"visa expiration date status with BN={border_number}",
            )

        if expected_status in VR_CANCELABLE:
            self.visas.cell(row=row, column=ColName.VISA_ACTIONS).s(
                self.VISA_CANCEL_BUTTON
            ).should(be.visible)
        else:
            self.visas.cell(row=row, column=ColName.VISA_ACTIONS).s(
                self.VISA_CANCEL_BUTTON
            ).should(be.hidden)

    @allure.step("Cancel visa with specified border number")
    def cancel_visa(self, border_number: str) -> None:
        self.visas.cell(row=have.text(border_number), column=ColName.VISA_ACTIONS).click()
        self.verify_cancel_modal_window(border_number=border_number)
        self.cancel_modal_go_back_button.click()
        self.visas.cell(row=have.text(border_number), column=ColName.VISA_ACTIONS).click()
        self.verify_cancel_modal_window(border_number=border_number)
        self.cancel_modal_cancel_visa_button.click()
        self.verify_confirm_modal_window(border_number=border_number)
        self.confirm_modal_back_button.click()
        self.popup.close_feedback_if_appeared()

    def verify_cancel_modal_window(self, border_number):
        self.cancel_modal.should(be.visible)
        soft_assert_text(
            self.cancel_modal_title, text=CANCEL_VISA, element_name="Cancel visa modal title"
        )
        soft_assert_text(
            self.cancel_modal_content,
            text=border_number,
            element_name="Cancel visa modal content border number",
        )
        self.cancel_modal_cancel_visa_button.should(be.visible)
        self.cancel_modal_go_back_button.should(be.visible)

    def verify_confirm_modal_window(self, border_number):
        self.confirm_modal.should(be.visible)
        soft_assert_text(
            self.confirm_modal_title,
            text=YOUR_REQUEST_HAS_BEEN_SENT,
            element_name="Confirm visa modal title",
        )
        soft_assert_text(
            self.confirm_modal_content,
            text=border_number,
            element_name="Confirm visa modal content border number",
        )
        self.confirm_modal_back_button.should(be.visible)

    def get_first_border_number(self):
        return self.visas.cell(row=Numbers.ONE, column=ColName.VISA_BORDER_NUMBER).get(query.text)
