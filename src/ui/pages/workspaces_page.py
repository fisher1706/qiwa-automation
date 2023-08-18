import time

import allure
from selene import Element, be, command, have
from selene.support.shared.jquery_style import s, ss


class WorkspacesPage:
    account_cards = s(".gXYHZg")
    individual_account_card = s(".hmkUlH")
    business_account_card = s(".feHDll")
    admin_account_card = s(".gORgzz")
    business_account_list = ss('[id="tabpanel-:r0:-0"] button')

    @allure.step
    def should_have_workspace_list_appear(self) -> Element:
        return self.account_cards.should(be.clickable)

    @allure.step
    def select_admin_account(self):
        self.admin_account_card.click()
        return self

    @allure.step
    def select_individual_account(self):
        self.individual_account_card.click()
        return self

    @allure.step
    def select_first_company_account(self):
        time.sleep(6)
        self.business_account_card.hover().click()
        self.business_account_list.first.click()
        return self

    @allure.step
    def select_company_account_with_sequence_number(self, sequence_number: int | str):
        self.business_account_list.element_by_its(
            ".workspaces-number", have.text(str(sequence_number))
        )
        return self
