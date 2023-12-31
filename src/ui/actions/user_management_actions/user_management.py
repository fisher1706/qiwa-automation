from __future__ import annotations

import time

import allure
from selene import Element, browser, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import ss

from data.constants import Language
from data.dedicated.models.user import User
from data.user_management import user_management_data
from data.user_management.user_management_datasets import (
    ArabicTranslations,
    ErrorsMessage,
    EstablishmentAddresses,
    Privileges,
    Texts,
)

from src.ui.pages.user_management_pages.add_new_establishment_delegator_page import AddNewEstablishmentDelegator

from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from src.ui.pages.establishment_info_page import EstablishmentInfoPage
from src.ui.pages.user_management_pages.annual_subscription_page import (
    AnnualSubscription,
)
from src.ui.pages.user_management_pages.confirmation_page import ConfirmationPage
from src.ui.pages.user_management_pages.main_page import UserManagementMainPage
from src.ui.pages.user_management_pages.owner_flow_page import OwnerFLowPage
from src.ui.pages.user_management_pages.payment_summary_page import PaymentSummary
from src.ui.pages.user_management_pages.renew_subscription_page import RenewSubscription
from src.ui.pages.user_management_pages.thank_you_page import ThankYouPage
from src.ui.pages.user_management_pages.user_detail_page import UserDetailsPage
from src.ui.qiwa import qiwa
from utils.assertion import assert_that


