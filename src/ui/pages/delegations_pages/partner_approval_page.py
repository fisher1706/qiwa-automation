from __future__ import annotations

import allure
from selene import browser, have
from selene.support.shared.jquery_style import s

import config
from data.delegation import general_data


class PartnerApprovalPage:
    page_title = s('p[data-testid="SendCodeTitle"]')
    title_on_unavailable_flow = s('p[data-testid="RequestNoValidTitle"]')
    subtitle_on_unavailable_flow = s('p[data-testid="RequestNoValidSubTitle"]')
    description_on_unavailable_flow = s('p[data-testid="RequestNoValidDescription"]')

    @allure.step
    def wait_partner_approval_page_to_load(self) -> PartnerApprovalPage:
        self.page_title.should(have.exact_text(general_data.TITLE_ON_PARTNER_APPROVAL))
        return self

    @allure.step
    def should_partner_approval_flow_be_not_available(self) -> PartnerApprovalPage:
        browser.should(have.url(f"{config.qiwa_urls.delegation_service}/request-no-valid"))
        self.title_on_unavailable_flow.should(
            have.exact_text(general_data.TITLE_ON_UNAVAILABLE_FLOW)
        )
        self.subtitle_on_unavailable_flow.should(
            have.exact_text(general_data.SUBTITLE_ON_UNAVAILABLE_FLOW)
        )
        self.description_on_unavailable_flow.should(
            have.exact_text(general_data.DESCRIPTION_ON_UNAVAILABLE_FLOW)
        )
        return self
