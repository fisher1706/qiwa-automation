from __future__ import annotations

from selene import have
from selene.support.shared.jquery_style import s, ss


class LaborOfficeAppointmentsCreatePage:
    search = s("#establishment-list")
    establishment_list = ss("[data-component='RadioButton'] span")
    next_btn = s("[type='submit']")
    service = s("#service")
    dropdown = ss("[class='tippy-content'] li")
    sub_service = s("#subService")
    sub_service_error = s("#subService-error")

    def select_establishment(self, name: str) -> LaborOfficeAppointmentsCreatePage:
        self.search.type(name)
        self.establishment_list.first.click()
        self.next_btn.click()
        return self

    def select_service_and_sub_service(
        self, service: str, sub_service: str
    ) -> LaborOfficeAppointmentsCreatePage:
        self.service.click()
        self.dropdown.element_by(have.exact_text(service)).click()
        self.sub_service.click()
        self.dropdown.element_by(have.exact_text(sub_service)).click()
        return self

    def check_sub_service_error(self, text: str) -> LaborOfficeAppointmentsCreatePage:
        self.sub_service_error.should(have.exact_text(text))
        return self
