from __future__ import annotations

from datetime import datetime

from selene import query, have
from selene.support.shared.jquery_style import ss


class BusinessPage:
    ESTABLISHMENT_INFORMATION = ss('.q-page-box__list dd')
    ESTABLISHMENT_STATUS = ESTABLISHMENT_INFORMATION[3]
    CR_END_DATE = ESTABLISHMENT_INFORMATION[8]

    QIWA_SERVICES = ss('.service-item')
    CHANGE_OCCUPATION = QIWA_SERVICES.element_by(have.text('Change Occupation'))

    def check_establishment_status(self, status: str) -> BusinessPage:
        self.ESTABLISHMENT_STATUS.should(have.exact_text(status))
        return self

    def check_cr_end_date(self) -> BusinessPage:
        assert self.CR_END_DATE.get(query.text) >= datetime.today().strftime('%Y-%m-%d')
        return self

    def select_change_occupation(self) -> BusinessPage:
        self.CHANGE_OCCUPATION.s('.btn').click()
        return self
