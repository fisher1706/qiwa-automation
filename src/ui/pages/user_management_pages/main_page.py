import dataclasses

import allure
from selene import be, have, query
from selene.support.shared.jquery_style import s, ss


@dataclasses.dataclass
class MainPageLocators:
    # todo: Move locators to the page class and rename string variables to element s, ss accordingly
    ADD_NEW_USER_BTN = "button[data-testid='add-user-btn'] p"
    USER_MANAGEMENT_TITLE = "//div[contains(@data-testid, 'page-title')]/div/div/p"

    YOUR_SUBSCRIPTION_TITLE = "//div[contains(@data-testid, 'your-subscription')]/p"
    USERS_ROLE = "//div[contains(@data-testid, 'owner-role')]//p"
    SUBSCRIPTION_VALID_UNTIL_TEXT = (
        "//div[contains(@data-testid, 'your-subscription')]//tbody/tr[3]/td/div/p"
    )
    SUBSCRIPTION_INFO_TEXT = "//*/table/tbody/tr[3]/td/div[2]/div[1]/p"
    SUBSCRIPTION_INFO_USER_NAME = "//*/table[contains(@class,'kVWEpi')]/tbody/tr[1]/td/div/p"
    HOW_TO_RENEW_BTN = "//div[contains(@data-testid, 'your-subscription')]//td/div/a/span"

    SEARCH_FIELD = "#search"
    COUNT_OF_USERS_IN_SELECTED_TAB_USERS_TABLE = (
        "//button[contains(@aria-selected,'true')]/div/div/p"
    )
    UNSELECTED_TAB_USERS_TABLE_BTN = "//button[contains(@aria-selected,'false')]"

    USERS_PERSONAL_NUMBER_IN_USERS_TABLE = ".hfRNGV:nth-child(2)"
    USER_NAME_IN_USERS_TABLE = ".hfRNGV:nth-child(1)"
    USER_STATUS_IN_USERS_TABLE = "div[data-testid='row-status-action'] div[role='status']"
    USERS_IN_COMPANY_TABLE = "//div[contains(@id, 'tabpanel-:r3:-0')]/div/div/div/table/tbody"
    USERS_IN_TABLE = "//div[contains(@id, 'tabpanel-:r0:-0')]/div/div/div/table/tbody"
    TITLE_IN_USERS_IN_COMPANY_TAB = "//button[contains(@id, 'tab-:r0:-0')]/div/p"
    TABLE_TRS = "tr.iaVuuG"
    USERS_TABLE = "table.kJwdzn"
    USERS_IN_UN_TABLE = "//div[contains(@id, 'tabpanel-:r0:-1')]/div/div/div/table/tbody"
    ACTION_BTN_TABLE = "td button[data-testid='row-actions']"
    USER_ROLE_IN_TABLE = "//div[contains(@id, 'tabpanel-:r0:-0')]//tbody/tr[1]/td[4]"
    VIEW_DETAILS_BTN = "button[data-testid='view-action']"
    RENEW_SUBSCRIPTION_BTN = "button[data-testid='renew-action']"

    NEXT_BTN_PAGINATION = "//button/span[contains(text(), 'Next')]"
    PREVIOUS_BTN_PAGINATION = "//button/span[contains(text(), 'Previous')]"
    FIRST_PAGE_BTN = "//button[contains(@aria-label, 'Page 1')]"
    SECOND_PAGE_BTN = "//button[contains(@aria-label, 'Page 2')]"

    CHANGE_LANGUAGE_ICON = (
        "//div[2]/div/button[contains(@class,'MenuTrigger__Trigger-ds__sc-4nl56o-0')]"
    )
    ARABIC_LANGUAGE = (
        "//div[contains(@data-component,'Menu')]/div/div/div/div[contains(@data-component,"
        "'NavigationGroup')]/a[2]"
    )


