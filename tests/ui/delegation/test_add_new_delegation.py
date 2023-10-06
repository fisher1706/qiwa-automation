import allure

from data.delegation import add_delegation_data
from data.delegation.users import (
    establishment_owner_with_one_partner,
    establishment_owner_with_two_partners,
    establishment_owner_without_partners,
)
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import (
    get_months_list,
    get_partners_data,
    get_random_employee,
    login_and_open_add_delegation_page,
    login_and_open_delegation_dashboard_page,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Verify 'Add delegation' button (desktop)")
@case_id(46599)
def test_open_add_new_delegation_flow():
    login_and_open_delegation_dashboard_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.delegation_dashboard_page.click_add_delegation_button()
    qiwa.add_delegation_page.wait_add_new_delegation_page_to_load()\
        .should_step_be_opened(step_id=add_delegation_data.FIRST_STEP_ID,
                               step_number=add_delegation_data.FIRST_STEP_NUMBER)\
        .should_url_for_add_delegation_page_be_correct()


@allure.title("Verify the default value of the Entity type")
@case_id(46603)
def test_the_default_value_for_entity_type():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    entity_types = qiwa_api.delegation_api.get_entity_type(headers)
    qiwa.add_delegation_page.should_government_entity_type_be_selected(entity_types[1]["nameEn"])\
        .should_financial_entity_type_be_disabled(entity_types[0]["nameEn"])\
        .should_telecom_entity_type_be_disabled(entity_types[2]["nameEn"])


@allure.title("Verify the ability to select the Entity name")
@case_id(46604, 46605)
def test_select_entity_name():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    entity_types = qiwa_api.delegation_api.get_entity_type(headers)
    entity_name = qiwa_api.delegation_api.get_entity_name(headers)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(entity_name)\
        .should_entity_name_be_selected(entity_name)\
        .click_next_button_on_add_delegation_page().should_step_be_completed(
        step_id=add_delegation_data.FIRST_STEP_ID)\
        .should_entity_data_be_displayed_on_completed_step(entity_data=[entity_types[1]["nameEn"], entity_name])\
        .should_step_be_opened(step_id=add_delegation_data.SECOND_STEP_ID,
                               step_number=add_delegation_data.SECOND_STEP_NUMBER)


@allure.title("Verify the possibility to select permission")
@case_id(46652, 46655)
def test_select_permission():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    permission = qiwa_api.delegation_api.get_entity_permission(headers)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(
        entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page().select_permission_on_add_delegation_page(
        permission=permission)\
        .should_permission_be_selected(permission=permission)\
        .click_next_button_on_add_delegation_page()\
        .should_step_be_completed(step_id=add_delegation_data.SECOND_STEP_ID)\
        .should_permission_be_displayed_on_completed_step(permission=permission)\
        .should_step_be_opened(step_id=add_delegation_data.THIRD_STEP_ID,
                               step_number=add_delegation_data.THIRD_STEP_NUMBER)


@allure.title("Verify the possibility to remove permission")
@case_id(46654)
def test_remove_permission():
    login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(
        entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page()\
        .select_permission_on_add_delegation_page(permission=add_delegation_data.PERMISSION)\
        .should_permission_be_selected(permission=add_delegation_data.PERMISSION)\
        .click_remove_button_for_selected_permission().should_option_be_removed()


@allure.title("Verify the possibility to select delegation duration")
@case_id(57390, 57414, 57388)
def test_select_delegation_duration():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    max_months = qiwa_api.delegation_api.get_max_months(headers)
    months_list = get_months_list(max_months)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page()\
        .select_permission_on_add_delegation_page(permission=add_delegation_data.PERMISSION)\
        .click_next_button_on_add_delegation_page()\
        .should_months_be_displayed_on_duration_list(months_list)\
        .select_duration_month(month_number=add_delegation_data.ONE_MONTH_DURATION)\
        .should_duration_month_be_selected(month_number=add_delegation_data.ONE_MONTH_DURATION)\
        .select_duration_month(month_number=add_delegation_data.TEN_MONTHS_DURATION)\
        .should_duration_month_be_selected(month_number=add_delegation_data.TEN_MONTHS_DURATION)\
        .click_next_button_on_add_delegation_page()\
        .should_step_be_completed(step_id=add_delegation_data.THIRD_STEP_ID)\
        .should_duration_be_displayed_on_completed_step(duration=add_delegation_data.TEN_MONTHS_DURATION)\
        .should_step_be_opened(step_id=add_delegation_data.FOURTH_STEP_ID,
                               step_number=add_delegation_data.FOURTH_STEP_NUMBER)


@allure.title("Verify the possibility to select delegate")
@case_id(55018, 78114)
def test_select_delegate():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    employees = qiwa_api.delegation_api.get_employees_list(headers)
    employee_data = get_random_employee(employee_list=employees)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(
        entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page()\
        .select_permission_on_add_delegation_page(permission=add_delegation_data.PERMISSION)\
        .click_next_button_on_add_delegation_page()\
        .select_duration_month(month_number=add_delegation_data.TEN_MONTHS_DURATION)\
        .click_next_button_on_add_delegation_page()\
        .should_number_of_employees_be_correct(number_of_delegates=employees["totalElements"])\
        .search_employee_list_by_nid(employee_nid=employee_data["nid"])\
        .should_employee_data_be_correct(employee_data)\
        .select_employee_on_add_delegation_page(employee_number=add_delegation_data.FIRST_EMPLOYEE_NUMBER)\
        .click_next_button_on_add_delegation_page()\
        .should_step_be_completed(step_id=add_delegation_data.FOURTH_STEP_ID)\
        .should_employee_data_be_displayed_on_completed_step(employee_data)\
        .should_step_be_opened(step_id=add_delegation_data.FIFTH_STEP_ID,
                               step_number=add_delegation_data.FIFTH_STEP_NUMBER)


@allure.title("Verify selecting by one Employee")
@case_id(55002)
def test_ability_to_select_one_employee():
    login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(
        entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page()\
        .select_permission_on_add_delegation_page(permission=add_delegation_data.PERMISSION)\
        .click_next_button_on_add_delegation_page()\
        .select_duration_month(month_number=add_delegation_data.TEN_MONTHS_DURATION)\
        .click_next_button_on_add_delegation_page()\
        .select_employee_on_add_delegation_page(employee_number=add_delegation_data.FIRST_EMPLOYEE_NUMBER)
    first_employee_name = qiwa.add_delegation_page.get_selected_employee_name_on_add_delegation_page(
        employee_number=add_delegation_data.FIRST_EMPLOYEE_NUMBER)
    second_employee_name = qiwa.add_delegation_page.get_selected_employee_name_on_add_delegation_page(
        employee_number=add_delegation_data.SECOND_EMPLOYEE_NUMBER)
    qiwa.add_delegation_page.should_employee_be_selected(employee_name=first_employee_name)\
        .select_employee_on_add_delegation_page(employee_number=add_delegation_data.SECOND_EMPLOYEE_NUMBER)\
        .should_employee_be_selected(employee_name=second_employee_name)\
        .click_remove_button_for_selected_employee()\
        .should_option_be_removed()


@allure.title("Verify step if Establishment doesn't have Partners")
@case_id(57503)
def test_create_delegation_in_establishment_without_partners():
    login_and_open_add_delegation_page(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(
        entity_name=add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page().select_permission_on_add_delegation_page(
        permission=add_delegation_data.PERMISSION)\
        .click_next_button_on_add_delegation_page()\
        .select_duration_month(month_number=add_delegation_data.TEN_MONTHS_DURATION)\
        .click_next_button_on_add_delegation_page()\
        .select_employee_on_add_delegation_page(employee_number=add_delegation_data.FIRST_EMPLOYEE_NUMBER)\
        .click_next_button_on_add_delegation_page()\
        .should_content_be_displayed_for_establishment_without_partner()\
        .click_next_button_on_add_delegation_page().should_confirmation_modal_be_opened()\
        .click_close_button_on_confirmation_modal().should_confirmation_modal_be_closed()\
        .click_next_button_on_add_delegation_page()\
        .click_confirm_request_button_on_confirmation_modal()\
        .should_successful_modal_be_opened(establishment_with_partners=False)\
        .click_go_back_to_delegations_button_on_modal()
    qiwa.delegation_dashboard_page.check_redirect_to_delegation_dashboard().should_delegations_table_is_displayed()


@allure.title("Verify step if Establishment has Partner(s) with a valid phone number")
@case_id(57504)
def test_create_delegation_in_establishment_with_partners():
    qiwa_api = login_and_open_add_delegation_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    partners_list = qiwa_api.delegation_api.get_partners(headers)
    partners_number = len(partners_list)
    partners = get_partners_data(partners_list)
    qiwa.add_delegation_page.select_entity_name_on_add_delegation_page(add_delegation_data.ENTITY_NAME)\
        .click_next_button_on_add_delegation_page()\
        .select_permission_on_add_delegation_page(add_delegation_data.PERMISSION)\
        .click_next_button_on_add_delegation_page().select_duration_month(add_delegation_data.TEN_MONTHS_DURATION)\
        .click_next_button_on_add_delegation_page()\
        .select_employee_on_add_delegation_page(add_delegation_data.FIRST_EMPLOYEE_NUMBER)\
        .click_next_button_on_add_delegation_page().scroll_to_the_fifth_step()\
        .should_content_be_displayed_for_establishment_with_partners()\
        .should_number_of_partners_be_correct(partners_number)\
        .should_partners_data_be_correct(partner_number=1, partners_data=partners[0])\
        .should_partners_data_be_correct(partner_number=2, partners_data=partners[1])\
        .click_next_button_on_add_delegation_page().click_confirm_request_button_on_confirmation_modal()\
        .should_successful_modal_be_opened(establishment_with_partners=True)\
        .click_go_back_to_delegations_button_on_modal()
