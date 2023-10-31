from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s

from data.delegation import general_data


class RevokeModal:
    revoke_modal = s('div[data-testid="RevokeModal"]')
    revoke_button_on_modal = s('button[data-testid="RevokeModalAction"]')
    title_on_modal = s('p[data-testid="RevokeModalTitle"]')
    description_on_modal = s('p[data-testid="RevokeModalDescription"]')
    go_back_button_on_revoke_modal = s('button[data-testid="RevokeModalClose"]')
    close_button_on_modal = s('button[aria-label="Close modal"]')

    @allure.step
    def should_revoke_confirmation_modal_be_displayed(
        self,
    ) -> RevokeModal:
        self.revoke_modal.should(be.visible)
        self.title_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_TITLE))
        self.description_on_modal.should(have.exact_text(general_data.REVOKE_MODAL_DESCRIPTION))
        self.revoke_button_on_modal.should(have.exact_text(general_data.REVOKE_BUTTON))
        self.go_back_button_on_revoke_modal.should(have.exact_text(general_data.GO_BACK_BUTTON))
        self.close_button_on_modal.should(be.visible)
        return self

    @allure.step
    def click_revoke_delegation_button(self) -> RevokeModal:
        self.revoke_button_on_modal.click()
        return self
