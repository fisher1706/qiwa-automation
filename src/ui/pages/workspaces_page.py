import time

import allure
from selene import be, have
from selene.support.shared.jquery_style import ss


class WorkspacesPage:
    account_cards = ss("[data-component='Tile']")
    individual_account_card = account_cards.element_by(have.text("Individual account"))
    lo_agent_card = account_cards.element_by(have.text("LO agent"))
    business_account_card = account_cards.element_by(have.text("Business Account"))
    admin_account_card = account_cards.element_by(have.text("Qiwa Admin"))
    business_account_list = ss("[data-component='TabPanel'] button")

    @allure.step
    def should_have_workspace_list_appear(self):
        self.account_cards.should(be.clickable.each)
        return self

    @allure.step
    def select_admin_account(self):
        self.admin_account_card.click()
        return self

    @allure.step
    def select_individual_account(self):
        self.individual_account_card.click()
        return self

    @allure.step
    def select_lo_agent(self):
        # TODO investigate the possibility to remove time sleep
        time.sleep(5)
        self.lo_agent_card.click()
        return self

    @allure.step
    def select_business_account(self):
        # TODO investigate the possibility to remove time sleep
        time.sleep(10)
        self.business_account_card.click()
        return self

    @allure.step
    def select_first_company_account(self):
        self.select_business_account()
        self.business_account_list.first.click()
        return self

    @allure.step
    def select_company_account_with_sequence_number(self, sequence_number: int | str):
        self.select_business_account()
        self.business_account_list.element_by(have.text(str(sequence_number))).click()
        return self
