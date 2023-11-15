from __future__ import annotations

from datetime import datetime

import allure
from selene import have, query
from selene.support.shared.jquery_style import s, ss


class BusinessPage:
    ESTABLISHMENT_INFORMATION = ss(".q-page-box__list dd")
    ESTABLISHMENT_STATUS = ESTABLISHMENT_INFORMATION[3]
    CR_END_DATE = ESTABLISHMENT_INFORMATION[8]

    QIWA_SERVICES = ss(".service-item")
    CHANGE_OCCUPATION = QIWA_SERVICES.element_by(have.text("Change Occupation"))
    LO_WORK_PERMIT = QIWA_SERVICES.element_by(have.text("Work Permit"))
    LO_SAUDI_CERTIFICATE = s(".service-item .btn")

    def check_establishment_status(self, status: str) -> BusinessPage:
        self.ESTABLISHMENT_STATUS.should(have.exact_text(status))
        return self

    def check_cr_end_date(self) -> BusinessPage:
        assert self.CR_END_DATE.get(query.text) >= datetime.today().strftime("%Y-%m-%d")
        return self

    def select_change_occupation(self) -> BusinessPage:
        self.CHANGE_OCCUPATION.s(".btn").click()
        return self

    def select_work_permit(self) -> BusinessPage:
        self.LO_WORK_PERMIT.s(".btn").click()
        return self

    @allure.step("click on saudi certificate btn")
    def select_saudization_certificate(self) -> BusinessPage:
        self.LO_SAUDI_CERTIFICATE.click()
        return self
