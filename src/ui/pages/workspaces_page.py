from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s, ss

from data.constants import Language, Workspaces
from utils.allure import allure_steps


@allure_steps
class WorkspacesPage:
    language = Language.EN
    page_content = s('//*[@data-component="Layout"]//*[contains(@class, "Tile")]')
    label_choose_account = s("//*[text()='Choose your account type']")

    dropdown_choose_language = s('(//*[contains(@class, "NavigationAction")])[1]')
    option_language_en = s('//*[contains(text(), "English")]')

    account_cards = ss("[data-component='Tile']")
    individual_account_card = account_cards.element_by(have.text("Individual account"))
    lo_agent_card = account_cards.element_by(have.text("LO agent"))
    admin_account_card = account_cards.element_by(have.text("Qiwa Admin"))
    business_account_list = ss("[data-component='TabPanel'] button")
    search = s("#search")
    lmi_admin_card = ss("[data-component='Tile'] p").element_by(have.text("LMI Admin"))
    btn_subscribe = ss("//*[@id='tabpanel-:r0:-0']//button//a")

    def should_have_workspace_list_appear(self) -> WorkspacesPage:
        self.account_cards[0].with_(timeout=120).wait_until(be.visible)
        return self

    def wait_page_to_load(self) -> WorkspacesPage:
        self.label_choose_account.should(be.visible)
        return self

    def select_admin_account(self) -> WorkspacesPage:
        self.admin_account_card.click()
        return self

    def select_individual_account(self) -> WorkspacesPage:
        self.individual_account_card.wait_until(be.visible)
        self.individual_account_card.click()
        return self

    def select_lo_agent(self) -> WorkspacesPage:
        self.lo_agent_card.click()
        return self

    def select_business_account(self) -> WorkspacesPage:
        business_account_card = self.account_cards.element_by(
            have.text(Workspaces.BUSINESS_ACCOUNT_CARD[self.language])
        )
        business_account_card.click()
        return self

    def select_first_company_account(self) -> WorkspacesPage:
        self.select_business_account()
        self.business_account_list.first.click()
        return self

    def select_company_account_with_sequence_number(
        self, sequence_number: int | str
    ) -> WorkspacesPage:
        self.select_business_account()
        self.business_account_list.element_by(have.text(str(sequence_number))).click()
        return self

    def select_company_account_by_name(self, name: str) -> WorkspacesPage:
        self.select_business_account()
        self.search.type(name)
        self.business_account_list[0].should(have.text(name)).click()
        return self

    def select_lmi_admin(self) -> WorkspacesPage:
        self.lmi_admin_card.click()
        return self

    def click_btn_subscribe(self, user_type: str, number: int = None) -> WorkspacesPage:
        if user_type != "active":
            self.btn_subscribe[number].click() if number else self.btn_subscribe[0].click()
        else:
            for item in self.btn_subscribe:
                item.should(be.hidden)
        return self
