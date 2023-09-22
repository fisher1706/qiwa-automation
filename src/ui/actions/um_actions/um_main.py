import allure

from data.um.um_datasets import ArabicTranslations, Texts
from src.ui.actions.sign_in import LoginActions
from src.ui.pages.um_pages.main_page import MainPage
from src.ui.pages.um_pages.owner_flow_page import OwnerFLowPage
from src.ui.pages.um_pages.user_detail_page import UserDetailsPage
from src.ui.pages.workspaces_page import WorkspacesPage


class MainPageActions(
    MainPage, UserDetailsPage, OwnerFLowPage
):  # pylint: disable=too-many-ancestors
    def __init__(self):
        super().__init__()
        self.login_action = LoginActions()
        self.workspace_actions = WorkspacesPage()

    @allure.step
    def log_in_and_navigate_to_um(self, user):
        self.login_action.complete_login(user.account)
        self.workspace_actions.select_first_company_account()
        MainPage.navigate_to_user_management()

    @allure.step
    def check_texts_on_main_page(self):
        self.check_subscription_text_is_present(Texts.SUBSCRIPTION_INFO)

    @allure.step
    def check_search_main_page(self, user_info):
        for data_type in user_info:
            self.input_user_name_or_id(data_type)
            self.check_user_personal_number(user_info[0])
            self.check_user_name(user_info[1])

    @allure.step
    def check_company_title_in_users_table(self, labor_office_id: int, seq_number: int):
        title_test = f"Users in {labor_office_id}-{seq_number}"
        self.get_title_in_user_company_table(title_test)

    @allure.step
    def compare_number_of_users_in_table(self):
        self.wait_until_page_is_loaded()
        self.get_number_of_subscribed_user_in_company()
        self.get_users_in_table()
        count_of_users = self.get_number_of_subscribed_user_in_company(False)
        assert count_of_users == str(self.get_all_users_in_table())

    @allure.step
    def navigate_to_view_details_page(self):
        self.wait_until_page_is_loaded()
        self.click_view_details_in_table()
        self.navigate_to_view_details()
        self.check_user_details_title(Texts.Workspace_User_Details)

    @allure.title
    def navigate_to_owner_flow(self):
        self.wait_until_page_is_loaded()
        self.click_subscribe_btn()
        self.check_title(Texts.Establishment_And_User_Details)
        self.click_proceed_with_subscription_btn()
        self.check_title(Texts.Add_New_Workspace_User)

    @allure.step
    def check_localization(self):
        self.check_translation(
            ArabicTranslations.User_Management_Title,
            ArabicTranslations.Add_New_User_Btn,
            ArabicTranslations.Your_Subscription_Title,
            ArabicTranslations.User_Role,
            ArabicTranslations.Subscription_Valid_Until,
            ArabicTranslations.SUBSCRIPTION_Info_Text,
            ArabicTranslations.Extend_Subscription_Btn,
            ArabicTranslations.How_To_Renew_Btn,
            ArabicTranslations.Search,
        )
