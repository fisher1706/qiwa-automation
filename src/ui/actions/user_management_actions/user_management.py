from __future__ import annotations

import allure

from data.constants import Language
from data.user_management.user_management_datasets import (
    ArabicTranslations,
    Privileges,
    Texts,
)
from src.ui.pages.user_management_pages.annual_subscription_page import (
    AnnualSubscription,
)
from src.ui.pages.user_management_pages.establishment_user_details_page import (
    EstablishmentUser,
)
from src.ui.pages.user_management_pages.main_page import UserManagementMainPage
from src.ui.pages.user_management_pages.owner_flow_page import OwnerFLowPage
from src.ui.pages.user_management_pages.payment_summary_page import PaymentSummary
from src.ui.pages.user_management_pages.user_detail_page import UserDetailsPage
from src.ui.pages.user_management_pages.thank_you_page import ThankYouPage
from src.ui.qiwa import qiwa


class UserManagementActions(
    UserManagementMainPage,
    UserDetailsPage,
    OwnerFLowPage,
    EstablishmentUser,
    AnnualSubscription,
    PaymentSummary,
    ThankYouPage
):  # pylint: disable=too-many-ancestors
    @allure.step
    def log_in_and_navigate_to_um(self, user, sequence_number) -> UserManagementActions:
        qiwa.login_as_user(login=user)
        qiwa.workspace_page.should_have_workspace_list_appear()
        qiwa.header.change_local(Language.EN)
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
    def navigate_to_view_details_page(self, user_nid: str = None) -> UserManagementActions:
        if user_nid is None:
            self.click_view_details_in_table()
        else:
            self.click_view_details_in_table_for_selected_user(user_nid)
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
        self.click_view_details_in_table()
        self.navigate_to_view_details()
        self.check_user_details_title(Texts.establishment_user_details)
        qiwa.header.change_local(Language.AR)
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

    @allure.step
    def open_select_privileges_modal_for_no_access_workspace(self) -> UserManagementActions:
        self.select_no_access_tab()
        self.click_add_access_button()
        self.check_select_privileges_modal_is_displayed()
        return self

    @allure.step
    def check_privileges_are_grouped(self) -> UserManagementActions:
        self.click_show_more_privileges_btn_for_groups()
        self.check_privileges_group_names(Privileges.groups_data)
        return self

    @allure.step
    def select_all_privileges(self) -> UserManagementActions:
        self.wait_until_privilege_list_is_displayed()
        self.click_all_privileges_checkbox()
        self.check_privileges_are_selected()
        return self

    @allure.step
    def unselect_the_privilege(self, privilege_name: str) -> UserManagementActions:
        self.click_privilege_from_the_list(privilege_name)
        self.check_all_privileges_checkbox_is_unselected()
        return self

    @allure.step
    def unselect_all_privileges(self) -> UserManagementActions:
        self.click_all_privileges_checkbox()
        self.check_non_default_privileges_are_unselected()
        return self

    @allure.step
    def check_establishment_user_details(self) -> UserManagementActions:
        self.wait_until_page_load(locator=EstablishmentUser.main_text)
        self.click_btn_proceed_subscription()
        return self

    @allure.step
    def check_annual_subscription(self) -> UserManagementActions:
        self.wait_until_page_load(locator=AnnualSubscription.main_text)
        self.check_checkbox_read_accept()
        self.click_button_go_to_payment()
        return self

    @allure.step
    def make_establishment_payment(self, payment: str = None) -> UserManagementActions:
        self.wait_until_page_load(locator=PaymentSummary.main_text)
        self.choose_and_make_payment(payment_type=payment)
        self.check_checkbox_read_accept()
        self.click_btn_submit_pay()
        self.complete_payment(payment_type=payment)
        return self

    @allure.step
    def check_thank_you_page(self) -> UserManagementActions:
        self.wait_until_page_load(locator=ThankYouPage.main_text)
        self.check_data_thank_you_page()
        return self
