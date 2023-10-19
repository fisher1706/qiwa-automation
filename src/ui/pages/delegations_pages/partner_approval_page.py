from __future__ import annotations

import allure
from selene import browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.delegation import general_data


class PartnerApprovalPage:
    page_title = s("p.jTYGiy")
    title_on_invalid_link = s("p.kskrEg")
    toast = s('[data-component="Toast"]')
    localization_button = ss('[data-component="MenuTrigger"] button').element(0)
    localization_state = localization_button.s('[data-component="Box"] p')
    english_localization = s('div[data-component="Menu"] a:nth-child(1)')

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
        self.toast.should(have.exact_text(general_data.ERROR_TOAST))
        return self

    @allure.step
    def select_english_localization_on_partner_approval_page(self) -> PartnerApprovalPage:
        # pylint: disable=R0801
        # TODO move method to components
        self.localization_button.click()
        self.english_localization.click()
        self.localization_state.wait_until(have.exact_text(general_data.ENGLISH_LOCAL))
        return self
