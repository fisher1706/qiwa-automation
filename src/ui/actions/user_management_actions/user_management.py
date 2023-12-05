from __future__ import annotations

import allure
from selene import have
from selene.support.conditions import be

from data.constants import Language
from data.user_management import user_management_data
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
from src.ui.pages.user_management_pages.renew_subscription_page import RenewSubscription
from src.ui.pages.user_management_pages.thank_you_page import ThankYouPage
from src.ui.pages.user_management_pages.user_detail_page import UserDetailsPage
from src.ui.qiwa import qiwa


class UserManagementActions(
    UserManagementMainPage,
    UserDetailsPage,
    OwnerFLowPage,
    EstablishmentUser,
    AnnualSubscription,
    PaymentSummary,
    ThankYouPage,
    RenewSubscription,
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
    def open_select_privileges_modal_for_no_access_workspace(
        self, establishment: str
    ) -> UserManagementActions:
        self.switch_to_tab(user_management_data.NO_ACCESS)
        self.click_add_access_button_for_workspace_without_access(establishment)
        self.check_add_privileges_modal_is_displayed()
        return self

    @allure.step
    def check_privileges_are_grouped(self) -> UserManagementActions:
        self.click_show_more_privileges_btn_for_all_groups()
        self.check_privileges_group_names(Privileges.groups_data)
        return self

    @allure.step
    def select_all_privileges(self) -> UserManagementActions:
        self.wait_until_privilege_list_is_displayed()
        self.click_all_privileges_checkbox()
        self.check_all_privileges_are_selected()
        return self

    @allure.step
    def unselect_the_privilege(self, privilege_name: str) -> UserManagementActions:
        self.click_privilege_from_the_list([privilege_name])
        self.check_all_privileges_checkbox_is_unselected()
        return self

    @allure.step
    def unselect_all_privileges(self) -> UserManagementActions:
        self.click_all_privileges_checkbox()
        self.check_non_default_privileges_are_unselected()
        return self

    @allure.step
    def select_paired_privileges(
        self, privilege_name: list, selected_privileges: list
    ) -> UserManagementActions:
        self.click_privilege_from_the_list(privilege_name)
        self.check_privileges_are_selected(selected_privileges, active_state=False)
        self.click_privilege_from_the_list(privilege_name)
        self.check_privileges_are_selected(selected_privileges, active_state=True)
        self.click_privilege_from_the_list(selected_privileges)
        return self

    @allure.step
    def check_expanding_privilege_group_list(self) -> UserManagementActions:
        group = self.privilege_groups.element_by(
            have.text(user_management_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE)
        )
        self.check_show_more_btn_is_displayed(group, 7)
        self.click_show_more_btn_for_group(group)
        self.check_hide_privileges_btn_is_displayed(group)
        self.click_privilege_from_the_list(Privileges.groups_data[1]["privileges"][-7:])
        self.check_hide_privileges_btn_is_not_displayed(group)
        return self

    @allure.step
    def check_collapsing_privilege_group_list(self) -> UserManagementActions:
        group = self.privilege_groups.element_by(
            have.text(user_management_data.ESTABLISHMENT_MANAGEMENT_GROUP_TITLE)
        )
        self.click_privilege_from_the_list([user_management_data.NATIONALIZATION_OF_OPERATION])
        self.click_hide_btn_for_group(group)
        self.check_show_more_btn_is_displayed(group, 1)
        return self

    @allure.step
    def add_access_with_fundamental_privileges(self, establishment: str) -> UserManagementActions:
        self.click_add_access_btn_on_add_privileges_modal()
        self.switch_to_tab(user_management_data.ALLOWED_ACCESS)
        self.check_establishment_is_added_to_allowed_access(establishment=establishment)
        self.success_message_is_hidden()
        return self

    @allure.step
    def add_access_with_not_fundamental_privileges(
        self, establishment: str
    ) -> UserManagementActions:
        self.click_privilege_from_the_list(
            [user_management_data.VISA_ISSUANCE_SERVICE, user_management_data.WAGE_DISBURSEMENT]
        )
        self.click_add_access_btn_on_add_privileges_modal()
        self.switch_to_tab(user_management_data.ALLOWED_ACCESS)
        self.check_establishment_is_added_to_allowed_access(establishment=establishment)
        return self

    @allure.step
    def check_success_message_and_privileges_after_add_access(
        self, row: int
    ) -> UserManagementActions:
        establishment_name = self.get_establishment_name(row)
        self.check_success_message_is_displayed(establishment_name)
        self.open_edit_privilege_modal(row)
        self.check_privileges_are_selected(
            [user_management_data.VISA_ISSUANCE_SERVICE, user_management_data.WAGE_DISBURSEMENT]
        )
        return self

    @allure.step
    def possibility_switch_to_establishment_page(self, user_type: str) -> UserManagementActions:
        qiwa.workspace_page.click_btn_subscribe(user_type)
        return self

    @allure.step
    def check_establishment_user_details(self) -> UserManagementActions:
        EstablishmentUser.main_text.wait_until(be.visible)
        self.click_btn_proceed_subscription()
        return self

    @allure.step
    def check_annual_subscription(self) -> UserManagementActions:
        AnnualSubscription.main_text.wait_until(be.visible)
        self.check_checkbox_read_accept()
        self.click_button_go_to_payment()
        return self

    @allure.step
    def check_renew_subscription(self) -> UserManagementActions:
        RenewSubscription.main_text.wait_until(be.visible)
        self.check_checkbox_read_accept()
        self.click_btn_go_to_payment()
        return self

    @allure.step
    def make_establishment_payment(self, payment: str = None) -> UserManagementActions:
        PaymentSummary.main_text.wait_until(be.visible)
        self.choose_and_make_payment(payment_type=payment)
        self.check_checkbox_read_accept()
        self.click_btn_submit_pay()
        self.complete_payment(payment_type=payment)
        return self

    @allure.step
    def check_thank_you_page(self) -> UserManagementActions:
        ThankYouPage.main_text.wait_until(be.visible)
        self.check_data_thank_you_page()
        return self
