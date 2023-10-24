from __future__ import annotations

import allure
from selene import have
from selene.support.shared.jquery_style import s, ss

from data.delegation import general_data


class DelegationLocalisationChange:
    general_buttons = ss('[data-component="MenuTrigger"] button')
    localisation_button_on_public_pages = ss('[data-component="MenuTrigger"] button').element(0)
    english_localisation = s('div[data-component="Menu"] a:nth-child(1)')

    @allure.step
    def select_english_localisation_for_delegation_service(self) -> DelegationLocalisationChange:
        localisation_button = self.general_buttons.element(1).click()
        self.english_localisation.click()
        localisation_button.s('[data-component="Box"] p').wait_until(
            have.exact_text(general_data.ENGLISH_LOCAL)
        )
        return self

    @allure.step
    def select_english_localisation_for_public_pages(self) -> DelegationLocalisationChange:
        localisation_button = self.general_buttons.element(0).click()
        self.english_localisation.click()
        localisation_button.s('[data-component="Box"] p').wait_until(
            have.exact_text(general_data.ENGLISH_LOCAL)
        )
        return self
