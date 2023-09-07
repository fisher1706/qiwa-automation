from selene import have
from selene.support.shared.jquery_style import s, ss

from data.constants import Titles
from src.ui.components.raw.table import Table


class RequestsPage:
    header = s('.c-change-requests__heading')
    change_occupation_requests = Table(s('.table'))
    detail = ss('.detail .c-change-requests__laborer-item-value')
    iqama_number = detail[1]
    request_status = detail[3]
    iqama_number_bulk = detail[7]
    request_status_bulk = detail[9]
    btn_return_to_the_previous_page = s('.c-change-requests__action--back button')

    def check_request_title(self):
        self.header.hover().should(have.exact_text(Titles.CHANGE_OCCUPATION_REQUEST))
        return self

    def expand_details(self):
        self.change_occupation_requests.row(1).cell('Actions').s('a').click()
        return self

    def check_iqama_number(self, iqama_number: str):
        self.iqama_number.should(have.exact_text(iqama_number))
        return self

    def check_request_status(self, request_status: str):
        self.request_status.should(have.exact_text(request_status))
        return self

    def check_iqama_number_bulk(self, iqama_number: str):
        self.iqama_number_bulk.should(have.exact_text(iqama_number))
        return self

    def check_request_status_bulk(self, request_status: str):
        self.request_status_bulk.should(have.exact_text(request_status))
        return self

    def click_btn_return_to_the_previous_page(self):
        self.btn_return_to_the_previous_page.click()
        return self
