from __future__ import annotations

import allure
from selene import browser, have
from selene.support.shared.jquery_style import s

import config
from data.delegation import general_data


class PartnerApprovalPage:
    page_title = s("p.jTYGiy")
    title_on_invalid_link = s("p.kskrEg")

    @allure.step
    def wait_partner_approval_page_to_load(self) -> PartnerApprovalPage:
        self.page_title.should(have.exact_text(general_data.TITLE_ON_PARTNER_APPROVAL))
        return self

    @allure.step
    def should_partner_approval_flow_be_not_available(self) -> PartnerApprovalPage:
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/request-no-valid"))
        self.title_on_invalid_link.should(
            have.exact_text(general_data.TITLE_ON_NOT_AVAILABLE_FLOW)
        )
        return self
