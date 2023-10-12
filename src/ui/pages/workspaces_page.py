from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss
from selenium.common import NoSuchElementException


class WorkspacesPage:
    page_content = s('//*[@data-component="Layout"]//*[contains(@class, "Tile")]')
    label_choose_account = s("//*[text()='Choose your account type']")

    dropdown_choose_language = s('(//*[contains(@class, "NavigationAction")])[1]')
    option_language_en = s('//*[contains(text(), "English")]')

    account_cards = ss("[data-component='Tile']")
    individual_account_card = account_cards.element_by(have.text("Individual account"))
    lo_agent_card = account_cards.element_by(have.text("LO agent"))
    business_account_card = account_cards.element_by(have.text("Business Account"))
    admin_account_card = account_cards.element_by(have.text("Qiwa Admin"))
    business_account_list = ss("[data-component='TabPanel'] button")
    search = s("#search")
    lmi_admin_card = ss("[data-component='Tile'] p").element_by(have.text("LMI Admin"))

    @allure.step
    def should_have_workspace_list_appear(self) -> WorkspacesPage:
        self.account_cards[0].wait_until(be.visible)
        return self

    @allure.step
    def wait_page_to_load(self) -> WorkspacesPage:
        for _ in range(3):
            try:
                self.label_choose_account.should(be.visible)
            except NoSuchElementException:
                browser.driver.refresh()
                continue
        return self

    @allure.step
    def select_admin_account(self) -> WorkspacesPage:
        self.admin_account_card.click()
        return self

    @allure.step
    def select_individual_account(self) -> WorkspacesPage:
        self.individual_account_card.click()
        return self

    @allure.step
    def select_lo_agent(self) -> WorkspacesPage:
        self.lo_agent_card.click()
        return self

    @allure.step
    def select_business_account(self) -> WorkspacesPage:
        self.business_account_card.click()
        return self

    @allure.step
    def select_first_company_account(self) -> WorkspacesPage:
        self.select_business_account()
        self.business_account_list.first.click()
        return self

    @allure.step
    def select_company_account_with_sequence_number(
        self, sequence_number: int | str
    ) -> WorkspacesPage:
        self.select_business_account()
        self.business_account_list.element_by(have.text(str(sequence_number))).click()
        return self

    @allure.step
    def select_company_account_by_name(self, name: str) -> WorkspacesPage:
        self.select_business_account()
        self.search.type(name)
        self.business_account_list.second.click()
        return self

    @allure.step
    def select_lmi_admin(self) -> WorkspacesPage:
        self.lmi_admin_card.click()
        return self