class MainPage(MainPageLocators):
    def __init__(self):
        super().__init__()
        self.users_count = None

    def wait_until_page_is_loaded(self):
        s(self.USERS_IN_COMPANY_TABLE).wait_until(be.visible)

    def click_subscribe_btn(self):
        s(self.ADD_NEW_USER_BTN).click()

    def check_subscription_text_is_present(self, subscription_info_text: str):
        s(self.SUBSCRIPTION_INFO_TEXT).wait_until(be.visible)
        s(self.SUBSCRIPTION_INFO_TEXT).should(have.text(subscription_info_text))

    def input_user_name_or_id(self, user_info: str):
        s(self.SEARCH_FIELD).clear().type(user_info)

    def check_user_personal_number(self, personal_number: str):
        user_personal_number = s(self.USERS_PERSONAL_NUMBER_IN_USERS_TABLE)
        user_personal_number.wait_until(be.visible)
        user_personal_number.should(have.text(personal_number))

    def select_users_in_establishment_tab(self):
        s(self.UNSELECTED_TAB_USERS_TABLE_BTN).click()

    def check_user_name(self, user_name: str):
        user_name_tr = s(self.USERS_IN_COMPANY_TABLE)
        user_name_tr.wait_until(be.visible)
        user_name_tr.s(self.USER_NAME_IN_USERS_TABLE).should(have.text(user_name))

    def get_user_name(self):
        return s(self.SUBSCRIPTION_INFO_USER_NAME).get(query.text)

    def get_title_in_user_company_table(self, title_test: str):
        title = s(self.TITLE_IN_USERS_IN_COMPANY_TAB)
        title.wait_until(be.visible)
        title.should(have.text(title_test))

    def get_number_of_subscribed_user_in_company(self, selected: bool = True):
        if selected is False:
            self.select_users_in_establishment_tab()
        self.users_count = s(self.COUNT_OF_USERS_IN_SELECTED_TAB_USERS_TABLE).get(query.text)
        return self.users_count

    def get_users_in_table(self):
        return s(self.USERS_IN_TABLE).ss(self.TABLE_TRS).should(have.size(int(self.users_count)))

    def get_all_users_in_table(self):
        table = s(self.USERS_IN_UN_TABLE)
        table.should(be.visible)
        all_users_list = []
        for row_first_page in table.ss(self.TABLE_TRS):
            all_users_list.append(row_first_page)
        if s(self.NEXT_BTN_PAGINATION).matching(be.visible):
            s(self.NEXT_BTN_PAGINATION).click()
            table.should(be.visible)
            for row_second_page in table.ss(self.TABLE_TRS):
                all_users_list.append(row_second_page)
        return len(all_users_list)

    def click_view_details_in_table(self):
        ss(self.ACTION_BTN_TABLE).first.should(be.visible).click()

    def navigate_to_view_details(self):
        s(self.VIEW_DETAILS_BTN).should(be.visible).click()

    def check_user_status(self, selected: bool = True):
        table = s(self.USERS_IN_COMPANY_TABLE)
        table.wait_until(be.visible)
        if selected is False:
            self.select_users_in_establishment_tab()
            table = s(self.USERS_IN_UN_TABLE)
        for row in table.ss(self.TABLE_TRS):
            if row.s(self.USER_STATUS_IN_USERS_TABLE).matching(have.text("Active")):
                row.s(self.ACTION_BTN_TABLE).should(be.visible).click()
                s(self.VIEW_DETAILS_BTN).matching(be.visible)
                s(self.ACTION_BTN_TABLE).should(be.visible).click()
            elif row.s(self.USER_STATUS_IN_USERS_TABLE).matching(have.text("Inactive")):
                row.s(self.ACTION_BTN_TABLE).should(be.visible).click()
                s(self.RENEW_SUBSCRIPTION_BTN).matching(be.visible)
                s(self.ACTION_BTN_TABLE).should(be.visible).click()

    @allure.step
    def check_pagination_btns(self):
        self.select_users_in_establishment_tab()
        s(self.SECOND_PAGE_BTN).should(be.clickable).click()
        s(self.PREVIOUS_BTN_PAGINATION).matching(be.visible)
        s(self.NEXT_BTN_PAGINATION).matching(be.not_.visible)

        s(self.FIRST_PAGE_BTN).should(be.clickable).click()
        s(self.PREVIOUS_BTN_PAGINATION).matching(be.not_.visible)
        s(self.NEXT_BTN_PAGINATION).matching(be.visible)

    @allure.step
    def check_owner_role_in_table(self):
        s(self.USER_ROLE_IN_TABLE).should(have.text("Group Manager"))

    @allure.step
    def change_language_to_arabic(self):
        s(self.CHANGE_LANGUAGE_ICON).should(be.visible).click()
        s(self.ARABIC_LANGUAGE).should(be.visible).click()

    @allure.step
    def check_translation(
        self, text1: str, text2: str, text4: str, text5: str, text6: str, text7: str
    ):
        self.wait_until_page_is_loaded()
        s(self.USER_MANAGEMENT_TITLE).should(be.visible).should(have.text(text1))
        s(self.ADD_NEW_USER_BTN).should(be.visible).should(have.text(text2))
        s(self.USERS_ROLE).should(be.visible).should(have.text(text4))
        s(self.SUBSCRIPTION_VALID_UNTIL_TEXT).should(be.visible).should(have.text(text5))
        s(self.SUBSCRIPTION_INFO_TEXT).should(be.visible).should(have.text(text6))
        s(self.HOW_TO_RENEW_BTN).should(be.visible).should(have.text(text7))

    @allure.step
    def confirm_that_action_btn_is_missed(self):
        ss(self.ACTION_BTN_TABLE).first.should(be.absent)
