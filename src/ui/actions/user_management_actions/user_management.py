import allure

from data.user_management.user_management_datasets import ArabicTranslations, Texts
from src.ui.pages.user_management_pages.main_page import MainPage
from src.ui.pages.user_management_pages.owner_flow_page import OwnerFLowPage
from src.ui.pages.user_management_pages.user_detail_page import UserDetailsPage
from src.ui.qiwa import qiwa


class UserManagementActions(
    MainPage, UserDetailsPage, OwnerFLowPage
):  # pylint: disable=too-many-ancestors
    @allure.step
    def log_in_and_navigate_to_um(self, user, sequence_number):
        qiwa.login_as_user(login=user)
        qiwa.workspace_page.select_company_account_with_sequence_number(
            sequence_number=sequence_number
        )
        qiwa.open_user_management_page()

    @allure.step
    def check_texts_on_main_page(self):
        self.check_subscription_text_is_present(Texts.subscription_info)

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
        self.check_user_details_title(Texts.establishment_user_details)

    @allure.title
    def navigate_to_owner_flow(self):
        self.wait_until_page_is_loaded()
        self.click_subscribe_btn()
        self.check_title(Texts.establishment_and_user_details)
        self.click_proceed_with_subscription_btn()
        self.check_title(Texts.add_new_workspace_user)

    @allure.step
    def check_localization(self):
        self.change_language_to_arabic()
        self.check_translation(
            ArabicTranslations.user_management_title,
            ArabicTranslations.add_new_user_btn,
            ArabicTranslations.user_role,
            ArabicTranslations.subscription_valid_until,
            ArabicTranslations.renew_info,
            ArabicTranslations.how_to_renew_btn,
        )
