from __future__ import annotations

import allure

from data.user_management.user_management_datasets import ArabicTranslations, Texts
from src.ui.pages.user_management_pages.main_page import UserManagementMainPage
from src.ui.pages.user_management_pages.owner_flow_page import OwnerFLowPage
from src.ui.pages.user_management_pages.user_detail_page import UserDetailsPage
from src.ui.qiwa import qiwa


class UserManagementActions(
    UserManagementMainPage, UserDetailsPage, OwnerFLowPage
):  # pylint: disable=too-many-ancestors
    @allure.step
    def log_in_and_navigate_to_um(self, user, sequence_number) -> UserManagementActions:
        qiwa.login_as_user(login=user)
        qiwa.workspace_page.select_company_account_with_sequence_number(
            sequence_number=sequence_number
        )
        qiwa.open_user_management_page()
        return self

    @allure.step
    def check_company_title_in_users_table(
        self, labor_office_id: int, seq_number: int
    ) -> UserManagementActions:
        title_test = f"Users in {labor_office_id}-{seq_number}"
        self.get_title_in_user_company_table(title_test)
        return self

    @allure.step
    def compare_number_of_users_in_table(self) -> UserManagementActions:
        self.wait_until_page_is_loaded()
        self.get_number_of_subscribed_user_in_company()
        self.compare_count_of_users_in_table()
        self.compare_count_of_users_in_company_table()
        return self

    @allure.step
    def navigate_to_view_details_page(self) -> UserManagementActions:
        self.wait_until_page_is_loaded()
        self.click_view_details_in_table()
        self.navigate_to_view_details()
        self.check_user_details_title(Texts.establishment_user_details)
        self.check_users_info_block()
        self.check_companies_table_is_displayed()
        return self

    @allure.title
    def navigate_to_owner_flow(self) -> UserManagementActions:
        self.wait_until_page_is_loaded()
        self.click_subscribe_btn()
        self.check_title(Texts.establishment_and_user_details)
        self.click_proceed_with_subscription_btn()
        self.check_title(Texts.add_new_workspace_user)
        return self

    @allure.step
    def check_localization_for_main_page(self) -> UserManagementActions:
        self.change_language_to_arabic()
        self.check_translation(
            ArabicTranslations.user_management_title,
            ArabicTranslations.add_new_user_btn,
            ArabicTranslations.user_role,
            ArabicTranslations.subscription_valid_until,
            ArabicTranslations.renew_info,
            ArabicTranslations.how_to_renew_btn,
        )
        return self

    @allure.step
    def check_localization_for_details_page(self) -> UserManagementActions:
        self.wait_until_page_is_loaded()
        self.click_view_details_in_table()
        self.navigate_to_view_details()
        self.check_user_details_title(Texts.establishment_user_details)
        self.change_language_to_arabic()
        self.check_ar_localization(
            ArabicTranslations.full_name,
            ArabicTranslations.national_id,
            ArabicTranslations.subscription_period,
            ArabicTranslations.subscription_expiry_date,
            ArabicTranslations.terminate_btn,
            ArabicTranslations.terminate_text,
            ArabicTranslations.establishment_table_title,
            ArabicTranslations.establishment_table_text,
            ArabicTranslations.search,
            ArabicTranslations.no_access,
            ArabicTranslations.establishment_name,
            ArabicTranslations.establishment_id,
            ArabicTranslations.privileges,
            ArabicTranslations.actions,
            ArabicTranslations.establishment_delegator_details_breadcrumbs,
        )
        return self