class UserManagementActions(
    UserManagementMainPage,
    UserDetailsPage,
    OwnerFLowPage,
    ConfirmationPage,
    AnnualSubscription,
    PaymentSummary,
    ThankYouPage,
    RenewSubscription,
    AddNewEstablishmentDelegator,
    EstablishmentInfoPage,
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
        self.should_main_page_be_displayed()
        self.get_number_of_subscribed_user_in_company()
        self.compare_count_of_users_in_table()
        self.compare_count_of_users_in_company_table()
        return self

    @allure.step
    def navigate_to_view_details_page(self, user_nid: str = None) -> UserManagementActions:
        if user_nid is None:
            self.click_view_details_in_table()
        else:
            self.click_actions_in_table_for_selected_user(user_nid)
        self.navigate_to_view_details()
        self.check_user_details_title(Texts.establishment_user_details)
        self.check_users_info_block()
        self.check_companies_table_is_displayed()
        return self

    @allure.step
    def navigate_to_owner_flow(self) -> UserManagementActions:
        self.should_main_page_be_displayed()
        self.click_subscribe_btn()
        self.check_title(Texts.establishment_and_user_details)
        self.click_btn_proceed_subscription()
        self.check_title(Texts.add_new_workspace_user)
        return self

    @allure.step
    def navigate_to_user_details(self, personal_number: int) -> UserManagementActions:
        qiwa.open_user_details_page(personal_number)
        self.check_users_info_block()
        return self

    @allure.step
    def navigate_to_user_details_without_um_permission(
        self, personal_number: int
    ) -> UserManagementActions:
        qiwa.open_user_details_page(personal_number)
        self.check_error_message_for_um_page_without_permission(
            ErrorsMessage.user_doesnt_have_access_to_um, ErrorsMessage.no_access_error_description
        )
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
            ArabicTranslations.allowed_access,
            ArabicTranslations.no_access,
            ArabicTranslations.establishment_name,
            ArabicTranslations.establishment_id,
            ArabicTranslations.privileges,
            ArabicTranslations.actions,
            ArabicTranslations.establishment_delegator_details_breadcrumbs,
        )
        return self

    @allure.step
    def check_localization_for_add_access_modal(
        self, establishment: str, hidden_privileges: str = 7
    ) -> UserManagementActions:
        self.switch_to_tab_on_user_details(ArabicTranslations.no_access)
        self.check_ar_localization_for_add_access_btn()
        establishment_without_access = self.get_establishment_row_on_no_access_table(establishment)
        self.click_add_access_button_for_workspace_without_access(establishment_without_access)
        self.check_ar_localization_for_content_on_select_privileges_modal(
            ArabicTranslations.selected_establishment_text_on_add_access_modal,
            ArabicTranslations.all_privileges,
            ArabicTranslations.hide_privileges,
            f"{ArabicTranslations.show_more_privileges.format(hidden_privileges)}",
            ArabicTranslations.occupation_management_description,
            ArabicTranslations.employee_transfer_description,
            ArabicTranslations.issue_working_permits_description,
        )
        self.check_ar_localization_for_select_privileges_modal(
            elements=[self.texts_on_select_privileges_modal.first, self.add_access_btn_on_modal],
            texts=[
                ArabicTranslations.title_on_add_access_modal,
                ArabicTranslations.add_access_btn,
            ],
        )
        return self

    @allure.step
    def check_localization_for_edit_privileges_modal(
        self, establishment: str, hidden_privileges: str = 7
    ) -> UserManagementActions:
        self.switch_to_tab_on_user_details(ArabicTranslations.allowed_access)
        establishment_with_access = self.get_establishment_row_on_allowed_access_table(
            establishment
        )
        self.check_actions_ar_texts_on_allowed_access_table(establishment_with_access)
        self.select_edit_privileges_action()
        self.check_edit_privileges_modal_is_displayed()
        self.check_ar_localization_for_content_on_select_privileges_modal(
            ArabicTranslations.selected_establishment_text_on_add_access_modal,
            ArabicTranslations.all_privileges,
            ArabicTranslations.hide_privileges,
            f"{ArabicTranslations.show_more_privileges.format(hidden_privileges)}",
            ArabicTranslations.occupation_management_description,
            ArabicTranslations.employee_transfer_description,
            ArabicTranslations.issue_working_permits_description,
        )
        self.check_ar_localization_for_select_privileges_modal(
            elements=[
                self.texts_on_select_privileges_modal.first,
                self.save_btn_on_edit_privilege_modal,
                self.remove_access_btn_on_edit_privilege_modal,
            ],
            texts=[
                ArabicTranslations.title_on_edit_privileges_modal,
                ArabicTranslations.save_and_close_btn,
                ArabicTranslations.remove_access_btn,
            ],
        )
        return self

    @allure.step
    def check_privileges_are_grouped(self, groups_data: list) -> UserManagementActions:
        self.click_show_more_privileges_btn_for_all_groups()
        self.check_privileges_group_names(groups_data)
        return self

    @allure.step
    def select_all_privileges(self) -> UserManagementActions:
        self.wait_until_privilege_list_is_displayed()
        self.click_all_privileges_checkbox()
        self.check_all_checkboxes_are_selected_on_user_details(self.privileges_checkboxes)
        return self

    @allure.step
    def unselect_the_privilege(self, privilege_name: str) -> UserManagementActions:
        self.click_privilege_from_the_list([privilege_name])
        self.check_all_privileges_checkbox_is_unselected()
        return self

    @allure.step
    def unselect_all_privileges(self) -> UserManagementActions:
        self.click_all_privileges_checkbox()
        self.check_all_checkboxes_are_unselected_on_user_details(
            ss(self.unselected_privilege_checkboxes)
        )
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
    def open_select_privileges_modal_for_no_access_workspace(
        self, establishment: str
    ) -> UserManagementActions:
        self.switch_to_tab_on_user_details(user_management_data.NO_ACCESS)
        establishment_without_access = self.get_establishment_row_on_no_access_table(establishment)
        self.click_add_access_button_for_workspace_without_access(establishment_without_access)
        self.check_add_privileges_modal_is_displayed()
        return self

    @allure.step
    def add_access_with_fundamental_privileges(self, establishment: str) -> UserManagementActions:
        establishment_without_access = self.get_establishment_row_on_no_access_table(establishment)
        establishment_with_access = self.get_establishment_row_on_allowed_access_table(
            establishment
        )
        self.click_add_access_btn_on_add_privileges_modal()
        self.success_message_is_hidden()
        self.check_establishment_is_added_to_table(
            user_management_data.ALLOWED_ACCESS, establishment_with_access
        )
        self.switch_to_tab_on_user_details(user_management_data.NO_ACCESS)
        self.check_establishment_is_removed_from_the_table(establishment_without_access)
        return self

    @allure.step
    def check_establishment_is_added_to_table(
        self, tab_name: str, establishment_row: Element
    ) -> UserManagementActions:
        self.switch_to_tab_on_user_details(tab_name)
        self.check_establishment_is_displayed_on_table(establishment_row)
        return self

    @allure.step
    def add_access_with_not_fundamental_privileges(self, user: User) -> UserManagementActions:
        establishment_without_access = self.get_establishment_row_on_no_access_table(
            user.sequence_number
        )
        self.click_privilege_from_the_list(
            [user_management_data.VISA_ISSUANCE_SERVICE, user_management_data.WAGE_DISBURSEMENT]
        )
        self.click_add_access_btn_on_add_privileges_modal()
        self.check_success_message_is_displayed(user.establishment_name_ar)
        self.check_establishment_is_removed_from_the_table_with_success_message(
            establishment_without_access
        )
        return self

    @allure.step
    def check_privileges_after_add_access_with_not_fundamental_privileges(
        self, establishment: str
    ) -> UserManagementActions:
        establishment_with_access = self.get_establishment_row_on_allowed_access_table(
            establishment
        )
        self.check_establishment_is_added_to_table(
            user_management_data.ALLOWED_ACCESS, establishment_with_access
        )
        self.open_edit_privilege_modal(establishment_with_access)
        self.check_edit_privileges_modal_is_displayed()
        self.check_privileges_are_selected(
            [user_management_data.VISA_ISSUANCE_SERVICE, user_management_data.WAGE_DISBURSEMENT]
        )
        return self

    @allure.step
    def check_remove_access_modal(self, user: User) -> UserManagementActions:
        establishment_with_access = self.get_establishment_row_on_allowed_access_table(
            user.sequence_number
        )
        self.open_edit_privilege_modal(establishment_with_access)
        self.check_edit_privileges_modal_is_displayed()
        self.click_remove_access_btn_on_edit_privileges_modal()
        self.check_remove_access_modal_is_displayed(user.establishment_name_ar, user.name)
        self.close_remove_access_modal()
        self.check_remove_access_modal_is_closed()
        self.check_edit_privileges_modal_is_displayed()
        return self

    @allure.step
    def remove_access_for_establishment(self, user: User) -> UserManagementActions:
        establishment_with_access = self.get_establishment_row_on_allowed_access_table(
            user.sequence_number
        )
        establishment_without_access = self.get_establishment_row_on_no_access_table(
            user.sequence_number
        )
        self.click_remove_access_btn_on_edit_privileges_modal()
        self.click_remove_btn_on_remove_access_modal()
        self.check_success_message_is_displayed_after_remove_access("1", user.name)
        self.check_establishment_is_removed_from_the_table_with_success_message(
            establishment_with_access
        )
        self.check_establishment_is_added_to_table(
            user_management_data.NO_ACCESS, establishment_without_access
        )
        return self

    @allure.step
    def select_all_allowed_access_establishments_checkbox(self) -> UserManagementActions:
        number_of_establishment = len(self.allowed_access_table.rows)
        self.click_all_allowed_access_establishments_checkbox()
        self.check_all_checkboxes_are_selected_on_user_details(
            self.allowed_establishments_checkboxes
        )
        self.check_buttons_below_establishments_table_are_displayed()
        self.check_elements_with_all_establishments_are_displayed(str(number_of_establishment))
        return self

    @allure.step
    def unselect_all_allowed_access_establishments_checkbox(self) -> UserManagementActions:
        self.click_all_allowed_access_establishments_checkbox()
        self.check_all_checkboxes_are_unselected_on_user_details(
            self.allowed_establishments_checkboxes
        )
        self.check_elements_below_establishments_table_are_hidden()
        return self

    @allure.step
    def select_allowed_access_establishment_checkbox(
        self, row_number: int = 2
    ) -> UserManagementActions:
        self.click_allowed_access_establishment_checkbox(row_number)
        self.check_establishment_checkbox_is_selected(row_number)
        return self

    @allure.step
    def check_establishment_checkbox_is_selected(self, row_number: int) -> UserManagementActions:
        number_of_establishment = len(self.allowed_access_table.rows)
        self.check_allowed_access_establishment_checkbox_is_selected(row_number)
        self.check_buttons_below_establishments_table_are_displayed()
        self.check_elements_with_selected_establishment_are_displayed(
            selected_establishments="1", all_establishments=str(number_of_establishment)
        )
        return self

    @allure.step
    def check_establishment_checkbox_is_selected_after_switching_between_tabs(
        self, row_number: int = 2
    ) -> UserManagementActions:
        self.switch_to_tab_on_user_details(user_management_data.NO_ACCESS)
        self.switch_to_tab_on_user_details(user_management_data.ALLOWED_ACCESS)
        self.check_establishment_checkbox_is_selected(row_number)
        return self

    @allure.step
    def terminate_user_from_all_establishments(self, user_name: str) -> UserManagementActions:
        self.click_all_allowed_access_establishments_checkbox()
        self.click_remove_access_btn()
        self.check_terminate_access_modal_is_displayed(user_name)
        self.confirm_terminating_user()
        return self

    @allure.step
    def check_user_is_terminated(self, national_id: str) -> UserManagementActions:
        self.check_success_message_after_terminate_user()
        self.close_success_modal()
        self.should_main_page_be_displayed()
        self.check_user_is_inactive_on_users_table(national_id)
        return self

    @allure.step
    def possibility_switch_to_establishment_page(self, user_type: str) -> UserManagementActions:
        qiwa.workspace_page.click_btn_subscribe(user_type)
        return self

    @allure.step
    def check_establishment_user_details(self) -> UserManagementActions:
        ConfirmationPage.page_title.wait_until(be.visible)
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
    def check_thank_you_page(self, user_type: str) -> UserManagementActions:
        ThankYouPage.main_text.wait_until(be.visible)
        self.check_data_thank_you_page(user_type)
        return self

    @allure.step
    def navigate_to_establishment_information(self, user: User) -> UserManagementActions:
        qiwa.workspace_page.business_account_list.element_by(
            have.text(str(user.sequence_number))
        ).click()
        return self

    @allure.step
    def possibility_open_renew_subscription_page(self) -> UserManagementActions:
        self.open_expired_page()
        self.check_establishment_user_details()
        return self

    @allure.step
    def check_opened_page(self, user_type: str) -> UserManagementActions:
        if user_type in ["expired", "without"]:
            RenewSubscription.main_text.wait_until(be.visible)
            self.check_group_manager_block()
            self.check_establishment_group_details_block()
            self.check_establishment_subscription_block(user_type)
            self.check_summary_block()
            self.check_total_value()
        else:
            self.should_main_page_be_displayed()
            self.check_page_is_displayed()
        return self

    @allure.step
    def check_db_subscription_date(self, user: User):
        self.check_db_data(user)
        return self

    @allure.step
    def check_confirmation_page_on_add_new_user_flow(self) -> UserManagementActions:
        self.click_subscribe_btn()
        self.check_confirmation_page_is_displayed()
        return self

    @allure.step
    def return_to_main_page_from_owner_subscription_flow(self) -> UserManagementActions:
        self.click_back_btn_on_owner_subscription_flow()
        self.should_main_page_be_displayed()
        self.should_main_page_url_be_correct()
        return self

    @allure.step
    def check_confirmation_page_is_opened(
        self, user_nid: str, action_name: str
    ) -> UserManagementActions:
        self.click_actions_in_table_for_selected_user(user_nid)
        self.select_action(action_name)
        self.check_confirmation_page_is_displayed()
        return self

    @allure.step
    def check_confirmation_page_is_hidden(
        self, user_nid: str, action_name: str
    ) -> UserManagementActions:
        self.click_actions_in_table_for_selected_user(user_nid)
        self.select_action(action_name)
        self.check_renew_terminated_page_is_opened(user_nid)
        return self

    @allure.step
    def check_content_on_confirmation_page_english_localization(
        self, establishment_data: dict, user: User
    ) -> UserManagementActions:
        establishment_number = f"{user.labor_office_id}-{user.sequence_number}"
        self.check_content_on_establishment_section(
            establishment_data["establishment_name"], establishment_number
        )
        self.check_sections_content_on_confirmation_page(
            user_management_data.CONTACT_INFO_SECTION,
            [establishment_data["notification_email"], establishment_data["notification_phone"]],
        )
        self.check_sections_content_on_confirmation_page(
            user_management_data.ESTABLISHMENT_ADDRESS_SECTION,
            establishment_data["establishment_address_en"],
        )
        return self

    @allure.step
    def check_content_on_confirmation_page_arabic_localization(
        self, establishment_data: dict
    ) -> UserManagementActions:
        qiwa.header.change_local(Language.AR)
        self.check_sections_content_on_confirmation_page(
            user_management_data.ESTABLISHMENT_ADDRESS_SECTION_AR,
            establishment_data["establishment_address_ar"],
        )
        self.check_sections_content_on_confirmation_page(
            user_management_data.ZAKAT_TAX_SECTION_AR, establishment_data["vat_number"]
        )
        return self

    @allure.step
    def confirm_payment_via_ui(self, payment_id: int, user_type: str) -> UserManagementActions:
        qiwa.open_payment_page(payment_id)
        self.make_establishment_payment().check_thank_you_page(user_type)
        return self

    @allure.step
    def check_confirmation_page_is_hidden_after_opening_subscription_page(
        self, user: User
    ) -> UserManagementActions:
        browser.driver.refresh()
        self.check_confirmation_page_is_opened(
            user.personal_number, user_management_data.RENEW_ACTION
        )
        self.click_btn_proceed_subscription()
        self.check_renew_terminated_page_is_opened(user.personal_number)
        self.return_to_main_page_from_owner_subscription_flow()
        self.check_confirmation_page_is_hidden(
            user.personal_number, user_management_data.RENEW_ACTION
        )
        self.return_to_main_page_from_owner_subscription_flow()
        return self

    @allure.step
    def check_confirmation_page_is_opened_after_changing_workspace(
        self, user: User
    ) -> UserManagementActions:
        qiwa.header.click_on_menu()
        self.click_change_workspace_btn()
        qiwa.workspace_page.select_company_account_with_sequence_number(user.sequence_number)
        self.check_confirmation_page_is_opened(
            user.personal_number, user_management_data.RENEW_ACTION
        )
        return self

    @allure.step
    def check_confirmation_page_is_opened_after_relogin(self, user: User) -> UserManagementActions:
        self.check_confirmation_page_is_opened(
            user.personal_number, user_management_data.RENEW_ACTION
        )
        self.click_btn_proceed_subscription(1)
        self.check_renew_terminated_page_is_opened(user.personal_number)
        return self

    @allure.step
    def check_english_localization_for_errors_on_confirmation_page(self) -> UserManagementActions:
        self.check_texts_for_main_error_block(
            user_management_data.ERROR_TITLE,
            [user_management_data.VAT_ERROR_LINK, user_management_data.ADDRESS_ERROR_LINK],
        )
        self.check_texts_for_address_error_block(
            user_management_data.ADDRESS_ERROR_TITLE,
            user_management_data.MISSING_ADDRESS_DATA,
            user_management_data.ADDRESS_BTN_TEXT,
        )
        self.check_texts_for_vat_error_block(
            user_management_data.VAT_ERROR_TITLE,
            user_management_data.VAT_ERROR_DESCRIPTION,
            [
                user_management_data.ADD_VAT_NUMBER_BTN,
                user_management_data.REGISTER_WITHOUT_VAT_BTN,
            ],
        )
        return self

    @allure.step
    def check_arabic_localization_for_errors_on_confirmation_page(self) -> UserManagementActions:
        self.check_texts_for_main_error_block(
            user_management_data.ERROR_TITLE_AR,
            [user_management_data.VAT_ERROR_LINK_AR, user_management_data.ADDRESS_ERROR_LINK_AR],
        )
        self.check_texts_for_address_error_block(
            user_management_data.ADDRESS_ERROR_TITLE_AR,
            user_management_data.MISSING_ADDRESS_DATA_AR,
            user_management_data.ADDRESS_BTN_TEXT_AR,
        )
        self.check_texts_for_vat_error_block(
            user_management_data.VAT_ERROR_TITLE_AR,
            user_management_data.VAT_ERROR_DESCRIPTION_AR,
            [
                user_management_data.ADD_VAT_NUMBER_BTN_AR,
                user_management_data.REGISTER_WITHOUT_VAT_BTN_AR,
            ],
        )
        return self

    @allure.step
    def check_establishment_data_error_is_displayed(self) -> UserManagementActions:
        self.check_confirmation_page_on_add_new_user_flow()
        self.check_texts_for_main_error_block(
            user_management_data.ERROR_TITLE,
            [user_management_data.ADDRESS_ERROR_LINK],
        )
        self.check_texts_for_address_error_block(
            user_management_data.ADDRESS_ERROR_TITLE,
            user_management_data.MISSING_ADDRESS_DATA,
            user_management_data.ADDRESS_BTN_TEXT,
        )
        self.click_btn_proceed_subscription()
        time.sleep(3)
        self.check_confirmation_page_is_displayed()
        return self

    @allure.step
    def check_vat_error_is_displayed(self) -> UserManagementActions:
        self.check_confirmation_page_on_add_new_user_flow()
        self.check_texts_for_main_error_block(
            user_management_data.ERROR_TITLE,
            [user_management_data.VAT_ERROR_LINK],
        )
        self.check_texts_for_vat_error_block(
            user_management_data.VAT_ERROR_TITLE,
            user_management_data.VAT_ERROR_DESCRIPTION,
            [
                user_management_data.ADD_VAT_NUMBER_BTN,
                user_management_data.REGISTER_WITHOUT_VAT_BTN,
            ],
        )
        self.check_sections_content_on_confirmation_page(
            user_management_data.ZAKAT_TAX_SECTION, [user_management_data.EMPTY_ON_UI]
        )
        self.click_btn_proceed_subscription()
        time.sleep(3)
        self.check_confirmation_page_is_displayed()
        return self

    @allure.step
    def update_address_data_from_confirmation_page(
        self,
        establishment_data: list,
        address_values_on_thank_you_popup: list,
        all_establishment_values: bool = True,
    ) -> UserManagementActions:
        self.check_financial_info_section_is_displayed()
        self.click_change_establishment_address_link()
        if all_establishment_values:
            self.enter_all_establishment_data(*establishment_data)
        else:
            self.update_district_and_street_data(*establishment_data)
        self.click_submit_btn()
        self.check_establishment_data_on_thank_you_popup(address_values_on_thank_you_popup)
        return self

    @allure.step
    def check_updated_address_data_on_confirmation_page(
        self,
        address_values_on_confirmation_page: list,
        owner_for_self_subscription: User = None,
    ) -> UserManagementActions:
        self.click_back_to_subscription_flow_btn()
        self.check_confirmation_page_is_displayed()
        self.check_error_message_is_not_displayed()
        self.check_sections_content_on_confirmation_page(
            user_management_data.ESTABLISHMENT_ADDRESS_SECTION, address_values_on_confirmation_page
        )
        if owner_for_self_subscription is None:
            self.proceed_owner_subscription_on_confirmation_page()
        else:
            self.proceed_self_subscription_on_confirmation_page(
                owner_for_self_subscription.labor_office_id,
                owner_for_self_subscription.sequence_number,
            )
        return self

    @allure.step
    def proceed_owner_subscription_on_confirmation_page(self) -> UserManagementActions:
        self.click_btn_proceed_subscription()
        self.check_subscribe_user_page_is_opened()
        return self

    def proceed_self_subscription_on_confirmation_page(
        self, office_id: str, sequence_number: str
    ) -> UserManagementActions:
        self.click_btn_proceed_subscription()
        self.check_self_renew_expired_page_is_opened(office_id, sequence_number)
        return self

    @allure.step
    def select_proceed_without_vat_on_confirmation_page(self) -> UserManagementActions:
        self.click_register_without_vat_btn()
        self.check_sections_content_on_confirmation_page(
            user_management_data.ZAKAT_TAX_SECTION, [user_management_data.REGISTERED_WITHOUT_VAT]
        )
        self.check_error_message_is_not_displayed()
        return self

    @allure.step
    def update_establishment_data_for_owner_subscription_flow(self) -> UserManagementActions:
        self.check_establishment_data_error_is_displayed()
        self.click_add_address_info_btn_on_confirmation_page()
        self.update_address_data_from_confirmation_page(
            EstablishmentAddresses.update_address_data_on_ui,
            EstablishmentAddresses.updated_address_data_on_thank_you_popup,
        )
        self.check_updated_address_data_on_confirmation_page(
            EstablishmentAddresses.updated_address_data_on_confirmation_page
        )
        return self

    @allure.step
    def update_establishment_data_for_self_subscription_flow(
        self, user_type: str, owner: User
    ) -> UserManagementActions:
        self.possibility_switch_to_establishment_page(user_type)
        self.check_confirmation_page_is_displayed()
        self.click_add_address_info_btn_on_confirmation_page()
        self.update_address_data_from_confirmation_page(
            EstablishmentAddresses.update_address_data_on_ui,
            EstablishmentAddresses.updated_address_data_on_thank_you_popup,
        )
        self.check_updated_address_data_on_confirmation_page(
            EstablishmentAddresses.updated_address_data_on_confirmation_page, owner
        )
        return self

    @allure.step
    def update_establishment_data_for_both_localizations(self) -> UserManagementActions:
        qiwa.header.change_local(Language.EN)
        self.click_edit_btn_for_section(user_management_data.ESTABLISHMENT_ADDRESS_SECTION)
        self.update_address_data_from_confirmation_page(
            EstablishmentAddresses.update_address_data_on_ui[:3],
            EstablishmentAddresses.updated_address_data_on_thank_you_popup,
            False,
        )
        self.check_updated_address_data_on_confirmation_page(
            EstablishmentAddresses.updated_address_data_on_confirmation_page
        )
        return self

    @allure.step
    def open_owner_extend_subscription_page(self, user: User) -> UserManagementActions:
        self.check_confirmation_page_is_opened(
            user.personal_number, user_management_data.EXTEND_ACTION
        )
        self.click_btn_proceed_subscription()
        self.check_extend_subscription_page_is_opened(user.personal_number)
        return self

    @allure.step
    def check_establishment_with_not_allowed_activities_is_hidden_from_owner_subscription_flow(
        self, user: User
    ) -> UserManagementActions:
        browser.driver.refresh()
        self.open_owner_extend_subscription_page(user)
        self.check_establishment_list_is_displayed_on_owner_subscription_page(
            sorted(user_management_data.ALLOWED_ESTABLISHMENT_LIST)
        )
        self.check_establishment_is_hidden_on_owner_subscription_page(
            user_management_data.ESTABLISHMENT_WITH_NOT_ALLOWED_ACTIVITIES
        )
        self.select_terms_and_conditions_checkbox_on_owner_subscription_page().click_go_to_payment_btn()
        self.make_establishment_payment().check_thank_you_page("owner_flow")
        establishment_list_from_db = UserManagementRequests().get_establishment_access_list(
            user.personal_number, user.unified_number_id
        )
        assert_that(establishment_list_from_db).equals_to(
            user_management_data.ALLOWED_ESTABLISHMENT_LIST
        )
        return self

    def extend_owner_subscription_and_check_added_establishments(
        self, subscribed_user: User, establishments_list: list
    ) -> UserManagementActions:
        self.second_page_btn_on_users_table.click()
        self.open_owner_extend_subscription_page(subscribed_user)
        self.check_establishment_list_is_displayed_on_owner_subscription_page(establishments_list)
        self.select_terms_and_conditions_checkbox_on_owner_subscription_page().click_go_to_payment_btn()
        self.make_establishment_payment().check_thank_you_page("owner_flow")
        self.click_go_back_to_um_btn()
        qiwa.main_page.should_main_page_be_displayed()
        self.second_page_btn_on_users_table.click()
        self.check_user_status_on_users_table(
            subscribed_user.personal_number, user_management_data.ACTIVE_STATUS
        )
        self.click_actions_in_table_for_selected_user(subscribed_user.personal_number)
        self.navigate_to_view_details()
        for establishment in establishments_list:
            establishment_row = self.get_establishment_row_on_allowed_access_table(establishment)
            self.check_establishment_is_displayed_on_table(establishment_row)
        return self

    @allure.step
    def check_open_add_establishment_delegator_page(self) -> UserManagementActions:
        self.click_subscribe_btn()
        ConfirmationPage.page_title.wait_until(be.visible)
        self.click_btn_proceed_subscription()
        AddNewEstablishmentDelegator.main_text.wait_until(be.visible)
        return self

    @allure.step
    def verify_possibility_upload_data_of_few_users_as_delegator(self, *args: User) -> UserManagementActions:
        for arg in args:
            self.upload_establishment_delegator_data(arg.personal_number)
            self.verify_user_identity(arg.personal_number)
            self.click_btn_check_another_users_data()
        return self

    @allure.step
    def verify_possibility_add_few_users_as_delegator(self, *args: User) -> UserManagementActions:
        for arg in args:
            self.upload_establishment_delegator_data(arg.personal_number)
            self.verify_user_identity(arg.personal_number)
            self.click_btn_add_establishment_delegator()
            self.verify_add_selected_user(arg.personal_number)
            if arg != args[-1]:
                self.click_btn_add_another_establishment_delegator()
        self.check_href_how_calculate_subscription_price()
        self.verify_total_selected(*args)
        return self

    @allure.step
    def verify_possibility_add_additional_users_as_delegator(self, *args: User) -> UserManagementActions:
        for arg in args:
            self.click_btn_add_another_establishment_delegator()
            self.upload_establishment_delegator_data(arg.personal_number)
            self.verify_user_identity(arg.personal_number)
            self.click_btn_add_establishment_delegator()
            self.verify_add_selected_user(arg.personal_number)
            if arg != args[-1]:
                self.click_btn_add_another_establishment_delegator()
        return self

    @allure.step
    def delete_establishment_delegator(self, *args: User) -> UserManagementActions:
        for arg in args:
            self.delete_user_from_new_establishment_delegators(arg.personal_number)
        return self

    @allure.step
    def verify_establishment_user_have_access(self, *args: User) -> UserManagementActions:
        self.click_btn_next_step()
        self.click_btn_next_step()
        self.verify_error_message()
        for arg in args:
            self.verify_added_users_into_workspace(arg.personal_number)
            self.select_establishment()
            self.click_btn_next_step()
            self.verify_selected_establishment()
            self.click_btn_customize_privileges()

            self.verify_fundamental_privileges()
            self.verify_employees_management()
            self.verify_establishment_management()
            self.verify_establishment_performance()
            self.verify_workspaces_management()

            self.click_btn_next_step()
        self.verify_access_and_privileges(*args)
        self.verify_summary_section(*args)
        return self

    @allure.step
    def verify_edit_establishment_delegator_section(self, *args: User) -> UserManagementActions:
        for arg in args:
            if arg != args[0]:
                self.click_btn_add_another_establishment_delegator()
            self.upload_establishment_delegator_data(arg.personal_number)
            self.click_btn_add_establishment_delegator()
            self.click_btn_next_step()
            self.verify_added_users_into_workspace(arg.personal_number)
            if arg == args[0]:
                self.click_btn_edit()
        return self

    @allure.step
    def go_to_payment_page(self) -> UserManagementActions:
        self.check_checkbox_read_accept()
        self.click_btn_go_to_payment()
        return self

    @allure.step
    def select_deselect_all_establishment(self) -> UserManagementActions:
        self.select_all_establishment()
        self.clear_all_establishment()
        return self

    @allure.step
    def check_field_search(self, *args: [str, int]) -> UserManagementActions:
        for arg in args:
            self.fill_field_search(arg)
            self.verify_field_search(arg) if arg != args[0] else self.verify_no_result_found()
        return self

    @allure.step
    def verify_ability_select_all_privileges_for_all_establishment(self) -> UserManagementActions:
        self.click_btn_next_step()
        self.select_establishment()
        self.click_btn_next_step()
        self.click_btn_customize_privileges()
        self.check_random_checkbox()
        self.click_btn_save_privileges()
        self.click_btn_next_step()
        self.select_all_establishment()
        self.click_btn_next_step()
        self.click_btn_customize_privileges()
        self.check_all_privileges_checkbox()
        self.click_btn_save_and_go_to_next_step()
        return self

    @allure.step
    def verify_warning_message(self) -> UserManagementActions:
        self.click_btn_go_to_payment()
        self.check_warning_message()
        return self
