from __future__ import annotations

from selene import browser
from selene.support.shared.jquery_style import s

import config


class LaborOfficeAppointmentsPage:
    book_appointment_btn = s("[data-component='Breadcrumbs'] + div p")

    def navigate_to_labor_office_appointments_page(self) -> LaborOfficeAppointmentsPage:
        browser.open(config.qiwa_urls.appointment_booking)
        return self

    def click_book_appointment_btn(self) -> LaborOfficeAppointmentsPage:
        self.book_appointment_btn.click()
        return self
