from __future__ import annotations

import random

import allure
from selene import be, command
from selene import have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys

from utils.helpers import scroll_to_coordinates
from data.user_management import user_management_data


class AddNewEstablishmentDelegator:
    main_text = s("//p[contains(text(), 'Add new Establishment Delegator')]")
    btn_upload_user_data = s("//button//p[contains(text(), 'Upload user data')]")
    btn_check_another_users_data = s('//button//p[contains(text(), "Check another user\'s data")]')
    btn_add_establishment_delegator = s("//p[contains(text(), 'Add Establishment Delegator')]")
    btn_add_another_establishment_delegator = s("//p[contains(text(), 'Add Another Establishment Delegator')]")
    user_name_value = s("//*[@id='root']//table//tr[1]//p[2]")
    user_id_value = s("//*[@id='root']//table//tr[2]//p[2]")
    field_user_national_id = s("//*[@id='user_nid']")
    number_of_added_users_value = s("//p[contains(text(), 'Number of added users')]/../p[2]")
    subscription_period_value = s("//p[contains(text(), 'Subscription period')]/../p[2]")
    total_summary_value = s("//p[contains(text(), 'Total')]/../div/p/span[1]")
    btn_next_step = s("//p[contains(text(), 'Next step')]")
    checkbox_select_establishment = ss("[data-component='Checkbox'] input")
    error_message = s("//p[contains(text(), 'Please select the establishments to which this user can have access.')]")
    access_and_privileges = ss("//p[contains(text(), 'Access and privileges')]/../../p")
    selected_establishments = ss("//p[contains(text(), 'Selected establishments')]/../div//p[2]")
    btn_customize_privileges = s("//*[@id='one']/../span")
    subscription_expiration_data_value = s("//p[contains(text(), 'Subscription expiration date')]/../p[2]")
    summary_section_total_value = ss("//p[contains(text(), 'Total')]/../..//span")
    btn_edit = ss('//button//p[contains(text(), "Edit")]')
    select_all_link = s("//a/span[contains(text(), 'Select all')]")
    clear_all_link = s("//a/span[contains(text(), 'Clear all')]")
    field_search = s("//*[@id='search']")
    clear_filter = s("[aria-label='Delete']")
    search_not_result = s("//p[contains(text(), 'No results found.')]")
    fundamental_privileges = s("//p[contains(text(), 'Fundamental privileges')]")
    fundamental_privileges_item = ss("//p[contains(text(), 'Fundamental privileges')]/../div[1]//p")
    employees_management = s("//p[contains(text(), 'Employees Management')]")
    employees_management_item = ss("//p[contains(text(), 'Employees Management')]/..//input/..//p")
    establishment_management = s("//p[contains(text(), 'Establishment Management')]")
    establishment_management_item = ss("//p[contains(text(), 'Establishment Management')]/..//input/..//p")
    establishment_performance = s("//*[text()='Establishment Performance']")
    establishment_performance_item = ss("//*[text()='Establishment Performance']/..//input/../span")
    workspaces_management = s("//p[contains(text(), 'Workspaces Management')]")
    workspaces_management_item = ss("//p[contains(text(), 'Workspaces Management')]/../..//label//p")
    checkboxes = ss("//div/label/input[contains(@aria-checked,'false')]")
    btn_save_privileges = s("//p[contains(text(), 'Save privileges')]/..")
    btn_save_and_go_to_next_step = s("//p[contains(text(), 'Save and go to next step')]/..")
    href_how_calculate_subscription_price = s("//span[contains(text(), "
                                              "'How is the price of subscription calculated?')]/..")
    warning_message = s("//p[contains(text(), "
                        "'Please read and accept Qiwa’s Terms and Conditions to submit the request')]")

    @allure.step
    def upload_establishment_delegator_data(self, personal_number: str) -> AddNewEstablishmentDelegator:
        self.field_user_national_id.should(be.visible).perform(command.js.set_value("")).type(personal_number)
        self.btn_upload_user_data.should(be.visible).click()
        return self

    @allure.step
    def verify_user_identity(self, personal_number: str) -> AddNewEstablishmentDelegator:
        self.user_name_value.should(be.visible)
        self.user_id_value.should(have.exact_text(personal_number))
        return self

    @allure.step
    def click_btn_check_another_users_data(self) -> AddNewEstablishmentDelegator:
        self.btn_check_another_users_data.should(be.visible).click()
        return self

    @allure.step
    def click_btn_add_establishment_delegator(self) -> AddNewEstablishmentDelegator:
        self.btn_add_establishment_delegator.should(be.visible).click()
        return self

    @allure.step
    def click_btn_add_another_establishment_delegator(self) -> AddNewEstablishmentDelegator:
        self.btn_add_another_establishment_delegator.should(be.visible).click()
        return self

    @allure.step
    def verify_add_selected_user(self, personal_number: str) -> AddNewEstablishmentDelegator:
        s(f"//td[contains(text(), '{personal_number}')]").should(be.visible)
        return self

    @allure.step
    def verify_total_selected(self, *args: str) -> AddNewEstablishmentDelegator:
        self.number_of_added_users_value.should(have.exact_text(str(len(args))))
        self.subscription_period_value.should(have.text(user_management_data.SUBSCRIPTION_PERIOD))
        self.total_summary_value.should(be.visible).should(have.text(user_management_data.SUBSCRIPTION_CURRENCY))
        return self

    @allure.step
    def delete_user_from_new_establishment_delegators(self, personal_number: str) -> AddNewEstablishmentDelegator:
        s(f"//td[contains(text(), '{personal_number}')]/..//a/span").click()
        s(f"//td[contains(text(), '{personal_number}')]").should(be.hidden)
        return self

    @allure.step
    def click_btn_next_step(self) -> AddNewEstablishmentDelegator:
        self.btn_next_step.wait_until(be.visible)
        self.btn_next_step.click()
        return self

    @allure.step
    def select_establishment(self, number: int = None) -> AddNewEstablishmentDelegator:
        self.checkbox_select_establishment[number].press(Keys.SPACE) if number \
            else self.checkbox_select_establishment[1].press(Keys.SPACE)
        return self

    @allure.step
    def verify_error_message(self) -> AddNewEstablishmentDelegator:
        self.error_message.should(be.visible)
        return self

    @allure.step
    def verify_access_and_privileges(self, *args: str) -> AddNewEstablishmentDelegator:
        self.access_and_privileges.should(be.visible.each).should(have.size(len(args)))
        return self

    @allure.step
    def verify_added_users_into_workspace(self, personal_number: str) -> AddNewEstablishmentDelegator:
        s(f"//p[contains(text(), 'New Workspace User(s) selected')]/../../../..//p[contains(text(), "
          f"'{personal_number}')]").should(be.visible)
        return self

    @allure.step
    def verify_selected_establishment(self) -> AddNewEstablishmentDelegator:
        self.selected_establishments.should(be.visible.each)
        return self

    @allure.step
    def click_btn_customize_privileges(self):
        self.btn_customize_privileges.should(be.visible).click()

    @allure.step
    def verify_summary_section(self, *args: str) -> AddNewEstablishmentDelegator:
        self.number_of_added_users_value.should(have.exact_text(str(len(args))))
        self.subscription_period_value.should(have.text(user_management_data.SUBSCRIPTION_PERIOD))
        self.subscription_expiration_data_value.should(be.visible)
        self.summary_section_total_value[0].should(be.visible)\
            .should(have.text(user_management_data.SUBSCRIPTION_CURRENCY))
        return self

    @allure.step
    def click_btn_edit(self, number: int = None) -> AddNewEstablishmentDelegator:
        scroll_to_coordinates()
        self.main_text.wait_until(be.visible)
        if number:
            self.btn_edit[number].wait_until(be.visible)
            self.btn_edit[number].click()
        else:
            self.btn_edit[0].wait_until(be.visible)
            self.btn_edit[0].click()
        return self

    @allure.step
    def select_all_establishment(self) -> AddNewEstablishmentDelegator:
        self.select_all_link.should(be.visible).click()
        return self

    @allure.step
    def clear_all_establishment(self) -> AddNewEstablishmentDelegator:
        self.clear_all_link.should(be.visible).click()
        return self

    @allure.step
    def fill_field_search(self, data: [str, int]) -> AddNewEstablishmentDelegator:
        self.field_search.should(be.visible).perform(command.js.set_value("")).type(data)
        return self

    @allure.step
    def verify_field_search(self, data: [str, int]) -> AddNewEstablishmentDelegator:
        s(f"//td[contains(text(), '{data}')]").should(be.visible)
        self.select_all_link.should(be.hidden)
        self.clear_filter.should(be.visible).click()
        self.select_all_link.should(be.visible)
        return self

    @allure.step
    def verify_no_result_found(self) -> AddNewEstablishmentDelegator:
        self.search_not_result.should(be.visible)
        self.select_all_link.should(be.hidden)
        self.clear_filter.should(be.visible).click()
        self.select_all_link.should(be.visible)
        return self

    @allure.step
    def verify_fundamental_privileges(self) -> AddNewEstablishmentDelegator:
        self.fundamental_privileges.wait_until(be.visible)
        self.fundamental_privileges.should(be.visible)
        self.fundamental_privileges_item.should(be.visible.each)\
            .should(have.size(user_management_data.COUNT_FUNDAMENTAL_PRIVILEGES))
        return self

    @allure.step
    def verify_employees_management(self) -> AddNewEstablishmentDelegator:
        self.employees_management.should(be.visible)
        self.employees_management_item.should(be.visible.each)\
            .should(have.size(user_management_data.COUNT_EMPLOYEES_MANAGEMENT))
        return self

    @allure.step
    def verify_establishment_management(self) -> AddNewEstablishmentDelegator:
        self.employees_management.should(be.visible)
        self.establishment_management_item.should(be.visible.each)\
            .should(have.size(user_management_data.COUNT_ESTABLISHMENT_MANAGEMENT))
        return self

    @allure.step
    def verify_establishment_performance(self) -> AddNewEstablishmentDelegator:
        self.establishment_performance.should(be.visible)
        self.establishment_performance_item.should(be.visible.each)\
            .should(have.size(user_management_data.COUNT_ESTABLISHMENT_PERFORMANCE))
        return self

    @allure.step
    def verify_workspaces_management(self) -> AddNewEstablishmentDelegator:
        self.workspaces_management.should(be.visible)
        self.workspaces_management_item.should(be.visible.each)\
            .should(have.size(user_management_data.COUNT_WORKSPACES_MANAGEMENT))
        return self

    @allure.step
    def check_random_checkbox(self) -> AddNewEstablishmentDelegator:
        self.checkboxes[random.randint(2, 20)].press(Keys.SPACE)
        return self

    @allure.step
    def check_all_privileges_checkbox(self) -> AddNewEstablishmentDelegator:
        self.checkboxes[0].press(Keys.SPACE)
        return self

    @allure.step
    def click_btn_save_privileges(self) -> AddNewEstablishmentDelegator:
        self.btn_save_privileges.should(be.visible).click()
        return self

    @allure.step
    def click_btn_save_and_go_to_next_step(self) -> AddNewEstablishmentDelegator:
        self.btn_save_and_go_to_next_step.should(be.visible).click()
        return self

    @allure.step
    def check_href_how_calculate_subscription_price(self) -> AddNewEstablishmentDelegator:
        self.href_how_calculate_subscription_price.should(be.visible)
        return self

    @allure.step
    def check_warning_message(self) -> AddNewEstablishmentDelegator:
        self.warning_message.should(be.visible)
        return self
